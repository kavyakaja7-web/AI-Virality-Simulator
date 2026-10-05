try:
    import easyocr
    EASYOCR_AVAILABLE = True
except ImportError:
    easyocr = None
    EASYOCR_AVAILABLE = False


# Lazy-loaded OCR reader
reader = None


def get_reader():
    global reader
    if not EASYOCR_AVAILABLE:
        return None
    if reader is None:
        print("   [EasyOCR] Initializing OCR model (downloading model weights if first time)...", flush=True)
        reader = easyocr.Reader(["en"])
    return reader


def extract_text_from_frames(frame_paths):
    """
    Detect text appearing inside video frames.
    """
    if not EASYOCR_AVAILABLE:
        print("   [EasyOCR] ⚠️ 'easyocr' is not installed in the active Python environment. Skipping OCR text extraction.")
        return []

    ocr_reader = get_reader()
    if ocr_reader is None:
        return []

    detected_text = []

    for frame_path in frame_paths:
        try:
            results = ocr_reader.readtext(frame_path)
        except Exception as e:
            print(f"   [EasyOCR] Warning: Failed to extract text from {frame_path}: {e}")
            continue

        for result in results:
            text = result[1]
            confidence = float(result[2])

            if confidence >= 0.40:
                detected_text.append({
                    "text": text,
                    "confidence": round(confidence, 2),
                    "frame": frame_path
                })

    return detected_text