import json
from services.audio_service import check_audio

video_path = "videos/test2.mp4"
print(f"Testing audio service on: {video_path}")

result = check_audio(video_path)
print("\n" + "=" * 50)
print("AUDIO ANALYSIS RESULT:")
print("=" * 50)
print(json.dumps(result, indent=2))
