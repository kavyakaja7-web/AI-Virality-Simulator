import random


def generate_virtual_population(
    audience_segments,
    population_size=1000
):
    """
    Generate a synthetic virtual population
    based on Agent 2 audience segments.
    """

    if not audience_segments:
        raise ValueError(
            "No audience segments provided."
        )

    # -------------------------------------------------
    # STEP 1 — Calculate total relevance
    # -------------------------------------------------

    total_relevance = sum(
        segment.get("relevance_score", 1.0)
        for segment in audience_segments
    )

    if total_relevance <= 0:
        raise ValueError(
            "Invalid audience relevance scores."
        )

    # -------------------------------------------------
    # STEP 2 — Calculate number of users per segment
    # -------------------------------------------------

    segment_counts = []

    for segment in audience_segments:

        relevance = segment.get(
            "relevance_score",
            1.0
        )

        proportion = (
            relevance / total_relevance
        )

        count = round(
            population_size * proportion
        )

        segment_counts.append(count)

    # Fix rounding difference
    difference = (
        population_size
        - sum(segment_counts)
    )

    segment_counts[0] += difference

    # -------------------------------------------------
    # STEP 3 — Generate users
    # -------------------------------------------------

    population = []

    user_id = 1

    for segment, count in zip(
        audience_segments,
        segment_counts
    ):

        age_range = segment.get(
            "age_range",
            "18-35"
        )

        min_age, max_age = parse_age_range(
            age_range
        )

        interests = segment.get(
            "interests",
            []
        )

        relevance = segment.get(
            "relevance_score",
            0.5
        )

        for _ in range(count):

            age = random.randint(
                min_age,
                max_age
            )

            user = {

                "user_id": user_id,

                "segment_id": segment.get(
                    "segment_id"
                ),

                "segment_name": segment.get(
                    "name"
                ),

                "age": age,

                "location": "India",

                "interests": interests,

                "relevance_score": relevance,

                "behavior": {

                    "watch_tendency": round(
                        random.uniform(
                            max(0.1, relevance - 0.20),
                            min(1.0, relevance + 0.10)
                        ),
                        3
                    ),

                    "completion_tendency": round(
                        random.uniform(
                            0.40,
                            0.90
                        ),
                        3
                    ),

                    "like_tendency": round(
                        random.uniform(
                            0.20,
                            0.70
                        ),
                        3
                    ),

                    "comment_tendency": round(
                        random.uniform(
                            0.05,
                            0.40
                        ),
                        3
                    ),

                    "share_tendency": round(
                        random.uniform(
                            0.05,
                            0.50
                        ),
                        3
                    )
                }
            }

            population.append(user)

            user_id += 1

    # -------------------------------------------------
    # STEP 4 — Shuffle population
    # -------------------------------------------------

    random.shuffle(population)

    return population


def parse_age_range(age_range):
    """
    Convert age range such as '18–24'
    or '18-24' into minimum and maximum age.
    """

    age_range = str(age_range).replace(
        "–",
        "-"
    )

    parts = age_range.split("-")

    if len(parts) != 2:
        return 18, 35

    try:

        min_age = int(
            parts[0].strip()
        )

        max_age = int(
            parts[1].strip()
        )

        return min_age, max_age

    except ValueError:

        return 18, 35
