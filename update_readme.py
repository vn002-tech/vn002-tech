#!/usr/bin/env python3
"""
update_readme.py
Programmatic generator for vn002-tech GitHub Profile README, Animated Luxury SVG Card,
AI Engineering Pillars Card SVG, AI Architecture Diagram SVG, and Cyber Telemetry Speedway Track SVG.
Strictly clean, modern, and professional aesthetic without informal emojis.
"""

from pathlib import Path
import time

CACHE_KEY = int(time.time())


def generate_svg_banner() -> str:
    """
    Generates a luxury, deep purple geometric layered executive card SVG banner (Pinterest style)
    with the animated neural network mesh cluster on the left side preserved and enhanced.
    """
    return """<svg width="1200" height="310" viewBox="0 0 1200 310" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Background Gradient -->
    <linearGradient id="card-bg" x1="0" y1="0" x2="1200" y2="310" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#08040F"/>
      <stop offset="35%" stop-color="#120822"/>
      <stop offset="70%" stop-color="#190A2E"/>
      <stop offset="100%" stop-color="#06020C"/>
    </linearGradient>

    <!-- Diagonal Geometric Ribbon Gradients (Pinterest Luxury Card Style) -->
    <linearGradient id="ribbon-dark-1" x1="0" y1="0" x2="600" y2="310" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#2D104E" stop-opacity="0.85"/>
      <stop offset="100%" stop-color="#120520" stop-opacity="0.95"/>
    </linearGradient>

    <linearGradient id="ribbon-bright-main" x1="280" y1="0" x2="520" y2="310" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#C084FC"/>
      <stop offset="40%" stop-color="#9333EA"/>
      <stop offset="80%" stop-color="#6B21A8"/>
      <stop offset="100%" stop-color="#3B0764"/>
    </linearGradient>

    <linearGradient id="ribbon-cross-thin" x1="150" y1="0" x2="450" y2="310" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#E879F9" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#7C3AED" stop-opacity="0.1"/>
    </linearGradient>

    <linearGradient id="ribbon-right-dark" x1="750" y1="0" x2="1200" y2="310" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#280C48" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#0D0417" stop-opacity="0.8"/>
    </linearGradient>

    <!-- Radial Glows -->
    <radialGradient id="core-glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#9333EA" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#9333EA" stop-opacity="0"/>
    </radialGradient>

    <radialGradient id="card-ambient-light" cx="65%" cy="30%" r="60%">
      <stop offset="0%" stop-color="#A855F7" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#08040F" stop-opacity="0"/>
    </radialGradient>

    <filter id="soft-blur" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="5" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>

    <filter id="ribbon-shadow" x="-30%" y="-30%" width="160%" height="160%">
      <feDropShadow dx="-6" dy="10" stdDeviation="8" flood-color="#000000" flood-opacity="0.85"/>
    </filter>
  </defs>

  <style>
    .font-title { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    .font-mono { font-family: 'JetBrains Mono', 'Fira Code', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; }

    @keyframes pulse-core {
      0%, 100% { transform: scale(1); opacity: 0.85; filter: drop-shadow(0 0 4px #A855F7); }
      50% { transform: scale(1.18); opacity: 1; filter: drop-shadow(0 0 12px #C084FC); }
    }

    @keyframes flow-data {
      0% { stroke-dashoffset: 24; }
      100% { stroke-dashoffset: 0; }
    }

    @keyframes radar-ping {
      0% { r: 3.5px; opacity: 1; }
      75%, 100% { r: 8px; opacity: 0; }
    }

    @keyframes glow-line {
      0%, 100% { stroke-opacity: 0.35; }
      50% { stroke-opacity: 0.95; }
    }

    .anim-pulse {
      transform-origin: 170px 120px;
      animation: pulse-core 3s ease-in-out infinite;
    }

    .anim-flow {
      stroke-dasharray: 4 4;
      animation: flow-data 1.5s linear infinite;
    }

    .anim-radar {
      animation: radar-ping 2s cubic-bezier(0, 0, 0.2, 1) infinite;
    }

    .anim-glow {
      animation: glow-line 2.5s ease-in-out infinite;
    }
  </style>

  <!-- Container Base Box -->
  <rect x="2" y="2" width="1196" height="306" rx="18" fill="url(#card-bg)" stroke="#3B1466" stroke-width="1.8"/>

  <!-- Ambient Luxury Backlights -->
  <rect x="2" y="2" width="1196" height="306" rx="18" fill="url(#card-ambient-light)"/>
  <circle cx="450" cy="140" r="180" fill="url(#core-glow)"/>
  <circle cx="1060" cy="90" r="160" fill="url(#core-glow)"/>

  <!-- ================= LUXURY GEOMETRIC LAYERED RIBBONS (PINTEREST BUSINESS CARD STYLE) ================= -->
  <!-- Layer 1: Dark Purple Background Angled Band -->
  <polygon points="240,0 370,0 100,310 0,310 0,260 210,0" fill="url(#ribbon-dark-1)"/>

  <!-- Layer 2: Primary Radiant Purple Cross Band (With Deep Shadow) -->
  <polygon points="430,0 540,0 230,310 120,310" fill="url(#ribbon-bright-main)" filter="url(#ribbon-shadow)"/>
  <!-- Highlight Edge Line on Main Ribbon -->
  <line x1="430" y1="0" x2="120" y2="310" stroke="#F3E8FF" stroke-width="1.2" opacity="0.65"/>
  <line x1="540" y1="0" x2="230" y2="310" stroke="#E9D5FF" stroke-width="0.8" opacity="0.35"/>

  <!-- Layer 3: Intersecting Thin Accent Ribbon -->
  <polygon points="80,0 130,0 360,310 310,310" fill="url(#ribbon-cross-thin)"/>

  <!-- Layer 4: Right Wing Geometric Facet -->
  <polygon points="840,0 1200,0 1200,240 960,310 800,310" fill="url(#ribbon-right-dark)"/>
  <line x1="840" y1="0" x2="1200" y2="240" stroke="#7C3AED" stroke-width="1" opacity="0.4"/>

  <!-- ================= LEFT: ANIMATED NEURAL NETWORK MESH (PRESERVED) ================= -->
  <g opacity="0.95" transform="translate(35, 45)">
    <!-- Connections -->
    <line x1="30" y1="120" x2="95" y2="60" stroke="#4C1D95" stroke-width="1.5" class="anim-flow"/>
    <line x1="30" y1="120" x2="95" y2="180" stroke="#4C1D95" stroke-width="1.5"/>
    <line x1="95" y1="60" x2="170" y2="38" stroke="#6B21A8" stroke-width="1.5"/>
    <line x1="95" y1="60" x2="170" y2="120" stroke="#A855F7" stroke-width="2" class="anim-glow"/>
    <line x1="95" y1="180" x2="170" y2="120" stroke="#A855F7" stroke-width="2" class="anim-glow"/>
    <line x1="95" y1="180" x2="170" y2="202" stroke="#6B21A8" stroke-width="1.5"/>
    <line x1="170" y1="38" x2="245" y2="80" stroke="#4C1D95" stroke-width="1.5"/>
    <line x1="170" y1="120" x2="245" y2="80" stroke="#C084FC" stroke-width="2" class="anim-flow"/>
    <line x1="170" y1="120" x2="245" y2="160" stroke="#C084FC" stroke-width="2" class="anim-flow"/>
    <line x1="170" y1="202" x2="245" y2="160" stroke="#4C1D95" stroke-width="1.5"/>

    <!-- Outer Nodes -->
    <circle cx="30" cy="120" r="5.5" fill="#170B2C" stroke="#8B5CF6" stroke-width="2"/>
    <circle cx="95" cy="60" r="6.5" fill="#170B2C" stroke="#A855F7" stroke-width="2"/>
    <circle cx="95" cy="180" r="6.5" fill="#170B2C" stroke="#A855F7" stroke-width="2"/>
    <circle cx="170" cy="38" r="5.5" fill="#170B2C" stroke="#8B5CF6" stroke-width="2"/>
    
    <!-- Central Pulsing Core Node -->
    <circle cx="170" cy="120" r="11" fill="#581C87" stroke="#E879F9" stroke-width="2.5" class="anim-pulse" filter="url(#soft-blur)"/>
    <circle cx="170" cy="120" r="4" fill="#FFFFFF"/>
    
    <circle cx="170" cy="202" r="5.5" fill="#170B2C" stroke="#8B5CF6" stroke-width="2"/>
    <circle cx="245" cy="80" r="7" fill="#170B2C" stroke="#C084FC" stroke-width="2"/>
    <circle cx="245" cy="160" r="7" fill="#170B2C" stroke="#C084FC" stroke-width="2"/>
  </g>

  <!-- Vertical Dividing Shadow Line -->
  <line x1="355" y1="30" x2="355" y2="280" stroke="#3B1466" stroke-width="1.5" opacity="0.6"/>

  <!-- ================= RIGHT: IDENTITY & EXECUTIVE CARD CONTENT ================= -->
  <!-- Top Status Badge with Radar Ping -->
  <rect x="385" y="32" width="265" height="26" rx="13" fill="#1C0B33" stroke="#7C3AED" stroke-width="1.2"/>
  <circle cx="402" cy="45" r="3.5" fill="#C084FC"/>
  <circle cx="402" cy="45" r="3.5" fill="#E879F9" class="anim-radar"/>
  <text x="416" y="49" fill="#E9D5FF" class="font-mono" font-size="10.5" font-weight="700" letter-spacing="1.2">AI ENGINEERING &amp; DATA SCIENCE</text>

  <!-- Name & Identifier -->
  <text x="385" y="104" fill="#FFFFFF" class="font-title" font-size="42" font-weight="800" letter-spacing="2">VAN</text>
  <rect x="500" y="80" width="112" height="28" rx="7" fill="#2A0E4E" stroke="#9333EA" stroke-width="1.2"/>
  <text x="556" y="98" fill="#E879F9" class="font-mono" font-size="12.5" font-weight="700" text-anchor="middle">vn002-tech</text>

  <!-- Primary Role -->
  <text x="385" y="138" fill="#F3E8FF" class="font-title" font-size="18.5" font-weight="700" letter-spacing="1.5">AI ENGINEER</text>
  <text x="385" y="162" fill="#C4B5FD" class="font-title" font-size="13.5" font-weight="400">AI Engineering · Machine Learning &amp; Data Science · LLMs &amp; Automation</text>

  <!-- Tech Stack Pills with Purple Bevel Borders -->
  <g transform="translate(385, 184)">
    <rect x="0" y="0" width="72" height="25" rx="6" fill="#180A2E" stroke="#6B21A8" stroke-width="1"/>
    <text x="36" y="17" fill="#E9D5FF" class="font-mono" font-size="11" font-weight="600" text-anchor="middle">Python</text>

    <rect x="80" y="0" width="80" height="25" rx="6" fill="#180A2E" stroke="#6B21A8" stroke-width="1"/>
    <text x="120" y="17" fill="#E9D5FF" class="font-mono" font-size="11" font-weight="600" text-anchor="middle">PyTorch</text>

    <rect x="168" y="0" width="102" height="25" rx="6" fill="#180A2E" stroke="#6B21A8" stroke-width="1"/>
    <text x="219" y="17" fill="#E9D5FF" class="font-mono" font-size="11" font-weight="600" text-anchor="middle">Scikit-learn</text>

    <rect x="278" y="0" width="76" height="25" rx="6" fill="#180A2E" stroke="#6B21A8" stroke-width="1"/>
    <text x="316" y="17" fill="#E9D5FF" class="font-mono" font-size="11" font-weight="600" text-anchor="middle">FastAPI</text>

    <rect x="362" y="0" width="96" height="25" rx="6" fill="#180A2E" stroke="#6B21A8" stroke-width="1"/>
    <text x="410" y="17" fill="#E9D5FF" class="font-mono" font-size="11" font-weight="600" text-anchor="middle">PostgreSQL</text>

    <rect x="466" y="0" width="72" height="25" rx="6" fill="#180A2E" stroke="#6B21A8" stroke-width="1"/>
    <text x="502" y="17" fill="#E9D5FF" class="font-mono" font-size="11" font-weight="600" text-anchor="middle">Docker</text>
  </g>

  <!-- Horizontal Luxury Divider -->
  <line x1="385" y1="226" x2="1150" y2="226" stroke="#3B1466" stroke-width="1"/>

  <!-- Social & Contact Badges (Executive Card Style) -->
  <g transform="translate(385, 240)">
    <rect x="0" y="0" width="170" height="34" rx="7" fill="#150826" stroke="#4C1D95" stroke-width="1"/>
    <path d="M18 17C18 12.58 21.58 9 26 9C30.42 9 34 12.58 34 17C34 20.54 31.7 23.54 28.52 24.6C28.12 24.67 27.97 24.43 27.97 24.21C27.97 24.02 27.98 23.36 27.98 22.56C25.75 23.05 25.28 21.61 25.28 21.61C24.92 20.69 24.39 20.45 24.39 20.45C23.66 19.95 24.45 19.96 24.45 19.96C25.26 20.02 25.68 20.79 25.68 20.79C26.4 22.02 27.56 21.67 28.02 21.46C28.09 20.94 28.3 20.58 28.53 20.38C26.75 20.18 24.88 19.49 24.88 16.42C24.88 15.55 25.19 14.83 25.7 14.27C25.62 14.07 25.35 13.25 25.78 12.16C25.78 12.16 26.45 11.95 27.97 12.98C28.61 12.8 29.29 12.71 29.97 12.71C30.65 12.71 31.33 12.8 31.97 12.98C33.49 11.95 34.16 12.16 34.16 12.16C34.59 13.25 34.32 14.07 34.24 14.27C34.75 14.83 35.06 15.55 35.06 16.42C35.06 19.5 33.18 20.18 31.4 20.37C31.69 20.62 31.95 21.11 31.95 21.87C31.95 22.96 31.94 23.84 31.94 24.21C31.94 24.43 31.79 24.68 31.38 24.6C28.2 23.53 25.9 20.53 25.9 17H18Z" fill="#C084FC" transform="translate(-8, -3) scale(0.85)"/>
    <text x="40" y="21" fill="#F3E8FF" class="font-mono" font-size="12" font-weight="600">vn002-tech</text>

    <rect x="180" y="0" width="130" height="34" rx="7" fill="#150826" stroke="#4C1D95" stroke-width="1"/>
    <rect x="194" y="9" width="16" height="16" rx="3.5" fill="#7C3AED"/>
    <text x="202" y="21" fill="#FFFFFF" class="font-title" font-size="10" font-weight="800" text-anchor="middle">in</text>
    <text x="218" y="21" fill="#F3E8FF" class="font-title" font-size="12" font-weight="600">LinkedIn</text>

    <rect x="320" y="0" width="255" height="34" rx="7" fill="#150826" stroke="#4C1D95" stroke-width="1"/>
    <path d="M335 11H349C350.1 11 351 11.9 351 13V21C351 22.1 350.1 23 349 23H335C333.9 23 333 22.1 333 21V13C333 11.9 333.9 11 335 11Z" stroke="#C084FC" stroke-width="1.3" fill="none"/>
    <path d="M333 13L342 18L351 13" stroke="#C084FC" stroke-width="1.3" fill="none"/>
    <text x="360" y="21" fill="#F3E8FF" class="font-mono" font-size="11.5" font-weight="500">wahidivansaputra@gmail.com</text>
  </g>
</svg>"""


