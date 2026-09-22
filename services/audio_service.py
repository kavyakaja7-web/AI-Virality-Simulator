import cv2


def check_audio(video_path):
    """
    Basic audio analysis placeholder.

    OpenCV is mainly used for video frames,
    so detailed audio analysis will be added later
    using an audio processing library.
    """

    video = cv2.VideoCapture(video_path)

    if not video.isOpened():
        raise ValueError("Could not open video.")

    video.release()

    return {
        "audio_analysis_status": "pending",
        "speech": "pending",
        "music": "pending",
        "sound_effects": "pending",
        "transcript": "pending"
    }