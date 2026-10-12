"""
=========================================================
GENERATE_DASHBOARD.PY — REFRESH DASHBOARD ASSETS
=========================================================

Utility script to ensure dashboard.html and outputs/dashboard.html
are synchronized with the latest simulation run artifacts.
=========================================================
"""

import os
import sys
import shutil

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def sync_dashboard():
    src = "dashboard.html"
    dst = os.path.join("outputs", "dashboard.html")
    if os.path.exists(src):
        os.makedirs("outputs", exist_ok=True)
        shutil.copyfile(src, dst)
        print(f"✓ Dashboard synchronized successfully -> {dst}")
        return dst
    else:
        print(f"❌ Error: {src} not found.")
        return None

if __name__ == "__main__":
    sync_dashboard()
