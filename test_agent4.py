import json
from agents.agent4_engagement_predictor import Agent4EngagementPredictor

def test_agent_4():
    print("Testing Agent 4 independently...")

    # Sample Population (Agent 3 output format)
    sample_population_profile = {
        "agent": {"id": "agent_3", "name": "Virtual Population Generator"},
        "population_size": 100,
        "users": [
            {
                "user_id": i + 1,
                "segment_id": 1 if i < 60 else 2,
                "segment_name": "College & Engineering Students" if i < 60 else "General Viewers",
                "age": 20 if i < 60 else 30,
                "interests": ["Coding", "Tech"],
                "relevance_score": 0.90 if i < 60 else 0.40,
                "behavior": {
                    "watch_tendency": 0.85 if i < 60 else 0.45,
                    "completion_tendency": 0.80 if i < 60 else 0.35,
                    "like_tendency": 0.45 if i < 60 else 0.15,
                    "comment_tendency": 0.20 if i < 60 else 0.05,
                    "share_tendency": 0.25 if i < 60 else 0.02
                }
            }
            for i in range(100)
        ]
    }

    # Sample Content Profile (Agent 1 output format)
    sample_content_profile = {
        "video_metadata": {
            "duration_seconds": 15.2,
            "orientation": "vertical"
        },
        "text_analysis": {
            "text_present": True
        }
    }

    agent4 = Agent4EngagementPredictor()
    result = agent4.predict(
        population_profile=sample_population_profile,
        content_profile=sample_content_profile
    )

    print("\n--- TEST PREDICTION RESULTS ---")
    print(json.dumps(result["simulation_summary"], indent=2))
    print(json.dumps(result["predicted_engagements"], indent=2))
    print(json.dumps(result["virality_verdict"], indent=2))

    assert "virality_score" in result["virality_verdict"]
    assert len(result["segment_breakdown"]) == 2
    assert "retention_curve" in result

    print("\n[SUCCESS] Agent 4 tests passed successfully!")

if __name__ == "__main__":
    test_agent_4()
