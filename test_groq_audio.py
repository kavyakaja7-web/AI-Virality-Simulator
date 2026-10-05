import os
import json
import secrets
import urllib.request
import urllib.error
from dotenv import load_dotenv

load_dotenv(override=True)
groq_key = os.getenv("GROQ_API_KEY", "").strip()

print("Groq key loaded:", bool(groq_key), "Length:", len(groq_key))
video_path = "videos/test2.mp4"

if not os.path.exists(video_path):
    print("Video does not exist:", video_path)
    exit(1)

file_size = os.path.getsize(video_path)
print(f"Video file: {video_path}, Size: {file_size} bytes ({round(file_size/(1024*1024), 2)} MB)")

url = "https://api.groq.com/openai/v1/audio/transcriptions"
boundary = "----WebKitFormBoundary" + secrets.token_hex(16)

with open(video_path, "rb") as f:
    video_bytes = f.read()

body = bytearray()
# model field
body.extend(f'--{boundary}\r\nContent-Disposition: form-data; name="model"\r\n\r\nwhisper-large-v3\r\n'.encode('utf-8'))
# response_format field
body.extend(f'--{boundary}\r\nContent-Disposition: form-data; name="response_format"\r\n\r\nverbose_json\r\n'.encode('utf-8'))
# file field
filename = os.path.basename(video_path)
body.extend(f'--{boundary}\r\nContent-Disposition: form-data; name="file"; filename="{filename}"\r\nContent-Type: video/mp4\r\n\r\n'.encode('utf-8'))
body.extend(video_bytes)
body.extend(f'\r\n--{boundary}--\r\n'.encode('utf-8'))

req = urllib.request.Request(
    url,
    data=bytes(body),
    headers={
        "Authorization": f"Bearer {groq_key}",
        "Content-Type": f"multipart/form-data; boundary={boundary}"
    },
    method="POST"
)

try:
    print("Sending request to Groq Whisper API...")
    with urllib.request.urlopen(req, timeout=60) as resp:
        res_data = json.loads(resp.read().decode("utf-8"))
        print("\n[SUCCESS] Groq Whisper Output:")
        print(json.dumps(res_data, indent=2))
except urllib.error.HTTPError as e:
    err = e.read().decode("utf-8") if e.fp else str(e)
    print(f"\n[HTTP ERROR {e.code}]: {err}")
except Exception as e:
    print(f"\n[ERROR]: {e}")
