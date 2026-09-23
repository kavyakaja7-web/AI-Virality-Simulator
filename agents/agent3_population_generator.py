"""
=========================================================
AGENT 3 — VIRTUAL POPULATION GENERATOR
=========================================================

Purpose:
    Convert Agent 2 audience segments into a synthetic
    virtual population.

Input:
    Agent 2 Audience Profile

Output:
    Synthetic virtual users

Agent 3 does NOT predict engagement.
That is Agent 4's responsibility.
=========================================================
"""

import json
import os

from services.population_service import (
    generate_virtual_population
)


class Agent3PopulationGenerator:
    """
    AGENT 3 — VIRTUAL POPULATION GENERATOR
    """

    def __init__(
        self,
        population_size=1000
    ):

        self.population_size = (
            population_size
        )

        print()
        print("=" * 60)
        print("👥 AGENT 3 — VIRTUAL POPULATION GENERATOR")
        print("=" * 60)

        print(
            f"Population size: "
            f"{self.population_size}"
        )

    def generate(
        self,
        audience_profile
    ):

        print()
        print("=" * 60)
        print("👥 AGENT 3 STARTED")
        print("=" * 60)

        # -------------------------------------------------
        # STEP 1 — Extract audience segments
        # -------------------------------------------------

        print()
        print("[Agent 3 - Step 1]")
        print(
            "Reading audience segments..."
        )

        audience_segments = (
            audience_profile.get(
                "audience_segments",
                []
            )
        )

        print(
            f"✓ "
            f"{len(audience_segments)} "
            f"audience segments loaded."
        )

        if not audience_segments:

            raise ValueError(
                "Agent 2 did not provide "
                "any audience segments."
            )

        # -------------------------------------------------
        # STEP 2 — Generate population
        # -------------------------------------------------

        print()
        print("[Agent 3 - Step 2]")
        print(
            "Generating virtual population..."
        )

        population = (
            generate_virtual_population(
                audience_segments,
                self.population_size
            )
        )

        print(
            f"✓ Generated "
            f"{len(population)} "
            f"virtual users."
        )

        # -------------------------------------------------
        # STEP 3 — Create output
        # -------------------------------------------------

        print()
        print("[Agent 3 - Step 3]")
        print(
            "Creating population profile..."
        )

        population_profile = {

            "agent": {
                "id": "agent_3",
                "name": (
                    "Virtual Population Generator"
                )
            },

            "population_size": len(
                population
            ),

            "source": {
                "agent": "agent_2",
                "input": (
                    "audience_profile.json"
                )
            },

            "users": population
        }

        print(
            "✓ Population profile created."
        )

        # -------------------------------------------------
        # STEP 4 — SAVE OUTPUT
        # -------------------------------------------------

        print()
        print("[Agent 3 - Step 4]")
        print(
            "Saving virtual population..."
        )

        os.makedirs("outputs", exist_ok=True)
        output_path = (
            "outputs/virtual_population.json"
        )

        with open(
            output_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                population_profile,
                file,
                indent=4
            )

        print(
            f"✓ Saved to {output_path}"
        )

        # -------------------------------------------------
        # AGENT 3 COMPLETE
        # -------------------------------------------------

        print()
        print("=" * 60)
        print("👥 AGENT 3 COMPLETED")
        print("=" * 60)

        return population_profile
