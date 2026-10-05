import os
import sys
import subprocess

print("Python:", sys.executable)

# Check imageio_ffmpeg
try:
    import imageio_ffmpeg
    print("imageio_ffmpeg found:", imageio_ffmpeg.get_ffmpeg_exe())
except Exception as e:
    print("imageio_ffmpeg error:", e)

# Check ffmpeg in PATH
try:
    res = subprocess.run(["ffmpeg", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print("ffmpeg in PATH found! Code:", res.returncode)
except Exception as e:
    print("ffmpeg in PATH error:", e)

# Check moviepy
try:
    import moviepy
    print("moviepy found:", moviepy)
except Exception as e:
    print("moviepy not found:", e)