def generate_pillars_svg() -> str:
    """
    Generates an ultra-sleek, animated 4-Card Vector Matrix SVG without informal emojis.
    """
    return """<svg width="1000" height="148" viewBox="0 0 1000 148" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Dark Card Background Gradient -->
    <linearGradient id="pil-card-grad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#111827"/>
      <stop offset="50%" stop-color="#0E1422"/>
      <stop offset="100%" stop-color="#080C14"/>
    </linearGradient>

    <!-- Glowing LLM Card Gradient -->
    <linearGradient id="pil-llm-grad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#24123E"/>
      <stop offset="50%" stop-color="#170E2A"/>
      <stop offset="100%" stop-color="#0C0816"/>
    </linearGradient>

    <!-- Glow Filter -->
    <filter id="pil-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    .font-mono { font-family: 'JetBrains Mono', 'Fira Code', ui-monospace, SFMono-Regular, Menlo, monospace; }

    @keyframes pulse-dot {
      0%, 100% { opacity: 0.35; transform: scale(0.9); }
      50% { opacity: 1; transform: scale(1.2); }
    }

    @keyframes radar-ring {
      0% { r: 3.5px; opacity: 1; }
      100% { r: 9px; opacity: 0; }
    }

    .anim-pulse {
      animation: pulse-dot 2.2s ease-in-out infinite;
    }

    .anim-radar {
      animation: radar-ring 1.8s cubic-bezier(0, 0, 0.2, 1) infinite;
    }
  </style>

  <!-- Frame Background -->
  <rect x="2" y="2" width="996" height="144" rx="14" fill="#080C14" stroke="#1E293B" stroke-width="1.5"/>

  <!-- ================= CARD 1: ML & DATA SCIENCE ================= -->
  <g transform="translate(16, 14)">
    <rect width="230" height="120" rx="10" fill="url(#pil-card-grad)" stroke="#2563EB" stroke-width="1.2" stroke-opacity="0.8"/>
    <circle cx="18" cy="20" r="4" fill="#60A5FA" class="anim-pulse"/>
    <text x="28" y="24" fill="#93C5FD" class="font-mono" font-size="10.5" font-weight="700" letter-spacing="0.8">ML &amp; DATA SCIENCE</text>
    <text x="16" y="49" fill="#F8FAFC" class="font-sans" font-size="13" font-weight="700">Predictive &amp; Analytics</text>
    <text x="16" y="73" fill="#94A3B8" class="font-sans" font-size="11">Feature Pipelines · XGBoost</text>
    <text x="16" y="93" fill="#64748B" class="font-sans" font-size="10.5">Statistical EDA &amp; Metrics</text>
  </g>

  <!-- ================= CARD 2: DEEP LEARNING ================= -->
  <g transform="translate(260, 14)">
    <rect width="230" height="120" rx="10" fill="url(#pil-card-grad)" stroke="#7C3AED" stroke-width="1.2" stroke-opacity="0.8"/>
    <circle cx="18" cy="20" r="4" fill="#A855F7" class="anim-pulse"/>
    <text x="28" y="24" fill="#C084FC" class="font-mono" font-size="10.5" font-weight="700" letter-spacing="0.8">DEEP LEARNING</text>
    <text x="16" y="49" fill="#F8FAFC" class="font-sans" font-size="13" font-weight="700">Neural Systems</text>
    <text x="16" y="73" fill="#94A3B8" class="font-sans" font-size="11">PyTorch · Tensors</text>
    <text x="16" y="93" fill="#64748B" class="font-sans" font-size="10.5">Dense Embeddings</text>
  </g>

  <!-- ================= CARD 3: LLMs & AUTOMATION (FOCAL) ================= -->
  <g transform="translate(504, 14)">
    <rect width="230" height="120" rx="10" fill="url(#pil-llm-grad)" stroke="#C084FC" stroke-width="1.4" filter="url(#pil-glow)"/>
    <circle cx="18" cy="20" r="4" fill="#E879F9"/>
    <circle cx="18" cy="20" r="4" fill="#C084FC" class="anim-radar"/>
    <text x="28" y="24" fill="#F0ABFC" class="font-mono" font-size="10.5" font-weight="700" letter-spacing="0.8">LLMs &amp; AUTOMATION</text>
    <text x="16" y="49" fill="#FFFFFF" class="font-sans" font-size="13" font-weight="700">AI Automation</text>
    <text x="16" y="73" fill="#E9D5FF" class="font-sans" font-size="11">RAG Pipelines · Vector DBs</text>
    <text x="16" y="93" fill="#D8B4FE" class="font-sans" font-size="10.5">Autonomous Workflows</text>
  </g>

  <!-- ================= CARD 4: MLOPS & SYSTEMS ================= -->
  <g transform="translate(748, 14)">
    <rect width="236" height="120" rx="10" fill="url(#pil-card-grad)" stroke="#10B981" stroke-width="1.2" stroke-opacity="0.8"/>
    <circle cx="18" cy="20" r="4" fill="#34D399" class="anim-pulse"/>
    <text x="28" y="24" fill="#6EE7B7" class="font-mono" font-size="10.5" font-weight="700" letter-spacing="0.8">MLOps &amp; SYSTEMS</text>
    <text x="16" y="49" fill="#F8FAFC" class="font-sans" font-size="13" font-weight="700">Serving &amp; Production</text>
    <text x="16" y="73" fill="#94A3B8" class="font-sans" font-size="11">FastAPI · Docker Runtime</text>
    <text x="16" y="93" fill="#64748B" class="font-sans" font-size="10.5">ETL &amp; Data Integrity</text>
  </g>
</svg>"""


