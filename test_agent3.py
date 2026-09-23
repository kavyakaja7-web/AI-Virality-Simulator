import json

from agents.agent3_population_generator import (
    Agent3PopulationGenerator
)


# -------------------------------------------------------
# LOAD AGENT 2 OUTPUT
# -------------------------------------------------------

with open(
    "outputs/audience_profile.json",
    "r",
    encoding="utf-8"
) as file:

    audience_profile = json.load(file)


# -------------------------------------------------------
# CREATE AGENT 3
# -------------------------------------------------------

agent3 = Agent3PopulationGenerator(
    population_size=1000
)


# -------------------------------------------------------
# GENERATE POPULATION
# -------------------------------------------------------

result = agent3.generate(
    audience_profile
)


# -------------------------------------------------------
# SHOW SAMPLE USERS
# -------------------------------------------------------

print()
print("=" * 60)
print("🤖 AGENT 3 OUTPUT")
print("=" * 60)

print(
    "Total users:",
    result["population_size"]
)

print()
print("First 5 virtual users:")

for user in result["users"][:5]:

    print(json.dumps(user, indent=2))
