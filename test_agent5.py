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

from agents.agent5_report_generator import Agent5ReportGenerator

# Load existing outputs if present, or provide sample mock data
if os.path.exists("outputs/content_profile.json") and os.path.exists("outputs/audience_profile.json") and os.path.exists("outputs/virtual_population.json") and os.path.exists("outputs/engagement_prediction.json"):
    with open("outputs/content_profile.json", "r", encoding="utf-8") as f:
        content_profile = json.load(f)
    with open("outputs/audience_profile.json", "r", encoding="utf-8") as f:
        audience_profile = json.load(f)
    with open("outputs/virtual_population.json", "r", encoding="utf-8") as f:
        population_profile = json.load(f)
    with open("outputs/engagement_prediction.json", "r", encoding="utf-8") as f:
        engagement_prediction = json.load(f)
else:
    content_profile = {
        "agent": {"id": "agent_1", "name": "Video Analysis Agent"},
        "video_metadata": {"duration_seconds": 15.2, "orientation": "vertical"},
        "visual_analysis": {"topic": "Tech Workplace & Student Coding Culture", "summary": "Coding at midnight"},
        "audio_analysis": {"speech_detected": True, "transcript": "Testing late night code"},
        "hook_analysis": {"hook_type": "Visual", "hook_strength": "High"},
        "structure_analysis": {"pacing": "Fast"}
    }
    audience_profile = {
        "content_summary": {"primary_niche": "Tech Workplace & Student Coding Culture"},
        "platform_distribution": [{"platform": "Instagram Reels", "suitability": "Optimal (95%)", "strength": "Viral peer sharing"}],
        "audience_segments": [{"name": "College & Engineering Students", "age_range": "18–24", "relevance_score": 0.94}]
    }
    population_profile = {"population_size": 1000}
    engagement_prediction = {
        "simulation_summary": {
            "population_size": 1000,
            "views": 680,
            "hook_retention_rate": "68.0%",
            "completions": 410,
            "completion_rate": "41.0%",
            "average_watch_time": "9.2s",
            "average_percentage_watched": "60.5%"
        },
        "predicted_engagements": {
            "likes": 92,
            "like_rate": "9.2%",
            "comments": 28,
            "comment_rate": "2.8%",
            "shares": 52,
            "share_rate": "5.2%"
        },
        "retention_curve": {"0s": 1000, "3s": 680, "25%": 550, "50%": 480, "75%": 430, "100%": 410},
        "segment_breakdown": [{"segment_name": "College & Engineering Students", "virality_contribution": "62%"}],
        "virality_verdict": {"virality_score": 64.0, "rating": "STRONG VIRAL POTENTIAL", "algorithm_push_probability": "High", "key_strength": "Relatable developer humor"}
    }


agent5 = Agent5ReportGenerator()
report = agent5.generate(
    content_profile=content_profile,
    audience_profile=audience_profile,
    population_profile=population_profile,
    engagement_prediction=engagement_prediction
)

print("\n" + "=" * 60)
print("📑 AGENT 5 OUTPUT — VIRALITY & CONTENT INTELLIGENCE REPORT")
print("=" * 60)
print(json.dumps(report, indent=4))

# Display Executive Scorecard in Terminal
agent5.print_terminal_summary(report)
