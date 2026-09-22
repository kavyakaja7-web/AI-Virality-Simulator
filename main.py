import json

from agents.agent1_video_analyzer import Agent1VideoAnalyzer


# -------------------------------------------------------
# VIDEO INPUT
# -------------------------------------------------------

VIDEO_PATH = "videos/test.mp4"


# -------------------------------------------------------
# CREATE AGENT 1
# -------------------------------------------------------

print()
print("=" * 60)
print("STARTING AI VIRALITY SIMULATOR")
print("=" * 60)

agent1 = Agent1VideoAnalyzer()


# -------------------------------------------------------
# RUN AGENT 1
# -------------------------------------------------------

result = agent1.analyze(VIDEO_PATH)


# -------------------------------------------------------
# DISPLAY RESULT
# -------------------------------------------------------

print()
print("=" * 60)
print("🤖 AGENT 1 OUTPUT")
print("VIDEO CONTENT PROFILE")
print("=" * 60)

print(
    json.dumps(
        result,
        indent=4
    )
)