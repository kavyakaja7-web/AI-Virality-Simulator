import os
import json
import base64
import urllib.request
import urllib.error
import cv2
from dotenv import load_dotenv

load_dotenv(override=True)
groq_key = os.getenv("GROQ_API_KEY", "").strip()

url = "https://api.groq.com/openai/v1/chat/completions"

def get_b64(path):
    img = cv2.imread(path)
    h, w = img.shape[:2]
    scale = 1024 / max(h, w)
    img = cv2.resize(img, (int(w * scale), int(h * scale)))
    _, buf = cv2.imencode(".jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), 80])
    return base64.b64encode(buf).decode("utf-8")

# Test with 2 frames
print("--- Test with 2 frames ---")
content_2 = [
    {"type": "text", "text": "Describe these frames briefly in JSON: {\"summary\": \"...\"}"},
    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{get_b64('outputs/frames/frame_1.jpg')}"}},
    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{get_b64('outputs/frames/frame_2.jpg')}"}}
]
payload_2 = {
    "model": "qwen/qwen3.8-27b",
    "messages": [{"role": "user", "content": content_2}],
    "response_format": {"type": "json_object"}
}
req = urllib.request.Request(
    url,
    data=json.dumps(payload_2).encode("utf-8"),
    headers={
        "Authorization": f"Bearer {groq_key}",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    },
    method="POST"
)
try:
    with urllib.request.urlopen(req, timeout=30) as res:
        print("2 frames SUCCESS!")
        print(res.read().decode("utf-8")[:200])
except urllib.error.HTTPError as e:
    print("2 frames FAILED:", e.code, e.read().decode("utf-8"))

# Test with 3 frames
print("\n--- Test with 3 frames ---")
content_3 = content_2 + [
    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{get_b64('outputs/frames/frame_3.jpg')}"}}
]
payload_3 = {
    "model": "qwen/qwen3.8-27b",
    "messages": [{"role": "user", "content": content_3}],
    "response_format": {"type": "json_object"}
}
req3 = urllib.request.Request(
    url,
    data=json.dumps(payload_3).encode("utf-8"),
    headers={
        "Authorization": f"Bearer {groq_key}",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    },
    method="POST"
)
try:
    with urllib.request.urlopen(req3, timeout=30) as res:
        print("3 frames SUCCESS!")
        print(res.read().decode("utf-8")[:200])
except urllib.error.HTTPError as e:
    print("3 frames FAILED:", e.code, e.read().decode("utf-8"))
