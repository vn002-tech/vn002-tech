#!/usr/bin/env python3
"""
update_readme.py
Programmatic generator for vn002-tech GitHub Profile README,
Studio Porcelain Ivory & Prussian Navy / Warm Champagne Gold Architecture & SVGs.
Editorial, Swiss-minimalist, human-crafted design completely free from generic AI black/neon tropes.
"""

from pathlib import Path
import time

CACHE_KEY = int(time.time())


def generate_svg_banner() -> str:
    """
    Generates an editorial Studio Porcelain Ivory & Prussian Navy executive card SVG banner
    with a bespoke Amber Gold & Glacier Blue neural lattice on the left side.
    """
    return """<svg width="1200" height="310" viewBox="0 0 1200 310" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Background Gradient: Crisp Studio Porcelain Ivory -->
    <linearGradient id="ivory-bg" x1="0" y1="0" x2="1200" y2="310" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#FAF9F5"/>
      <stop offset="40%" stop-color="#F4F1EA"/>
      <stop offset="80%" stop-color="#EBE7DE"/>
      <stop offset="100%" stop-color="#F5F3EC"/>
    </linearGradient>

    <!-- Diagonal Geometric Layer Gradients: Deep Prussian Navy & Champagne Gold -->
    <linearGradient id="ribbon-navy-1" x1="0" y1="0" x2="600" y2="310" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#0F172A" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#1E293B" stop-opacity="0.9"/>
    </linearGradient>

    <linearGradient id="ribbon-gold-light" x1="280" y1="0" x2="520" y2="310" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#F59E0B"/>
      <stop offset="40%" stop-color="#D97706"/>
      <stop offset="80%" stop-color="#B45309"/>
      <stop offset="100%" stop-color="#78350F"/>
    </linearGradient>

    <linearGradient id="ribbon-glacier-accent" x1="150" y1="0" x2="450" y2="310" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#0284C7" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="#0369A1" stop-opacity="0.2"/>
    </linearGradient>

    <linearGradient id="ribbon-linen-right" x1="750" y1="0" x2="1200" y2="310" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#E2DDD2" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#D5CFC2" stop-opacity="0.8"/>
    </linearGradient>

    <filter id="card-soft-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="12" stdDeviation="16" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>

    <filter id="ribbon-shadow-light" x="-30%" y="-30%" width="160%" height="160%">
      <feDropShadow dx="-4" dy="8" stdDeviation="6" flood-color="#0F172A" flood-opacity="0.2"/>
    </filter>

    <filter id="gold-pulse-glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <style>
    .font-title { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    .font-mono { font-family: 'JetBrains Mono', 'Fira Code', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; }

    @keyframes pulse-gold {
      0%, 100% { transform: scale(1); opacity: 0.9; }
      50% { transform: scale(1.18); opacity: 1; filter: drop-shadow(0 0 8px #D97706); }
    }

    @keyframes flow-navy-data {
      0% { stroke-dashoffset: 24; }
      100% { stroke-dashoffset: 0; }
    }

    @keyframes orbit-navy {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }

    @keyframes radar-ping-navy {
      0% { r: 3.5px; opacity: 1; }
      75%, 100% { r: 8px; opacity: 0; }
    }

    .anim-gold-core {
      transform-origin: 180px 155px;
      animation: pulse-gold 2.8s ease-in-out infinite;
    }

    .anim-navy-flow {
      stroke-dasharray: 5 4;
      animation: flow-navy-data 1.3s linear infinite;
    }

    .anim-navy-orbit {
      transform-origin: 180px 155px;
      animation: orbit-navy 14s linear infinite;
    }

    .anim-radar {
      animation: radar-ping-navy 2s cubic-bezier(0, 0, 0.2, 1) infinite;
    }
  </style>

  <!-- Container Base Box: Warm Ivory Porcelain with Slate Border & Soft Ambient Shadow -->
  <rect x="2" y="2" width="1196" height="306" rx="16" fill="url(#ivory-bg)" stroke="#D1C7B7" stroke-width="1.5" filter="url(#card-soft-shadow)"/>

  <!-- ================= LUXURY GEOMETRIC LAYERED RIBBONS (STUDIO EDITORIAL) ================= -->
  <!-- Layer 1: Navy Background Angled Band -->
  <polygon points="240,0 370,0 100,310 0,310 0,260 210,0" fill="url(#ribbon-navy-1)"/>

  <!-- Layer 2: Primary Champagne Gold Cross Band (With Deep Soft Shadow) -->
  <polygon points="430,0 535,0 230,310 125,310" fill="url(#ribbon-gold-light)" filter="url(#ribbon-shadow-light)"/>
  <!-- Highlight Edge Line -->
  <line x1="430" y1="0" x2="125" y2="310" stroke="#FEF3C7" stroke-width="1.2" opacity="0.9"/>
  <line x1="535" y1="0" x2="230" y2="310" stroke="#FDE68A" stroke-width="0.8" opacity="0.5"/>

  <!-- Layer 3: Thin Glacier Accent Ribbon -->
  <polygon points="80,0 125,0 355,310 310,310" fill="url(#ribbon-glacier-accent)"/>

  <!-- Layer 4: Right Wing Linen Facet -->
  <polygon points="840,0 1200,0 1200,240 960,310 800,310" fill="url(#ribbon-linen-right)"/>
  <line x1="840" y1="0" x2="1200" y2="240" stroke="#B8AFA0" stroke-width="1" opacity="0.6"/>

  <!-- ================= LEFT: BESPOKE STUDIO IVORY & PRUSSIAN NAVY NEURAL MESH ================= -->
  <g id="neural-lattice">
    <!-- Synapses (Input -> Hidden 1) -->
    <line x1="45" y1="95" x2="105" y2="75" stroke="#94A3B8" stroke-width="1.5" class="anim-navy-flow"/>
    <line x1="45" y1="95" x2="105" y2="125" stroke="#CBD5E1" stroke-width="1.2"/>
    <line x1="30" y1="155" x2="105" y2="125" stroke="#F59E0B" stroke-width="2" class="anim-navy-flow"/>
    <line x1="30" y1="155" x2="105" y2="185" stroke="#F59E0B" stroke-width="2" class="anim-navy-flow"/>
    <line x1="45" y1="215" x2="105" y2="185" stroke="#CBD5E1" stroke-width="1.2"/>
    <line x1="45" y1="215" x2="105" y2="235" stroke="#94A3B8" stroke-width="1.5" class="anim-navy-flow"/>

    <!-- Synapses (Hidden 1 -> Central Core) -->
    <line x1="105" y1="75" x2="180" y2="155" stroke="#0284C7" stroke-width="1.8" opacity="0.9" class="anim-navy-flow"/>
    <line x1="105" y1="125" x2="180" y2="155" stroke="#D97706" stroke-width="2.4" class="anim-navy-flow" filter="url(#gold-pulse-glow)"/>
    <line x1="105" y1="185" x2="180" y2="155" stroke="#D97706" stroke-width="2.4" class="anim-navy-flow" filter="url(#gold-pulse-glow)"/>
    <line x1="105" y1="235" x2="180" y2="155" stroke="#0284C7" stroke-width="1.8" opacity="0.9" class="anim-navy-flow"/>

    <!-- Synapses (Core -> Hidden 2) -->
    <line x1="180" y1="155" x2="255" y2="85" stroke="#0284C7" stroke-width="1.8" opacity="0.9" class="anim-navy-flow"/>
    <line x1="180" y1="155" x2="255" y2="155" stroke="#D97706" stroke-width="2.6" class="anim-navy-flow" filter="url(#gold-pulse-glow)"/>
    <line x1="180" y1="155" x2="255" y2="225" stroke="#0284C7" stroke-width="1.8" opacity="0.9" class="anim-navy-flow"/>

    <!-- Synapses (Hidden 2 -> Output) -->
    <line x1="255" y1="85" x2="315" y2="115" stroke="#94A3B8" stroke-width="1.5" class="anim-navy-flow"/>
    <line x1="255" y1="155" x2="315" y2="115" stroke="#F59E0B" stroke-width="1.5"/>
    <line x1="255" y1="155" x2="315" y2="195" stroke="#F59E0B" stroke-width="1.5"/>
    <line x1="255" y1="225" x2="315" y2="195" stroke="#94A3B8" stroke-width="1.5" class="anim-navy-flow"/>

    <!-- Diagonal Braces -->
    <line x1="105" y1="75" x2="105" y2="125" stroke="#475569" stroke-width="1" opacity="0.4"/>
    <line x1="105" y1="125" x2="105" y2="185" stroke="#475569" stroke-width="1" opacity="0.4"/>
    <line x1="105" y1="185" x2="105" y2="235" stroke="#475569" stroke-width="1" opacity="0.4"/>
    <line x1="255" y1="85" x2="255" y2="155" stroke="#475569" stroke-width="1" opacity="0.4"/>
    <line x1="255" y1="155" x2="255" y2="225" stroke="#475569" stroke-width="1" opacity="0.4"/>

    <!-- Tier 1 Nodes -->
    <circle cx="45" cy="95" r="5" fill="#F8FAFC" stroke="#0F172A" stroke-width="2.2"/>
    <circle cx="30" cy="155" r="6" fill="#FEF3C7" stroke="#D97706" stroke-width="2.4"/>
    <circle cx="45" cy="215" r="5" fill="#F8FAFC" stroke="#0F172A" stroke-width="2.2"/>

    <!-- Tier 2 Nodes -->
    <circle cx="105" cy="75" r="5.5" fill="#E0F2FE" stroke="#0284C7" stroke-width="2.2"/>
    <circle cx="105" cy="125" r="6.5" fill="#FEF3C7" stroke="#D97706" stroke-width="2.6"/>
    <circle cx="105" cy="185" r="6.5" fill="#FEF3C7" stroke="#D97706" stroke-width="2.6"/>
    <circle cx="105" cy="235" r="5.5" fill="#E0F2FE" stroke="#0284C7" stroke-width="2.2"/>

    <!-- Central Quantum Core -->
    <g class="anim-navy-orbit">
      <circle cx="180" cy="155" r="26" fill="none" stroke="#D97706" stroke-width="1.4" stroke-dasharray="5 7" opacity="0.85"/>
      <circle cx="180" cy="129" r="3.5" fill="#F59E0B"/>
      <circle cx="180" cy="181" r="3.5" fill="#0284C7"/>
    </g>
    <circle cx="180" cy="155" r="14" fill="#FEF3C7" stroke="#D97706" stroke-width="3" class="anim-gold-core"/>
    <circle cx="180" cy="155" r="5" fill="#0F172A"/>

    <!-- Tier 3 Nodes -->
    <circle cx="255" cy="85" r="5.5" fill="#E0F2FE" stroke="#0284C7" stroke-width="2.2"/>
    <circle cx="255" cy="155" r="7" fill="#FEF3C7" stroke="#D97706" stroke-width="2.6"/>
    <circle cx="255" cy="225" r="5.5" fill="#E0F2FE" stroke="#0284C7" stroke-width="2.2"/>

    <!-- Tier 4 Output Nodes -->
    <circle cx="315" cy="115" r="5.5" fill="#F8FAFC" stroke="#0F172A" stroke-width="2.2"/>
    <circle cx="315" cy="195" r="5.5" fill="#F8FAFC" stroke="#0F172A" stroke-width="2.2"/>
  </g>

  <!-- Vertical Divider -->
  <line x1="360" y1="30" x2="360" y2="280" stroke="#D1C7B7" stroke-width="1.5"/>

  <!-- ================= RIGHT: IDENTITY & EXECUTIVE CARD CONTENT ================= -->
  <!-- Top Status Badge with Radar Ping -->
  <rect x="390" y="32" width="265" height="26" rx="13" fill="#F1EBE1" stroke="#C4B7A4" stroke-width="1.2"/>
  <circle cx="407" cy="45" r="3.5" fill="#0284C7"/>
  <circle cx="407" cy="45" r="3.5" fill="#38BDF8" class="anim-radar"/>
  <text x="421" y="49" fill="#0F172A" class="font-mono" font-size="10.5" font-weight="700" letter-spacing="1.2">AI ENGINEERING &amp; DATA SCIENCE</text>

  <!-- Name & Identifier -->
  <text x="390" y="104" fill="#0F172A" class="font-title" font-size="42" font-weight="800" letter-spacing="2">VAN</text>
  <rect x="505" y="80" width="112" height="28" rx="7" fill="#0F172A" stroke="#0F172A" stroke-width="1.2"/>
  <text x="561" y="98" fill="#FDE68A" class="font-mono" font-size="12.5" font-weight="700" text-anchor="middle">vn002-tech</text>

  <!-- Primary Role -->
  <text x="390" y="138" fill="#1E293B" class="font-title" font-size="18.5" font-weight="700" letter-spacing="1.5">AI ENGINEER</text>
  <text x="390" y="162" fill="#475569" class="font-title" font-size="13.5" font-weight="500">AI Engineering · Machine Learning &amp; Data Science · LLMs &amp; Automation</text>

  <!-- Tech Stack Pills (Crisp Studio Linen & Navy) -->
  <g transform="translate(390, 184)">
    <rect x="0" y="0" width="72" height="25" rx="6" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.2"/>
    <text x="36" y="17" fill="#0F172A" class="font-mono" font-size="11" font-weight="600" text-anchor="middle">Python</text>

    <rect x="80" y="0" width="80" height="25" rx="6" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.2"/>
    <text x="120" y="17" fill="#0F172A" class="font-mono" font-size="11" font-weight="600" text-anchor="middle">PyTorch</text>

    <rect x="168" y="0" width="102" height="25" rx="6" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.2"/>
    <text x="219" y="17" fill="#0F172A" class="font-mono" font-size="11" font-weight="600" text-anchor="middle">Scikit-learn</text>

    <rect x="278" y="0" width="76" height="25" rx="6" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.2"/>
    <text x="316" y="17" fill="#0F172A" class="font-mono" font-size="11" font-weight="600" text-anchor="middle">FastAPI</text>

    <rect x="362" y="0" width="96" height="25" rx="6" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.2"/>
    <text x="410" y="17" fill="#0F172A" class="font-mono" font-size="11" font-weight="600" text-anchor="middle">PostgreSQL</text>

    <rect x="466" y="0" width="72" height="25" rx="6" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.2"/>
    <text x="502" y="17" fill="#0F172A" class="font-mono" font-size="11" font-weight="600" text-anchor="middle">Docker</text>
  </g>

  <!-- Horizontal Divider -->
  <line x1="390" y1="226" x2="1150" y2="226" stroke="#D1C7B7" stroke-width="1"/>

  <!-- Social & Contact Badges -->
  <g transform="translate(390, 240)">
    <rect x="0" y="0" width="170" height="34" rx="7" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.2"/>
    <path d="M18 17C18 12.58 21.58 9 26 9C30.42 9 34 12.58 34 17C34 20.54 31.7 23.54 28.52 24.6C28.12 24.67 27.97 24.43 27.97 24.21C27.97 24.02 27.98 23.36 27.98 22.56C25.75 23.05 25.28 21.61 25.28 21.61C24.92 20.69 24.39 20.45 24.39 20.45C23.66 19.95 24.45 19.96 24.45 19.96C25.26 20.02 25.68 20.79 25.68 20.79C26.4 22.02 27.56 21.67 28.02 21.46C28.09 20.94 28.3 20.58 28.53 20.38C26.75 20.18 24.88 19.49 24.88 16.42C24.88 15.55 25.19 14.83 25.7 14.27C25.62 14.07 25.35 13.25 25.78 12.16C25.78 12.16 26.45 11.95 27.97 12.98C28.61 12.8 29.29 12.71 29.97 12.71C30.65 12.71 31.33 12.8 31.97 12.98C33.49 11.95 34.16 12.16 34.16 12.16C34.59 13.25 34.32 14.07 34.24 14.27C34.75 14.83 35.06 15.55 35.06 16.42C35.06 19.5 33.18 20.18 31.4 20.37C31.69 20.62 31.95 21.11 31.95 21.87C31.95 22.96 31.94 23.84 31.94 24.21C31.94 24.43 31.79 24.68 31.38 24.6C28.2 23.53 25.9 20.53 25.9 17H18Z" fill="#0F172A" transform="translate(-8, -3) scale(0.85)"/>
    <text x="40" y="21" fill="#0F172A" class="font-mono" font-size="12" font-weight="600">vn002-tech</text>

    <rect x="180" y="0" width="130" height="34" rx="7" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.2"/>
    <rect x="194" y="9" width="16" height="16" rx="3.5" fill="#0A66C2"/>
    <text x="202" y="21" fill="#FFFFFF" class="font-title" font-size="10" font-weight="800" text-anchor="middle">in</text>
    <text x="218" y="21" fill="#0F172A" class="font-title" font-size="12" font-weight="600">LinkedIn</text>

    <rect x="320" y="0" width="255" height="34" rx="7" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.2"/>
    <path d="M335 11H349C350.1 11 351 11.9 351 13V21C351 22.1 350.1 23 349 23H335C333.9 23 333 22.1 333 21V13C333 11.9 333.9 11 335 11Z" stroke="#D97706" stroke-width="1.3" fill="none"/>
    <path d="M333 13L342 18L351 13" stroke="#D97706" stroke-width="1.3" fill="none"/>
    <text x="360" y="21" fill="#0F172A" class="font-mono" font-size="11.5" font-weight="500">wahidivansaputra@gmail.com</text>
  </g>
</svg>"""


