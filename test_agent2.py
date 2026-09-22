import json
from agents.agent2_audience_discovery import Agent2AudienceDiscovery

def test_audience_discovery():
    agent2 = Agent2AudienceDiscovery()

    # Case 1: Travel Video Content Profile (From User's Prompt Example)
    travel_profile = {
        "agent": {"id": "agent_1", "name": "Video Analysis Agent"},
        "video_metadata": {
            "orientation": "vertical",
            "duration_seconds": 25.0,
            "resolution": "1080x1920"
        },
        "text_analysis": {
            "text_present": True,
            "detected_text": [
                {"text": "Budget travel in India", "confidence": 0.95},
                {"text": "Top backpack destinations under 5000", "confidence": 0.88}
            ]
        },
        "visual_analysis": {}
    }

    travel_result = agent2.discover(travel_profile)
    print("\n--- TEST CASE 1: TRAVEL VIDEO ---")
    print(json.dumps(travel_result, indent=2))
    assert len(travel_result["audience_segments"]) >= 3
    assert "Budget" in travel_result["audience_segments"][0]["name"] or "Travel" in travel_result["audience_segments"][0]["name"]

    # Case 2: Computer Science / Lab Video
    tech_profile = {
        "agent": {"id": "agent_1", "name": "Video Analysis Agent"},
        "video_metadata": {
            "orientation": "vertical",
            "duration_seconds": 12.0,
            "resolution": "720x1280"
        },
        "text_analysis": {
            "text_present": True,
            "detected_text": [
                {"text": "Computer Science lab at 10:40", "confidence": 0.92},
                {"text": "Coding python late night", "confidence": 0.85}
            ]
        },
        "visual_analysis": {}
    }

    tech_result = agent2.discover(tech_profile)
    print("\n--- TEST CASE 2: TECH / LAB VIDEO ---")
    print(json.dumps(tech_result, indent=2))
    assert len(tech_result["audience_segments"]) >= 3
    assert "College" in tech_result["audience_segments"][0]["name"] or "Student" in tech_result["audience_segments"][0]["name"]

    print("\n[SUCCESS] All Agent 2 tests passed successfully!")

if __name__ == "__main__":
    test_audience_discovery()
