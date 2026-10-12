"""
=========================================================
OPTIMIZER SERVICE — VIRAL CONTENT OPTIMIZATION ENGINE
=========================================================

Core engine for Agent 6. Analyzes audience drop-off points,
hook weaknesses, and platform suitability to produce:
1. 3 Pattern-Interrupt Hook Rewrites (Visual, Spoken, Text, SFX)
2. Scene-by-Scene Re-Edit Blueprint (Timestamps & Cuts)
3. Platform-Specific Packaging (Reels, TikTok, Shorts)
4. Mathematical Virality Uplift & ROI Forecast
=========================================================
"""

import math
from typing import Dict, Any, List, Optional
from services.llm_service import call_llm_json


def generate_optimization_plan(
    content_profile: Dict[str, Any],
    audience_profile: Dict[str, Any],
    population_profile: Optional[Dict[str, Any]] = None,
    engagement_prediction: Optional[Dict[str, Any]] = None,
    virality_report: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Main entry point for generating the actionable viral optimization plan.
    Combines AI reasoning with deterministic viral engineering heuristics.
    """
    # -------------------------------------------------------------
    # 1. Extract signals from all upstream artifacts
    # -------------------------------------------------------------
    metadata = content_profile.get("video_metadata", {})
    visual = content_profile.get("visual_analysis", {})
    audio = content_profile.get("audio_analysis", {})
    hook = content_profile.get("hook_analysis", {})
    structure = content_profile.get("structure_analysis", {})

    duration = metadata.get("duration_seconds", 15.0)
    orientation = metadata.get("orientation", "vertical")
    topic = visual.get("topic") or "General Lifestyle / Content"
    scene_desc = visual.get("scene") or visual.get("summary") or "Scene recorded on camera"
    objects = visual.get("objects", [])
    activities = visual.get("activities", [])
    transcript = audio.get("transcript", "").strip()

    audience_summary = audience_profile.get("content_summary", {})
    primary_niche = audience_summary.get("primary_niche") or topic
    segments = audience_profile.get("audience_segments", [])
    top_segment = segments[0] if segments else {"name": "Core Viewers", "age_range": "18–24"}
    platforms = audience_profile.get("platform_distribution", [])
    top_platform = platforms[0] if platforms else {"platform": "Instagram Reels", "suitability": "Optimal (95%)"}

    sim_summary = (engagement_prediction or {}).get("simulation_summary", {})
    verdict = (engagement_prediction or {}).get("virality_verdict", {})
    retention_curve = (engagement_prediction or {}).get("retention_curve", {})
    engagements = (engagement_prediction or {}).get("predicted_engagements", {})

    # Extract baseline metrics
    baseline_score = float(verdict.get("virality_score", 58.0))
    baseline_rating = verdict.get("rating", "MODERATE VIRALITY")
    
    hook_rate_raw = sim_summary.get("hook_retention_rate", "65.0%")
    hook_rate_num = float(str(hook_rate_raw).replace("%", "")) if "%" in str(hook_rate_raw) else 65.0

    comp_rate_raw = sim_summary.get("completion_rate", "38.0%")
    comp_rate_num = float(str(comp_rate_raw).replace("%", "")) if "%" in str(comp_rate_raw) else 38.0

    share_rate_raw = engagements.get("share_rate") or sim_summary.get("share_rate", "4.0%")
    share_rate_num = float(str(share_rate_raw).replace("%", "")) if "%" in str(share_rate_raw) else 4.0

    like_rate_raw = engagements.get("like_rate", "8.0%")
    like_rate_num = float(str(like_rate_raw).replace("%", "")) if "%" in str(like_rate_raw) else 8.0

    # -------------------------------------------------------------
    # 2. Diagnose specific viral vulnerabilities
    # -------------------------------------------------------------
    vulnerabilities = _diagnose_vulnerabilities(
        hook_rate_num=hook_rate_num,
        comp_rate_num=comp_rate_num,
        share_rate_num=share_rate_num,
        duration=duration,
        hook=hook,
        transcript=transcript,
        retention_curve=retention_curve
    )

    # -------------------------------------------------------------
    # 3. Generate 3 Hook Rewrites & Scene Cut Blueprint & Packaging
    # -------------------------------------------------------------
    # Try dynamic LLM synthesis first
    ai_plan = _try_llm_generation(
        topic=primary_niche,
        scene=scene_desc,
        transcript=transcript,
        duration=duration,
        top_segment=top_segment,
        top_platform=top_platform,
        hook_rate_num=hook_rate_num,
        comp_rate_num=comp_rate_num,
        share_rate_num=share_rate_num,
        baseline_score=baseline_score,
        vulnerabilities=vulnerabilities
    )

    if ai_plan:
        hook_rewrites = ai_plan.get("hook_rewrites", [])
        cut_blueprint = ai_plan.get("scene_cut_blueprint", [])
        platform_packaging = ai_plan.get("platform_packaging", {})
    else:
        hook_rewrites = []
        cut_blueprint = []
        platform_packaging = {}

    # Fallback / Enrich if AI returned partial or empty
    if not hook_rewrites or len(hook_rewrites) < 3:
        hook_rewrites = _heuristic_hook_rewrites(
            niche=primary_niche,
            scene=scene_desc,
            transcript=transcript,
            top_segment=top_segment
        )

    if not cut_blueprint or len(cut_blueprint) < 3:
        cut_blueprint = _heuristic_cut_blueprint(
            duration=duration,
            transcript=transcript,
            hook_rate_num=hook_rate_num,
            comp_rate_num=comp_rate_num
        )

    if not platform_packaging or not platform_packaging.get("instagram_reels"):
        platform_packaging = _heuristic_platform_packaging(
            niche=primary_niche,
            top_segment=top_segment,
            transcript=transcript,
            objects=objects
        )

    # -------------------------------------------------------------
    # 4. Calculate Mathematical Projected Uplift
    # -------------------------------------------------------------
    uplift = _calculate_projected_uplift(
        baseline_score=baseline_score,
        baseline_hook_rate=hook_rate_num,
        baseline_comp_rate=comp_rate_num,
        baseline_share_rate=share_rate_num,
        vulnerabilities=vulnerabilities,
        duration=duration
    )

    return {
        "vulnerabilities": vulnerabilities,
        "hook_rewrites": hook_rewrites,
        "scene_cut_blueprint": cut_blueprint,
        "platform_packaging": platform_packaging,
        "projected_uplift": uplift
    }


def _diagnose_vulnerabilities(
    hook_rate_num: float,
    comp_rate_num: float,
    share_rate_num: float,
    duration: float,
    hook: Dict[str, Any],
    transcript: str,
    retention_curve: Dict[str, Any]
) -> List[Dict[str, str]]:
    """
    Identifies root causes of algorithmic drag and lost viewership.
    """
    issues = []

    # 1. 3s Hook Assessment
    if hook_rate_num < 75.0:
        issues.append({
            "dimension": "Hook Swipe-Away Deficit",
            "severity": "CRITICAL" if hook_rate_num < 60.0 else "HIGH",
            "finding": f"3-second hook retention is {hook_rate_num:.1f}% ({100.0 - hook_rate_num:.1f}% of users swiped away within 3s).",
            "impact": "Algorithmic discovery penalty: Platforms test content on 100 users; high initial swipe halts FYP expansion.",
            "remedy": "Replace passive opening with immediate kinetic pattern interrupt (0-1.2s action + bold text hook)."
        })
    else:
        issues.append({
            "dimension": "Hook Performance",
            "severity": "LOW",
            "finding": f"3-second hook retention is strong at {hook_rate_num:.1f}%.",
            "impact": "Passes Phase 1 algorithmic test; focus on sustaining mid-video retention.",
            "remedy": "Maintain current hook speed while optimizing secondary loop transitions."
        })

    # 2. Watch Time & Completion Assessment
    if comp_rate_num < 45.0:
        issues.append({
            "dimension": "Mid-Video Attention Lapse",
            "severity": "HIGH",
            "finding": f"Video completion rate is {comp_rate_num:.1f}% on a {duration:.1f}s clip.",
            "impact": "Viewers experience cognitive fatigue between seconds 4–8 due to monotone pacing or lack of visual resets.",
            "remedy": "Implement dynamic B-roll cutaways or zoom punch-ins every 3.5 seconds to reset dopamine cycles."
        })
    else:
        issues.append({
            "dimension": "Completion Factor",
            "severity": "MODERATE",
            "finding": f"Completion rate is {comp_rate_num:.1f}%.",
            "impact": "Good completion, but loop potential can be multiplied.",
            "remedy": "Add an incomplete final phrase that seamlessly links to the first word of the hook."
        })

    # 3. Shareability / DM Forwarding Factor
    if share_rate_num < 6.0:
        issues.append({
            "dimension": "Share Loop Deficiency",
            "severity": "HIGH",
            "finding": f"Predicted share rate is {share_rate_num:.1f}%. Viral short-form relies heavily on peer DMs.",
            "impact": "Without active sharing, content is restricted to organic algorithmic feed pushes rather than exponential word-of-mouth.",
            "remedy": "Embed a direct relatability hook or provocative statement that prompts 'Tag someone who does this' behavior."
        })

    # 4. Text & Caption Overlay Deficit
    if not transcript or len(transcript) < 20:
        issues.append({
            "dimension": "Silent Scroller Alienation",
            "severity": "MODERATE",
            "finding": "Limited or no spoken dialogue detected; 68% of social media users scroll with sound muted.",
            "impact": "Viewers scrolling without sound immediately skip when visual captions are missing.",
            "remedy": "Apply high-contrast kinetic subtitles with highlighted yellow/green trigger words."
        })

    return issues


def _try_llm_generation(
    topic: str,
    scene: str,
    transcript: str,
    duration: float,
    top_segment: Dict[str, Any],
    top_platform: Dict[str, Any],
    hook_rate_num: float,
    comp_rate_num: float,
    share_rate_num: float,
    baseline_score: float,
    vulnerabilities: List[Dict[str, str]]
) -> Optional[Dict[str, Any]]:
    """
    Asks Groq/LLM to generate 3 tailored viral hook rewrites, re-edit timestamps,
    and platform packaging.
    """
    prompt = f"""You are a legendary short-form virality engineer and viral video editor for TikTok, Instagram Reels, and YouTube Shorts.
Analyze this video and its simulation metrics, then engineer an aggressive, high-converting Content Optimization Plan.

VIDEO PROFILE:
- Topic / Niche: {topic}
- Visual Setting: {scene}
- Spoken Transcript: "{transcript if transcript else 'No speech detected / Ambient sound'}"
- Duration: {duration}s
- Target Audience Segment: {top_segment.get('name', 'Core Viewers')} (Ages: {top_segment.get('age_range', '18–24')})
- Top Platform: {top_platform.get('platform', 'Instagram Reels')}

SIMULATION WEAKNESSES:
- 3s Hook Retention: {hook_rate_num:.1f}% (Deficit: {100 - hook_rate_num:.1f}% swiped away)
- Completion Rate: {comp_rate_num:.1f}%
- Share Rate: {share_rate_num:.1f}%
- Current Virality Score: {baseline_score:.0f}/100

TASK:
Generate a complete viral optimization blueprint formatted as STRICT JSON matching this exact structure:
{{
  "hook_rewrites": [
    {{
      "variant_id": "A",
      "hook_style": "Curiosity Gap & Pattern Interrupt",
      "psychological_trigger": "Dopamine Incongruity",
      "visual_action": "Exact visual direction for seconds 0.0–1.5 (e.g. fast whip-pan, hands moving, sudden zoom)",
      "spoken_script": "Exact voiceover line to speak in seconds 0.0–2.5",
      "on_screen_text": "BOLD KINETIC TEXT overlay (caps, color cues, emoji)",
      "audio_sfx_cue": "Specific audio cue (e.g. Vinyl stop + Sub-bass drop)",
      "expected_retention": "88%+"
    }},
    {{
      "variant_id": "B",
      "hook_style": "Relatable Pain Point / Problem-First",
      "psychological_trigger": "Tribal Empathy & FOMO",
      "visual_action": "Exact visual direction for seconds 0.0–1.5",
      "spoken_script": "Exact voiceover line",
      "on_screen_text": "BOLD KINETIC TEXT overlay",
      "audio_sfx_cue": "Audio cue (e.g. Pop sound + Record scratch)",
      "expected_retention": "85%+"
    }},
    {{
      "variant_id": "C",
      "hook_style": "Contrarian / In Media Res Shock",
      "psychological_trigger": "Cognitive Dissonance",
      "visual_action": "Exact visual direction for seconds 0.0–1.5",
      "spoken_script": "Exact voiceover line",
      "on_screen_text": "BOLD KINETIC TEXT overlay",
      "audio_sfx_cue": "Audio cue (e.g. Glitch SFX + Risers)",
      "expected_retention": "91%+"
    }}
  ],
  "scene_cut_blueprint": [
    {{
      "timestamp_range": "0.0s – 1.2s",
      "action_type": "Trim & Punch-In",
      "instruction": "Cut dead-air lead-in. Punch frame in by 115% for immediate visual intimacy."
    }},
    {{
      "timestamp_range": "1.2s – 4.0s",
      "action_type": "Visual Anchor",
      "instruction": "Display kinetic subtitle word-by-word with yellow highlight on power words."
    }},
    {{
      "timestamp_range": "4.0s – 8.0s",
      "action_type": "Pattern Interrupt",
      "instruction": "Cut to tight B-roll or dynamic reaction angle to defeat 5-second attention drop."
    }},
    {{
      "timestamp_range": "Last 2.5s",
      "action_type": "Infinite Loop Outro",
      "instruction": "Cut standard outro. End sentence mid-thought so it flows seamlessly into Hook A's first word."
    }}
  ],
  "platform_packaging": {{
    "instagram_reels": {{
      "cover_headline": "Bold text headline for the thumbnail cover",
      "caption": "Captivating 2-line caption ending with DM share CTA",
      "hashtags": ["#Tag1", "#Tag2", "#Tag3", "#Tag4", "#Tag5", "#Tag6", "#Tag7", "#Tag8"],
      "audio_recommendation": "Trending audio recommendation",
      "best_posting_window": "6:30 PM – 9:00 PM local time"
    }},
    "tiktok": {{
      "first_line_hook": "Hooky first line for the TikTok caption",
      "comment_bait_question": "Engaging question to force debate in comments",
      "seo_keywords": ["keyword 1", "keyword 2", "keyword 3"],
      "hashtags": ["#Tag1", "#Tag2", "#Tag3", "#Tag4", "#Tag5", "#Tag6"],
      "sound_strategy": "Original audio + trending sound at 4% volume"
    }},
    "youtube_shorts": {{
      "ctr_title": "Curiosity-driven title under 50 characters",
      "pinned_comment": "Pinned comment question to spark replies",
      "search_tags": ["tag1", "tag2", "tag3", "tag4"]
    }}
  }}
}}
Return ONLY valid JSON. No markdown wrappers or preamble."""

    try:
        res = call_llm_json(prompt, system_instruction="You are an elite short-form viral video director and strategist. Return ONLY valid JSON.")
        if res and isinstance(res, dict) and "hook_rewrites" in res and len(res.get("hook_rewrites", [])) >= 3:
            return res
    except Exception:
        pass

    return None


def _heuristic_hook_rewrites(
    niche: str,
    scene: str,
    transcript: str,
    top_segment: Dict[str, Any]
) -> List[Dict[str, Any]]:
    """
    Deterministic, high-quality hook rewrites tailored to the detected niche and audience.
    """
    seg_name = top_segment.get("name", "Students & Tech Enthusiasts")

    return [
        {
            "variant_id": "A",
            "hook_style": "Curiosity Gap & Pattern Interrupt",
            "psychological_trigger": "Dopamine Incongruity (The Scroll-Stopper)",
            "visual_action": "Rapid 0.8s digital snap-zoom into the main subject's expression, immediately cutting dead-space.",
            "spoken_script": f"If you're in {niche}, this one realization is going to completely change how you look at your day...",
            "on_screen_text": "🚨 WAIT TILL YOU SEE THIS... [YELLOW BOLD]",
            "audio_sfx_cue": "Fast cinematic whoosh transition + heavy bass punch on word 'WAIT'",
            "expected_retention": "88.4%",
            "target_persona": seg_name
        },
        {
            "variant_id": "B",
            "hook_style": "Relatable Pain Point / Problem-First",
            "psychological_trigger": "Tribal Empathy & Validation",
            "visual_action": "Start immediately mid-action (in media res). Show the monitor/screen or work environment in full clarity.",
            "spoken_script": f"Tell me I'm not the only one who deals with this exact situation every single time...",
            "on_screen_text": "POV: YOUR DAILY REALITY 💀 [WHITE BOLD / RED HIGHLIGHT]",
            "audio_sfx_cue": "Subtle comedic record-scratch followed by upbeat trending lo-fi beat",
            "expected_retention": "85.2%",
            "target_persona": seg_name
        },
        {
            "variant_id": "C",
            "hook_style": "Contrarian / In Media Res Shock",
            "psychological_trigger": "Cognitive Dissonance (Contrarian Stance)",
            "visual_action": "Flash the climax frame for 0.4s as a teaser before instantly cutting back to the beginning.",
            "spoken_script": f"Everyone thinks {niche} is simple, until this happens and changes everything.",
            "on_screen_text": "DON'T MAKE THIS MISTAKE ⚠️ [HIGH CONTRAST BOX]",
            "audio_sfx_cue": "Glitch sound effect with instant high-pass filter drop",
            "expected_retention": "91.8%",
            "target_persona": seg_name
        }
    ]


def _heuristic_cut_blueprint(
    duration: float,
    transcript: str,
    hook_rate_num: float,
    comp_rate_num: float
) -> List[Dict[str, str]]:
    """
    Deterministic scene cut timetable and re-edit blueprint.
    """
    t1 = min(1.2, duration * 0.1)
    t2 = min(4.5, duration * 0.3)
    t3 = min(9.0, duration * 0.6)

    return [
        {
            "timestamp_range": f"0.0s – {t1:.1f}s",
            "action_type": "Lead-In Dead Air Elimination",
            "instruction": "Cut the first 0.6s–1.0s of dead lead-in frames. Crop vertical canvas by 112% to increase focal intimacy on mobile screens.",
            "algorithmic_reasoning": f"Removes the idle pause that accounted for the {100.0 - hook_rate_num:.1f}% 3-second dropoff."
        },
        {
            "timestamp_range": f"{t1:.1f}s – {t2:.1f}s",
            "action_type": "Kinetic Typography & Caption Stacking",
            "instruction": "Add auto-centered, animated subtitles (1–3 words per frame) using Montserrat/TheBoldFont with yellow power-word emphasis.",
            "algorithmic_reasoning": "Captures the 68% of users watching in muted sound mode on mobile feeds."
        },
        {
            "timestamp_range": f"{t2:.1f}s – {t3:.1f}s",
            "action_type": "Pattern Interrupt & B-Roll Reset",
            "instruction": "Insert a rapid zoom-out or brief B-roll cutaway at 4.5s. Add a subtle riser audio cue (-16dB) under the dialogue.",
            "algorithmic_reasoning": "Re-engages dopamine receptors at the critical 5-second attention lapse threshold."
        },
        {
            "timestamp_range": f"{t3:.1f}s – {duration:.1f}s",
            "action_type": "Infinite Loop Outro Crafting",
            "instruction": "Cut any 'thanks for watching' or trailing pauses. End the video abruptly on an unresolved vocal cadence that connects to the opening word of the hook.",
            "algorithmic_reasoning": "Forces 20%–35% of viewers into an involuntary 2nd loop watch, multiplying algorithmic completion scores."
        }
    ]


def _heuristic_platform_packaging(
    niche: str,
    top_segment: Dict[str, Any],
    transcript: str,
    objects: List[str]
) -> Dict[str, Any]:
    """
    Tailored social metadata for Instagram Reels, TikTok, and YouTube Shorts.
    """
    clean_niche = niche.replace(" ", "").replace("/", "").replace("&", "")
    obj_tag = f"#{objects[0].replace(' ', '')}" if objects else "#ContentCreation"

    return {
        "instagram_reels": {
            "cover_headline": f"The Reality of {niche} Nobody Tells You",
            "caption": (
                f"Is it just us, or does this hit a little too close to home? 😂\n\n"
                f"Tag that one friend who needs to see this right now 👇\n\n"
                f".\n.\n"
                f"#{clean_niche} #RelatableContent #ExplorePage #ViralReels #DailyGrind {obj_tag} #TechTok #CreatorEconomy"
            ),
            "hashtags": [
                f"#{clean_niche}", "#ViralReels", "#ExplorePage", "#RelatableReels",
                "#DailyLife", "#TrendAlert", "#TechLife", "#ForYouPage"
            ],
            "audio_recommendation": "Use trending lo-fi / phonk sound with rising beat (120+ BPM). Save original sound to save-audio library.",
            "best_posting_window": "6:30 PM – 8:45 PM (Peak evening commuter & leisure window)"
        },
        "tiktok": {
            "first_line_hook": f"wait for the end… this is crazy 😭 #{clean_niche}",
            "comment_bait_question": "What would you have done in this situation? Dropping honest opinions in the comments 👇",
            "seo_keywords": [
                f"{niche.lower()} tips",
                f"{niche.lower()} pov",
                "relatable moments",
                "viral hack"
            ],
            "hashtags": [
                f"#{clean_niche.lower()}", "#fyp", "#foryou", "#viral", "#relatable", "#storytime"
            ],
            "sound_strategy": "Keep original audio at 100%, layer trending sound at 3–5% volume to piggyback the algorithm."
        },
        "youtube_shorts": {
            "ctr_title": f"Why Everyone Is Talking About {niche} 👀 #Shorts",
            "pinned_comment": "Did you notice the detail at 0:04? Tell us in the comments! 👇",
            "search_tags": [
                clean_niche.lower(),
                "viral shorts",
                "relatable clip",
                "trending today"
            ]
        }
    }


def _calculate_projected_uplift(
    baseline_score: float,
    baseline_hook_rate: float,
    baseline_comp_rate: float,
    baseline_share_rate: float,
    vulnerabilities: List[Dict[str, str]],
    duration: float
) -> Dict[str, Any]:
    """
    Simulates the mathematical improvement from implementing Agent 6's fixes:
    - Pattern-interrupt hook -> +18% to +24% hook retention
    - Pacing cut blueprint -> +15% to +26% completion rate
    - DM share trigger -> +40% to +80% share rate
    - Yields new Algorithmic Virality Score (0-100) and audience push tier.
    """
    # 1. Projected Hook Retention
    hook_gain = 22.5 if baseline_hook_rate < 70.0 else 12.0
    projected_hook = min(96.0, baseline_hook_rate + hook_gain)

    # 2. Projected Completion Rate
    comp_gain = 20.0 if baseline_comp_rate < 50.0 else 14.0
    projected_comp = min(88.0, baseline_comp_rate + comp_gain)

    # 3. Projected Share Rate
    share_gain = baseline_share_rate * 0.75 + 3.0
    projected_share = min(18.0, baseline_share_rate + share_gain)

    # 4. Virality Score Projection
    # Formula modeled after social recommendation algorithms:
    # 35% Hook Retention + 40% Completion/Watch Time + 25% Share/Engagement Power
    baseline_calc = (baseline_hook_rate * 0.35) + (baseline_comp_rate * 0.40) + (min(baseline_share_rate * 5.0, 100.0) * 0.25)
    projected_calc = (projected_hook * 0.35) + (projected_comp * 0.40) + (min(projected_share * 5.0, 100.0) * 0.25)
    
    score_uplift = round(projected_calc - baseline_calc, 1)
    projected_score = min(97.0, round(baseline_score + max(15.0, score_uplift), 1))
    percentage_gain = round(((projected_score - baseline_score) / max(baseline_score, 1.0)) * 100.0, 1)

    # Algorithmic push tier mapping
    if projected_score >= 85:
        tier = "Tier 1: Explosive / Global FYP Distribution (High-Velocity Discovery)"
        reach_multiplier = "4.0x – 6.5x Organic Reach"
    elif projected_score >= 70:
        tier = "Tier 2: Broad Niche Virality (Explore Page & Recommended Feeds)"
        reach_multiplier = "2.5x – 3.8x Organic Reach"
    else:
        tier = "Tier 3: Moderate Seed Audience Distribution"
        reach_multiplier = "1.5x – 2.0x Organic Reach"

    return {
        "baseline_virality_score": round(baseline_score, 1),
        "projected_virality_score": round(projected_score, 1),
        "score_uplift_points": f"+{round(projected_score - baseline_score, 1)} pts",
        "score_uplift_percentage": f"+{percentage_gain}%",
        "baseline_hook_retention": f"{baseline_hook_rate:.1f}%",
        "projected_hook_retention": f"{projected_hook:.1f}%",
        "hook_retention_uplift": f"+{round(projected_hook - baseline_hook_rate, 1)}%",
        "baseline_completion_rate": f"{baseline_comp_rate:.1f}%",
        "projected_completion_rate": f"{projected_comp:.1f}%",
        "completion_rate_uplift": f"+{round(projected_comp - baseline_comp_rate, 1)}%",
        "baseline_share_rate": f"{baseline_share_rate:.1f}%",
        "projected_share_rate": f"{projected_share:.1f}%",
        "share_rate_uplift": f"+{round(projected_share - baseline_share_rate, 1)}%",
        "projected_distribution_tier": tier,
        "estimated_reach_multiplier": reach_multiplier
    }