def generate_pillars_svg() -> str:
    """
    Generates an editorial 4-Card Vector Matrix SVG in Studio Ivory Porcelain with Mineral accents:
    Glacier Steel | Champagne Amber | Deep Sage Emerald | Terracotta Rust.
    """
    return """<svg width="1000" height="148" viewBox="0 0 1000 148" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Studio Ivory Card Background Gradient -->
    <linearGradient id="pil-white-card" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="#F8FAFC"/>
    </linearGradient>

    <filter id="card-soft-subtle" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#0F172A" flood-opacity="0.05"/>
    </filter>
  </defs>

  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    .font-mono { font-family: 'JetBrains Mono', 'Fira Code', ui-monospace, SFMono-Regular, Menlo, monospace; }

    @keyframes pulse-dot-light {
      0%, 100% { opacity: 0.4; transform: scale(0.9); }
      50% { opacity: 1; transform: scale(1.2); }
    }

    @keyframes radar-ring-light {
      0% { r: 3.5px; opacity: 1; }
      100% { r: 9px; opacity: 0; }
    }

    .anim-pulse {
      animation: pulse-dot-light 2.2s ease-in-out infinite;
    }

    .anim-radar {
      animation: radar-ring-light 1.8s cubic-bezier(0, 0, 0.2, 1) infinite;
    }
  </style>

  <!-- Frame Background: Studio Porcelain Ivory -->
  <rect x="2" y="2" width="996" height="144" rx="14" fill="#FAF9F5" stroke="#D1C7B7" stroke-width="1.5"/>

  <!-- ================= CARD 1: ML & DATA SCIENCE (GLACIER STEEL) ================= -->
  <g transform="translate(16, 14)">
    <rect width="230" height="120" rx="10" fill="url(#pil-white-card)" stroke="#0284C7" stroke-width="1.4" filter="url(#card-soft-subtle)"/>
    <circle cx="18" cy="20" r="4" fill="#0284C7" class="anim-pulse"/>
    <text x="28" y="24" fill="#0284C7" class="font-mono" font-size="10.5" font-weight="700" letter-spacing="0.8">ML &amp; DATA SCIENCE</text>
    <text x="16" y="49" fill="#0F172A" class="font-sans" font-size="13" font-weight="700">Predictive &amp; Analytics</text>
    <text x="16" y="73" fill="#475569" class="font-sans" font-size="11">Feature Pipelines · XGBoost</text>
    <text x="16" y="93" fill="#64748B" class="font-sans" font-size="10.5">Statistical EDA &amp; Metrics</text>
  </g>

  <!-- ================= CARD 2: DEEP LEARNING (CHAMPAGNE AMBER) ================= -->
  <g transform="translate(260, 14)">
    <rect width="230" height="120" rx="10" fill="url(#pil-white-card)" stroke="#D97706" stroke-width="1.4" filter="url(#card-soft-subtle)"/>
    <circle cx="18" cy="20" r="4" fill="#D97706" class="anim-pulse"/>
    <text x="28" y="24" fill="#B45309" class="font-mono" font-size="10.5" font-weight="700" letter-spacing="0.8">DEEP LEARNING</text>
    <text x="16" y="49" fill="#0F172A" class="font-sans" font-size="13" font-weight="700">Neural Systems</text>
    <text x="16" y="73" fill="#475569" class="font-sans" font-size="11">PyTorch · Tensors</text>
    <text x="16" y="93" fill="#64748B" class="font-sans" font-size="10.5">Dense Embeddings</text>
  </g>

  <!-- ================= CARD 3: LLMs & AUTOMATION (SAGE EMERALD FOCAL) ================= -->
  <g transform="translate(504, 14)">
    <rect width="230" height="120" rx="10" fill="url(#pil-white-card)" stroke="#059669" stroke-width="1.6" filter="url(#card-soft-subtle)"/>
    <circle cx="18" cy="20" r="4" fill="#059669"/>
    <circle cx="18" cy="20" r="4" fill="#10B981" class="anim-radar"/>
    <text x="28" y="24" fill="#047857" class="font-mono" font-size="10.5" font-weight="700" letter-spacing="0.8">LLMs &amp; AUTOMATION</text>
    <text x="16" y="49" fill="#0F172A" class="font-sans" font-size="13" font-weight="700">AI Automation</text>
    <text x="16" y="73" fill="#047857" class="font-sans" font-size="11">RAG Pipelines · Vector DBs</text>
    <text x="16" y="93" fill="#065F46" class="font-sans" font-size="10.5">Autonomous Workflows</text>
  </g>

  <!-- ================= CARD 4: MLOPS & SYSTEMS (TERRACOTTA RUST) ================= -->
  <g transform="translate(748, 14)">
    <rect width="236" height="120" rx="10" fill="url(#pil-white-card)" stroke="#EA580C" stroke-width="1.4" filter="url(#card-soft-subtle)"/>
    <circle cx="18" cy="20" r="4" fill="#EA580C" class="anim-pulse"/>
    <text x="28" y="24" fill="#C2410C" class="font-mono" font-size="10.5" font-weight="700" letter-spacing="0.8">MLOps &amp; SYSTEMS</text>
    <text x="16" y="49" fill="#0F172A" class="font-sans" font-size="13" font-weight="700">Serving &amp; Production</text>
    <text x="16" y="73" fill="#475569" class="font-sans" font-size="11">FastAPI · Docker Runtime</text>
    <text x="16" y="93" fill="#64748B" class="font-sans" font-size="10.5">ETL &amp; Data Integrity</text>
  </g>
</svg>"""


