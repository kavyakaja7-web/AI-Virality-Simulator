"""
=========================================================
LLM SERVICE — DYNAMIC AI REASONING VIA GROQ & GEMINI
=========================================================

Provides dynamic LLM capabilities (audience segmentation,
virality diagnosis, and strategic recommendations) using
Groq (llama-3.3-70b-versatile / llama-3.1-8b-instant) with
automatic Gemini and rule-based fallbacks.
=========================================================
"""

import os
import json
import urllib.request
import urllib.error
from typing import Dict, Any, Optional
from dotenv import load_dotenv

load_dotenv(override=True)


def call_llm_json(
    prompt: str,
    system_instruction: str = "You are an expert viral content strategist and AI data analyst. Return ONLY a valid JSON object matching the requested schema.",
    preferred_model: str = "llama-3.3-70b-versatile"
) -> Optional[Dict[str, Any]]:
    """
    Call Groq (or Gemini) with strict JSON output formatting.
    Returns parsed dictionary, or None if all API calls fail.
    """
    groq_api_key = os.getenv("GROQ_API_KEY", "").strip().strip('"').strip("'")
    gemini_api_key = os.getenv("GEMINI_API_KEY", "").strip().strip('"').strip("'")

    # 1. Try Groq
    if groq_api_key and groq_api_key != "gsk_your_groq_key_here":
        models_to_try = [preferred_model, "llama-3.1-8b-instant"]
        for model in models_to_try:
            try:
                res_data = _call_groq_chat(groq_api_key, prompt, system_instruction, model=model)
                if res_data:
                    return res_data
            except Exception as e:
                # Try next model
                continue

    # 2. Try Gemini fallback
    if gemini_api_key and gemini_api_key != "your_gemini_api_key_here" and not gemini_api_key.startswith("AQ."):
        try:
            res_data = _call_gemini_json(gemini_api_key, prompt, system_instruction)
            if res_data:
                return res_data
        except Exception:
            pass

    return None


def _call_groq_chat(
    api_key: str,
    prompt: str,
    system_instruction: str,
    model: str = "llama-3.3-70b-versatile"
) -> Dict[str, Any]:
    url = "https://api.groq.com/openai/v1/chat/completions"
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": prompt}
        ],
        "response_format": {"type": "json_object"},
        "temperature": 0.3
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

    with urllib.request.urlopen(req, timeout=30) as response:
        data = json.loads(response.read().decode("utf-8"))
        raw_text = data.get("choices", [{}])[0].get("message", {}).get("content", "{}").strip()
        cleaned = _clean_json_text(raw_text)
        return json.loads(cleaned)


def _call_gemini_json(api_key: str, prompt: str, system_instruction: str) -> Dict[str, Any]:
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": f"{system_instruction}\n\nTask:\n{prompt}"}
                ]
            }
        ],
        "generationConfig": {
            "response_mime_type": "application/json",
            "temperature": 0.3
        }
    }

    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    with urllib.request.urlopen(req, timeout=30) as response:
        data = json.loads(response.read().decode("utf-8"))
        candidates = data.get("candidates", [])
        if candidates:
            raw_text = candidates[0].get("content", {}).get("parts", [{}])[0].get("text", "{}")
            cleaned = _clean_json_text(raw_text)
            return json.loads(cleaned)
    return {}


def _clean_json_text(text: str) -> str:
    text = text.strip()
    if text.startswith("```json"):
        text = text[7:]
    elif text.startswith("```"):
        text = text[3:]
    if text.endswith("```"):
        text = text[:-3]
    return text.strip()
