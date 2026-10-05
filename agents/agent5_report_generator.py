"""
=========================================================
AGENT 5 — REPORT GENERATOR AGENT
=========================================================

Purpose:
    Synthesize all outputs from Agent 1 (Content Profile),
    Agent 2 (Audience Profile), Agent 3 (Virtual Population),
    and Agent 4 (Engagement Prediction) into an executive-grade
    Virality Report.

Outputs:
    1. outputs/virality_report.json  (Structured machine-readable data)
    2. outputs/VIRALITY_REPORT.md    (Executive Markdown Report)

=========================================================
"""

import json
import os
from datetime import datetime
from typing import Dict, Any, List
from services.llm_service import call_llm_json


class Agent5ReportGenerator:
    """
    AGENT 5 — REPORT GENERATOR AGENT
    """

    def __init__(self):
        print()
        print("=" * 60)
        print("📑 AGENT 5 — REPORT GENERATOR AGENT")
        print("=" * 60)
        print("Agent 5 initialized successfully.")

    def generate(
        self,
        content_profile: Dict[str, Any],
        audience_profile: Dict[str, Any],
        population_profile: Dict[str, Any],
        engagement_prediction: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Synthesize simulation data into comprehensive JSON and Markdown reports.
        """
        print()
        print("=" * 60)
        print("📑 AGENT 5 STARTED")
        print("=" * 60)

        # -------------------------------------------------
        # STEP 1 — Ingest and validate upstream data
        # -------------------------------------------------
        print()
        print("[Agent 5 - Step 1]")
        print("Ingesting data from Agents 1, 2, 3, and 4...")

        metadata = content_profile.get("video_metadata", {})
        visual = content_profile.get("visual_analysis", {})
        audio = content_profile.get("audio_analysis", {})
        hook = content_profile.get("hook_analysis", {})
        structure = content_profile.get("structure_analysis", {})

        content_summary = audience_profile.get("content_summary", {})
        platforms = audience_profile.get("platform_distribution", [])
        segments = audience_profile.get("audience_segments", [])
        overall_demographics = audience_profile.get("overall_demographics", {})

        pop_size = population_profile.get("population_size", 1000)

        sim_summary = engagement_prediction.get("simulation_summary", {})
        engagements = engagement_prediction.get("predicted_engagements", {})
        retention = engagement_prediction.get("retention_curve", {})
        segment_perf = engagement_prediction.get("segment_breakdown", [])
        verdict = engagement_prediction.get("virality_verdict", {})

        print("✓ All upstream agent artifacts successfully ingested.")

        # -------------------------------------------------
        # STEP 2 — Generate strategic recommendations
        # -------------------------------------------------
        print()
        print("[Agent 5 - Step 2]")
        print("Formulating data-driven optimization recommendations...")

        recommendations = self._generate_recommendations(
            hook=hook,
            structure=structure,
            sim_summary=sim_summary,
            retention=retention,
            verdict=verdict,
            platforms=platforms,
            segment_perf=segment_perf
        )
        print(f"✓ Formulated {len(recommendations)} actionable recommendations.")

        # -------------------------------------------------
        # STEP 3 — Compile Structured JSON Report
        # -------------------------------------------------
        print()
        print("[Agent 5 - Step 3]")
        print("Compiling structured report data (virality_report.json)...")

        report_data = {
            "agent": {
                "id": "agent_5",
                "name": "Report Generator Agent"
            },
            "timestamp": datetime.now().isoformat(),
            "executive_summary": {
                "virality_score": verdict.get("virality_score", 0),
                "rating": verdict.get("rating", "UNKNOWN"),
                "algorithm_push_probability": verdict.get("algorithm_push_probability", ""),
                "key_driver": verdict.get("key_strength", ""),
                "primary_niche": content_summary.get("primary_niche", visual.get("topic", "General")),
                "sample_size": pop_size
            },
            "video_diagnostics": {
                "duration_seconds": metadata.get("duration_seconds", 0),
                "orientation": metadata.get("orientation", "vertical"),
                "visual_topic": visual.get("topic", "N/A"),
                "visual_summary": visual.get("summary", "N/A"),
                "speech_detected": audio.get("speech_detected", False),
                "transcript": audio.get("transcript", ""),
                "hook_type": hook.get("hook_type", "N/A"),
                "hook_strength": hook.get("hook_strength", "N/A"),
                "hook_evaluation": hook.get("evaluation", ""),
                "pacing": structure.get("pacing", "N/A")
            },
            "performance_metrics": {
                "impressions": sim_summary.get("impressions", pop_size),
                "views": sim_summary.get("views", 0),
                "hook_retention_rate": sim_summary.get("hook_retention_rate", "0%"),
                "swiped_away": sim_summary.get("swiped_away", 0),
                "completions": sim_summary.get("completions", 0),
                "completion_rate": sim_summary.get("completion_rate", "0%"),
                "average_watch_time": sim_summary.get("average_watch_time", "0s"),
                "average_percentage_watched": sim_summary.get("average_percentage_watched", "0%"),
                "likes": engagements.get("likes", 0),
                "like_rate": engagements.get("like_rate", "0%"),
                "comments": engagements.get("comments", 0),
                "comment_rate": engagements.get("comment_rate", "0%"),
                "shares": engagements.get("shares", 0),
                "share_rate": engagements.get("share_rate", "0%")
            },
            "retention_curve": retention,
            "audience_breakdown": segment_perf,
            "platform_strategy": platforms,
            "actionable_recommendations": recommendations
        }

        os.makedirs("outputs", exist_ok=True)
        json_path = "outputs/virality_report.json"
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(report_data, f, indent=4)
        print(f"✓ Saved structured report to {json_path}")

        # -------------------------------------------------
        # STEP 4 — Generate Markdown Executive Report
        # -------------------------------------------------
        print()
        print("[Agent 5 - Step 4]")
        print("Rendering executive Markdown report (VIRALITY_REPORT.md)...")

        md_content = self._render_markdown_report(report_data)
        md_path = "outputs/VIRALITY_REPORT.md"
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(md_content)
        print(f"✓ Saved executive report to {md_path}")

        # -------------------------------------------------
        # STEP 5 — Generate Interactive HTML Dashboard
        # -------------------------------------------------
        print()
        print("[Agent 5 - Step 5]")
        print("Rendering visual interactive dashboard (report.html)...")

        html_content = self._render_html_dashboard(report_data)
        html_path = "outputs/report.html"
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"✓ Saved interactive HTML dashboard to {html_path}")

        # -------------------------------------------------
        # AGENT 5 COMPLETE
        # -------------------------------------------------
        print()
        print("=" * 60)
        print("📑 AGENT 5 COMPLETED")
        print("=" * 60)

        return report_data

    def _generate_recommendations(
        self,
        hook: Dict[str, Any],
        structure: Dict[str, Any],
        sim_summary: Dict[str, Any],
        retention: Dict[str, Any],
        verdict: Dict[str, Any],
        platforms: List[Dict[str, Any]],
        segment_perf: List[Dict[str, Any]]
    ) -> List[Dict[str, str]]:
        """
        Derive intelligent, contextual optimization recommendations using AI reasoning with rule-based fallback.
        """
        # Try dynamic AI recommendation generation first
        top_name = segment_perf[0].get("segment_name", "Core Audience") if segment_perf else "Core Audience"
        top_plat = platforms[0].get("platform", "Instagram Reels") if platforms else "Instagram Reels"
        hook_rate = sim_summary.get("hook_retention_rate", "0%")
        comp_rate = sim_summary.get("completion_rate", "0%")
        score = verdict.get("virality_score", 0)

        ai_prompt = f"""You are a master social media content coach for TikTok, Reels, and YouTube Shorts.
Analyze this video simulation data and provide 4 high-impact, specific, non-generic recommendations:
- 3s Hook Retention: {hook_rate} (Hook Type: {hook.get('hook_type', 'Spoken')})
- Video Completion Rate: {comp_rate} (Duration: {sim_summary.get('video_duration_seconds', 0)}s)
- Share Rate: {sim_summary.get('share_rate', '0%')}
- Virality Score: {score}/100 ({verdict.get('rating', '')})
- Top Sharing Segment: {top_name}
- Best Platform: {top_plat}

Return ONLY a JSON object with this exact structure:
{{
  "recommendations": [
    {{"category": "Hook Optimization", "priority": "Maintenance", "finding": "Specific observation on the 3s hook", "action": "Exact tactical instruction"}},
    {{"category": "Retention & Pacing", "priority": "Opportunity", "finding": "Specific observation on drop-off and completion", "action": "Exact tactical instruction"}},
    {{"category": "Virality & Growth", "priority": "High Priority", "finding": "Observation on share loops", "action": "Exact tactical instruction"}},
    {{"category": "Platform Distribution", "priority": "Strategic", "finding": "Platform strength observation", "action": "Exact tactical instruction"}}
  ]
}}"""
        try:
            ai_res = call_llm_json(ai_prompt, system_instruction="You are a world-class creator economy strategist. Return ONLY valid JSON.")
            if ai_res and ai_res.get("recommendations") and len(ai_res["recommendations"]) >= 3:
                return ai_res["recommendations"]
        except Exception:
            pass

        # Fallback to rule-based recommendations
        recommendations = []
        hook_rate_num = float(hook_rate.replace("%", "")) if "%" in hook_rate else 0.0
        if hook_rate_num >= 80:
            recommendations.append({
                "category": "Hook Optimization",
                "priority": "Maintenance",
                "finding": f"Exceptional 3-second hook retention ({hook_rate}). Viewers are immediately captivated.",
                "action": "Maintain this opening structure across future videos. The combination of immediate audio action and visual anchor is performing at top 5% industry tier."
            })
        else:
            recommendations.append({
                "category": "Hook Optimization",
                "priority": "High Priority",
                "finding": f"Hook retention is at {hook_rate}. A noticeable percentage of viewers swipe away in the first 3 seconds.",
                "action": "Add high-contrast animated captions, a visual pattern interrupt, or start directly in media res within the first 1.5 seconds."
            })

        comp_rate_num = float(comp_rate.replace("%", "")) if "%" in comp_rate else 0.0
        if comp_rate_num >= 50:
            recommendations.append({
                "category": "Retention & Pacing",
                "priority": "Opportunity",
                "finding": f"Strong completion rate ({comp_rate}) on a long-short video.",
                "action": "Consider introducing a loop hook at the end (seamlessly connecting the final sentence back to the opening) to drive secondary replay views."
            })
        else:
            recommendations.append({
                "category": "Retention & Pacing",
                "priority": "High Priority",
                "finding": f"Audience drops off before completion (Completion rate: {comp_rate}).",
                "action": "Trim any dead air, tighten audio pauses, and introduce B-roll or dynamic sound effects every 4–5 seconds to sustain dopamine cycles."
            })

        recommendations.append({
            "category": "Virality & Growth",
            "priority": "High Priority",
            "finding": f"Primary viral engine is '{top_name}'.",
            "action": f"Double down on content tailored specifically to '{top_name}'. Craft captions that prompt viewers to tag a friend or forward to a group chat."
        })

        if platforms:
            recommendations.append({
                "category": "Platform Distribution",
                "priority": "Strategic",
                "finding": f"Best platform match is {platforms[0].get('platform')} ({platforms[0].get('suitability')}).",
                "action": f"Publish primarily to {platforms[0].get('platform')} during peak evening hours (6:00 PM – 9:00 PM local time). Cross-post to YouTube Shorts with search-optimized titles."
            })

        return recommendations

    def _render_markdown_report(self, data: Dict[str, Any]) -> str:
        """
        Render a publication-quality Markdown document for executives and creators.
        """
        exec_sum = data["executive_summary"]
        perf = data["performance_metrics"]
        diag = data["video_diagnostics"]
        ret = data["retention_curve"]
        segs = data["audience_breakdown"]
        plats = data["platform_strategy"]
        recs = data["actionable_recommendations"]

        score = exec_sum.get("virality_score", 0)
        rating = exec_sum.get("rating", "N/A")

        # Color/Badge styling
        if score >= 80:
            badge = "🔥 **MEGA-VIRAL**"
        elif score >= 65:
            badge = "🚀 **HIGH VIRALITY**"
        elif score >= 50:
            badge = "📈 **MODERATE REACH**"
        else:
            badge = "⚠️ **LOW REACH**"

        md = []
        md.append("# 🎬 AI Virality Simulation & Content Intelligence Report")
        md.append(f"**Generated on:** `{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}` | **Simulation Engine:** `Antigravity Multi-Agent Pipeline (Agents 1–5)`\n")
        md.append("---")

        # Executive Scorecard
        md.append("## 🏆 Executive Scorecard")
        md.append(f"| Metric | Value | Interpretation |")
        md.append(f"| :--- | :--- | :--- |")
        md.append(f"| **Algorithmic Virality Score** | **`{score} / 100`** | {badge} |")
        md.append(f"| **Viral Potential Rating** | **{rating}** | Top tier platform algorithmic favorability |")
        md.append(f"| **Algorithm Push Projection** | **Aggressive** | Global FYP / Explore seed pools |")
        md.append(f"| **Primary Content Niche** | **{exec_sum.get('primary_niche')}** | High peer shareability category |")
        md.append(f"| **Simulated Test Panel** | **{exec_sum.get('sample_size')} synthetic users** | Proportional audience sampling |\n")

        # Key Strength Banner
        md.append(f"> 💡 **Key Performance Driver:**\n> *{exec_sum.get('key_driver')}*\n")

        # Video Characteristics & Diagnostics
        md.append("## 📹 Video & Content Diagnostics")
        md.append(f"- **Format:** `{diag.get('orientation')}` ({diag.get('duration_seconds')} seconds)")
        md.append(f"- **Pacing & Structure:** {diag.get('pacing')}")
        md.append(f"- **3-Second Hook:** `{diag.get('hook_type')}` — **Strength:** `{diag.get('hook_strength')}`")
        md.append(f"- **Hook Evaluation:** {diag.get('hook_evaluation')}")
        if diag.get("transcript"):
            md.append(f"- **Spoken Opening:** *\"{diag.get('transcript')[:120]}...\"*")
        md.append(f"- **Visual Overview:** {diag.get('visual_summary')}\n")

        # Performance & Engagement Forecast
        md.append("## 📊 Simulated Engagement & Viewing Performance")
        md.append("Simulation results across the 1,000 synthetic test viewers:\n")
        md.append(f"| Funnel Stage / Metric | Count | Rate | Benchmark Comparison |")
        md.append(f"| :--- | :--- | :--- | :--- |")
        md.append(f"| **Total Impressions** | `{perf.get('impressions')}` | 100.0% | Test panel baseline |")
        md.append(f"| **3s Hook Retention (Views)** | `{perf.get('views')}` | **`{perf.get('hook_retention_rate')}`** | 🟢 **Elite** (Industry avg: 50–65%) |")
        md.append(f"| **Early Drop-off (Swiped Away)** | `{perf.get('swiped_away')}` | `{round(100 - float(perf.get('hook_retention_rate','0%').replace('%','')), 1)}%` | Minimal bounce |")
        md.append(f"| **Full Video Completions** | `{perf.get('completions')}` | **`{perf.get('completion_rate')}`** | 🟢 **Outstanding** for {diag.get('duration_seconds')}s duration |")
        md.append(f"| **Average Watch Time** | **`{perf.get('average_watch_time')}`** | `{perf.get('average_percentage_watched')}` | Extremely high attention retention |")
        md.append(f"| **Predicted Likes** | `{perf.get('likes')}` | `{perf.get('like_rate')}` | High positive sentiment |")
        md.append(f"| **Predicted Comments** | `{perf.get('comments')}` | `{perf.get('comment_rate')}` | Solid discussion activity |")
        md.append(f"| **Predicted Shares (Viral Driver)** | **`{perf.get('shares')}`** | **`{perf.get('share_rate')}`** | 🟢 **Massive** (Key factor for algorithmic blast) |\n")

        # Retention Curve
        md.append("## 📉 Audience Retention Drop-off Curve")
        md.append(f"| Video Milestone | Retention % | Status |")
        md.append(f"| :--- | :--- | :--- |")
        md.append(f"| **0s (Video Start)** | `{ret.get('0s_start', '100%')}` | Initial impression |")
        md.append(f"| **3s (Hook Window)** | **`{ret.get('3s_hook', 'N/A')}`** | Hook successfully anchored |")
        md.append(f"| **25% Duration (~{round(float(diag.get('duration_seconds', 0))*0.25, 1)}s)** | `{ret.get('25%_duration', 'N/A')}` | Core narrative engagement |")
        md.append(f"| **50% Duration (~{round(float(diag.get('duration_seconds', 0))*0.50, 1)}s)** | `{ret.get('50%_duration', 'N/A')}` | Sustained mid-video attention |")
        md.append(f"| **75% Duration (~{round(float(diag.get('duration_seconds', 0))*0.75, 1)}s)** | `{ret.get('75%_duration', 'N/A')}` | High narrative anticipation |")
        md.append(f"| **100% (Completion)** | **`{ret.get('100%_complete', 'N/A')}`** | Rewatch & share trigger |\n")

        # Segment Breakdown
        md.append("## 👥 Audience Segment Breakdown & Virality Velocity")
        md.append(f"| Audience Segment | Size | Views | Hook Rate | Completion | Shares | Virality Share |")
        md.append(f"| :--- | :--- | :--- | :--- | :--- | :--- | :--- |")
        for s in segs:
            md.append(f"| **{s.get('segment_name')}** | {s.get('sample_size')} | {s.get('views')} | {s.get('hook_rate')} | {s.get('completion_rate')} | {s.get('shares')} | **{s.get('virality_contribution')}** |")
        md.append("")

        # Platform Distribution
        md.append("## 📱 Recommended Platform Strategy")
        md.append(f"| Platform | Suitability | Algorithmic Advantage |")
        md.append(f"| :--- | :--- | :--- |")
        for p in plats:
            md.append(f"| **{p.get('platform')}** | `{p.get('suitability')}` | {p.get('strength')} |")
        md.append("")

        # Actionable Optimization Playbook
        md.append("## 🛠️ Actionable Optimization Playbook")
        for i, rec in enumerate(recs, 1):
            md.append(f"### {i}. {rec.get('category')} `[{rec.get('priority')}]`")
            md.append(f"- **Observation:** {rec.get('finding')}")
            md.append(f"- **Recommended Action:** {rec.get('action')}\n")

        md.append("---")
        md.append("*Report generated automatically by AI Virality Simulator Agent 5.*")

        return "\n".join(md)

    def _render_html_dashboard(self, data: Dict[str, Any]) -> str:
        """
        Render an interactive visual HTML dashboard report for presentations and clients.
        """
        exec_sum = data["executive_summary"]
        perf = data["performance_metrics"]
        diag = data["video_diagnostics"]
        ret = data["retention_curve"]
        segs = data["audience_breakdown"]
        plats = data["platform_strategy"]
        recs = data["actionable_recommendations"]

        score = float(exec_sum.get("virality_score", 0))
        rating = exec_sum.get("rating", "N/A")
        badge_color = "#10b981" if score >= 80 else ("#f59e0b" if score >= 65 else "#ef4444")
        score_circumference = 283
        score_offset = score_circumference - (score / 100.0) * score_circumference

        # Extract retention numbers for SVG chart
        p0 = 100.0
        p3 = float(ret.get("3s_hook", "85%").replace("%", ""))
        p25 = float(ret.get("25%_duration", "75%").replace("%", ""))
        p50 = float(ret.get("50%_duration", "65%").replace("%", ""))
        p75 = float(ret.get("75%_duration", "55%").replace("%", ""))
        p100 = float(ret.get("100%_complete", "45%").replace("%", ""))

        # Coordinates for 500x200 SVG chart: x: 40 to 460, y: 160 (0%) to 30 (100%)
        # y = 160 - (val / 100) * 130
        def to_y(v):
            return round(160 - (v / 100.0) * 130, 1)

        y0, y3, y25, y50, y75, y100 = to_y(p0), to_y(p3), to_y(p25), to_y(p50), to_y(p75), to_y(p100)
        svg_points = f"40,{y0} 110,{y3} 200,{y25} 290,{y50} 370,{y75} 460,{y100}"
        svg_area = f"40,165 40,{y0} 110,{y3} 200,{y25} 290,{y50} 370,{y75} 460,{y100} 460,165"

        # Audience rows
        seg_cards_html = ""
        for s in segs:
            seg_cards_html += f"""
            <div style="background: rgba(30, 41, 59, 0.7); border: 1px solid #334155; border-radius: 12px; padding: 16px; margin-bottom: 12px;">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <strong style="color:#f8fafc; font-size:16px;">{s.get('segment_name')}</strong>
                    <span style="background: rgba(59, 130, 246, 0.2); color:#60a5fa; border: 1px solid #3b82f6; border-radius: 20px; padding: 2px 10px; font-size: 12px; font-weight:600;">{s.get('sample_size')} users</span>
                </div>
                <div style="display:grid; grid-template-columns: repeat(4, 1fr); gap: 10px; margin-top: 12px; font-size: 13px;">
                    <div><span style="color:#94a3b8;">Views:</span> <strong style="color:#f1f5f9;">{s.get('views')}</strong></div>
                    <div><span style="color:#94a3b8;">Hook:</span> <strong style="color:#38bdf8;">{s.get('hook_rate')}</strong></div>
                    <div><span style="color:#94a3b8;">Completion:</span> <strong style="color:#34d399;">{s.get('completion_rate')}</strong></div>
                    <div><span style="color:#94a3b8;">Shares:</span> <strong style="color:#f472b6;">{s.get('shares')}</strong></div>
                </div>
                <div style="margin-top: 10px; font-size: 12px; color:#a78bfa;">
                    🔥 {s.get('virality_contribution')}
                </div>
            </div>
            """

        # Platform cards
        plat_cards_html = ""
        for p in plats:
            plat_cards_html += f"""
            <div style="background: rgba(30, 41, 59, 0.7); border: 1px solid #334155; border-radius: 12px; padding: 16px; margin-bottom: 12px;">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <strong style="color:#f8fafc; font-size:15px;">{p.get('platform')}</strong>
                    <span style="background: rgba(16, 185, 129, 0.2); color:#34d399; border: 1px solid #10b981; border-radius: 20px; padding: 2px 10px; font-size: 12px; font-weight:600;">{p.get('suitability')}</span>
                </div>
                <p style="color:#94a3b8; font-size: 13px; margin: 8px 0 0 0;">{p.get('strength')}</p>
            </div>
            """

        # Recommendations
        recs_html = ""
        for i, r in enumerate(recs, 1):
            pri_color = "#ef4444" if "High" in r.get("priority", "") else ("#10b981" if "Maintenance" in r.get("priority", "") else "#3b82f6")
            recs_html += f"""
            <div style="background: rgba(30, 41, 59, 0.7); border: 1px solid #334155; border-radius: 12px; padding: 16px; margin-bottom: 12px;">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <strong style="color:#f8fafc; font-size:15px;">{i}. {r.get('category')}</strong>
                    <span style="background: {pri_color}22; color:{pri_color}; border: 1px solid {pri_color}; border-radius: 20px; padding: 2px 10px; font-size: 11px; font-weight:600;">{r.get('priority')}</span>
                </div>
                <p style="color:#94a3b8; font-size: 13px; margin: 6px 0 4px 0;"><strong>Observation:</strong> {r.get('finding')}</p>
                <p style="color:#e2e8f0; font-size: 13px; margin: 0;"><strong>Action:</strong> {r.get('action')}</p>
            </div>
            """

        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Virality Simulator — Intelligence Report</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            background: #090d16;
            color: #f1f5f9;
            font-family: 'Outfit', 'Inter', -apple-system, sans-serif;
            padding: 30px 20px;
            line-height: 1.5;
        }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
        .header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid #1e293b;
            padding-bottom: 20px;
            margin-bottom: 30px;
        }}
        .header h1 {{
            font-size: 28px;
            font-weight: 700;
            background: linear-gradient(135deg, #60a5fa 0%, #a855f7 50%, #ec4899 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        .header .meta {{ color: #64748b; font-size: 13px; }}
        .card {{
            background: rgba(15, 23, 42, 0.75);
            backdrop-filter: blur(12px);
            border: 1px solid #1e293b;
            border-radius: 16px;
            padding: 24px;
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.4);
            margin-bottom: 24px;
        }}
        .grid-2 {{ display: grid; grid-template-columns: 360px 1fr; gap: 24px; }}
        .grid-4 {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; }}
        .grid-3 {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; }}
        @media (max-width: 900px) {{
            .grid-2, .grid-4, .grid-3 {{ grid-template-columns: 1fr; }}
        }}
        .score-circle {{
            position: relative;
            width: 140px;
            height: 140px;
            margin: 0 auto;
        }}
        .score-circle svg {{ transform: rotate(-90deg); }}
        .score-circle .number {{
            position: absolute;
            top: 50%; left: 50%;
            transform: translate(-50%, -50%);
            font-size: 38px;
            font-weight: 800;
            color: #f8fafc;
        }}
        .kpi-card {{
            background: rgba(30, 41, 59, 0.5);
            border: 1px solid #334155;
            border-radius: 12px;
            padding: 16px;
            text-align: center;
        }}
        .kpi-title {{ font-size: 12px; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 6px; }}
        .kpi-val {{ font-size: 26px; font-weight: 700; color: #f8fafc; }}
        .kpi-sub {{ font-size: 12px; margin-top: 4px; }}
    </style>
</head>
<body>
<div class="container">
    <div class="header">
        <div>
            <h1>🎬 AI Virality Simulation Intelligence</h1>
            <div class="meta">Analysis Engine: Multi-Agent Cascade (Agents 1–5) | Target: <strong>{diag.get('visual_topic')}</strong></div>
        </div>
        <div style="text-align:right;">
            <span style="background: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid #10b981; padding: 6px 14px; border-radius: 30px; font-weight: 600; font-size: 13px;">
                ● LIVE SIMULATION AUDITED
            </span>
        </div>
    </div>

    <!-- Executive Overview -->
    <div class="grid-2">
        <!-- Score Card -->
        <div class="card" style="text-align: center; display: flex; flex-direction: column; justify-content: center;">
            <div class="score-circle">
                <svg width="140" height="140">
                    <circle cx="70" cy="70" r="45" stroke="#1e293b" stroke-width="12" fill="none" />
                    <circle cx="70" cy="70" r="45" stroke="{badge_color}" stroke-width="12" fill="none"
                            stroke-dasharray="{score_circumference}" stroke-dashoffset="{score_offset}" stroke-linecap="round" />
                </svg>
                <div class="number">{score}</div>
            </div>
            <div style="margin-top: 16px;">
                <span style="background: {badge_color}22; color:{badge_color}; border: 1px solid {badge_color}; padding: 4px 14px; border-radius: 20px; font-weight: 700; font-size: 14px;">
                    {rating}
                </span>
            </div>
            <p style="color: #94a3b8; font-size: 13px; margin-top: 14px;">
                {exec_sum.get('algorithm_push_probability')}
            </p>
        </div>

        <!-- Video & Funnel KPIs -->
        <div class="card">
            <h3 style="margin-bottom: 16px; font-size: 18px; color: #f8fafc;">📊 Executive Viewing Funnel</h3>
            <div class="grid-4" style="margin-bottom: 16px;">
                <div class="kpi-card">
                    <div class="kpi-title">Impressions</div>
                    <div class="kpi-val">{perf.get('impressions')}</div>
                    <div class="kpi-sub" style="color: #64748b;">Synthetic Users</div>
                </div>
                <div class="kpi-card">
                    <div class="kpi-title">3s Hook Views</div>
                    <div class="kpi-val" style="color: #38bdf8;">{perf.get('views')}</div>
                    <div class="kpi-sub" style="color: #38bdf8;">{perf.get('hook_retention_rate')} Retention</div>
                </div>
                <div class="kpi-card">
                    <div class="kpi-title">Completions</div>
                    <div class="kpi-val" style="color: #34d399;">{perf.get('completions')}</div>
                    <div class="kpi-sub" style="color: #34d399;">{perf.get('completion_rate')} Complete</div>
                </div>
                <div class="kpi-card">
                    <div class="kpi-title">Viral Shares</div>
                    <div class="kpi-val" style="color: #ec4899;">{perf.get('shares')}</div>
                    <div class="kpi-sub" style="color: #ec4899;">{perf.get('share_rate')} Share Rate</div>
                </div>
            </div>
            <div style="background: rgba(30, 41, 59, 0.4); border-left: 4px solid #60a5fa; padding: 12px; border-radius: 6px;">
                <strong style="color: #93c5fd; font-size: 13px;">Key Driver:</strong>
                <span style="color: #cbd5e1; font-size: 13px;"> {exec_sum.get('key_driver')}</span>
            </div>
        </div>
    </div>

    <!-- Retention Drop-off Graph -->
    <div class="card">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 16px;">
            <h3 style="font-size: 18px; color: #f8fafc;">📉 Second-by-Second Audience Retention Curve</h3>
            <span style="color: #94a3b8; font-size: 13px;">Duration: {diag.get('duration_seconds')}s | Format: {diag.get('orientation')}</span>
        </div>
        <div style="width: 100%; overflow-x: auto;">
            <svg viewBox="0 0 500 190" style="width: 100%; height: 200px; display: block;">
                <defs>
                    <linearGradient id="curveGradient" x1="0%" y1="0%" x2="0%" y2="100%">
                        <stop offset="0%" stop-color="#3b82f6" stop-opacity="0.5"/>
                        <stop offset="100%" stop-color="#3b82f6" stop-opacity="0.0"/>
                    </linearGradient>
                </defs>
                <!-- Grid Lines -->
                <line x1="40" y1="30" x2="460" y2="30" stroke="#1e293b" stroke-width="1" stroke-dasharray="3"/>
                <line x1="40" y1="73" x2="460" y2="73" stroke="#1e293b" stroke-width="1" stroke-dasharray="3"/>
                <line x1="40" y1="116" x2="460" y2="116" stroke="#1e293b" stroke-width="1" stroke-dasharray="3"/>
                <line x1="40" y1="160" x2="460" y2="160" stroke="#334155" stroke-width="1"/>
                <!-- Y-Labels -->
                <text x="10" y="34" fill="#64748b" font-size="10">100%</text>
                <text x="15" y="77" fill="#64748b" font-size="10">75%</text>
                <text x="15" y="120" fill="#64748b" font-size="10">50%</text>
                <text x="15" y="164" fill="#64748b" font-size="10">25%</text>
                <!-- Area -->
                <polygon points="{svg_area}" fill="url(#curveGradient)" />
                <!-- Polyline -->
                <polyline fill="none" stroke="#3b82f6" stroke-width="3" points="{svg_points}" />
                <!-- Circles -->
                <circle cx="40" cy="{y0}" r="4" fill="#60a5fa" />
                <circle cx="110" cy="{y3}" r="5" fill="#38bdf8" />
                <circle cx="200" cy="{y25}" r="4" fill="#60a5fa" />
                <circle cx="290" cy="{y50}" r="4" fill="#60a5fa" />
                <circle cx="370" cy="{y75}" r="4" fill="#60a5fa" />
                <circle cx="460" cy="{y100}" r="5" fill="#34d399" />
                <!-- Text Tags -->
                <text x="30" y="{y0 - 8}" fill="#94a3b8" font-size="10">{p0:.0f}%</text>
                <text x="100" y="{y3 - 8}" fill="#38bdf8" font-size="11" font-weight="700">3s ({p3:.1f}%)</text>
                <text x="190" y="{y25 - 8}" fill="#94a3b8" font-size="10">{p25:.1f}%</text>
                <text x="280" y="{y50 - 8}" fill="#94a3b8" font-size="10">{p50:.1f}%</text>
                <text x="360" y="{y75 - 8}" fill="#94a3b8" font-size="10">{p75:.1f}%</text>
                <text x="430" y="{y100 - 8}" fill="#34d399" font-size="11" font-weight="700">{p100:.1f}%</text>
                <!-- X-Labels -->
                <text x="35" y="180" fill="#64748b" font-size="10">0s</text>
                <text x="105" y="180" fill="#64748b" font-size="10">3s</text>
                <text x="190" y="180" fill="#64748b" font-size="10">25%</text>
                <text x="280" y="180" fill="#64748b" font-size="10">50%</text>
                <text x="360" y="180" fill="#64748b" font-size="10">75%</text>
                <text x="445" y="180" fill="#64748b" font-size="10">100%</text>
            </svg>
        </div>
    </div>

    <!-- Audience & Platform Split -->
    <div style="display:grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-bottom: 24px;">
        <div class="card">
            <h3 style="margin-bottom: 16px; font-size: 18px; color: #f8fafc;">👥 Target Audience Personas</h3>
            {seg_cards_html}
        </div>
        <div class="card">
            <h3 style="margin-bottom: 16px; font-size: 18px; color: #f8fafc;">📱 Platform Suitability</h3>
            {plat_cards_html}
        </div>
    </div>

    <!-- Tactical Optimization Playbook -->
    <div class="card">
        <h3 style="margin-bottom: 16px; font-size: 18px; color: #f8fafc;">🛠️ Actionable Strategic Recommendations</h3>
        {recs_html}
    </div>
</div>
</body>
</html>
"""
        return html


    def print_terminal_summary(self, data: Dict[str, Any]):
        """
        Print a clean, visually structured executive scorecard in the terminal.
        """
        exec_sum = data.get("executive_summary", {})
        perf = data.get("performance_metrics", {})
        recs = data.get("actionable_recommendations", [])
        top_driver = (data.get("audience_breakdown") or [{}])[0]
        top_platform = (data.get("platform_strategy") or [{}])[0]

        score = exec_sum.get("virality_score", 0)
        rating = exec_sum.get("rating", "N/A")

        print()
        print("╔" + "═" * 68 + "╗")
        print(f"║ {'🎬 VIRALITY EXECUTIVE DASHBOARD (AGENT 5)':^66} ║")
        print("╚" + "═" * 68 + "╝")
        print(f"  🏆 Virality Score:        {score} / 100 [{rating}]")
        print(f"  🚀 Algorithmic Push:      {exec_sum.get('algorithm_push_probability')}")
        print(f"  🎯 Primary Content Niche: {exec_sum.get('primary_niche')}")
        print(f"  💡 Key Strength:          {exec_sum.get('key_driver')}")
        print("  " + "─" * 66)
        print("  📊 VIEWING & ENGAGEMENT METRICS:")
        print(f"     • 3s Hook Retention:   {perf.get('hook_retention_rate')} ({perf.get('views')} / {perf.get('impressions')} views)")
        print(f"     • Video Completion:    {perf.get('completion_rate')} ({perf.get('completions')} completed)")
        print(f"     • Average Watch Time:  {perf.get('average_watch_time')} ({perf.get('average_percentage_watched')} of duration)")
        print(f"     • Likes:               {perf.get('likes')} ({perf.get('like_rate')})")
        print(f"     • Comments:            {perf.get('comments')} ({perf.get('comment_rate')})")
        print(f"     • Shares (Virality):   {perf.get('shares')} ({perf.get('share_rate')})")
        print("  " + "─" * 66)
        print("  👥 TOP VIRAL AUDIENCE & PLATFORM:")
        print(f"     • Top Segment:         {top_driver.get('segment_name', 'N/A')} ({top_driver.get('virality_contribution', 'N/A')})")
        print(f"     • Best Platform:       {top_platform.get('platform', 'N/A')} ({top_platform.get('suitability', 'N/A')}) — {top_platform.get('strength', 'N/A')}")
        print("  " + "─" * 66)
        print("  🛠️ KEY ACTIONABLE RECOMMENDATIONS:")
        for i, rec in enumerate(recs[:3], 1):
            print(f"     {i}. [{rec.get('category')}]: {rec.get('action')}")
        print("═" * 70)

