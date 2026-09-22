"""
=========================================================
AGENT 1 — VIDEO ANALYSIS AGENT
=========================================================

Purpose:
    Analyze an uploaded video and generate a structured
    Content Profile.

Input:
    Video file

Output:
    Structured JSON containing video characteristics.

Agent 1 does NOT predict final virality.

It only answers:

    "What is in this video?"

The output of Agent 1 will later be given to Agent 2.
=========================================================
"""


from services.frame_service import (
    get_video_info,
    extract_frames
)

from services.ocr_service import (
    extract_text_from_frames
)

from services.audio_service import (
    check_audio
)

from services.vision_service import (
    analyze_frames
)


class Agent1VideoAnalyzer:
    """
    AGENT 1 — VIDEO ANALYSIS AGENT
    """

    def __init__(self):

        print()
        print("=" * 60)
        print("🤖 AGENT 1 — VIDEO ANALYSIS AGENT")
        print("=" * 60)

        print("Agent 1 initialized successfully.")

    def analyze(self, video_path):

        print()
        print("=" * 60)
        print("🤖 AGENT 1 STARTED")
        print("=" * 60)

        # -------------------------------------------------
        # STEP 1 — VIDEO METADATA
        # -------------------------------------------------

        print()
        print("[Agent 1 - Step 1]")
        print("Analyzing video metadata...")

        video_info = get_video_info(
            video_path
        )

        print("✓ Video metadata extracted.")

        # -------------------------------------------------
        # STEP 2 — FRAME EXTRACTION
        # -------------------------------------------------

        print()
        print("[Agent 1 - Step 2]")
        print("Extracting representative frames...")

        frame_paths = extract_frames(
            video_path,
            output_folder="outputs/frames",
            number_of_frames=5
        )

        print(
            f"✓ {len(frame_paths)} frames extracted."
        )

        # -------------------------------------------------
        # STEP 3 — OCR
        # -------------------------------------------------

        print()
        print("[Agent 1 - Step 3]")
        print("Detecting on-screen text...")

        text_results = extract_text_from_frames(
            frame_paths
        )

        print(
            f"✓ {len(text_results)} text elements detected."
        )

        # -------------------------------------------------
        # STEP 4 — AUDIO
        # -------------------------------------------------

        print()
        print("[Agent 1 - Step 4]")
        print("Analyzing audio...")

        audio_results = check_audio(
            video_path
        )

        print("✓ Audio analysis completed.")

        # -------------------------------------------------
        # STEP 5 — VISUAL ANALYSIS
        # -------------------------------------------------

        print()
        print("[Agent 1 - Step 5]")
        print("Analyzing visual content...")

        visual_results = analyze_frames(
            frame_paths
        )

        print("✓ Visual analysis completed.")

        # -------------------------------------------------
        # STEP 6 — CREATE CONTENT PROFILE
        # -------------------------------------------------

        print()
        print("[Agent 1 - Step 6]")
        print("Creating content profile...")

        content_profile = {

            "agent": {
                "id": "agent_1",
                "name": "Video Analysis Agent"
            },

            "video_metadata": video_info,

            "visual_analysis": visual_results,

            "text_analysis": {
                "text_present": len(text_results) > 0,
                "detected_text": text_results
            },

            "audio_analysis": audio_results,

            "hook_analysis": {
                "status": "pending"
            },

            "structure_analysis": {
                "status": "pending"
            }
        }

        print("✓ Content profile created.")

        # -------------------------------------------------
        # AGENT 1 COMPLETE
        # -------------------------------------------------

        print()
        print("=" * 60)
        print("🤖 AGENT 1 COMPLETED")
        print("=" * 60)

        return content_profile