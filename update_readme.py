#!/usr/bin/env python3
"""
update_readme.py
Programmatic generator for vn002-tech GitHub Profile README, Animated SVG Banner,
AI Engineering Pillars Card SVG, AI Architecture Diagram SVG, and Cyber Telemetry Speedway Track SVG.
"""

from pathlib import Path


def generate_svg_banner() -> str:
    """Generates an animated, ultra-sleek dark-themed SVG banner with CSS keyframes."""
    return """<svg width="1200" height="280" viewBox="0 0 1200 280" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Background Gradient -->
    <linearGradient id="bg-grad" x1="0" y1="0" x2="1200" y2="280" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#080C14"/>
      <stop offset="50%" stop-color="#0B0F19"/>
      <stop offset="100%" stop-color="#060910"/>
    </linearGradient>

    <!-- Purple Gradient -->
    <linearGradient id="purple-grad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#C084FC"/>
      <stop offset="50%" stop-color="#A855F7"/>
      <stop offset="100%" stop-color="#6366F1"/>
    </linearGradient>

    <!-- Node Glow Filter -->
    <filter id="glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="4" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <style>
    .font-title { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    .font-mono { font-family: 'JetBrains Mono', 'Fira Code', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; }

    /* Keyframe Animations */
    @keyframes pulse-core {
      0%, 100% { transform: scale(1); opacity: 0.85; filter: drop-shadow(0 0 4px #A855F7); }
      50% { transform: scale(1.15); opacity: 1; filter: drop-shadow(0 0 10px #C084FC); }
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
      0%, 100% { stroke-opacity: 0.3; }
      50% { stroke-opacity: 0.9; }
    }

    .anim-pulse {
      transform-origin: 170px 105px;
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

  <!-- Container Box -->
  <rect x="2" y="2" width="1196" height="276" rx="16" fill="url(#bg-grad)" stroke="#1E293B" stroke-width="1.5"/>

  <!-- Ambient Glows -->
  <circle cx="160" cy="140" r="110" fill="#7C3AED" opacity="0.06" filter="url(#glow)"/>
  <circle cx="1060" cy="80" r="100" fill="#6366F1" opacity="0.04" filter="url(#glow)"/>

  <!-- Neural Mesh / Graph Cluster (Left Side) -->
  <g opacity="0.9" transform="translate(40, 35)">
    <!-- Connections -->
    <line x1="30" y1="105" x2="95" y2="50" stroke="#334155" stroke-width="1.5" class="anim-flow"/>
    <line x1="30" y1="105" x2="95" y2="160" stroke="#334155" stroke-width="1.5"/>
    <line x1="95" y1="50" x2="170" y2="30" stroke="#475569" stroke-width="1.5"/>
    <line x1="95" y1="50" x2="170" y2="105" stroke="#7C3AED" stroke-width="1.8" class="anim-glow"/>
    <line x1="95" y1="160" x2="170" y2="105" stroke="#7C3AED" stroke-width="1.8" class="anim-glow"/>
    <line x1="95" y1="160" x2="170" y2="180" stroke="#475569" stroke-width="1.5"/>
    <line x1="170" y1="30" x2="240" y2="70" stroke="#334155" stroke-width="1.5"/>
    <line x1="170" y1="105" x2="240" y2="70" stroke="#A855F7" stroke-width="1.8" class="anim-flow"/>
    <line x1="170" y1="105" x2="240" y2="140" stroke="#A855F7" stroke-width="1.8" class="anim-flow"/>
    <line x1="170" y1="180" x2="240" y2="140" stroke="#334155" stroke-width="1.5"/>

    <!-- Nodes -->
    <circle cx="30" cy="105" r="5" fill="#1E293B" stroke="#64748B" stroke-width="2"/>
    <circle cx="95" cy="50" r="6" fill="#0F172A" stroke="#818CF8" stroke-width="2"/>
    <circle cx="95" cy="160" r="6" fill="#0F172A" stroke="#818CF8" stroke-width="2"/>
    <circle cx="170" cy="30" r="5" fill="#1E293B" stroke="#64748B" stroke-width="2"/>
    
    <!-- Central Pulsing Core Node -->
    <circle cx="170" cy="105" r="10" fill="#581C87" stroke="#C084FC" stroke-width="2.5" class="anim-pulse" filter="url(#glow)"/>
    <circle cx="170" cy="105" r="3.5" fill="#FFFFFF"/>
    
    <circle cx="170" cy="180" r="5" fill="#1E293B" stroke="#64748B" stroke-width="2"/>
    <circle cx="240" cy="70" r="6.5" fill="#0F172A" stroke="#A855F7" stroke-width="2"/>
    <circle cx="240" cy="140" r="6.5" fill="#0F172A" stroke="#A855F7" stroke-width="2"/>
  </g>

  <!-- Vertical Divider -->
  <line x1="330" y1="32" x2="330" y2="248" stroke="#1E293B" stroke-width="1.5"/>

  <!-- Right Content Area -->
  <!-- Top Status Badge with Radar Ping -->
  <rect x="360" y="32" width="260" height="24" rx="12" fill="#150E28" stroke="#581C87" stroke-width="1"/>
  <circle cx="376" cy="44" r="3.5" fill="#A855F7"/>
  <circle cx="376" cy="44" r="3.5" fill="#C084FC" class="anim-radar"/>
  <text x="390" y="48" fill="#D8B4FE" class="font-mono" font-size="10.5" font-weight="600" letter-spacing="1">AI ENGINEERING &amp; DATA SCIENCE</text>

  <!-- Name & Identifier -->
  <text x="360" y="94" fill="#F8FAFC" class="font-title" font-size="36" font-weight="800" letter-spacing="2">VAN</text>
  <rect x="460" y="72" width="105" height="26" rx="6" fill="#1E152F" stroke="#4C1D95" stroke-width="1"/>
  <text x="512" y="89" fill="#C084FC" class="font-mono" font-size="12" font-weight="600" text-anchor="middle">vn002-tech</text>

  <!-- Primary Role -->
  <text x="360" y="126" fill="#E2E8F0" class="font-title" font-size="17" font-weight="700" letter-spacing="1.5">AI ENGINEER</text>
  <text x="360" y="150" fill="#94A3B8" class="font-title" font-size="13.5" font-weight="400">AI Engineering · Machine Learning &amp; Data Science · LLMs &amp; Automation</text>

  <!-- Tech Stack Pills -->
  <g transform="translate(360, 170)">
    <rect x="0" y="0" width="68" height="24" rx="5" fill="#0F172A" stroke="#334155" stroke-width="1"/>
    <text x="34" y="16" fill="#CBD5E1" class="font-mono" font-size="11" font-weight="500" text-anchor="middle">Python</text>

    <rect x="76" y="0" width="76" height="24" rx="5" fill="#0F172A" stroke="#334155" stroke-width="1"/>
    <text x="114" y="16" fill="#CBD5E1" class="font-mono" font-size="11" font-weight="500" text-anchor="middle">PyTorch</text>

    <rect x="160" y="0" width="98" height="24" rx="5" fill="#0F172A" stroke="#334155" stroke-width="1"/>
    <text x="209" y="16" fill="#CBD5E1" class="font-mono" font-size="11" font-weight="500" text-anchor="middle">Scikit-learn</text>

    <rect x="266" y="0" width="72" height="24" rx="5" fill="#0F172A" stroke="#334155" stroke-width="1"/>
    <text x="302" y="16" fill="#CBD5E1" class="font-mono" font-size="11" font-weight="500" text-anchor="middle">FastAPI</text>

    <rect x="346" y="0" width="92" height="24" rx="5" fill="#0F172A" stroke="#334155" stroke-width="1"/>
    <text x="392" y="16" fill="#CBD5E1" class="font-mono" font-size="11" font-weight="500" text-anchor="middle">PostgreSQL</text>

    <rect x="446" y="0" width="68" height="24" rx="5" fill="#0F172A" stroke="#334155" stroke-width="1"/>
    <text x="480" y="16" fill="#CBD5E1" class="font-mono" font-size="11" font-weight="500" text-anchor="middle">Docker</text>
  </g>

  <!-- Horizontal Divider -->
  <line x1="360" y1="208" x2="1140" y2="208" stroke="#1E293B" stroke-width="1"/>

  <!-- Social & Contact Badges -->
  <g transform="translate(360, 220)">
    <rect x="0" y="0" width="165" height="32" rx="6" fill="#090E17" stroke="#1E293B" stroke-width="1"/>
    <path d="M18 17C18 12.58 21.58 9 26 9C30.42 9 34 12.58 34 17C34 20.54 31.7 23.54 28.52 24.6C28.12 24.67 27.97 24.43 27.97 24.21C27.97 24.02 27.98 23.36 27.98 22.56C25.75 23.05 25.28 21.61 25.28 21.61C24.92 20.69 24.39 20.45 24.39 20.45C23.66 19.95 24.45 19.96 24.45 19.96C25.26 20.02 25.68 20.79 25.68 20.79C26.4 22.02 27.56 21.67 28.02 21.46C28.09 20.94 28.3 20.58 28.53 20.38C26.75 20.18 24.88 19.49 24.88 16.42C24.88 15.55 25.19 14.83 25.7 14.27C25.62 14.07 25.35 13.25 25.78 12.16C25.78 12.16 26.45 11.95 27.97 12.98C28.61 12.8 29.29 12.71 29.97 12.71C30.65 12.71 31.33 12.8 31.97 12.98C33.49 11.95 34.16 12.16 34.16 12.16C34.59 13.25 34.32 14.07 34.24 14.27C34.75 14.83 35.06 15.55 35.06 16.42C35.06 19.5 33.18 20.18 31.4 20.37C31.69 20.62 31.95 21.11 31.95 21.87C31.95 22.96 31.94 23.84 31.94 24.21C31.94 24.43 31.79 24.68 31.38 24.6C28.2 23.53 25.9 20.53 25.9 17H18Z" fill="#94A3B8" transform="translate(-10, -4) scale(0.85)"/>
    <text x="36" y="20" fill="#E2E8F0" class="font-mono" font-size="11.5" font-weight="500">vn002-tech</text>

    <rect x="175" y="0" width="125" height="32" rx="6" fill="#090E17" stroke="#1E293B" stroke-width="1"/>
    <rect x="187" y="8" width="15" height="15" rx="3" fill="#2563EB"/>
    <text x="194.5" y="19" fill="#FFFFFF" class="font-title" font-size="9.5" font-weight="800" text-anchor="middle">in</text>
    <text x="210" y="20" fill="#E2E8F0" class="font-title" font-size="11.5" font-weight="500">LinkedIn</text>

    <rect x="310" y="0" width="240" height="32" rx="6" fill="#090E17" stroke="#1E293B" stroke-width="1"/>
    <path d="M323 10H337C338 10 339 10.8 339 11.8V20.2C339 21.2 338 22 337 22H323C322 22 321 21.2 321 20.2V11.8C321 10.8 322 10 323 10Z" stroke="#A855F7" stroke-width="1.2" fill="none"/>
    <path d="M321 12L330 17L339 12" stroke="#A855F7" stroke-width="1.2" fill="none"/>
    <text x="347" y="20" fill="#E2E8F0" class="font-mono" font-size="11" font-weight="500">wahidivansaputra@gmail.com</text>
  </g>
</svg>"""


