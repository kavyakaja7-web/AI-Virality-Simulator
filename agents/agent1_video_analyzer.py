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
        # STEP 6 — HOOK & STRUCTURE ANALYSIS
        # -------------------------------------------------

        print()
        print("[Agent 1 - Step 6]")
        print("Evaluating hook and narrative structure...")

        hook_info = self._analyze_hook(text_results, audio_results, visual_results)
        structure_info = self._analyze_structure(video_info, text_results, audio_results)

        print("✓ Hook and structure evaluated.")

        # -------------------------------------------------
        # STEP 7 — CREATE CONTENT PROFILE
        # -------------------------------------------------

        print()
        print("[Agent 1 - Step 7]")
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

            "hook_analysis": hook_info,

            "structure_analysis": structure_info
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

    def _analyze_hook(self, text_results, audio_results, visual_results):
        transcript = audio_results.get("transcript", "")
        has_spoken_words = audio_results.get("speech_detected", False)
        first_frame_text = [t.get("text", "") for t in text_results if "frame_1" in t.get("frame", "")]

        hook_elements = []
        if first_frame_text:
            hook_elements.append(f"On-screen text: '{first_frame_text[0]}'")
        if has_spoken_words and transcript and transcript != "(No spoken words detected in video)":
            words = transcript.split()
            first_words = " ".join(words[:8])
            hook_elements.append(f"Spoken opening: '{first_words}...'")

        scene = visual_results.get("scene", "visual action")
        strength = "Strong" if (first_frame_text or has_spoken_words) else "Moderate"
        hook_type = "Spoken Dialogue Hook" if has_spoken_words else ("Text Banner Hook" if first_frame_text else "Visual Action Hook")

        return {
            "status": "completed",
            "hook_type": hook_type,
            "hook_strength": strength,
            "primary_cues": hook_elements if hook_elements else [f"Visual opening depicting {scene}"],
            "evaluation": "Clear opening stimuli anchoring viewer attention in the first 3 seconds." if strength == "Strong" else "Subtle opening; adding bold on-screen captions or spoken hook would further boost 3-second retention."
        }

    def _analyze_structure(self, video_info, text_results, audio_results):
        duration = video_info.get("duration_seconds", 0)
        has_speech = audio_results.get("speech_detected", False)

        if duration <= 15:
            format_type = "Micro-Short (Fast High Pacing)"
        elif duration <= 60:
            format_type = "Standard Short-Form (High Engagement)"
        else:
            format_type = "Long-Form Deep Dive"

        pacing = "Fast and punchy" if duration <= 30 else "Steady narrative"
        if duration <= 15:
            rec = f"Micro-short length ({duration:.1f}s) is primed for seamless rewatch loops and rapid algorithmic swipe-feed testing."
        elif duration <= 60:
            rec = f"Optimal short-form duration ({duration:.1f}s) for Reels/TikTok/Shorts. Pacing ({pacing.lower()}) sustains viewer momentum through the climax."
        else:
            rec = f"Extended duration ({duration:.1f}s) requires strong chapter markers and visual resets every 8–10 seconds to combat mid-video drop-off."

        return {
            "status": "completed",
            "pacing": pacing,
            "format_category": format_type,
            "storytelling_mode": "Audiovisual demonstration" if has_speech else "Visual-led observational content",
            "retention_recommendation": rec
        }