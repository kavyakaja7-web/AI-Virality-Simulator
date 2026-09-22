import easyocr


# Lazy-loaded OCR reader
reader = None


def get_reader():
    global reader
    if reader is None:
        print("   [EasyOCR] Initializing OCR model (downloading model weights if first time)...", flush=True)
        reader = easyocr.Reader(["en"])
    return reader


def extract_text_from_frames(frame_paths):
    """
    Detect text appearing inside video frames.
    """
    ocr_reader = get_reader()
    detected_text = []

    for frame_path in frame_paths:

        results = ocr_reader.readtext(frame_path)

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