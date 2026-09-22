import cv2
import os


def get_video_info(video_path):
    """
    Get basic information about the video.
    """

    video = cv2.VideoCapture(video_path)

    if not video.isOpened():
        raise ValueError("Could not open video.")

    fps = video.get(cv2.CAP_PROP_FPS)
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    if fps == 0:
        video.release()
        raise ValueError("Invalid FPS.")

    duration = total_frames / fps

    # Determine orientation
    if height > width:
        orientation = "vertical"
    elif width > height:
        orientation = "horizontal"
    else:
        orientation = "square"

    video.release()

    return {
        "duration_seconds": round(duration, 2),
        "fps": round(fps, 2),
        "total_frames": total_frames,
        "width": width,
        "height": height,
        "resolution": f"{width}x{height}",
        "orientation": orientation
    }


def extract_frames(
    video_path,
    output_folder="outputs/frames",
    number_of_frames=5
):
    """
    Extract representative frames from the video.
    """

    os.makedirs(output_folder, exist_ok=True)

    video = cv2.VideoCapture(video_path)

    if not video.isOpened():
        raise ValueError("Could not open video.")

    total_frames = int(
        video.get(cv2.CAP_PROP_FRAME_COUNT)
    )

    if total_frames == 0:
        video.release()
        raise ValueError("Video contains no frames.")

    frame_paths = []

    for i in range(number_of_frames):

        # Select frames from different parts of the video
        frame_position = int(
            i * (total_frames - 1) / (number_of_frames - 1)
        )

        video.set(
            cv2.CAP_PROP_POS_FRAMES,
            frame_position
        )

        success, frame = video.read()

        if success:

            file_path = os.path.join(
                output_folder,
                f"frame_{i + 1}.jpg"
            )

            cv2.imwrite(
                file_path,
                frame
            )

            frame_paths.append(file_path)

    video.release()

    return frame_paths