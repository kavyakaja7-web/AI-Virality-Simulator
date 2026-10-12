"""
=========================================================
AGENT 6 — CONTENT OPTIMIZER & VIRAL FIXER AGENT
=========================================================

Purpose:
    The definitive actionable finale of the AI Virality Simulator.
    Transforms simulation diagnostics, audience drop-off curves,
    and platform strengths into an executive-grade viral remediation
    and growth playbook:
    1. 3 Pattern-Interrupt Hook Rewrites (Visual, Spoken, Text, SFX)
    2. Scene-by-Scene Pacing & Cut Instructions (The Re-Edit Blueprint)
    3. Platform-Specific Viral Packaging (Reels, TikTok, Shorts)
    4. Mathematical Projected Virality Uplift & Reach Multiplier

Outputs:
    1. outputs/viral_optimization_plan.json (Structured machine-readable data)
    2. outputs/VIRAL_OPTIMIZATION_PLAN.md   (Executive Creator Playbook)
    3. outputs/optimization_dashboard.html  (Interactive HTML Dashboard)

=========================================================
"""

import json
import os
import sys
from datetime import datetime
from typing import Dict, Any, Optional

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
if hasattr(sys.stderr, "reconfigure"):
    try:
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

from services.optimizer_service import generate_optimization_plan



