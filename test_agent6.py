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

from agents.agent6_content_optimizer import Agent6ContentOptimizer


def test_agent_6():
    print("Testing Agent 6 (Content Optimizer & Viral Fixer)...")

    # If outputs exist from previous pipeline runs, load them; otherwise use realistic test fixtures
    if os.path.exists("outputs/content_profile.json") and os.path.exists("outputs/audience_profile.json"):
        with open("outputs/content_profile.json", "r", encoding="utf-8") as f:
            content_profile = json.load(f)
        with open("outputs/audience_profile.json", "r", encoding="utf-8") as f:
            audience_profile = json.load(f)
        
        population_profile = None
        if os.path.exists("outputs/virtual_population.json"):
            with open("outputs/virtual_population.json", "r", encoding="utf-8") as f:
                population_profile = json.load(f)

        engagement_prediction = None
        if os.path.exists("outputs/engagement_prediction.json"):
            with open("outputs/engagement_prediction.json", "r", encoding="utf-8") as f:
                engagement_prediction = json.load(f)

        virality_report = None
        if os.path.exists("outputs/virality_report.json"):
            with open("outputs/virality_report.json", "r", encoding="utf-8") as f:
                virality_report = json.load(f)
    else:
        # Realistic sample profiles for standalone testing
        content_profile = {
            "agent": {"id": "agent_1", "name": "Video Analysis Agent"},
            "video_metadata": {
                "duration_seconds": 15.2,
                "orientation": "vertical",
                "resolution": "1080x1920"
            },
            "visual_analysis": {
                "topic": "Casual Office / Computer Lab Scene",
                "scene": "Indoor office cubicle with computer monitors and people working",
                "objects": ["Computer monitor", "Desk", "Office chair", "Ceiling fan"],
                "activities": ["Coding", "Looking at monitor", "Standing near cubicle"],
                "summary": "A developer standing near a cubicle in a tech office computer lab."
            },
            "audio_analysis": {
                "speech_detected": True,
                "transcript": "When the code finally works at 2am and you don't even know why."
            },
            "hook_analysis": {
                "hook_type": "Visual / Candid",
                "hook_strength": "Moderate",
                "pacing": "Normal"
            }
        }

        audience_profile = {
            "agent": {"id": "agent_2", "name": "Audience Discovery Agent"},
            "content_summary": {
                "primary_niche": "Tech Workplace & Student Coding Culture"
            },
            "audience_segments": [
                {
                    "name": "College & Engineering Students",
                    "age_range": "18–24",
                    "relevance_score": 0.94
                },
                {
                    "name": "Early-Career Software Engineers",
                    "age_range": "22–29",
                    "relevance_score": 0.88
                }
            ],
            "platform_distribution": [
                {
                    "platform": "Instagram Reels",
                    "suitability": "Optimal (95%)",
                    "strength": "High peer-to-peer shareability via DMs"
                },
                {
                    "platform": "TikTok",
                    "suitability": "Optimal (91%)",
                    "strength": "Relatable coding meme virality on FYP"
                }
            ]
        }

        engagement_prediction = {
            "simulation_summary": {
                "population_size": 1000,
                "views": 640,
                "hook_retention_rate": "64.0%",
                "completions": 382,
                "completion_rate": "38.2%",
                "share_rate": "4.2%"
            },
            "predicted_engagements": {
                "likes": 84,
                "like_rate": "8.4%",
                "comments": 22,
                "comment_rate": "2.2%",
                "shares": 42,
                "share_rate": "4.2%"
            },
            "virality_verdict": {
                "virality_score": 58.0,
                "rating": "MODERATE VIRALITY"
            }
        }
        population_profile = None
        virality_report = None

    agent6 = Agent6ContentOptimizer()
    plan = agent6.optimize(
        content_profile=content_profile,
        audience_profile=audience_profile,
        population_profile=population_profile,
        engagement_prediction=engagement_prediction,
        virality_report=virality_report
    )

    # Assertions
    assert "hook_rewrites" in plan, "Plan must contain hook_rewrites"
    assert len(plan["hook_rewrites"]) >= 3, "Plan must contain at least 3 hook rewrites"
    assert "scene_cut_blueprint" in plan, "Plan must contain scene_cut_blueprint"
    assert "platform_packaging" in plan, "Plan must contain platform_packaging"
    assert "projected_uplift" in plan, "Plan must contain projected_uplift"
    assert float(plan["projected_uplift"]["projected_virality_score"]) > float(plan["projected_uplift"]["baseline_virality_score"])

    # Verify generated files
    assert os.path.exists("outputs/viral_optimization_plan.json"), "JSON output must exist"
    assert os.path.exists("outputs/VIRAL_OPTIMIZATION_PLAN.md"), "Markdown output must exist"
    assert os.path.exists("outputs/optimization_dashboard.html"), "HTML dashboard must exist"

    print("\n" + "=" * 60)
    print("🚀 AGENT 6 TERMINAL SCORECARD")
    print("=" * 60)
    agent6.print_terminal_summary(plan)

    print("\n[SUCCESS] Agent 6 executed and verified successfully!")

if __name__ == "__main__":
    test_agent_6()