def generate_pipeline_svg() -> str:
    """
    Generates an animated, ultra-modern Multi-Tier AI Architecture SVG Diagram without informal emojis.
    """
    return """<svg width="1000" height="420" viewBox="0 0 1000 420" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Background Gradient -->
    <linearGradient id="pipe-bg" x1="0" y1="0" x2="1000" y2="420" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#080C14"/>
      <stop offset="50%" stop-color="#0B0F19"/>
      <stop offset="100%" stop-color="#060910"/>
    </linearGradient>

    <!-- Card Background Gradient -->
    <linearGradient id="card-grad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#131B2E"/>
      <stop offset="100%" stop-color="#0D1322"/>
    </linearGradient>

    <linearGradient id="llm-card-grad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#24123E"/>
      <stop offset="100%" stop-color="#110B1E"/>
    </linearGradient>

    <!-- Glow Filter -->
    <filter id="p-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3.5" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    .font-mono { font-family: 'JetBrains Mono', 'Fira Code', ui-monospace, SFMono-Regular, Menlo, monospace; }

    @keyframes flow-fwd {
      0% { stroke-dashoffset: 24; }
      100% { stroke-dashoffset: 0; }
    }

    @keyframes pulse-dot {
      0%, 100% { opacity: 0.35; transform: scale(0.9); }
      50% { opacity: 1; transform: scale(1.2); }
    }

    @keyframes radar-ring {
      0% { r: 4px; opacity: 1; }
      100% { r: 11px; opacity: 0; }
    }

    .anim-flow-fwd {
      stroke-dasharray: 6 4;
      animation: flow-fwd 1.4s linear infinite;
    }

    .anim-pulse {
      animation: pulse-dot 2.2s ease-in-out infinite;
    }

    .anim-radar-llm {
      animation: radar-ring 1.8s cubic-bezier(0, 0, 0.2, 1) infinite;
    }
  </style>

  <!-- Container Frame -->
  <rect x="2" y="2" width="996" height="416" rx="16" fill="url(#pipe-bg)" stroke="#1E293B" stroke-width="1.5"/>

  <!-- ================= SECTION LABELS ================= -->
  <text x="35" y="32" fill="#64748B" class="font-mono" font-size="10.5" font-weight="700" letter-spacing="1.5">TIER 1: DATA &amp; FEATURE FOUNDATION</text>
  <text x="35" y="160" fill="#A855F7" class="font-mono" font-size="10.5" font-weight="700" letter-spacing="1.5">TIER 2: INTELLIGENCE &amp; MODELING BRANCHES (ML &amp; DATA SCIENCE · DL · LLM)</text>
  <text x="35" y="300" fill="#38BDF8" class="font-mono" font-size="10.5" font-weight="700" letter-spacing="1.5">TIER 3: SERVING, AGENTS &amp; AI AUTOMATION</text>

  <!-- ================= TIER 1: DATA FOUNDATION ================= -->
  <!-- 01. Ingestion -->
  <g transform="translate(35, 45)">
    <rect width="430" height="75" rx="10" fill="url(#card-grad)" stroke="#334155" stroke-width="1.2"/>
    <circle cx="22" cy="22" r="4" fill="#38BDF8" class="anim-pulse"/>
    <text x="36" y="26" fill="#38BDF8" class="font-mono" font-size="11" font-weight="700">01. DATA INGESTION &amp; VALIDATION</text>
    <text x="22" y="47" fill="#F8FAFC" class="font-sans" font-size="13" font-weight="600">ETL Pipelines &amp; Schema Integrity</text>
    <text x="22" y="65" fill="#94A3B8" class="font-sans" font-size="11">PostgreSQL · Automated Data Cleaning · Assertions</text>
  </g>

  <!-- Flow Line Tier 1 (1 to 2) -->
  <line x1="465" y1="82" x2="535" y2="82" stroke="#7C3AED" stroke-width="2" class="anim-flow-fwd"/>
  <polygon points="535,82 527,78 527,86" fill="#C084FC"/>

  <!-- 02. Feature & Embedding Matrix -->
  <g transform="translate(535, 45)">
    <rect width="430" height="75" rx="10" fill="url(#card-grad)" stroke="#7C3AED" stroke-width="1.2"/>
    <circle cx="22" cy="22" r="4" fill="#C084FC" class="anim-pulse"/>
    <text x="36" y="26" fill="#C084FC" class="font-mono" font-size="11" font-weight="700">02. FEATURE &amp; EMBEDDING PIPELINE</text>
    <text x="22" y="47" fill="#F8FAFC" class="font-sans" font-size="13" font-weight="600">Encoders, Scaling &amp; Vectorization</text>
    <text x="22" y="65" fill="#94A3B8" class="font-sans" font-size="11">Scikit-learn · Pandas · Dense Representations</text>
  </g>

  <!-- Connectors from Tier 1 (02) down to Tier 2 (3 branches) -->
  <path d="M750 120 V145 H175 V175" stroke="#64748B" stroke-width="1.5" class="anim-flow-fwd"/>
  <path d="M750 120 V175" stroke="#7C3AED" stroke-width="1.8" class="anim-flow-fwd"/>
  <path d="M750 120 V145 H825 V175" stroke="#A855F7" stroke-width="2" class="anim-flow-fwd"/>

  <!-- ================= TIER 2: 3 CORE INTELLIGENCE BRANCHES ================= -->

  <!-- Branch A: ML & Data Science -->
  <g transform="translate(35, 175)">
    <rect width="280" height="85" rx="10" fill="url(#card-grad)" stroke="#334155" stroke-width="1.2"/>
    <circle cx="20" cy="22" r="4" fill="#60A5FA" class="anim-pulse"/>
    <text x="32" y="26" fill="#60A5FA" class="font-mono" font-size="10.5" font-weight="700">03A. ML &amp; DATA SCIENCE</text>
    <text x="20" y="49" fill="#F8FAFC" class="font-sans" font-size="12.5" font-weight="600">Statistical Modeling &amp; Prediction</text>
    <text x="20" y="68" fill="#94A3B8" class="font-sans" font-size="10.5">XGBoost · Scikit-learn · EDA &amp; Analysis</text>
  </g>

  <!-- Branch B: Deep Learning -->
  <g transform="translate(360, 175)">
    <rect width="280" height="85" rx="10" fill="url(#card-grad)" stroke="#7C3AED" stroke-width="1.2"/>
    <circle cx="20" cy="22" r="4" fill="#C084FC" class="anim-pulse"/>
    <text x="32" y="26" fill="#C084FC" class="font-mono" font-size="10.5" font-weight="700">03B. DEEP LEARNING</text>
    <text x="20" y="49" fill="#F8FAFC" class="font-sans" font-size="12.5" font-weight="600">Neural &amp; Dense Networks</text>
    <text x="20" y="68" fill="#94A3B8" class="font-sans" font-size="10.5">PyTorch · Tensors · Embeddings</text>
  </g>

  <!-- Branch C: LLM & AI Automation (FOCAL POINT) -->
  <g transform="translate(685, 175)">
    <rect width="280" height="85" rx="10" fill="url(#llm-card-grad)" stroke="#C084FC" stroke-width="1.5" filter="url(#p-glow)"/>
    <circle cx="20" cy="22" r="4" fill="#E879F9"/>
    <circle cx="20" cy="22" r="4" fill="#C084FC" class="anim-radar-llm"/>
    <text x="32" y="26" fill="#F0ABFC" class="font-mono" font-size="10.5" font-weight="700">03C. LLMs &amp; AUTOMATION</text>
    <text x="20" y="49" fill="#FFFFFF" class="font-sans" font-size="12.5" font-weight="700">RAG &amp; Autonomous Agents</text>
    <text x="20" y="68" fill="#D8B4FE" class="font-sans" font-size="10.5">Vector Search · Tool Use · Chains</text>
  </g>

  <!-- Connectors from Tier 2 down to Tier 3 -->
  <path d="M175 260 V285 H330 V315" stroke="#64748B" stroke-width="1.5" class="anim-flow-fwd"/>
  <path d="M500 260 V315" stroke="#7C3AED" stroke-width="1.8" class="anim-flow-fwd"/>
  <path d="M825 260 V285 H670 V315" stroke="#A855F7" stroke-width="2" class="anim-flow-fwd"/>

  <!-- ================= TIER 3: SERVING, AGENTS & AUTOMATION ================= -->

  <!-- 04. Evaluation & Metrics -->
  <g transform="translate(35, 315)">
    <rect width="280" height="85" rx="10" fill="url(#card-grad)" stroke="#334155" stroke-width="1.2"/>
    <circle cx="20" cy="22" r="4" fill="#818CF8" class="anim-pulse"/>
    <text x="32" y="26" fill="#818CF8" class="font-mono" font-size="10.5" font-weight="700">04. EVALUATION &amp; METRICS</text>
    <text x="20" y="49" fill="#F8FAFC" class="font-sans" font-size="12.5" font-weight="600">Empirical Validation</text>
    <text x="20" y="68" fill="#94A3B8" class="font-sans" font-size="10.5">ROC-AUC · Recall · Benchmark Cost</text>
  </g>

  <!-- 05. FastAPI Serving -->
  <g transform="translate(360, 315)">
    <rect width="280" height="85" rx="10" fill="url(#card-grad)" stroke="#10B981" stroke-width="1.2"/>
    <circle cx="20" cy="22" r="4" fill="#34D399" class="anim-pulse"/>
    <text x="32" y="26" fill="#34D399" class="font-mono" font-size="10.5" font-weight="700">05. FASTAPI SERVING</text>
    <text x="20" y="49" fill="#F8FAFC" class="font-sans" font-size="12.5" font-weight="600">Async Inference Endpoints</text>
    <text x="20" y="68" fill="#94A3B8" class="font-sans" font-size="10.5">REST APIs · Docker Containerization</text>
  </g>

  <!-- 06. Autonomous AI Applications & UI -->
  <g transform="translate(685, 315)">
    <rect width="280" height="85" rx="10" fill="url(#card-grad)" stroke="#F59E0B" stroke-width="1.2"/>
    <circle cx="20" cy="22" r="4" fill="#FBBF24" class="anim-pulse"/>
    <text x="32" y="26" fill="#FBBF24" class="font-mono" font-size="10.5" font-weight="700">06. AI APPS &amp; AUTOMATION</text>
    <text x="20" y="49" fill="#F8FAFC" class="font-sans" font-size="12.5" font-weight="600">Client UI &amp; Workflows</text>
    <text x="20" y="68" fill="#94A3B8" class="font-sans" font-size="10.5">Streamlit · Real-Time Trigger Agents</text>
  </g>
</svg>"""