class Agent6ContentOptimizer:
    """
    AGENT 6 — CONTENT OPTIMIZER & VIRAL FIXER AGENT
    """

    def __init__(self):
        print()
        print("=" * 60)
        print("🚀 AGENT 6 — CONTENT OPTIMIZER & VIRAL FIXER AGENT")
        print("=" * 60)
        print("Agent 6 initialized successfully.")

    def optimize(
        self,
        content_profile: Dict[str, Any],
        audience_profile: Dict[str, Any],
        population_profile: Optional[Dict[str, Any]] = None,
        engagement_prediction: Optional[Dict[str, Any]] = None,
        virality_report: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Synthesize simulation diagnostics into an actionable, high-impact
        viral remediation plan and projected uplift simulation.
        """
        print()
        print("=" * 60)
        print("🚀 AGENT 6 STARTED")
        print("=" * 60)

        # -------------------------------------------------
        # STEP 1 — Ingest diagnostics and simulation results
        # -------------------------------------------------
        print()
        print("[Agent 6 - Step 1]")
        print("Ingesting diagnostic data & drop-off curves from Agents 1–5...")

        # If engagement_prediction or virality_report wasn't passed, check files
        if not engagement_prediction and os.path.exists("outputs/engagement_prediction.json"):
            try:
                with open("outputs/engagement_prediction.json", "r", encoding="utf-8") as f:
                    engagement_prediction = json.load(f)
            except Exception:
                pass

        if not virality_report and os.path.exists("outputs/virality_report.json"):
            try:
                with open("outputs/virality_report.json", "r", encoding="utf-8") as f:
                    virality_report = json.load(f)
            except Exception:
                pass

        # -------------------------------------------------
        # STEP 2 — Generate AI Optimization Plan
        # -------------------------------------------------
        print()
        print("[Agent 6 - Step 2]")
        print("Engineering high-retention hooks and scene re-edit blueprint...")

        raw_plan = generate_optimization_plan(
            content_profile=content_profile,
            audience_profile=audience_profile,
            population_profile=population_profile,
            engagement_prediction=engagement_prediction,
            virality_report=virality_report
        )

        metadata = content_profile.get("video_metadata", {})
        visual = content_profile.get("visual_analysis", {})
        primary_niche = audience_profile.get("content_summary", {}).get("primary_niche") or visual.get("topic", "General")

        optimization_data = {
            "agent": {
                "id": "agent_6",
                "name": "Content Optimizer & Viral Fixer Agent"
            },
            "timestamp": datetime.now().isoformat(),
            "target_content": {
                "primary_niche": primary_niche,
                "duration_seconds": metadata.get("duration_seconds", 15.0),
                "orientation": metadata.get("orientation", "vertical")
            },
            "vulnerability_diagnosis": raw_plan["vulnerabilities"],
            "hook_rewrites": raw_plan["hook_rewrites"],
            "scene_cut_blueprint": raw_plan["scene_cut_blueprint"],
            "platform_packaging": raw_plan["platform_packaging"],
            "projected_uplift": raw_plan["projected_uplift"]
        }

        print(f"✓ Engineered {len(optimization_data['hook_rewrites'])} pattern-interrupt hook rewrites.")
        print(f"✓ Formulated {len(optimization_data['scene_cut_blueprint'])} scene re-edit cut points.")
        print("✓ Packaged platform publishing kits for Instagram Reels, TikTok, and YouTube Shorts.")
        print(f"✓ Projected Virality Uplift: {optimization_data['projected_uplift']['baseline_virality_score']} ➡️  {optimization_data['projected_uplift']['projected_virality_score']} ({optimization_data['projected_uplift']['score_uplift_percentage']})")

        # -------------------------------------------------
        # STEP 3 — Save JSON Artifact
        # -------------------------------------------------
        print()
        print("[Agent 6 - Step 3]")
        print("Compiling structured optimization output (viral_optimization_plan.json)...")

        os.makedirs("outputs", exist_ok=True)
        json_path = "outputs/viral_optimization_plan.json"
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(optimization_data, f, indent=4)
        print(f"✓ Saved structured optimization plan to {json_path}")

        # -------------------------------------------------
        # STEP 4 — Render Executive Markdown Playbook
        # -------------------------------------------------
        print()
        print("[Agent 6 - Step 4]")
        print("Rendering executive creator playbook (VIRAL_OPTIMIZATION_PLAN.md)...")

        md_content = self._render_markdown_playbook(optimization_data)
        md_path = "outputs/VIRAL_OPTIMIZATION_PLAN.md"
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(md_content)
        print(f"✓ Saved executive creator playbook to {md_path}")

        # -------------------------------------------------
        # STEP 5 — Render Interactive HTML Dashboard
        # -------------------------------------------------
        print()
        print("[Agent 6 - Step 5]")
        print("Rendering interactive optimization dashboard (optimization_dashboard.html)...")

        html_content = self._render_html_dashboard(optimization_data)
        html_path = "outputs/optimization_dashboard.html"
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"✓ Saved interactive HTML dashboard to {html_path}")

        # -------------------------------------------------
        # AGENT 6 COMPLETE
        # -------------------------------------------------
        print()
        print("=" * 60)
        print("🚀 AGENT 6 COMPLETED")
        print("=" * 60)

        return optimization_data

    def _render_markdown_playbook(self, data: Dict[str, Any]) -> str:
        """
        Renders a publication-grade, creator-ready Markdown playbook.
        """
        target = data["target_content"]
        vulns = data["vulnerability_diagnosis"]
        hooks = data["hook_rewrites"]
        cuts = data["scene_cut_blueprint"]
        pkg = data["platform_packaging"]
        uplift = data["projected_uplift"]

        reels = pkg.get("instagram_reels", {})
        tiktok = pkg.get("tiktok", {})
        shorts = pkg.get("youtube_shorts", {})

        md = f"""# 🚀 Viral Content Optimization Playbook (Agent 6)

**Niche:** `{target.get('primary_niche')}` | **Duration:** `{target.get('duration_seconds')}s` | **Format:** `{target.get('orientation')}`  
**Generated:** `{data.get('timestamp')}`

---

## 📈 Executive Uplift & ROI Summary

| Metric | Baseline (Current) | Projected (Optimized) | Net Improvement |
| :--- | :---: | :---: | :---: |
| **Virality Score** | **{uplift.get('baseline_virality_score')} / 100** | **{uplift.get('projected_virality_score')} / 100** | **`{uplift.get('score_uplift_points')}` (`{uplift.get('score_uplift_percentage')}`)** |
| **3s Hook Retention** | {uplift.get('baseline_hook_retention')} | {uplift.get('projected_hook_retention')} | `{uplift.get('hook_retention_uplift')}` |
| **Completion Rate** | {uplift.get('baseline_completion_rate')} | {uplift.get('projected_completion_rate')} | `{uplift.get('completion_rate_uplift')}` |
| **Viral Share Rate** | {uplift.get('baseline_share_rate')} | {uplift.get('projected_share_rate')} | `{uplift.get('share_rate_uplift')}` |
| **Algorithmic Tier** | Seed Discovery | {uplift.get('projected_distribution_tier')} | **{uplift.get('estimated_reach_multiplier')}** |

---

## ⚠️ Diagnosed Drop-Off Bottlenecks

"""
        for v in vulns:
            badge = "🔴" if v.get("severity") == "CRITICAL" else ("🟠" if v.get("severity") == "HIGH" else "🟡")
            md += f"""### {badge} {v.get('dimension')} `[{v.get('severity')}]`
- **Finding:** {v.get('finding')}
- **Algorithmic Impact:** {v.get('impact')}
- **Remediation Action:** {v.get('remedy')}

"""

        md += """---

## 🎣 3 High-Retention Pattern-Interrupt Hook Rewrites

To overcome algorithmic swipe-away within the first 3 seconds, deploy one of these tested hook variants:

"""
        for h in hooks:
            md += f"""### Variant {h.get('variant_id')}: {h.get('hook_style')}
*Trigger: `{h.get('psychological_trigger')}` | Projected Hook Retention: `{h.get('expected_retention')}`*

- **Visual Direction (0.0s – 1.5s):**  
  > {h.get('visual_action')}
- **Spoken Voiceover Script:**  
  > 🗣️ *"{h.get('spoken_script')}"*
- **On-Screen Text Overlay:**  
  > 🔤 **{h.get('on_screen_text')}**
- **Audio / SFX Cue:**  
  > 🔊 `{h.get('audio_sfx_cue')}`

"""

        md += """---

## ✂️ Scene-by-Scene Re-Edit Cut Blueprint

Execute these timeline adjustments in your video editor (CapCut, Premiere Pro, DaVinci):

| Timestamp | Action Type | Exact Editing Direction | Algorithmic Rationale |
| :--- | :--- | :--- | :--- |
"""
        for c in cuts:
            md += f"| `{c.get('timestamp_range')}` | **{c.get('action_type')}** | {c.get('instruction')} | {c.get('algorithmic_reasoning', 'Pacing reset')} |\n"

        md += f"""
---

## 📱 Platform-Specific Publishing Kits

### 1. 📸 Instagram Reels Strategy
- **Cover Headline:** `{reels.get('cover_headline')}`
- **Audio Cue:** {reels.get('audio_recommendation')}
- **Best Posting Window:** `{reels.get('best_posting_window')}`
- **Caption & DM Trigger:**
```text
{reels.get('caption')}
```
- **Recommended Hashtags:**
`{' '.join(reels.get('hashtags', []))}`

---

### 2. 🎵 TikTok Strategy
- **First-Line Hook:** `{tiktok.get('first_line_hook')}`
- **Sound Strategy:** {tiktok.get('sound_strategy')}
- **Comment-Bait Question:**
> *"{tiktok.get('comment_bait_question')}"*
- **TikTok Search SEO Keywords:**
`{', '.join(tiktok.get('seo_keywords', []))}`
- **Hashtags:**
`{' '.join(tiktok.get('hashtags', []))}`

---

### 3. 🔴 YouTube Shorts Strategy
- **CTR Title:** `{shorts.get('ctr_title')}`
- **Pinned Comment:**
> *"{shorts.get('pinned_comment')}"*
- **Search Tags:**
`{', '.join(shorts.get('search_tags', []))}`

---

*Generated by AI Virality Simulator Agent 6. Ready for creator execution.*
"""
        return md

    def _render_html_dashboard(self, data: Dict[str, Any]) -> str:
        """
        Renders an ultra-modern dark-mode interactive HTML dashboard.
        """
        target = data["target_content"]
        vulns = data["vulnerability_diagnosis"]
        hooks = data["hook_rewrites"]
        cuts = data["scene_cut_blueprint"]
        pkg = data["platform_packaging"]
        uplift = data["projected_uplift"]

        reels = pkg.get("instagram_reels", {})
        tiktok = pkg.get("tiktok", {})
        shorts = pkg.get("youtube_shorts", {})

        # Build hook cards HTML
        hook_cards_html = ""
        for h in hooks:
            hook_cards_html += f"""
            <div class="hook-card">
                <div class="hook-header">
                    <span class="hook-badge">Variant {h.get('variant_id')}</span>
                    <span class="hook-style">{h.get('hook_style')}</span>
                    <span class="hook-stat">⚡ {h.get('expected_retention')} Est. Retention</span>
                </div>
                <div class="hook-body">
                    <div class="hook-row">
                        <span class="hook-label">👁️ Visual Cue:</span>
                        <span class="hook-val">{h.get('visual_action')}</span>
                    </div>
                    <div class="hook-row">
                        <span class="hook-label">🗣️ Voiceover:</span>
                        <span class="hook-val quote">"{h.get('spoken_script')}"</span>
                    </div>
                    <div class="hook-row">
                        <span class="hook-label">🔤 Text Overlay:</span>
                        <span class="hook-val highlight">{h.get('on_screen_text')}</span>
                    </div>
                    <div class="hook-row">
                        <span class="hook-label">🔊 SFX Cue:</span>
                        <span class="hook-val sfx">{h.get('audio_sfx_cue')}</span>
                    </div>
                </div>
            </div>
            """

        # Build cut rows HTML
        cut_rows_html = ""
        for c in cuts:
            cut_rows_html += f"""
            <tr class="cut-row">
                <td class="time-col"><code>{c.get('timestamp_range')}</code></td>
                <td class="action-col"><span class="action-tag">{c.get('action_type')}</span></td>
                <td class="desc-col">{c.get('instruction')}</td>
                <td class="reason-col">{c.get('algorithmic_reasoning', 'Pacing reset')}</td>
            </tr>
            """

        # Build vulnerabilities HTML
        vuln_cards_html = ""
        for v in vulns:
            sev_class = "sev-crit" if v.get("severity") == "CRITICAL" else ("sev-high" if v.get("severity") == "HIGH" else "sev-mod")
            vuln_cards_html += f"""
            <div class="vuln-card {sev_class}">
                <div class="vuln-top">
                    <span class="vuln-dim">{v.get('dimension')}</span>
                    <span class="vuln-badge">{v.get('severity')}</span>
                </div>
                <p class="vuln-find">{v.get('finding')}</p>
                <div class="vuln-rem"><strong>Fix:</strong> {v.get('remedy')}</div>
            </div>
            """

        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Virality Simulator — Agent 6 Viral Optimization Playbook</title>
    <style>
        :root {{
            --bg: #0b0f19;
            --card-bg: #111827;
            --border: rgba(255, 255, 255, 0.08);
            --border-subtle: rgba(255, 255, 255, 0.12);
            --primary: #3b82f6;
            --accent: #6366f1;
            --success: #10b981;
            --warning: #f59e0b;
            --danger: #ef4444;
            --text-main: #f8fafc;
            --text-sub: #94a3b8;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Plus Jakarta Sans", sans-serif; }}
        body {{ background: var(--bg); color: var(--text-main); padding: 32px 20px; line-height: 1.5; }}
        .container {{ max-width: 1200px; margin: 0 auto; }}

        /* Header */
        .header {{
            display: flex; justify-content: space-between; align-items: center;
            background: var(--card-bg);
            border: 1px solid var(--border); border-radius: 14px; padding: 20px 28px;
            margin-bottom: 24px; box-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
        }}
        .header h1 {{ font-size: 22px; font-weight: 700; color: #f8fafc; }}
        .header-meta {{ display: flex; gap: 12px; font-size: 13px; color: var(--text-sub); }}
        .badge {{ background: rgba(59, 130, 246, 0.12); color: #60a5fa; padding: 4px 10px; border-radius: 6px; border: 1px solid rgba(59, 130, 246, 0.25); font-weight: 600; font-size: 12px; }}

        /* Scorecard Section */
        .scorecard-banner {{
            display: grid; grid-template-columns: 1.2fr 2fr; gap: 20px; margin-bottom: 24px;
        }}
        .uplift-dial-card {{
            background: var(--card-bg);
            border: 1px solid var(--border); border-radius: 14px; padding: 24px;
            display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
        }}
        .dial-label {{ font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; color: var(--text-sub); margin-bottom: 8px; font-weight: 600; }}
        .dial-comparison {{ display: flex; align-items: baseline; gap: 12px; margin: 12px 0; }}
        .score-old {{ font-size: 32px; font-weight: 700; color: #64748b; text-decoration: line-through; }}
        .score-arrow {{ font-size: 24px; color: var(--primary); }}
        .score-new {{ font-size: 56px; font-weight: 800; color: #10b981; }}
        .score-gain-pill {{ background: rgba(16, 185, 129, 0.12); color: #10b981; border: 1px solid rgba(16, 185, 129, 0.25); padding: 4px 12px; border-radius: 6px; font-size: 13px; font-weight: 600; }}

        .metrics-grid {{
            display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px;
        }}
        .metric-card {{
            background: var(--card-bg); border: 1px solid var(--border); border-radius: 14px; padding: 18px;
            display: flex; flex-direction: column; justify-content: space-between;
        }}
        .metric-title {{ font-size: 13px; color: var(--text-sub); }}
        .metric-val {{ font-size: 22px; font-weight: 800; margin: 4px 0; color: #f8fafc; }}
        .metric-uplift {{ font-size: 12px; font-weight: 600; color: #34d399; }}

        /* Sections */
        .section-card {{
            background: var(--card-bg); border: 1px solid var(--border); border-radius: 16px; padding: 28px;
            margin-bottom: 24px; backdrop-filter: blur(8px);
        }}
        .section-title {{ font-size: 20px; font-weight: 700; color: #f8fafc; margin-bottom: 20px; display: flex; align-items: center; gap: 10px; }}

        /* Vulnerabilities */
        .vuln-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px; }}
        .vuln-card {{ background: rgba(15, 23, 42, 0.6); border-radius: 12px; padding: 16px; border-left: 4px solid #64748b; }}
        .sev-crit {{ border-left-color: var(--danger); }}
        .sev-high {{ border-left-color: var(--warning); }}
        .sev-mod {{ border-left-color: var(--primary); }}
        .vuln-top {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; }}
        .vuln-dim {{ font-size: 14px; font-weight: 700; color: #f8fafc; }}
        .vuln-badge {{ font-size: 10px; font-weight: 800; padding: 2px 6px; border-radius: 4px; background: rgba(255, 255, 255, 0.1); }}
        .vuln-find {{ font-size: 13px; color: #cbd5e1; margin-bottom: 8px; }}
        .vuln-rem {{ font-size: 12px; color: #93c5fd; background: rgba(59, 130, 246, 0.1); padding: 6px 10px; border-radius: 6px; }}

        /* Hook Cards */
        .hooks-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px; }}
        .hook-card {{
            background: rgba(15, 23, 42, 0.8); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 14px;
            padding: 20px; transition: transform 0.2s, border-color 0.2s;
        }}
        .hook-card:hover {{ transform: translateY(-3px); border-color: rgba(99, 102, 241, 0.4); }}
        .hook-header {{ display: flex; align-items: center; gap: 8px; margin-bottom: 14px; flex-wrap: wrap; }}
        .hook-badge {{ background: #4f46e5; color: #fff; font-size: 11px; font-weight: 800; padding: 3px 8px; border-radius: 6px; }}
        .hook-style {{ font-size: 14px; font-weight: 700; color: #f8fafc; flex: 1; }}
        .hook-stat {{ font-size: 11px; color: #34d399; font-weight: 700; }}
        .hook-row {{ margin-bottom: 10px; font-size: 13px; display: flex; flex-direction: column; gap: 2px; }}
        .hook-label {{ font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; color: var(--text-sub); }}
        .hook-val {{ color: #e2e8f0; }}
        .hook-val.quote {{ color: #93c5fd; font-style: italic; background: rgba(30, 41, 59, 0.5); padding: 8px; border-radius: 6px; }}
        .hook-val.highlight {{ color: #fef08a; font-weight: 700; }}
        .hook-val.sfx {{ color: #c084fc; font-family: monospace; font-size: 12px; }}

        /* Cuts Table */
        .table-wrap {{ overflow-x: auto; }}
        table {{ width: 100%; border-collapse: collapse; text-align: left; font-size: 13px; }}
        th {{ color: var(--text-sub); font-size: 11px; text-transform: uppercase; padding: 12px 14px; border-bottom: 1px solid var(--border); }}
        td {{ padding: 14px; border-bottom: 1px solid rgba(255, 255, 255, 0.04); vertical-align: top; }}
        .time-col code {{ background: rgba(59, 130, 246, 0.15); color: #93c5fd; padding: 3px 8px; border-radius: 4px; font-weight: 700; }}
        .action-tag {{ background: rgba(139, 92, 246, 0.15); color: #c084fc; padding: 3px 8px; border-radius: 4px; font-weight: 600; }}
        .desc-col {{ color: #e2e8f0; }}
        .reason-col {{ color: #94a3b8; font-size: 12px; }}

        /* Platform Packaging Tabs */
        .platform-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px; }}
        .plat-card {{ background: rgba(15, 23, 42, 0.8); border: 1px solid var(--border); border-radius: 14px; padding: 20px; }}
        .plat-card h4 {{ font-size: 16px; margin-bottom: 12px; display: flex; align-items: center; gap: 8px; }}
        .copy-block {{ background: rgba(0, 0, 0, 0.3); border: 1px solid rgba(255, 255, 255, 0.05); border-radius: 8px; padding: 12px; font-size: 12px; color: #cbd5e1; white-space: pre-wrap; font-family: monospace; margin: 8px 0; }}
        .tag-pill {{ display: inline-block; background: rgba(255, 255, 255, 0.06); color: #94a3b8; font-size: 11px; padding: 2px 6px; border-radius: 4px; margin: 2px; }}
    </style>
</head>
<body>
<div class="container">

    <!-- Top Header -->
    <div class="header">
        <div>
            <h1>🚀 Viral Content Optimization Playbook</h1>
            <p style="color: var(--text-sub); font-size: 13px; margin-top: 4px;">Agent 6 Definitive Action Plan & Projected Virality Uplift</p>
        </div>
        <div class="header-meta">
            <span class="badge">Niche: {target.get('primary_niche')}</span>
            <span class="badge">{target.get('duration_seconds')}s Duration</span>
            <span class="badge">{target.get('orientation')}</span>
        </div>
    </div>

    <!-- Uplift Scorecard -->
    <div class="scorecard-banner">
        <div class="uplift-dial-card">
            <div class="dial-label">Projected Virality Score Uplift</div>
            <div class="dial-comparison">
                <span class="score-old">{uplift.get('baseline_virality_score')}</span>
                <span class="score-arrow">➡️</span>
                <span class="score-new">{uplift.get('projected_virality_score')}</span>
            </div>
            <div class="score-gain-pill">{uplift.get('score_uplift_points')} ({uplift.get('score_uplift_percentage')} Uplift)</div>
            <div style="font-size: 12px; color: var(--text-sub); margin-top: 12px;">{uplift.get('projected_distribution_tier')}</div>
        </div>

        <div class="metrics-grid">
            <div class="metric-card">
                <div class="metric-title">3s Hook Retention</div>
                <div class="metric-val">{uplift.get('projected_hook_retention')}</div>
                <div class="metric-uplift">↑ {uplift.get('hook_retention_uplift')} (from {uplift.get('baseline_hook_retention')})</div>
            </div>
            <div class="metric-card">
                <div class="metric-title">Video Completion Rate</div>
                <div class="metric-val">{uplift.get('projected_completion_rate')}</div>
                <div class="metric-uplift">↑ {uplift.get('completion_rate_uplift')} (from {uplift.get('baseline_completion_rate')})</div>
            </div>
            <div class="metric-card">
                <div class="metric-title">Viral Share Multiplier</div>
                <div class="metric-val">{uplift.get('projected_share_rate')}</div>
                <div class="metric-uplift">↑ {uplift.get('share_rate_uplift')} (from {uplift.get('baseline_share_rate')})</div>
            </div>
            <div class="metric-card">
                <div class="metric-title">Estimated Organic Reach</div>
                <div class="metric-val" style="font-size: 18px; color: #38bdf8;">{uplift.get('estimated_reach_multiplier')}</div>
                <div class="metric-uplift" style="color: #94a3b8;">FYP Algorithm Expansion</div>
            </div>
        </div>
    </div>

    <!-- Diagnosed Vulnerabilities -->
    <div class="section-card">
        <div class="section-title">⚠️ Identified Retention Bottlenecks</div>
        <div class="vuln-grid">
            {vuln_cards_html}
        </div>
    </div>

    <!-- 3 Hook Rewrites -->
    <div class="section-card">
        <div class="section-title">🎣 3 Pattern-Interrupt Hook Rewrites (Pattern Disruptors)</div>
        <div class="hooks-grid">
            {hook_cards_html}
        </div>
    </div>

    <!-- Scene-by-Scene Cuts -->
    <div class="section-card">
        <div class="section-title">✂️ Scene-by-Scene Re-Edit Cut Blueprint</div>
        <div class="table-wrap">
            <table>
                <thead>
                    <tr>
                        <th>Timestamp</th>
                        <th>Action Type</th>
                        <th>Video Editing Direction</th>
                        <th>Algorithmic Rationale</th>
                    </tr>
                </thead>
                <tbody>
                    {cut_rows_html}
                </tbody>
            </table>
        </div>
    </div>

    <!-- Platform Packaging -->
    <div class="section-card">
        <div class="section-title">📱 Multi-Platform Publishing Kits</div>
        <div class="platform-grid">
            <!-- Instagram -->
            <div class="plat-card">
                <h4 style="color: #ec4899;">📸 Instagram Reels</h4>
                <div style="font-size: 12px; color: var(--text-sub); margin-bottom: 6px;"><strong>Cover Text:</strong> {reels.get('cover_headline')}</div>
                <div style="font-size: 12px; color: var(--text-sub); margin-bottom: 6px;"><strong>Posting Window:</strong> {reels.get('best_posting_window')}</div>
                <div class="copy-block">{reels.get('caption')}</div>
                <div>{' '.join([f'<span class="tag-pill">{t}</span>' for t in reels.get('hashtags', [])])}</div>
            </div>

            <!-- TikTok -->
            <div class="plat-card">
                <h4 style="color: #38bdf8;">🎵 TikTok</h4>
                <div style="font-size: 12px; color: var(--text-sub); margin-bottom: 6px;"><strong>First-Line Hook:</strong> {tiktok.get('first_line_hook')}</div>
                <div style="font-size: 12px; color: var(--text-sub); margin-bottom: 6px;"><strong>Sound Cue:</strong> {tiktok.get('sound_strategy')}</div>
                <div class="copy-block">Question: {tiktok.get('comment_bait_question')}</div>
                <div>{' '.join([f'<span class="tag-pill">{t}</span>' for t in tiktok.get('hashtags', [])])}</div>
            </div>

            <!-- YouTube Shorts -->
            <div class="plat-card">
                <h4 style="color: #ef4444;">🔴 YouTube Shorts</h4>
                <div style="font-size: 12px; color: var(--text-sub); margin-bottom: 6px;"><strong>CTR Title:</strong> {shorts.get('ctr_title')}</div>
                <div class="copy-block">Pinned Comment: {shorts.get('pinned_comment')}</div>
                <div>{' '.join([f'<span class="tag-pill">#{t}</span>' for t in shorts.get('search_tags', [])])}</div>
            </div>
        </div>
    </div>

</div>
</body>
</html>
"""
        return html

    def print_terminal_summary(self, data: Dict[str, Any]):
        """
        Print a striking, formatted executive optimization scorecard in the terminal.
        """
        uplift = data.get("projected_uplift", {})
        target = data.get("target_content", {})
        hooks = data.get("hook_rewrites", [])
        cuts = data.get("scene_cut_blueprint", [])
        pkg = data.get("platform_packaging", {})
        reels = pkg.get("instagram_reels", {})

        print()
        print("╔" + "═" * 68 + "╗")
        print(f"║ {'🚀 VIRAL CONTENT OPTIMIZATION PLAYBOOK (AGENT 6)':^66} ║")
        print("╚" + "═" * 68 + "╝")
        print(f"  🎯 Content Niche:         {target.get('primary_niche')}")
        print(f"  ⏱️ Video Duration:        {target.get('duration_seconds')}s ({target.get('orientation')})")
        print("  " + "─" * 66)
        print("  📈 PROJECTED VIRALITY UPLIFT & ROI:")
        print(f"     • Virality Score:      {uplift.get('baseline_virality_score')} ➡️  {uplift.get('projected_virality_score')} / 100 [{uplift.get('score_uplift_points')}, {uplift.get('score_uplift_percentage')}]")
        print(f"     • 3s Hook Retention:   {uplift.get('baseline_hook_retention')} ➡️  {uplift.get('projected_hook_retention')} [{uplift.get('hook_retention_uplift')}]")
        print(f"     • Completion Rate:     {uplift.get('baseline_completion_rate')} ➡️  {uplift.get('projected_completion_rate')} [{uplift.get('completion_rate_uplift')}]")
        print(f"     • Share Rate:          {uplift.get('baseline_share_rate')} ➡️  {uplift.get('projected_share_rate')} [{uplift.get('share_rate_uplift')}]")
        print(f"     • Organic Multiplier:  {uplift.get('estimated_reach_multiplier')}")
        print(f"     • Discovery Tier:      {uplift.get('projected_distribution_tier')}")
        print("  " + "─" * 66)
        print("  🎣 3 HIGH-RETENTION PATTERN-INTERRUPT HOOK REWRITES:")
        for h in hooks:
            print(f"     [{h.get('variant_id')}] {h.get('hook_style')} ({h.get('expected_retention')} Est. Retention)")
            print(f"         👁️ Action:   {h.get('visual_action')}")
            print(f"         🗣️ Voiceover: \"{h.get('spoken_script')}\"")
            print(f"         🔤 Overlay:   {h.get('on_screen_text')}")
            print(f"         🔊 SFX Cue:   {h.get('audio_sfx_cue')}")
            print()
        print("  " + "─" * 66)
        print("  ✂️ SCENE RE-EDIT CUT BLUEPRINT:")
        for i, c in enumerate(cuts[:3], 1):
            print(f"     {i}. [{c.get('timestamp_range')}] {c.get('action_type')}: {c.get('instruction')}")
        print("  " + "─" * 66)
        print("  📱 RECOMMENDED PUBLISHING KIT (INSTAGRAM REELS):")
        print(f"     • Cover Title:    {reels.get('cover_headline')}")
        print(f"     • Best Window:    {reels.get('best_posting_window')}")
        print(f"     • Top Hashtags:   {' '.join(reels.get('hashtags', [])[:6])}")
        print("═" * 70)
