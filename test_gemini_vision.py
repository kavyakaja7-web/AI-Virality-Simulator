import os
import json
from services.vision_service import analyze_frames

def test_vision():
    frame_dir = "outputs/frames"
    if not os.path.exists(frame_dir):
        print(f"[TEST] Frames directory {frame_dir} not found.")
        return

    frame_files = [
        os.path.join(frame_dir, f)
        for f in sorted(os.listdir(frame_dir))
        if f.endswith((".jpg", ".png"))
    ]

    print(f"[TEST] Found {len(frame_files)} frames: {frame_files}")
    
    result = analyze_frames(frame_files)
    print("\n[TEST RESULT]")
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    test_vision()