def generate_pipeline_svg() -> str:
    """
    Generates a Multi-Tier AI Architecture SVG Diagram in Studio Porcelain Ivory & Prussian Navy.
    """
    return """<svg width="1000" height="420" viewBox="0 0 1000 420" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Background Gradient -->
    <linearGradient id="pipe-ivory-bg" x1="0" y1="0" x2="1000" y2="420" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#FAF9F5"/>
      <stop offset="50%" stop-color="#F4F1EA"/>
      <stop offset="100%" stop-color="#EBE7DE"/>
    </linearGradient>

    <!-- Card Background Gradient: Pure Studio White with Soft Border -->
    <linearGradient id="pipe-white-card" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="#F8FAFC"/>
    </linearGradient>

    <filter id="pipe-shadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#0F172A" flood-opacity="0.06"/>
    </filter>
  </defs>

  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    .font-mono { font-family: 'JetBrains Mono', 'Fira Code', ui-monospace, SFMono-Regular, Menlo, monospace; }

    @keyframes flow-fwd-light {
      0% { stroke-dashoffset: 24; }
      100% { stroke-dashoffset: 0; }
    }

    @keyframes pulse-dot-light {
      0%, 100% { opacity: 0.4; transform: scale(0.9); }
      50% { opacity: 1; transform: scale(1.2); }
    }

    @keyframes radar-ring-light {
      0% { r: 4px; opacity: 1; }
      100% { r: 11px; opacity: 0; }
    }

    .anim-flow-fwd {
      stroke-dasharray: 6 4;
      animation: flow-fwd-light 1.4s linear infinite;
    }

    .anim-pulse {
      animation: pulse-dot-light 2.2s ease-in-out infinite;
    }

    .anim-radar-sage {
      animation: radar-ring-light 1.8s cubic-bezier(0, 0, 0.2, 1) infinite;
    }
  </style>

  <!-- Container Frame -->
  <rect x="2" y="2" width="996" height="416" rx="16" fill="url(#pipe-ivory-bg)" stroke="#D1C7B7" stroke-width="1.5"/>

  <!-- ================= SECTION LABELS ================= -->
  <text x="35" y="32" fill="#64748B" class="font-mono" font-size="10.5" font-weight="700" letter-spacing="1.5">TIER 1: DATA &amp; FEATURE FOUNDATION</text>
  <text x="35" y="160" fill="#0284C7" class="font-mono" font-size="10.5" font-weight="700" letter-spacing="1.5">TIER 2: INTELLIGENCE &amp; MODELING BRANCHES (ML &amp; DATA SCIENCE · DL · LLM)</text>
  <text x="35" y="300" fill="#D97706" class="font-mono" font-size="10.5" font-weight="700" letter-spacing="1.5">TIER 3: SERVING, AGENTS &amp; AI AUTOMATION</text>

  <!-- ================= TIER 1: DATA FOUNDATION ================= -->
  <!-- 01. Ingestion -->
  <g transform="translate(35, 45)">
    <rect width="430" height="75" rx="10" fill="url(#pipe-white-card)" stroke="#CBD5E1" stroke-width="1.2" filter="url(#pipe-shadow)"/>
    <circle cx="22" cy="22" r="4" fill="#0284C7" class="anim-pulse"/>
    <text x="36" y="26" fill="#0284C7" class="font-mono" font-size="11" font-weight="700">01. DATA INGESTION &amp; VALIDATION</text>
    <text x="22" y="47" fill="#0F172A" class="font-sans" font-size="13" font-weight="600">ETL Pipelines &amp; Schema Integrity</text>
    <text x="22" y="65" fill="#64748B" class="font-sans" font-size="11">PostgreSQL · Automated Data Cleaning · Assertions</text>
  </g>

  <!-- Flow Line Tier 1 (1 to 2) -->
  <line x1="465" y1="82" x2="535" y2="82" stroke="#D97706" stroke-width="2" class="anim-flow-fwd"/>
  <polygon points="535,82 527,78 527,86" fill="#D97706"/>

  <!-- 02. Feature & Embedding Matrix -->
  <g transform="translate(535, 45)">
    <rect width="430" height="75" rx="10" fill="url(#pipe-white-card)" stroke="#D97706" stroke-width="1.2" filter="url(#pipe-shadow)"/>
    <circle cx="22" cy="22" r="4" fill="#D97706" class="anim-pulse"/>
    <text x="36" y="26" fill="#B45309" class="font-mono" font-size="11" font-weight="700">02. FEATURE &amp; EMBEDDING PIPELINE</text>
    <text x="22" y="47" fill="#0F172A" class="font-sans" font-size="13" font-weight="600">Encoders, Scaling &amp; Vectorization</text>
    <text x="22" y="65" fill="#64748B" class="font-sans" font-size="11">Scikit-learn · Pandas · Dense Representations</text>
  </g>

  <!-- Connectors from Tier 1 (02) down to Tier 2 (3 branches) -->
  <path d="M750 120 V145 H175 V175" stroke="#94A3B8" stroke-width="1.5" class="anim-flow-fwd"/>
  <path d="M750 120 V175" stroke="#0284C7" stroke-width="1.8" class="anim-flow-fwd"/>
  <path d="M750 120 V145 H825 V175" stroke="#059669" stroke-width="2" class="anim-flow-fwd"/>

  <!-- ================= TIER 2: 3 CORE INTELLIGENCE BRANCHES ================= -->

  <!-- Branch A: ML & Data Science -->
  <g transform="translate(35, 175)">
    <rect width="280" height="85" rx="10" fill="url(#pipe-white-card)" stroke="#0284C7" stroke-width="1.2" filter="url(#pipe-shadow)"/>
    <circle cx="20" cy="22" r="4" fill="#0284C7" class="anim-pulse"/>
    <text x="32" y="26" fill="#0284C7" class="font-mono" font-size="10.5" font-weight="700">03A. ML &amp; DATA SCIENCE</text>
    <text x="20" y="49" fill="#0F172A" class="font-sans" font-size="12.5" font-weight="600">Statistical Modeling &amp; Prediction</text>
    <text x="20" y="68" fill="#64748B" class="font-sans" font-size="10.5">XGBoost · Scikit-learn · EDA &amp; Analysis</text>
  </g>

  <!-- Branch B: Deep Learning -->
  <g transform="translate(360, 175)">
    <rect width="280" height="85" rx="10" fill="url(#pipe-white-card)" stroke="#D97706" stroke-width="1.2" filter="url(#pipe-shadow)"/>
    <circle cx="20" cy="22" r="4" fill="#D97706" class="anim-pulse"/>
    <text x="32" y="26" fill="#B45309" class="font-mono" font-size="10.5" font-weight="700">03B. DEEP LEARNING</text>
    <text x="20" y="49" fill="#0F172A" class="font-sans" font-size="12.5" font-weight="600">Neural &amp; Dense Networks</text>
    <text x="20" y="68" fill="#64748B" class="font-sans" font-size="10.5">PyTorch · Tensors · Embeddings</text>
  </g>

  <!-- Branch C: LLM & AI Automation (FOCAL POINT) -->
  <g transform="translate(685, 175)">
    <rect width="280" height="85" rx="10" fill="url(#pipe-white-card)" stroke="#059669" stroke-width="1.5" filter="url(#pipe-shadow)"/>
    <circle cx="20" cy="22" r="4" fill="#059669"/>
    <circle cx="20" cy="22" r="4" fill="#10B981" class="anim-radar-sage"/>
    <text x="32" y="26" fill="#047857" class="font-mono" font-size="10.5" font-weight="700">03C. LLMs &amp; AUTOMATION</text>
    <text x="20" y="49" fill="#0F172A" class="font-sans" font-size="12.5" font-weight="700">RAG &amp; Autonomous Agents</text>
    <text x="20" y="68" fill="#065F46" class="font-sans" font-size="10.5">Vector Search · Tool Use · Chains</text>
  </g>

  <!-- Connectors from Tier 2 down to Tier 3 -->
  <path d="M175 260 V285 H330 V315" stroke="#94A3B8" stroke-width="1.5" class="anim-flow-fwd"/>
  <path d="M500 260 V315" stroke="#D97706" stroke-width="1.8" class="anim-flow-fwd"/>
  <path d="M825 260 V285 H670 V315" stroke="#059669" stroke-width="2" class="anim-flow-fwd"/>

  <!-- ================= TIER 3: SERVING, AGENTS & AUTOMATION ================= -->

  <!-- 04. Evaluation & Metrics -->
  <g transform="translate(35, 315)">
    <rect width="280" height="85" rx="10" fill="url(#pipe-white-card)" stroke="#64748B" stroke-width="1.2" filter="url(#pipe-shadow)"/>
    <circle cx="20" cy="22" r="4" fill="#475569" class="anim-pulse"/>
    <text x="32" y="26" fill="#334155" class="font-mono" font-size="10.5" font-weight="700">04. EVALUATION &amp; METRICS</text>
    <text x="20" y="49" fill="#0F172A" class="font-sans" font-size="12.5" font-weight="600">Empirical Validation</text>
    <text x="20" y="68" fill="#64748B" class="font-sans" font-size="10.5">ROC-AUC · Recall · Benchmark Cost</text>
  </g>

  <!-- 05. FastAPI Serving -->
  <g transform="translate(360, 315)">
    <rect width="280" height="85" rx="10" fill="url(#pipe-white-card)" stroke="#EA580C" stroke-width="1.2" filter="url(#pipe-shadow)"/>
    <circle cx="20" cy="22" r="4" fill="#EA580C" class="anim-pulse"/>
    <text x="32" y="26" fill="#C2410C" class="font-mono" font-size="10.5" font-weight="700">05. FASTAPI SERVING</text>
    <text x="20" y="49" fill="#0F172A" class="font-sans" font-size="12.5" font-weight="600">Async Inference Endpoints</text>
    <text x="20" y="68" fill="#64748B" class="font-sans" font-size="10.5">REST APIs · Docker Containerization</text>
  </g>

  <!-- 06. Autonomous AI Applications & UI -->
  <g transform="translate(685, 315)">
    <rect width="280" height="85" rx="10" fill="url(#pipe-white-card)" stroke="#D97706" stroke-width="1.2" filter="url(#pipe-shadow)"/>
    <circle cx="20" cy="22" r="4" fill="#D97706" class="anim-pulse"/>
    <text x="32" y="26" fill="#B45309" class="font-mono" font-size="10.5" font-weight="700">06. AI APPS &amp; AUTOMATION</text>
    <text x="20" y="49" fill="#0F172A" class="font-sans" font-size="12.5" font-weight="600">Client UI &amp; Workflows</text>
    <text x="20" y="68" fill="#64748B" class="font-sans" font-size="10.5">Streamlit · Real-Time Trigger Agents</text>
  </g>
</svg>"""