def generate_pillars_svg() -> str:
    """
    Generates an ultra-sleek, animated 4-Card Vector Matrix SVG for:
    ML & Data Science | Deep Learning | LLMs & Automation | MLOps & Systems.
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
    <text x="28" y="24" fill="#93C5FD" class="font-mono" font-size="10.5" font-weight="700" letter-spacing="0.5">🧠 ML &amp; DATA SCIENCE</text>
    <text x="16" y="49" fill="#F8FAFC" class="font-sans" font-size="13" font-weight="700">Predictive &amp; Analytics</text>
    <text x="16" y="73" fill="#94A3B8" class="font-sans" font-size="11">Feature Pipelines · XGBoost</text>
    <text x="16" y="93" fill="#64748B" class="font-sans" font-size="10.5">Statistical EDA &amp; Metrics</text>
  </g>

  <!-- ================= CARD 2: DEEP LEARNING ================= -->
  <g transform="translate(260, 14)">
    <rect width="230" height="120" rx="10" fill="url(#pil-card-grad)" stroke="#7C3AED" stroke-width="1.2" stroke-opacity="0.8"/>
    <circle cx="18" cy="20" r="4" fill="#A855F7" class="anim-pulse"/>
    <text x="28" y="24" fill="#C084FC" class="font-mono" font-size="10.5" font-weight="700" letter-spacing="0.5">⚡ DEEP LEARNING</text>
    <text x="16" y="49" fill="#F8FAFC" class="font-sans" font-size="13" font-weight="700">Neural Systems</text>
    <text x="16" y="73" fill="#94A3B8" class="font-sans" font-size="11">PyTorch · Tensors</text>
    <text x="16" y="93" fill="#64748B" class="font-sans" font-size="10.5">Dense Embeddings</text>
  </g>

  <!-- ================= CARD 3: LLMs & AUTOMATION (FOCAL) ================= -->
  <g transform="translate(504, 14)">
    <rect width="230" height="120" rx="10" fill="url(#pil-llm-grad)" stroke="#C084FC" stroke-width="1.4" filter="url(#pil-glow)"/>
    <circle cx="18" cy="20" r="4" fill="#E879F9"/>
    <circle cx="18" cy="20" r="4" fill="#C084FC" class="anim-radar"/>
    <text x="28" y="24" fill="#F0ABFC" class="font-mono" font-size="10.5" font-weight="700" letter-spacing="0.5">🤖 LLMs &amp; AUTOMATION</text>
    <text x="16" y="49" fill="#FFFFFF" class="font-sans" font-size="13" font-weight="700">AI Automation</text>
    <text x="16" y="73" fill="#E9D5FF" class="font-sans" font-size="11">RAG Pipelines · Vector DBs</text>
    <text x="16" y="93" fill="#D8B4FE" class="font-sans" font-size="10.5">Autonomous Workflows</text>
  </g>

  <!-- ================= CARD 4: MLOPS & SYSTEMS ================= -->
  <g transform="translate(748, 14)">
    <rect width="236" height="120" rx="10" fill="url(#pil-card-grad)" stroke="#10B981" stroke-width="1.2" stroke-opacity="0.8"/>
    <circle cx="18" cy="20" r="4" fill="#34D399" class="anim-pulse"/>
    <text x="28" y="24" fill="#6EE7B7" class="font-mono" font-size="10.5" font-weight="700" letter-spacing="0.5">⚙️ MLOps &amp; SYSTEMS</text>
    <text x="16" y="49" fill="#F8FAFC" class="font-sans" font-size="13" font-weight="700">Serving &amp; Production</text>
    <text x="16" y="73" fill="#94A3B8" class="font-sans" font-size="11">FastAPI · Docker Runtime</text>
    <text x="16" y="93" fill="#64748B" class="font-sans" font-size="10.5">ETL &amp; Data Integrity</text>
  </g>
</svg>"""


