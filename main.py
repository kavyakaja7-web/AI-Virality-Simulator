import os
import json

from agents.agent1_video_analyzer import Agent1VideoAnalyzer
from agents.agent2_audience_discovery import Agent2AudienceDiscovery
from agents.agent3_population_generator import Agent3PopulationGenerator
from agents.agent4_engagement_predictor import Agent4EngagementPredictor
from agents.agent5_report_generator import Agent5ReportGenerator


# -------------------------------------------------------
# VIDEO INPUT
# -------------------------------------------------------

VIDEO_PATH = "videos/test3.mp4"


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
print("Sample Virtual User:")
if population_profile.get("users"):
    print(json.dumps(population_profile["users"][0], indent=4))
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

# Display Executive Scorecard in Terminal
agent5.print_terminal_summary(virality_report)


print()
print("=" * 60)
print("🎉 AI VIRALITY SIMULATOR PIPELINE COMPLETED (AGENTS 1–5)")
print("=" * 60)