"""
=========================================================
VISION SERVICE — MULTIMODAL VIDEO FRAME ANALYSIS
=========================================================

Analyzes representative video frames using Groq Vision AI
(or Google Gemini Vision as fallback) to identify scenes,
objects, actions, tone, and visual topics.
=========================================================
"""

import os
import json
import base64
import urllib.request
import urllib.error
import cv2
from typing import List, Dict, Any
from dotenv import load_dotenv

# Load environment variables from .env file (override=True ensures fresh values)
load_dotenv(override=True)


def _encode_image_to_base64(image_path: str, max_dimension: int = 1024) -> str:
    """Read an image file, resize if large for fast upload, and convert to base64."""
    try:
        img = cv2.imread(image_path)
        if img is not None:
            h, w = img.shape[:2]
            if max(h, w) > max_dimension:
                scale = max_dimension / max(h, w)
                new_w, new_h = int(w * scale), int(h * scale)
                img = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_AREA)

            success, buffer = cv2.imencode(".jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), 80])
            if success:
                return base64.b64encode(buffer).decode("utf-8")
    except Exception:
        pass

    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")


def _call_groq_vision_api(api_key: str, prompt: str, frame_paths: List[str]) -> Dict[str, Any]:
    """
    Call Groq Vision API using Qwen multimodal vision model (qwen/qwen3.8-27b).
    """
    url = "https://api.groq.com/openai/v1/chat/completions"

    # Send representative keyframe (1 frame = ~1,800 tokens, safely within Groq's 7,000 ITPM free limit)
    content_parts: List[Dict[str, Any]] = [{"type": "text", "text": prompt}]
    for fp in frame_paths[:1]:
        b64 = _encode_image_to_base64(fp)
        content_parts.append({
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{b64}"
            }
        })

    model = "qwen/qwen3.8-27b"
    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": content_parts
            }
        ],
        "response_format": {"type": "json_object"},
        "temperature": 0.2
    }

    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        },
        method="POST"
    )

    try:
        with urllib.request.urlopen(req, timeout=45) as res:
            res_json = json.loads(res.read().decode("utf-8"))
            choice = res_json.get("choices", [{}])[0]
            text_out = choice.get("message", {}).get("content", "{}").strip()
            if text_out.startswith("```json"):
                text_out = text_out[7:]
            elif text_out.startswith("```"):
                text_out = text_out[3:]
            if text_out.endswith("```"):
                text_out = text_out[:-3]
            return json.loads(text_out.strip())
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8") if e.fp else str(e)
        raise RuntimeError(f"Groq Vision failed (HTTP {e.code}): {error_body}")
    except Exception as e:
        raise RuntimeError(f"Groq Vision failed: {e}")


def _call_gemini_api(api_key: str, parts: List[Dict[str, Any]], model: str = "gemini-1.5-flash") -> Dict[str, Any]:
    """
    Call the Google Gemini REST API to generate structured content from multimodal parts.
    """
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"

    payload = {
        "contents": [
            {
                "parts": parts
            }
        ],
        "generationConfig": {
            "response_mime_type": "application/json",
            "temperature": 0.2
        }
    }

    req_data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=req_data,
        headers={
            "Content-Type": "application/json",
            "x-goog-api-key": api_key
        },
        method="POST"
    )

    try:
        with urllib.request.urlopen(req, timeout=60) as response:
            res_data = response.read().decode("utf-8")
            res_json = json.loads(res_data)
    except urllib.error.HTTPError as e:
        if e.code in [400, 401]:
            fallback_url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
            req_fallback = urllib.request.Request(
                fallback_url,
                data=req_data,
                headers={"Content-Type": "application/json"},
                method="POST"
            )
            with urllib.request.urlopen(req_fallback, timeout=60) as response:
                res_data = response.read().decode("utf-8")
                res_json = json.loads(res_data)
        else:
            raise

    candidates = res_json.get("candidates", [])
    if not candidates:
        raise ValueError("No response candidates returned by Gemini API.")

    raw_text = candidates[0].get("content", {}).get("parts", [{}])[0].get("text", "{}")

    cleaned_text = raw_text.strip()
    if cleaned_text.startswith("```json"):
        cleaned_text = cleaned_text[7:]
    elif cleaned_text.startswith("```"):
        cleaned_text = cleaned_text[3:]
    if cleaned_text.endswith("```"):
        cleaned_text = cleaned_text[:-3]

    return json.loads(cleaned_text.strip())