def generate_telemetry_track_svg() -> str:
    """
    Generates an animated Cyber Speedway Track SVG without informal emojis.
    """
    return """<svg width="1000" height="220" viewBox="0 0 1000 220" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Background Gradient -->
    <linearGradient id="track-bg" x1="0" y1="0" x2="1000" y2="220" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#080C14"/>
      <stop offset="50%" stop-color="#0B0F19"/>
      <stop offset="100%" stop-color="#060910"/>
    </linearGradient>

    <!-- Area Gradient under Track -->
    <linearGradient id="track-area" x1="0" y1="60" x2="0" y2="200" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#A855F7" stop-opacity="0.35"/>
      <stop offset="60%" stop-color="#6366F1" stop-opacity="0.1"/>
      <stop offset="100%" stop-color="#060910" stop-opacity="0"/>
    </linearGradient>

    <!-- Neon Track Stroke Gradient -->
    <linearGradient id="track-line" x1="0" y1="0" x2="1000" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#38BDF8"/>
      <stop offset="35%" stop-color="#818CF8"/>
      <stop offset="70%" stop-color="#C084FC"/>
      <stop offset="100%" stop-color="#F43F5E"/>
    </linearGradient>

    <!-- Glow Filter -->
    <filter id="car-glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="4" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
    .font-mono { font-family: 'JetBrains Mono', 'Fira Code', monospace; }

    @keyframes pulse-node {
      0%, 100% { r: 3.5px; opacity: 0.6; }
      50% { r: 6px; opacity: 1; filter: drop-shadow(0 0 6px #C084FC); }
    }

    @keyframes grid-glow {
      0%, 100% { opacity: 0.15; }
      50% { opacity: 0.3; }
    }

    .anim-node { animation: pulse-node 2.2s ease-in-out infinite; }
    .anim-grid { animation: grid-glow 3s ease-in-out infinite; }
  </style>

  <!-- Frame -->
  <rect x="2" y="2" width="996" height="216" rx="14" fill="url(#track-bg)" stroke="#1E293B" stroke-width="1.5"/>

  <!-- Background Telemetry Grid Lines -->
  <g class="anim-grid" stroke="#334155" stroke-width="0.8" stroke-dasharray="3 6" opacity="0.25">
    <line x1="50" y1="50" x2="950" y2="50"/>
    <line x1="50" y1="90" x2="950" y2="90"/>
    <line x1="50" y1="130" x2="950" y2="130"/>
    <line x1="50" y1="170" x2="950" y2="170"/>
    <line x1="200" y1="40" x2="200" y2="190"/>
    <line x1="400" y1="40" x2="400" y2="190"/>
    <line x1="600" y1="40" x2="600" y2="190"/>
    <line x1="800" y1="40" x2="800" y2="190"/>
  </g>

  <!-- HUD Header without emojis -->
  <text x="40" y="32" fill="#38BDF8" class="font-mono" font-size="11" font-weight="700" letter-spacing="1.5">TELEMETRY CIRCUIT // INFERENCE ACCELERATION TRACK</text>
  <text x="960" y="32" fill="#A855F7" class="font-mono" font-size="10" font-weight="600" text-anchor="end">SYSTEM STATUS: HIGH VELOCITY</text>

  <!-- Filled Area Under Graph Track -->
  <path d="M 40 160 C 160 160, 240 70, 360 70 C 480 70, 540 180, 660 180 C 760 180, 830 50, 940 50 L 940 200 L 40 200 Z" fill="url(#track-area)"/>

  <!-- Track Outline Base (Wide Glow) -->
  <path id="race-track" d="M 40 160 C 160 160, 240 70, 360 70 C 480 70, 540 180, 660 180 C 760 180, 830 50, 940 50" fill="none" stroke="url(#track-line)" stroke-width="4.5" stroke-linecap="round" filter="url(#car-glow)"/>

  <!-- Track Center Dashed Guideline -->
  <path d="M 40 160 C 160 160, 240 70, 360 70 C 480 70, 540 180, 660 180 C 760 180, 830 50, 940 50" fill="none" stroke="#FFFFFF" stroke-width="1.2" stroke-dasharray="6 8" opacity="0.8"/>

  <!-- Checkpoint Telemetry Nodes along Graph -->
  <!-- Checkpoint 1 -->
  <g transform="translate(200, 115)">
    <circle cx="0" cy="0" r="5" fill="#0F172A" stroke="#38BDF8" stroke-width="2" class="anim-node"/>
    <rect x="-40" y="12" width="80" height="18" rx="4" fill="#090E17" stroke="#1E293B" stroke-width="1"/>
    <text x="0" y="24" fill="#94A3B8" class="font-mono" font-size="9" font-weight="600" text-anchor="middle">01. INGEST</text>
  </g>

  <!-- Checkpoint 2 -->
  <g transform="translate(360, 70)">
    <circle cx="0" cy="0" r="5" fill="#0F172A" stroke="#818CF8" stroke-width="2" class="anim-node"/>
    <rect x="-45" y="-26" width="90" height="18" rx="4" fill="#090E17" stroke="#1E293B" stroke-width="1"/>
    <text x="0" y="-14" fill="#C084FC" class="font-mono" font-size="9" font-weight="600" text-anchor="middle">02. EMBEDDINGS</text>
  </g>

  <!-- Checkpoint 3 -->
  <g transform="translate(540, 140)">
    <circle cx="0" cy="0" r="5" fill="#0F172A" stroke="#A855F7" stroke-width="2" class="anim-node"/>
    <rect x="-40" y="12" width="80" height="18" rx="4" fill="#090E17" stroke="#1E293B" stroke-width="1"/>
    <text x="0" y="24" fill="#D8B4FE" class="font-mono" font-size="9" font-weight="600" text-anchor="middle">03. NEURAL</text>
  </g>

  <!-- Checkpoint 4 -->
  <g transform="translate(660, 180)">
    <circle cx="0" cy="0" r="5" fill="#0F172A" stroke="#C084FC" stroke-width="2" class="anim-node"/>
    <rect x="-45" y="12" width="90" height="18" rx="4" fill="#090E17" stroke="#1E293B" stroke-width="1"/>
    <text x="0" y="24" fill="#F0ABFC" class="font-mono" font-size="9" font-weight="600" text-anchor="middle">04. RAG / AGENT</text>
  </g>

  <!-- Checkpoint 5 (Peak Throughput) -->
  <g transform="translate(940, 50)">
    <circle cx="0" cy="0" r="6" fill="#581C87" stroke="#F43F5E" stroke-width="2" class="anim-node"/>
    <rect x="-55" y="-26" width="105" height="18" rx="4" fill="#1E0A2A" stroke="#701A75" stroke-width="1"/>
    <text x="-2" y="-14" fill="#F472B6" class="font-mono" font-size="9" font-weight="700" text-anchor="middle">05. PROD SERVING</text>
  </g>

  <!-- ================= RACING CYBER CAR ================= -->
  <g id="cyber-speedster">
    <!-- Clean Futuristic LED Tail Lights -->
    <rect x="-17" y="-5" width="2.5" height="3" rx="1" fill="#F43F5E" filter="url(#car-glow)"/>
    <rect x="-17" y="2" width="2.5" height="3" rx="1" fill="#F43F5E" filter="url(#car-glow)"/>

    <!-- Car Body -->
    <rect x="-16" y="-6" width="32" height="12" rx="4" fill="#0F172A" stroke="#C084FC" stroke-width="1.4"/>
    
    <!-- Windshield & Cockpit -->
    <polygon points="-4,-4 8,-4 5,4 -4,4" fill="#38BDF8" opacity="0.9"/>

    <!-- Headlights Beam (Front Glow) -->
    <polygon points="16,-4 42,-8 42,8 16,4" fill="#38BDF8" opacity="0.35" filter="url(#car-glow)"/>
    <circle cx="16" cy="-3" r="1.8" fill="#E0F2FE"/>
    <circle cx="16" cy="3" r="1.8" fill="#E0F2FE"/>

    <!-- Rear Spoiler -->
    <line x1="-15" y1="-7" x2="-15" y2="7" stroke="#A855F7" stroke-width="1.8" stroke-linecap="round"/>

    <!-- Neon Wheels -->
    <circle cx="-10" cy="-6" r="2" fill="#C084FC"/>
    <circle cx="10" cy="-6" r="2" fill="#C084FC"/>
    <circle cx="-10" cy="6" r="2" fill="#C084FC"/>
    <circle cx="10" cy="6" r="2" fill="#C084FC"/>

    <!-- Motion Animation along the Track Path -->
    <animateMotion dur="4.5s" repeatCount="indefinite" rotate="auto">
      <mpath href="#race-track"/>
    </animateMotion>
  </g>
</svg>"""


