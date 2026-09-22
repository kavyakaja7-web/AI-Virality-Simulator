import cv2
import numpy as np
import os

def create_sample_video():
    os.makedirs("videos", exist_ok=True)
    output_path = os.path.join("videos", "test.mp4")

    # Video specifications
    width, height = 720, 1280  # Vertical 9:16 format (Reels/Shorts/TikTok)
    fps = 30
    duration_seconds = 5
    total_frames = fps * duration_seconds

    # Use MP4V codec for maximum cross-platform OpenCV compatibility
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    if not writer.isOpened():
        print("Error: Could not create VideoWriter with mp4v. Trying fallback...")
        fourcc = cv2.VideoWriter_fourcc(*"XVID")
        writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    print(f"Generating sample video ({width}x{height}, {fps} FPS, {duration_seconds}s)...")

    messages = [
        "VIRAL AI SIMULATOR",
        "HOW TO GO VIRAL IN 2026",
        "SECRET HOOK STRATEGY",
        "ENGAGEMENT SKYROCKETING",
        "WATCH UNTIL THE END"
    ]

    for frame_idx in range(total_frames):
        # Determine background color based on progress (smooth color transition)
        progress = frame_idx / total_frames
        b = int(30 + 100 * (1 - progress))
        g = int(20 + 80 * progress)
        r = int(70 + 150 * np.sin(progress * np.pi))

        frame = np.full((height, width, 3), (b, g, r), dtype=np.uint8)

        # Message index corresponding to 5 segments
        msg_idx = min(int(progress * len(messages)), len(messages) - 1)
        headline = messages[msg_idx]

        # Draw a banner box
        cv2.rectangle(frame, (40, 480), (680, 620), (0, 0, 0), -1)
        cv2.rectangle(frame, (40, 480), (680, 620), (0, 215, 255), 3)

        # Text overlay
        cv2.putText(
            frame,
            headline,
            (60, 560),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (255, 255, 255),
            2,
            cv2.LINE_AA
        )

        # Subtitle
        sub_text = f"Sample Frame {frame_idx + 1}/{total_frames}"
        cv2.putText(
            frame,
            sub_text,
            (60, 600),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 215, 255),
            1,
            cv2.LINE_AA
        )

        # Bottom Call-To-Action
        cv2.putText(
            frame,
            "FOLLOW FOR MORE",
            (200, 1100),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.0,
            (255, 255, 255),
            2,
            cv2.LINE_AA
        )

        writer.write(frame)

    writer.release()
    print(f"[SUCCESS] Sample video created successfully at: {output_path}")

if __name__ == "__main__":
    create_sample_video()
