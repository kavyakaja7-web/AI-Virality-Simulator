import os
import sys
import json

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

from agents.agent1_video_analyzer import Agent1VideoAnalyzer
from agents.agent2_audience_discovery import Agent2AudienceDiscovery
from agents.agent3_population_generator import Agent3PopulationGenerator
from agents.agent4_engagement_predictor import Agent4EngagementPredictor
from agents.agent5_report_generator import Agent5ReportGenerator
from agents.agent6_content_optimizer import Agent6ContentOptimizer
from generate_dashboard import sync_dashboard


def resolve_video_path(preferred_path=None):
    """
    Finds the video to analyze:
    1. Uses preferred_path if passed and exists.
    2. Uses CLI argument if passed: python main.py <path>
    3. Finds the most recent video in the 'videos/' directory.
    """
    if preferred_path and os.path.exists(preferred_path):
        return preferred_path

    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        return sys.argv[1]

    videos_dir = "videos"
    if os.path.exists(videos_dir):
        exts = (".mp4", ".mov", ".avi", ".mkv", ".webm")
        files = [
            os.path.join(videos_dir, f)
            for f in os.listdir(videos_dir)
            if f.lower().endswith(exts)
        ]
        if files:
            # Sort by modification time descending (latest video first)
            files.sort(key=lambda p: os.path.getmtime(p), reverse=True)
            return files[0]

    for fb in ["videos/test4.mp4", "videos/test.mp4", "videos/test3.mp4"]:
        if os.path.exists(fb):
            return fb

    raise FileNotFoundError("No video found in 'videos/' directory. Please place an MP4 file into 'videos/'.")


def run_pipeline(video_path=None):
    video_path = resolve_video_path(video_path)
    file_size_mb = os.path.getsize(video_path) / (1024 * 1024)

    print()
    print("=" * 60)
    print("🚀 STARTING AI VIRALITY SIMULATOR PIPELINE")
    print(f"🎥 TARGET VIDEO: {video_path} ({file_size_mb:.2f} MB)")
    print("=" * 60)

    os.makedirs("outputs", exist_ok=True)
    with open("outputs/active_video.json", "w", encoding="utf-8") as f:
        json.dump({
            "name": os.path.basename(video_path),
            "size_mb": round(file_size_mb, 2),
            "path": video_path
        }, f, indent=4)

    # -------------------------------------------------------
    # AGENT 1: VIDEO CONTENT ANALYSIS
    # -------------------------------------------------------
    agent1 = Agent1VideoAnalyzer()
    content_profile = agent1.analyze(video_path)
    if "video_metadata" in content_profile and isinstance(content_profile["video_metadata"], dict):
        content_profile["video_metadata"]["filename"] = os.path.basename(video_path)
        content_profile["video_metadata"]["video_path"] = video_path

    with open("outputs/content_profile.json", "w", encoding="utf-8") as f:
        json.dump(content_profile, f, indent=4)

    print()
    print("=" * 60)
    print("🤖 AGENT 1 OUTPUT — VIDEO CONTENT PROFILE")
    print("=" * 60)
    print(json.dumps(content_profile, indent=4))
    print("\n[✓ Saved to outputs/content_profile.json]")

    # -------------------------------------------------------
    # AGENT 2: AUDIENCE DISCOVERY
    # -------------------------------------------------------
    agent2 = Agent2AudienceDiscovery()
    audience_profile = agent2.discover(content_profile)

    with open("outputs/audience_profile.json", "w", encoding="utf-8") as f:
        json.dump(audience_profile, f, indent=4)

    print()
    print("=" * 60)
    print("👥 AGENT 2 OUTPUT — DISCOVERED AUDIENCES")
    print("=" * 60)
    print(json.dumps(audience_profile, indent=4))
    print("\n[✓ Saved to outputs/audience_profile.json]")

    # -------------------------------------------------------
    # AGENT 3: VIRTUAL POPULATION GENERATOR
    # -------------------------------------------------------
    agent3 = Agent3PopulationGenerator(population_size=1000)
    population_profile = agent3.generate(audience_profile)

    print()
    print("=" * 60)
    print("👥 AGENT 3 OUTPUT — VIRTUAL POPULATION SUMMARY")
    print("=" * 60)
    print(f"Generated {population_profile['population_size']} virtual users across {len(audience_profile['audience_segments'])} segments.")
    print("\n[✓ Saved to outputs/virtual_population.json]")

    # -------------------------------------------------------
    # AGENT 4: ENGAGEMENT & VIRALITY PREDICTOR
    # -------------------------------------------------------
    agent4 = Agent4EngagementPredictor()
    engagement_prediction = agent4.predict(
        population_profile=population_profile,
        content_profile=content_profile,
        audience_profile=audience_profile
    )

    print()
    print("=" * 60)
    print("📊 AGENT 4 OUTPUT — VIRALITY & ENGAGEMENT PREDICTION")
    print("=" * 60)
    print(json.dumps(engagement_prediction, indent=4))
    print("\n[✓ Saved to outputs/engagement_prediction.json]")

    # -------------------------------------------------------
    # AGENT 5: REPORT GENERATOR
    # -------------------------------------------------------
    agent5 = Agent5ReportGenerator()
    virality_report = agent5.generate(
        content_profile=content_profile,
        audience_profile=audience_profile,
        population_profile=population_profile,
        engagement_prediction=engagement_prediction
    )

    print()
    print("=" * 60)
    print("📑 AGENT 5 OUTPUT — VIRALITY & CONTENT INTELLIGENCE REPORT")
    print("=" * 60)
    print(json.dumps(virality_report, indent=4))
    print("\n[✓ Saved to outputs/virality_report.json]")
    print("[✓ Saved to outputs/VIRALITY_REPORT.md]")
    print("[✓ Saved to outputs/report.html]")

    agent5.print_terminal_summary(virality_report)

    # -------------------------------------------------------
    # AGENT 6: CONTENT OPTIMIZER & VIRAL FIXER
    # -------------------------------------------------------
    agent6 = Agent6ContentOptimizer()
    optimization_plan = agent6.optimize(
        content_profile=content_profile,
        audience_profile=audience_profile,
        population_profile=population_profile,
        engagement_prediction=engagement_prediction,
        virality_report=virality_report
    )

    print()
    print("=" * 60)
    print("🚀 AGENT 6 OUTPUT — VIRAL CONTENT OPTIMIZATION PLAN")
    print("=" * 60)
    print(json.dumps(optimization_plan, indent=4))
    print("\n[✓ Saved to outputs/viral_optimization_plan.json]")
    print("[✓ Saved to outputs/VIRAL_OPTIMIZATION_PLAN.md]")
    print("[✓ Saved to outputs/optimization_dashboard.html]")

    agent6.print_terminal_summary(optimization_plan)

    # Sync interactive dashboard
    sync_dashboard()

    print()
    print("=" * 60)
    print("🎉 AI VIRALITY SIMULATOR PIPELINE COMPLETED (AGENTS 1–6)")
    print("=" * 60)
    print()
    print("🌐 INTERACTIVE DASHBOARD READY:")
    print("   • Direct Browser View: file://" + os.path.abspath("dashboard.html").replace("\\", "/"))
    print("   • Live Web Server:     Run 'python serve.py' to launch on http://localhost:8000/dashboard.html")
    print("=" * 60)

    return {
        "content_profile": content_profile,
        "audience_profile": audience_profile,
        "population_profile": population_profile,
        "engagement_prediction": engagement_prediction,
        "virality_report": virality_report,
        "optimization_plan": optimization_plan
    }


if __name__ == "__main__":
    run_pipeline()