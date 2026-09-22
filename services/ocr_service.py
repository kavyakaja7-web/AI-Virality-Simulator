import easyocr


# Create OCR reader
reader = easyocr.Reader(["en"])


def extract_text_from_frames(frame_paths):
    """
    Detect text appearing inside video frames.
    """

    detected_text = []

    for frame_path in frame_paths:

        results = reader.readtext(frame_path)

        for result in results:

            text = result[1]
            confidence = float(result[2])

            if confidence >= 0.40:

                detected_text.append({
                    "text": text,
                    "confidence": round(
                        confidence,
                        2
                    ),
                    "frame": frame_path
                })

    return detected_text