def generate_telemetry_track_svg() -> str:
    """
    Generates an editorial Cyber Speedway Track SVG in Studio Porcelain Ivory, Glacier Blue, and Warm Amber.
    """
    return """<svg width="1000" height="220" viewBox="0 0 1000 220" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Background Gradient -->
    <linearGradient id="track-ivory-bg" x1="0" y1="0" x2="1000" y2="220" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#FAF9F5"/>
      <stop offset="50%" stop-color="#F4F1EA"/>
      <stop offset="100%" stop-color="#EBE7DE"/>
    </linearGradient>

    <!-- Area Gradient under Track: Soft Warm Amber -->
    <linearGradient id="track-gold-area" x1="0" y1="60" x2="0" y2="200" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#F59E0B" stop-opacity="0.2"/>
      <stop offset="60%" stop-color="#0284C7" stop-opacity="0.06"/>
      <stop offset="100%" stop-color="#FAF9F5" stop-opacity="0"/>
    </linearGradient>

    <!-- Track Stroke Gradient (Glacier Blue -> Emerald -> Amber -> Rust) -->
    <linearGradient id="track-ivory-line" x1="0" y1="0" x2="1000" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#0284C7"/>
      <stop offset="35%" stop-color="#059669"/>
      <stop offset="70%" stop-color="#D97706"/>
      <stop offset="100%" stop-color="#EA580C"/>
    </linearGradient>
  </defs>

  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
    .font-mono { font-family: 'JetBrains Mono', 'Fira Code', monospace; }

    @keyframes pulse-node-light {
      0%, 100% { r: 3.5px; opacity: 0.6; }
      50% { r: 6px; opacity: 1; }
    }

    @keyframes grid-glow-light {
      0%, 100% { opacity: 0.4; }
      50% { opacity: 0.7; }
    }

    .anim-node { animation: pulse-node-light 2.2s ease-in-out infinite; }
    .anim-grid { animation: grid-glow-light 3s ease-in-out infinite; }
  </style>

  <!-- Frame -->
  <rect x="2" y="2" width="996" height="216" rx="14" fill="url(#track-ivory-bg)" stroke="#D1C7B7" stroke-width="1.5"/>

  <!-- Background Telemetry Grid Lines -->
  <g class="anim-grid" stroke="#CBD5E1" stroke-width="0.8" stroke-dasharray="3 6" opacity="0.6">
    <line x1="50" y1="50" x2="950" y2="50"/>
    <line x1="50" y1="90" x2="950" y2="90"/>
    <line x1="50" y1="130" x2="950" y2="130"/>
    <line x1="50" y1="170" x2="950" y2="170"/>
    <line x1="200" y1="40" x2="200" y2="190"/>
    <line x1="400" y1="40" x2="400" y2="190"/>
    <line x1="600" y1="40" x2="600" y2="190"/>
    <line x1="800" y1="40" x2="800" y2="190"/>
  </g>

  <!-- HUD Header -->
  <text x="40" y="32" fill="#0284C7" class="font-mono" font-size="11" font-weight="700" letter-spacing="1.5">TELEMETRY CIRCUIT // INFERENCE ACCELERATION TRACK</text>
  <text x="960" y="32" fill="#D97706" class="font-mono" font-size="10" font-weight="600" text-anchor="end">SYSTEM STATUS: HIGH VELOCITY</text>

  <!-- Filled Area Under Graph Track -->
  <path d="M 40 160 C 160 160, 240 70, 360 70 C 480 70, 540 180, 660 180 C 760 180, 830 50, 940 50 L 940 200 L 40 200 Z" fill="url(#track-gold-area)"/>

  <!-- Track Outline Base -->
  <path id="race-track" d="M 40 160 C 160 160, 240 70, 360 70 C 480 70, 540 180, 660 180 C 760 180, 830 50, 940 50" fill="none" stroke="url(#track-ivory-line)" stroke-width="4.5" stroke-linecap="round"/>

  <!-- Track Center Dashed Guideline -->
  <path d="M 40 160 C 160 160, 240 70, 360 70 C 480 70, 540 180, 660 180 C 760 180, 830 50, 940 50" fill="none" stroke="#FFFFFF" stroke-width="1.4" stroke-dasharray="6 8" opacity="0.9"/>

  <!-- Checkpoint Telemetry Nodes along Graph -->
  <!-- Checkpoint 1 -->
  <g transform="translate(200, 115)">
    <circle cx="0" cy="0" r="5" fill="#FFFFFF" stroke="#0284C7" stroke-width="2.2" class="anim-node"/>
    <rect x="-40" y="12" width="80" height="18" rx="4" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
    <text x="0" y="24" fill="#0284C7" class="font-mono" font-size="9" font-weight="700" text-anchor="middle">01. INGEST</text>
  </g>

  <!-- Checkpoint 2 -->
  <g transform="translate(360, 70)">
    <circle cx="0" cy="0" r="5" fill="#FFFFFF" stroke="#059669" stroke-width="2.2" class="anim-node"/>
    <rect x="-45" y="-26" width="90" height="18" rx="4" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
    <text x="0" y="-14" fill="#059669" class="font-mono" font-size="9" font-weight="700" text-anchor="middle">02. EMBEDDINGS</text>
  </g>

  <!-- Checkpoint 3 -->
  <g transform="translate(540, 140)">
    <circle cx="0" cy="0" r="5" fill="#FFFFFF" stroke="#D97706" stroke-width="2.2" class="anim-node"/>
    <rect x="-40" y="12" width="80" height="18" rx="4" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
    <text x="0" y="24" fill="#D97706" class="font-mono" font-size="9" font-weight="700" text-anchor="middle">03. NEURAL</text>
  </g>

  <!-- Checkpoint 4 -->
  <g transform="translate(660, 180)">
    <circle cx="0" cy="0" r="5" fill="#FFFFFF" stroke="#B45309" stroke-width="2.2" class="anim-node"/>
    <rect x="-45" y="12" width="90" height="18" rx="4" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
    <text x="0" y="24" fill="#B45309" class="font-mono" font-size="9" font-weight="700" text-anchor="middle">04. RAG / AGENT</text>
  </g>

  <!-- Checkpoint 5 (Peak Throughput) -->
  <g transform="translate(940, 50)">
    <circle cx="0" cy="0" r="6" fill="#EA580C" stroke="#C2410C" stroke-width="2.2" class="anim-node"/>
    <rect x="-55" y="-26" width="105" height="18" rx="4" fill="#FFF7ED" stroke="#FDBA74" stroke-width="1"/>
    <text x="-2" y="-14" fill="#EA580C" class="font-mono" font-size="9" font-weight="700" text-anchor="middle">05. PROD SERVING</text>
  </g>

  <!-- ================= RACING PRUSSIAN NAVY CYBER SPEEDSTER ================= -->
  <g id="cyber-speedster">
    <!-- Clean Tail Lights -->
    <rect x="-17" y="-5" width="2.5" height="3" rx="1" fill="#EA580C"/>
    <rect x="-17" y="2" width="2.5" height="3" rx="1" fill="#EA580C"/>

    <!-- Car Body in Deep Prussian Navy with Amber Accents -->
    <rect x="-16" y="-6" width="32" height="12" rx="4" fill="#0F172A" stroke="#D97706" stroke-width="1.4"/>
    
    <!-- Windshield -->
    <polygon points="-4,-4 8,-4 5,4 -4,4" fill="#38BDF8" opacity="0.95"/>

    <!-- Headlights Beam (Amber Gold Glow) -->
    <polygon points="16,-4 42,-8 42,8 16,4" fill="#FDE68A" opacity="0.5"/>
    <circle cx="16" cy="-3" r="1.8" fill="#F59E0B"/>
    <circle cx="16" cy="3" r="1.8" fill="#F59E0B"/>

    <!-- Rear Spoiler -->
    <line x1="-15" y1="-7" x2="-15" y2="7" stroke="#D97706" stroke-width="1.8" stroke-linecap="round"/>

    <!-- Navy Wheels -->
    <circle cx="-10" cy="-6" r="2" fill="#D97706"/>
    <circle cx="10" cy="-6" r="2" fill="#D97706"/>
    <circle cx="-10" cy="6" r="2" fill="#D97706"/>
    <circle cx="10" cy="6" r="2" fill="#D97706"/>

    <!-- Motion Animation along the Track Path -->
    <animateMotion dur="4.5s" repeatCount="indefinite" rotate="auto">
      <mpath href="#race-track"/>
    </animateMotion>
  </g>
</svg>"""


