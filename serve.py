"""
=========================================================
SERVE.PY — LAUNCH AI VIRALITY SIMULATOR DASHBOARD
=========================================================

Starts a lightweight local HTTP server and automatically
opens dashboard.html in your default web browser.
=========================================================
"""

import os
import sys
import webbrowser
import http.server
import socketserver

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def run():
    # Allow port reuse
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}/dashboard.html"
        print()
        print("=" * 64)
        print("🚀 AI VIRALITY SIMULATOR — AUTONOMOUS DASHBOARD ONLINE")
        print("=" * 64)
        print(f"  🌐 URL:  {url}")
        print("  ⚡ Press Ctrl+C in terminal to stop the server.")
        print("=" * 64)
        print()
        
        # Open in default browser
        webbrowser.open(url)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server. Goodbye!")

if __name__ == "__main__":
    run()
