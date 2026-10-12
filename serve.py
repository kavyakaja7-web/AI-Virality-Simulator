"""
=========================================================
SERVE.PY — LAUNCH AI VIRALITY SIMULATOR DASHBOARD & API
=========================================================

Starts a local HTTP server that:
1. Serves dashboard.html and visual simulation artifacts.
2. Provides an interactive API to upload videos and trigger
   the complete 6-Agent pipeline directly from the UI.
=========================================================
"""

import os
import sys
import json
import webbrowser
import http.server
import socketserver

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

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))


class ViralityStudioHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        if self.path == "/api/current_video":
            from main import resolve_video_path
            try:
                curr = resolve_video_path()
                size_mb = os.path.getsize(curr) / (1024 * 1024)
                name = os.path.basename(curr)
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"status": "ok", "video": name, "size_mb": round(size_mb, 2), "path": curr}).encode("utf-8"))
            except Exception as e:
                self.send_response(500)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"status": "error", "message": str(e)}).encode("utf-8"))
            return

        elif self.path == "/api/list_videos":
            videos_dir = os.path.join(DIRECTORY, "videos")
            result = []
            if os.path.exists(videos_dir):
                exts = (".mp4", ".mov", ".avi", ".mkv", ".webm")
                for f in os.listdir(videos_dir):
                    if f.lower().endswith(exts):
                        fpath = os.path.join(videos_dir, f)
                        result.append({
                            "name": f,
                            "size_mb": round(os.path.getsize(fpath) / (1024 * 1024), 2),
                            "mtime": os.path.getmtime(fpath)
                        })
                result.sort(key=lambda x: x["mtime"], reverse=True)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "ok", "videos": result}).encode("utf-8"))
            return
        elif self.path == "/api/latest_results":
            outputs_dir = os.path.join(DIRECTORY, "outputs")
            data = {}
            for fname in ["content_profile.json", "audience_profile.json", "virtual_population.json", "engagement_prediction.json", "virality_report.json", "viral_optimization_plan.json"]:
                fpath = os.path.join(outputs_dir, fname)
                key = fname.replace(".json", "")
                if os.path.exists(fpath):
                    try:
                        with open(fpath, "r", encoding="utf-8") as f:
                            data[key] = json.load(f)
                    except Exception:
                        data[key] = {}
                else:
                    data[key] = {}
            
            av_file = os.path.join(DIRECTORY, "outputs", "active_video.json")
            if os.path.exists(av_file):
                try:
                    with open(av_file, "r", encoding="utf-8") as f:
                        data["active_video"] = json.load(f)
                except Exception:
                    pass

            if not data.get("active_video"):
                cp_meta = data.get("content_profile", {}).get("video_metadata", {})
                candidate_name = cp_meta.get("filename") or (os.path.basename(cp_meta.get("video_path", "")) if cp_meta.get("video_path") else None)
                if candidate_name and os.path.exists(os.path.join(DIRECTORY, "videos", candidate_name)):
                    target_path = os.path.join(DIRECTORY, "videos", candidate_name)
                    size_mb = os.path.getsize(target_path) / (1024 * 1024)
                    data["active_video"] = {"name": candidate_name, "size_mb": round(size_mb, 2), "path": target_path}
                else:
                    from main import resolve_video_path
                    try:
                        curr = resolve_video_path()
                        size_mb = os.path.getsize(curr) / (1024 * 1024)
                        name = os.path.basename(curr)
                        data["active_video"] = {"name": name, "size_mb": round(size_mb, 2), "path": curr}
                    except Exception:
                        data["active_video"] = {"name": "test4.mp4", "size_mb": 6.33}

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "ok", "data": data}).encode("utf-8"))
            return

        super().do_GET()

    def do_POST(self):
        if self.path == "/api/upload":
            raw_filename = self.headers.get("X-Filename", "uploaded_video.mp4")
            filename = os.path.basename(raw_filename)
            while filename.lower().endswith(".mp4.mp4"):
                filename = filename[:-4]
            if not filename.lower().endswith((".mp4", ".mov", ".avi", ".mkv", ".webm")):
                filename += ".mp4"

            save_path = os.path.join(DIRECTORY, "videos", filename)
            os.makedirs(os.path.dirname(save_path), exist_ok=True)

            content_length = int(self.headers.get("Content-Length", 0))
            print(f"\n[Server] Receiving new video upload: {filename} ({content_length / (1024 * 1024):.2f} MB)...")

            with open(save_path, "wb") as f:
                remaining = content_length
                while remaining > 0:
                    chunk = self.rfile.read(min(remaining, 65536))
                    if not chunk:
                        break
                    f.write(chunk)
                    remaining -= len(chunk)

            print(f"[Server] ✓ Saved video to {save_path}. Executing 6-Agent pipeline...")

            try:
                from main import run_pipeline
                run_pipeline(save_path)
                
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({
                    "status": "success",
                    "message": "Pipeline completed successfully!",
                    "video": filename
                }).encode("utf-8"))
            except Exception as e:
                print(f"[Server] ❌ Pipeline execution error: {e}")
                self.send_response(500)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({
                    "status": "error",
                    "message": str(e)
                }).encode("utf-8"))
            return

        elif self.path == "/api/run_pipeline":
            print("\n[Server] Re-running 6-Agent pipeline on active video...")
            try:
                from main import run_pipeline
                run_pipeline()
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({
                    "status": "success",
                    "message": "Pipeline completed successfully!"
                }).encode("utf-8"))
            except Exception as e:
                self.send_response(500)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
        elif self.path == "/api/select_video":
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length).decode("utf-8") if content_length > 0 else "{}"
            try:
                data = json.loads(body)
                video_name = data.get("video")
                target_path = os.path.join(DIRECTORY, "videos", video_name)
                if not os.path.exists(target_path):
                    self.send_response(404)
                    self.send_header("Content-Type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps({"status": "error", "message": f"Video {video_name} not found"}).encode("utf-8"))
                    return

                print(f"\n[Server] Switching to video: {video_name} and running pipeline...")
                from main import run_pipeline
                run_pipeline(target_path)
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"status": "success", "video": video_name}).encode("utf-8"))
            except Exception as e:
                self.send_response(500)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"status": "error", "message": str(e)}).encode("utf-8"))
            return

        self.send_response(404)
        self.end_headers()


def run():
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), ViralityStudioHandler) as httpd:
        url = f"http://localhost:{PORT}/dashboard.html"
        print()
        print("=" * 66)
        print("🚀 AI VIRALITY SIMULATOR — AUTONOMOUS DASHBOARD & API SERVER")
        print("=" * 66)
        print(f"  🌐 URL:               {url}")
        print("  📤 Upload Endpoint:   POST /api/upload (Interactive in Web UI)")
        print("  ⚡ Press Ctrl+C in terminal to stop the server.")
        print("=" * 66)
        print()

        webbrowser.open(url)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server. Goodbye!")


if __name__ == "__main__":
    run()