def generate_readme() -> str:
    """Generates the comprehensive, professional GitHub Profile README in Studio Porcelain Ivory & Prussian Navy palette."""
    return f"""<div align="center">

<img src="https://raw.githubusercontent.com/vn002-tech/vn002-tech/main/assets/ai-engineer-profile.svg?cachebust={CACHE_KEY}" width="100%" alt="VAN — AI Engineer Banner" />

<br/><br/>

<!-- Animated Typing SVG (Crisp Prussian Navy Typography) -->
<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=20&pause=1200&color=0F172A&center=true&vCenter=true&width=760&lines=AI+Engineering+%7C+Machine+Learning+%26+Data+Science;LLMs+%C2%B7+RAG+%C2%B7+Deep+Learning+%26+AI+Automation;Python+%7C+PyTorch+%7C+Scikit-learn+%7C+FastAPI+%7C+Docker;From+Data+Pipelines+to+Production-Ready+AI+Systems" alt="Typing SVG" />
</a>

<br/><br/>

<!-- Action & Contact Badges -->
<a href="https://github.com/vn002-tech"><img src="https://img.shields.io/badge/GitHub-vn002--tech-0F172A?style=for-the-badge&logo=github&logoColor=FFFFFF" alt="GitHub" /></a>
&nbsp;
<a href="https://linkedin.com"><img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
&nbsp;
<a href="mailto:wahidivansaputra@gmail.com"><img src="https://img.shields.io/badge/Email-wahidivansaputra-D97706?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" /></a>

<br/><br/>

<!-- 4-Pillar Core AI Engineering Matrix SVG Card -->
<img src="https://raw.githubusercontent.com/vn002-tech/vn002-tech/main/assets/ai-pillars.svg?cachebust={CACHE_KEY}" width="100%" alt="4-Pillar Core AI Engineering Domains" />

</div>

---

### End-to-End AI Engineering Architecture

<div align="center">

<img src="https://raw.githubusercontent.com/vn002-tech/vn002-tech/main/assets/ai-engineering-pipeline.svg?cachebust={CACHE_KEY}" width="100%" alt="AI Engineering Architecture Diagram" />

<br/><br/>

> **Data Foundation → Feature &amp; Embedding Engine → [ML &amp; Data Science · Deep Learning · LLM &amp; Automation] → FastAPI Serving → Autonomous Client**

</div>

---

### Telemetry Velocity &amp; Real-Time System Activity

<div align="center">

<!-- Cyber Speedster Racing Across Telemetry Waveform Track -->
<img src="https://raw.githubusercontent.com/vn002-tech/vn002-tech/main/assets/ai-telemetry-track.svg?cachebust={CACHE_KEY}" width="100%" alt="AI Inference Velocity Track with Cyber Car" />

<br/><br/>

<!-- Live GitHub Contribution Calendar (Royal Cobalt Blue) -->
<img src="https://ghchart.rshah.org/0284C7/vn002-tech" width="100%" alt="vn002-tech Live GitHub Contribution Calendar" />

</div>

<br/><br/>

<div align="center">

<b>“Build systems that turn data into decisions.”</b><br/>
<sub>— VAN · vn002-tech</sub>

<br/><br/>

<!-- Animated Wave Footer (Studio Ivory to Warm Sand Gradient) -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:faf9f5,50:ebe7de,100:d5cfc2&height=100&section=footer" width="100%" alt="Footer Wave" />

</div>
"""


