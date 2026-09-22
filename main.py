import os
import json

from agents.agent1_video_analyzer import Agent1VideoAnalyzer
from agents.agent2_audience_discovery import Agent2AudienceDiscovery


# -------------------------------------------------------
# VIDEO INPUT
# -------------------------------------------------------

VIDEO_PATH = "videos/test.mp4"


# -------------------------------------------------------
# START SIMULATOR
# -------------------------------------------------------

print()
print("=" * 60)
print("🚀 STARTING AI VIRALITY SIMULATOR PIPELINE")
print("=" * 60)

os.makedirs("outputs", exist_ok=True)


# -------------------------------------------------------
# AGENT 1: VIDEO CONTENT ANALYSIS
# -------------------------------------------------------

agent1 = Agent1VideoAnalyzer()
content_profile = agent1.analyze(VIDEO_PATH)

# Save Agent 1 output
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

# Save Agent 2 output
with open("outputs/audience_profile.json", "w", encoding="utf-8") as f:
    json.dump(audience_profile, f, indent=4)

print()
print("=" * 60)
print("👥 AGENT 2 OUTPUT — DISCOVERED AUDIENCES")
print("=" * 60)
print(json.dumps(audience_profile, indent=4))
print("\n[✓ Saved to outputs/audience_profile.json]")


print()
print("=" * 60)
print("🎉 AI VIRALITY SIMULATOR PIPELINE COMPLETED")
print("=" * 60)