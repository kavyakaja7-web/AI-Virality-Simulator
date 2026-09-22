import urllib.request
import urllib.error
import json
import os
from dotenv import load_dotenv

load_dotenv(override=True)

groq_key = os.getenv("GROQ_API_KEY", "").strip().strip('"').strip("'")
gemini_key = os.getenv("GEMINI_API_KEY", "").strip().strip('"').strip("'")

print("=" * 60)
print("🔑 API KEY DIAGNOSTIC TEST")
print("=" * 60)

# -------------------------------------------------------------
# TEST GROQ API KEY
# -------------------------------------------------------------
if groq_key and groq_key != "gsk_your_groq_key_here":
    print(f"\n[GROQ] Testing Key: {groq_key[:6]}...{groq_key[-4:]} (Length: {len(groq_key)})")
    try:
        req = urllib.request.Request(
            "https://api.groq.com/openai/v1/models",
            headers={
                "Authorization": f"Bearer {groq_key}",
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            }
        )
        with urllib.request.urlopen(req, timeout=15) as res:
            data = json.loads(res.read().decode("utf-8"))
            models = [m.get("id") for m in data.get("data", [])]
            print(f"✓ SUCCESS! Groq API Key is VALID! ({len(models)} models available)")
            print("All Available Groq Models:")
            for m in sorted(models):
                print(f"  - {m}")
    except urllib.error.HTTPError as e:
        print(f"❌ GROQ ERROR (HTTP {e.code}):", e.read().decode("utf-8"))
    except Exception as e:
        print(f"❌ GROQ ERROR: {e}")
else:
    print("\n[GROQ] No GROQ_API_KEY found in .env.")
    print("       Get free key at: https://console.groq.com/keys")

# -------------------------------------------------------------
# TEST GEMINI API KEY
# -------------------------------------------------------------
if gemini_key and gemini_key != "your_gemini_api_key_here":
    print(f"\n[GEMINI] Testing Key: {gemini_key[:6]}...{gemini_key[-4:]} (Length: {len(gemini_key)})")
    try:
        req = urllib.request.Request(
            "https://generativelanguage.googleapis.com/v1beta/models",
            headers={"x-goog-api-key": gemini_key}
        )
        with urllib.request.urlopen(req, timeout=15) as res:
            data = json.loads(res.read().decode("utf-8"))
            print(f"✓ SUCCESS! Gemini API Key is VALID! ({len(data.get('models', []))} models available)")
    except urllib.error.HTTPError as e:
        print(f"❌ GEMINI ERROR (HTTP {e.code}):", e.read().decode("utf-8"))
    except Exception as e:
        print(f"❌ GEMINI ERROR: {e}")
else:
    print("\n[GEMINI] No GEMINI_API_KEY configured in .env.")

print("\n" + "=" * 60)