def main():
    root = Path(__file__).resolve().parent
    assets_dir = root / "assets"
    assets_dir.mkdir(parents=True, exist_ok=True)

    # 1. Update SVG Banner
    svg_path = assets_dir / "ai-engineer-profile.svg"
    svg_path.write_text(generate_svg_banner(), encoding="utf-8")
    print(f"Generated animated SVG banner: {svg_path}")

    # 2. Update AI Pillars SVG
    pillars_svg_path = assets_dir / "ai-pillars.svg"
    pillars_svg_path.write_text(generate_pillars_svg(), encoding="utf-8")
    print(f"Generated AI Pillars SVG: {pillars_svg_path}")

    # 3. Update AI Engineering Pipeline SVG
    pipeline_svg_path = assets_dir / "ai-engineering-pipeline.svg"
    pipeline_svg_path.write_text(generate_pipeline_svg(), encoding="utf-8")
    print(f"Generated AI Engineering pipeline SVG: {pipeline_svg_path}")

    # 4. Update Cyber Car Telemetry Track SVG
    track_svg_path = assets_dir / "ai-telemetry-track.svg"
    track_svg_path.write_text(generate_telemetry_track_svg(), encoding="utf-8")
    print(f"Generated Cyber Telemetry Speedway Track SVG: {track_svg_path}")

    # 5. Update README.md
    readme_path = root / "README.md"
    readme_path.write_text(generate_readme(), encoding="utf-8")
    print(f"Generated README: {readme_path}")


if __name__ == "__main__":
    main()