def analyze_frames(frame_paths: List[str]) -> Dict[str, Any]:
    """
    Analyze representative frames using Groq Vision (or Gemini Vision).

    Parameters:
        frame_paths (list): List of file paths to extracted video frames.

    Returns:
        dict: Structured visual analysis dictionary matching content profile schema.
    """
    groq_api_key = os.getenv("GROQ_API_KEY", "").strip().strip('"').strip("'")
    gemini_api_key = os.getenv("GEMINI_API_KEY", "").strip().strip('"').strip("'")

    # Check for valid key
    has_groq = bool(groq_api_key and groq_api_key != "gsk_your_groq_key_here")
    has_gemini = bool(gemini_api_key and gemini_api_key != "your_gemini_api_key_here" and not gemini_api_key.startswith("AQ."))

    if not has_groq and not has_gemini and not gemini_api_key:
        print()
        print("   [Vision Service] ⚠️ No API key configured in .env file.")
        print("   [Vision Service] Recommended: Add your Groq API key in .env:")
        print("     1. Get free key at: https://console.groq.com/keys")
        print("     2. Set GROQ_API_KEY=\"gsk_...\" in AI-Virality-Simulator/.env")
        return {
            "topic": "pending (requires GROQ_API_KEY in .env)",
            "category": "pending",
            "scene": "pending",
            "activities": [],
            "objects": [],
            "people": "pending",
            "emotion": "pending",
            "tone": "pending",
            "visual_quality": "pending",
            "summary": "Visual analysis pending: add GROQ_API_KEY to .env to enable real AI vision."
        }

    # Verify existing frames
    valid_frames = [f for f in frame_paths if os.path.isfile(f)]
    if not valid_frames:
        print("   [Vision Service] ⚠️ No valid frame image files found to analyze.")
        return {
            "topic": "unknown",
            "category": "unknown",
            "scene": "unknown",
            "activities": [],
            "objects": [],
            "people": "unknown",
            "emotion": "unknown",
            "tone": "unknown",
            "visual_quality": "unknown",
            "summary": "No extracted frames were available for analysis."
        }

    prompt = (
        "You are an expert video content analyst. Analyze these representative video frames "
        "and evaluate the visual scene, subject matter, activities, and aesthetic tone.\n\n"
        "Return ONLY a valid JSON object matching this exact schema:\n"
        "{\n"
        '  "topic": "Specific topic (e.g., Weightlifting & Gym Workout, Python Programming, Cooking Pasta, Travel Vlog)",\n'
        '  "category": "Broad category (e.g., Fitness & Health, Technology, Food & Drink, Travel, Education, Comedy, Lifestyle)",\n'
        '  "scene": "Specific environment/setting (e.g., Commercial gym, College computer lab, Home kitchen, Outdoor park)",\n'
        '  "activities": ["list", "of", "actions", "taking", "place"],\n'
        '  "objects": ["list", "of", "notable", "visible", "objects"],\n'
        '  "people": "description of visible people (e.g., 1 adult male working out, 2 students in discussion, no people)",\n'
        '  "emotion": "predominant mood or emotional tone (e.g., Focused and determined, Joyful, Educational, Serious)",\n'
        '  "tone": "visual vibe and lighting style (e.g., High-contrast motivational, Natural warm vlog, Clean minimal)",\n'
        '  "visual_quality": "camera quality and framing (e.g., High-definition vertical 4K, clear lighting, well-centered)",\n'
        '  "summary": "2-3 sentence concise description summarizing what happens visually across these frames."\n'
        "}"
    )

    # 1. Try Groq Vision if GROQ_API_KEY is available
    if has_groq:
        print("   [Vision Service] Connecting to Groq Vision AI with video keyframe...")
        try:
            result = _call_groq_vision_api(groq_api_key, prompt, valid_frames)
            print("   [Vision Service] ✓ Successfully analyzed visual content with Groq Vision.")
            return result
        except Exception as e:
            print(f"   [Vision Service] ⚠️ Groq Vision failed: {e}")
            if not has_gemini:
                return {
                    "topic": "pending",
                    "category": "pending",
                    "scene": "pending",
                    "activities": [],
                    "objects": [],
                    "people": "pending",
                    "emotion": "pending",
                    "tone": "pending",
                    "visual_quality": "pending",
                    "summary": f"Groq Vision call failed: {e}"
                }

    # 2. Try Gemini Vision if GEMINI_API_KEY is available
    if has_gemini or gemini_api_key:
        print(f"   [Vision Service] Connecting to Google Gemini Vision with {len(valid_frames)} frames...")
        parts: List[Dict[str, Any]] = [{"text": prompt}]
        for frame_path in valid_frames[:5]:
            try:
                b64_data = _encode_image_to_base64(frame_path)
                parts.append({
                    "inline_data": {
                        "mime_type": "image/jpeg",
                        "data": b64_data
                    }
                })
            except Exception as e:
                print(f"   [Vision Service] Warning: Could not encode frame {frame_path}: {e}")

        models_to_try = ["gemini-1.5-flash", "gemini-2.0-flash"]
        last_error = None
        for model in models_to_try:
            try:
                result = _call_gemini_api(gemini_api_key, parts, model=model)
                print(f"   [Vision Service] ✓ Successfully analyzed visual content with {model}.")
                return result
            except urllib.error.HTTPError as http_err:
                error_msg = http_err.read().decode("utf-8") if http_err.fp else str(http_err)
                last_error = f"HTTP {http_err.code}: {error_msg}"
            except Exception as e:
                last_error = str(e)

        print(f"   [Vision Service] ⚠️ Gemini Vision API call failed: {last_error}")
        return {
            "topic": "pending",
            "category": "pending",
            "scene": "pending",
            "activities": [],
            "objects": [],
            "people": "pending",
            "emotion": "pending",
            "tone": "pending",
            "visual_quality": "pending",
            "summary": f"Visual analysis failed: {last_error}"
        }

    return {
        "topic": "pending",
        "category": "pending",
        "scene": "pending",
        "activities": [],
        "objects": [],
        "people": "pending",
        "emotion": "pending",
        "tone": "pending",
        "visual_quality": "pending",
        "summary": "No active API key found."
    }