def generate_pipeline_svg() -> str:
    """
    Generates an animated, ultra-modern Multi-Tier AI Architecture SVG Diagram:
    Data Foundation -> ML & Data Science -> Deep Learning -> LLM & Automation -> Serving.
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
    Generates an animated Cyber Speedway Track SVG where a futuristic Cyber Sports Car
    races continuously along an AI inference telemetry waveform track.
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

  <!-- HUD Header -->
  <text x="40" y="32" fill="#38BDF8" class="font-mono" font-size="11" font-weight="700" letter-spacing="1.5">🏎️ TELEMETRY CIRCUIT // INFERENCE ACCELERATION TRACK</text>
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
    <!-- Clean Futuristic LED Tail Lights (No flame) -->
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
    """Generates the comprehensive, visual, modern, and animated GitHub Profile README."""
    return """<div align="center">

<img src="./assets/ai-engineer-profile.svg" width="100%" alt="VAN — AI Engineer Banner" />

<br/><br/>

<!-- Animated Typing SVG -->
<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=20&pause=1200&color=C084FC&center=true&vCenter=true&width=760&lines=%E2%9A%A1+AI+Engineering+%7C+Machine+Learning+%26+Data+Science;%F0%9F%A7%A0+LLMs+%C2%B7+RAG+%C2%B7+Deep+Learning+%26+AI+Automation;%F0%9F%9B%A0%EF%B8%8F+Python+%7C+PyTorch+%7C+Scikit-learn+%7C+FastAPI+%7C+Docker;%F0%9F%93%8A+From+Data+Pipelines+to+Production-Ready+AI+Systems" alt="Typing SVG" />
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
<img src="./assets/ai-pillars.svg" width="100%" alt="4-Pillar Core AI Engineering Domains" />

</div>

---

### 🌐 End-to-End AI Engineering Architecture

<div align="center">

<img src="./assets/ai-engineering-pipeline.svg" width="100%" alt="AI Engineering Architecture Diagram" />

<br/><br/>

> **Data Foundation → Feature &amp; Embedding Engine → [ML &amp; Data Science · Deep Learning · LLM &amp; Automation] → FastAPI Serving → Autonomous Client**

</div>

---

### 🏎️ Telemetry Velocity &amp; Real-Time System Activity

<div align="center">

<!-- Cyber Speedster Racing Across Telemetry Waveform Track -->
<img src="./assets/ai-telemetry-track.svg" width="100%" alt="AI Inference Velocity Track with Cyber Car" />

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
