import json
from agents.agent5_report_generator import Agent5ReportGenerator

# Load existing outputs from agents 1, 2, 3, and 4
with open("outputs/content_profile.json", "r", encoding="utf-8") as f:
    content_profile = json.load(f)

with open("outputs/audience_profile.json", "r", encoding="utf-8") as f:
    audience_profile = json.load(f)

with open("outputs/virtual_population.json", "r", encoding="utf-8") as f:
    population_profile = json.load(f)

with open("outputs/engagement_prediction.json", "r", encoding="utf-8") as f:
    engagement_prediction = json.load(f)

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