def generate_readme() -> str:
    """Generates the comprehensive, professional GitHub Profile README without informal emojis."""
    return f"""<div align="center">

<img src="./assets/ai-engineer-profile.svg?raw=true&v={CACHE_KEY}" width="100%" alt="VAN — AI Engineer Banner" />

<br/><br/>

<!-- Animated Typing SVG (Clean Professional Typography) -->
<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=20&pause=1200&color=C084FC&center=true&vCenter=true&width=760&lines=AI+Engineering+%7C+Machine+Learning+%26+Data+Science;LLMs+%C2%B7+RAG+%C2%B7+Deep+Learning+%26+AI+Automation;Python+%7C+PyTorch+%7C+Scikit-learn+%7C+FastAPI+%7C+Docker;From+Data+Pipelines+to+Production-Ready+AI+Systems" alt="Typing SVG" />
</a>

<br/><br/>

<!-- Action & Contact Badges -->
<a href="https://github.com/vn002-tech"><img src="https://img.shields.io/badge/GitHub-vn002--tech-0B0F17?style=for-the-badge&logo=github&logoColor=F8FAFC" alt="GitHub" /></a>
&nbsp;
<a href="https://linkedin.com"><img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
&nbsp;
<a href="mailto:wahidivansaputra@gmail.com"><img src="https://img.shields.io/badge/Email-wahidivansaputra-7C3AED?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" /></a>

<br/><br/>

<!-- 4-Pillar Core AI Engineering Matrix SVG Card -->
<img src="./assets/ai-pillars.svg?raw=true&v={CACHE_KEY}" width="100%" alt="4-Pillar Core AI Engineering Domains" />

</div>

---

### End-to-End AI Engineering Architecture

<div align="center">

<img src="./assets/ai-engineering-pipeline.svg?raw=true&v={CACHE_KEY}" width="100%" alt="AI Engineering Architecture Diagram" />

<br/><br/>

> **Data Foundation → Feature &amp; Embedding Engine → [ML &amp; Data Science · Deep Learning · LLM &amp; Automation] → FastAPI Serving → Autonomous Client**

</div>

---

### Telemetry Velocity &amp; Real-Time System Activity

<div align="center">

<!-- Cyber Speedster Racing Across Telemetry Waveform Track -->
<img src="./assets/ai-telemetry-track.svg?raw=true&v={CACHE_KEY}" width="100%" alt="AI Inference Velocity Track with Cyber Car" />

<br/><br/>

<!-- Live GitHub Contribution Calendar (Purple Obsidian Theme) -->
<img src="https://ghchart.rshah.org/A855F7/vn002-tech" width="100%" alt="vn002-tech Live GitHub Contribution Calendar" />

</div>

<br/><br/>

<div align="center">

<b>“Build systems that turn data into decisions.”</b><br/>
<sub>— VAN · vn002-tech</sub>

<br/><br/>

<!-- Animated Wave Footer -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0b0f17,50:2E1065,100:6D28D9&height=100&section=footer" width="100%" alt="Footer Wave" />

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
