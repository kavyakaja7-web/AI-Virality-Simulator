import random
from typing import Dict, List, Any


def simulate_viewing_sessions(
    users: List[Dict[str, Any]],
    duration_seconds: float,
    content_profile: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Simulate individual viewing sessions for all synthetic users.
    Calculates watch time, drop-offs, likes, comments, and shares.
    """
    if not users:
        raise ValueError("Virtual population cannot be empty.")

    if duration_seconds <= 0:
        duration_seconds = 15.0

    metadata = content_profile.get("video_metadata", {})
    orientation = metadata.get("orientation", "vertical")
    text_analysis = content_profile.get("text_analysis", {})
    has_text = text_analysis.get("text_present", False)

    # Content boost factors
    hook_boost = 0.05 if orientation == "vertical" else 0.0
    if has_text:
        hook_boost += 0.03

    total_users = len(users)
    views = 0
    completions = 0
    total_watch_time = 0.0
    total_likes = 0
    total_comments = 0
    total_shares = 0

    # For retention curve calculation (0%, 25%, 50%, 75%, 100%)
    retention_counts = {
        "at_0s": total_users,
        "at_3s": 0,
        "at_25_pct": 0,
        "at_50_pct": 0,
        "at_75_pct": 0,
        "at_100_pct": 0
    }

    t_3s = min(3.0, duration_seconds)
    t_25 = duration_seconds * 0.25
    t_50 = duration_seconds * 0.50
    t_75 = duration_seconds * 0.75

    # Segment tracking
    segments_data: Dict[Any, Dict[str, Any]] = {}

    for user in users:
        seg_id = user.get("segment_id", "default")
        seg_name = user.get("segment_name", "General Audience")
        behavior = user.get("behavior", {})
        relevance = user.get("relevance_score", 0.5)

        if seg_id not in segments_data:
            segments_data[seg_id] = {
                "segment_id": seg_id,
                "segment_name": seg_name,
                "user_count": 0,
                "views": 0,
                "completions": 0,
                "watch_time": 0.0,
                "likes": 0,
                "comments": 0,
                "shares": 0
            }

        seg = segments_data[seg_id]
        seg["user_count"] += 1

        watch_tendency = behavior.get("watch_tendency", 0.5)
        completion_tendency = behavior.get("completion_tendency", 0.5)
        like_tendency = behavior.get("like_tendency", 0.3)
        comment_tendency = behavior.get("comment_tendency", 0.1)
        share_tendency = behavior.get("share_tendency", 0.1)

        # -------------------------------------------------
        # STEP 1: HOOK DECISION (0 to 3s)
        # -------------------------------------------------
        hook_probability = min(
            0.95,
            max(0.10, watch_tendency + hook_boost + (relevance - 0.5) * 0.15)
        )

        is_view = random.random() <= hook_probability

        if is_view:
            views += 1
            seg["views"] += 1
            retention_counts["at_3s"] += 1

            # -------------------------------------------------
            # STEP 2: WATCH TIME & COMPLETION DECISION
            # -------------------------------------------------
            duration_factor = 1.1 if duration_seconds <= 15 else 0.85
            completion_prob = min(
                0.95,
                max(0.08, completion_tendency * duration_factor + (relevance - 0.5) * 0.15)
            )

            is_completion = random.random() <= completion_prob

            if is_completion:
                watch_time = duration_seconds
                completions += 1
                seg["completions"] += 1
            else:
                # Dropped off between 3s and 95% of duration
                watch_time = round(random.uniform(3.0, duration_seconds * 0.95), 2)

            # -------------------------------------------------
            # STEP 3: SOCIAL ENGAGEMENTS (Like, Comment, Share)
            # -------------------------------------------------
            watch_ratio = watch_time / duration_seconds

            # Like: Requires watching at least 40% of the video
            if watch_ratio >= 0.40:
                like_prob = like_tendency * watch_ratio * (0.9 + 0.2 * relevance)
                if random.random() <= like_prob:
                    total_likes += 1
                    seg["likes"] += 1

            # Comment: Driven by curiosity and discussion tendency
            comment_prob = comment_tendency * (0.8 if is_completion else 0.35)
            if random.random() <= comment_prob:
                total_comments += 1
                seg["comments"] += 1

            # Share: The holy grail of virality, requires high completion
            if watch_ratio >= 0.70:
                share_prob = share_tendency * (1.3 if is_completion else 0.4) * (relevance ** 0.5)
                if random.random() <= share_prob:
                    total_shares += 1
                    seg["shares"] += 1

        else:
            # Swiped away during the first 3 seconds
            watch_time = round(random.uniform(0.5, min(2.8, duration_seconds)), 2)

        total_watch_time += watch_time
        seg["watch_time"] += watch_time

        # Update retention milestones
        if watch_time >= t_25:
            retention_counts["at_25_pct"] += 1
        if watch_time >= t_50:
            retention_counts["at_50_pct"] += 1
        if watch_time >= t_75:
            retention_counts["at_75_pct"] += 1
        if watch_time >= duration_seconds:
            retention_counts["at_100_pct"] += 1

    # -------------------------------------------------
    # STEP 4: COMPILE METRICS & SEGMENT BREAKDOWN
    # -------------------------------------------------
    avg_watch_time = round(total_watch_time / total_users, 2)
    avg_pct_watched = round((avg_watch_time / duration_seconds) * 100, 1)

    hook_rate = round((views / total_users) * 100, 1)
    completion_rate = round((completions / total_users) * 100, 1)
    like_rate = round((total_likes / total_users) * 100, 1)
    comment_rate = round((total_comments / total_users) * 100, 1)
    share_rate = round((total_shares / total_users) * 100, 1)

    # Process segment breakdowns
    segment_breakdown = []
    for s in segments_data.values():
        cnt = s["user_count"]
        if cnt == 0:
            continue
        seg_retention = round((s["completions"] / cnt) * 100, 1)
        seg_share_share = round((s["shares"] / max(1, total_shares)) * 100, 1)
        
        contribution = "High" if seg_share_share >= 40 else ("Moderate" if seg_share_share >= 20 else "Low")
        
        segment_breakdown.append({
            "segment_name": s["segment_name"],
            "sample_size": cnt,
            "views": s["views"],
            "hook_rate": f"{round((s['views'] / cnt) * 100, 1)}%",
            "completion_rate": f"{seg_retention}%",
            "likes": s["likes"],
            "shares": s["shares"],
            "virality_contribution": f"{contribution} (Drives {seg_share_share}% of all shares)"
        })

    # Sort segments by completion rate
    segment_breakdown.sort(key=lambda x: float(x["completion_rate"].replace("%", "")), reverse=True)

    summary = {
        "sample_size": total_users,
        "video_duration_seconds": round(duration_seconds, 2),
        "impressions": total_users,
        "views": views,
        "swiped_away": total_users - views,
        "hook_retention_rate": f"{hook_rate}%",
        "completions": completions,
        "completion_rate": f"{completion_rate}%",
        "average_watch_time": f"{avg_watch_time}s",
        "average_percentage_watched": f"{avg_pct_watched}%"
    }

    engagements = {
        "likes": total_likes,
        "like_rate": f"{like_rate}%",
        "comments": total_comments,
        "comment_rate": f"{comment_rate}%",
        "shares": total_shares,
        "share_rate": f"{share_rate}%"
    }

    retention_curve = {
        "0s_start": "100.0%",
        "3s_hook": f"{round((retention_counts['at_3s'] / total_users) * 100, 1)}%",
        "25%_duration": f"{round((retention_counts['at_25_pct'] / total_users) * 100, 1)}%",
        "50%_duration": f"{round((retention_counts['at_50_pct'] / total_users) * 100, 1)}%",
        "75%_duration": f"{round((retention_counts['at_75_pct'] / total_users) * 100, 1)}%",
        "100%_complete": f"{round((retention_counts['at_100_pct'] / total_users) * 100, 1)}%"
    }

    # -------------------------------------------------
    # STEP 5: VIRALITY SCORE & ALGORITHM VERDICT
    # -------------------------------------------------
    virality_verdict = calculate_virality_score(
        completion_rate=completion_rate,
        share_rate=share_rate,
        hook_rate=hook_rate,
        like_rate=like_rate,
        comment_rate=comment_rate,
        top_segment_name=segment_breakdown[0]["segment_name"] if segment_breakdown else "Target Audience"
    )

    return {
        "simulation_summary": summary,
        "predicted_engagements": engagements,
        "retention_curve": retention_curve,
        "segment_breakdown": segment_breakdown,
        "virality_verdict": virality_verdict
    }


def calculate_virality_score(
    completion_rate: float,
    share_rate: float,
    hook_rate: float,
    like_rate: float,
    comment_rate: float,
    top_segment_name: str
) -> Dict[str, Any]:
    """
    Compute algorithmic virality score (0-100) using social platform ranking weights:
    - Watch Time / Completion: 35%
    - Share Velocity: 30%
    - 3-Second Hook Retention: 20%
    - Engagement (Likes + Comments): 15%
    """
    # Normalize components
    comp_score = min(100.0, completion_rate * 1.5)
    # 8%+ share rate is considered elite virality on TikTok/Reels
    share_score = min(100.0, (share_rate / 8.0) * 100.0)
    hook_score = min(100.0, hook_rate)
    like_score = min(100.0, (like_rate / 30.0) * 70.0 + (comment_rate / 8.0) * 30.0)

    score = (
        0.35 * comp_score +
        0.30 * share_score +
        0.20 * hook_score +
        0.15 * like_score
    )
    score = round(max(0.0, min(100.0, score)), 1)

    if score >= 80.0:
        rating = "MEGA-VIRAL POTENTIAL"
        push = "Aggressive. The algorithm will push this video beyond niche circles to global For You / Explore feeds with exponential reach."
        diagnosis = f"Outstanding completion and share velocity. High resonance in '{top_segment_name}' creates strong organic word-of-mouth loops."
    elif score >= 65.0:
        rating = "HIGH VIRALITY POTENTIAL"
        push = "High. Algorithm will test with Tier-2 broader audience batches (projected 100k+ views)."
        diagnosis = f"Solid hook retention and strong engagement in '{top_segment_name}'. Slight mid-video drop-off prevents mega-viral status."
    elif score >= 50.0:
        rating = "MODERATE REACH"
        push = "Moderate. Strong performance inside direct niche communities (projected 10k–50k views), but lower share velocity limits broad spillover."
        diagnosis = "Core audience engages well, but general viewers drop off after the 3-second hook."
    else:
        rating = "LOW VIRALITY"
        push = "Restricted. High early drop-off signals the algorithm to keep distribution restricted to small testing pools."
        diagnosis = "Hook fails to retain viewers past 3 seconds. Pacing or visual clarity needs improvement."

    return {
        "virality_score": score,
        "rating": rating,
        "algorithm_push_probability": push,
        "key_strength": diagnosis
    }
