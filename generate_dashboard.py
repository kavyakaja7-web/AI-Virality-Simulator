"""
=========================================================
GENERATE_DASHBOARD.PY — DYNAMIC SIMULATION DATA HYDRATION
=========================================================

Reads all 6 agent outputs from outputs/*.json, builds
a comprehensive simulation payload, and syncs both
dashboard.html and outputs/dashboard.html with fresh data.
=========================================================
"""

import os
import sys
import json
import shutil

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
if hasattr(sys.stderr, "reconfigure"):
    try:
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def get_latest_data():
    outputs_dir = "outputs"
    data = {}
    for fname in [
        "content_profile.json",
        "audience_profile.json",
        "virtual_population.json",
        "engagement_prediction.json",
        "virality_report.json",
        "viral_optimization_plan.json"
    ]:
        fpath = os.path.join(outputs_dir, fname)
        key = fname.replace(".json", "")
        if os.path.exists(fpath):
            try:
                with open(fpath, "r", encoding="utf-8") as f:
                    data[key] = json.load(f)
                    if key == "virtual_population" and isinstance(data[key], dict) and "users" in data[key]:
                        # Keep population_size but only include a small sample of users for dashboard efficiency
                        data[key]["users"] = data[key]["users"][:10]
            except Exception:
                data[key] = {}
        else:
            data[key] = {}

    av_file = os.path.join(outputs_dir, "active_video.json")
    if os.path.exists(av_file):
        try:
            with open(av_file, "r", encoding="utf-8") as f:
                data["active_video"] = json.load(f)
        except Exception:
            pass

    if not data.get("active_video"):
        cp_meta = data.get("content_profile", {}).get("video_metadata", {})
        candidate_name = cp_meta.get("filename") or (os.path.basename(cp_meta.get("video_path", "")) if cp_meta.get("video_path") else None)
        if candidate_name and os.path.exists(os.path.join("videos", candidate_name)):
            target_path = os.path.join("videos", candidate_name)
            size_mb = os.path.getsize(target_path) / (1024 * 1024)
            data["active_video"] = {"name": candidate_name, "size_mb": round(size_mb, 2), "path": target_path}
        else:
            try:
                from main import resolve_video_path
                curr = resolve_video_path()
                size_mb = os.path.getsize(curr) / (1024 * 1024)
                name = os.path.basename(curr)
                data["active_video"] = {"name": name, "size_mb": round(size_mb, 2), "path": curr}
            except Exception:
                data["active_video"] = {"name": "test4.mp4", "size_mb": 6.33}

    return data


def sync_dashboard():
    src = "dashboard.html"
    dst = os.path.join("outputs", "dashboard.html")
    if not os.path.exists(src):
        print(f"❌ Error: {src} not found.")
        return None

    data = get_latest_data()
    data_json_str = json.dumps(data)

    with open(src, "r", encoding="utf-8") as f:
        content = f.read()

    marker_start = "/* SIMULATION_DATA_START */"
    marker_end = "/* SIMULATION_DATA_END */"

    if marker_start in content and marker_end in content:
        before = content.split(marker_start)[0]
        after = content.split(marker_end)[1]
        new_content = before + marker_start + "\n    window.SIMULATION_DATA = " + data_json_str + ";\n    " + marker_end + after
        with open(src, "w", encoding="utf-8") as f:
            f.write(new_content)
        content = new_content

    os.makedirs("outputs", exist_ok=True)
    with open(dst, "w", encoding="utf-8") as f:
        f.write(content)

    try:
        shutil.copyfile(src, "index.html")
    except Exception:
        pass

    active_name = data.get("active_video", {}).get("name", "video")
    score = data.get("virality_report", {}).get("executive_summary", {}).get("virality_score") or data.get("engagement_prediction", {}).get("virality_score", {}).get("score_0_to_100", 0)
    print(f"✓ Dashboard synchronized with real video data [{active_name} | Score: {score}] -> {dst}")
    return dst


if __name__ == "__main__":
    sync_dashboard()
