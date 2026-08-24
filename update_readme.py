#!/usr/bin/env python3
"""
update_readme.py
Programmatic generator for vn002-tech GitHub Profile README, Animated SVG Banner,
and Animated AI Engineering Lifecycle Pipeline Diagram.
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
  <rect x="360" y="32" width="230" height="24" rx="12" fill="#150E28" stroke="#581C87" stroke-width="1"/>
  <circle cx="376" cy="44" r="3.5" fill="#A855F7"/>
  <circle cx="376" cy="44" r="3.5" fill="#C084FC" class="anim-radar"/>
  <text x="390" y="48" fill="#D8B4FE" class="font-mono" font-size="11" font-weight="600" letter-spacing="1">AI &amp; ML SYSTEMS ENGINEER</text>

  <!-- Name & Identifier -->
  <text x="360" y="94" fill="#F8FAFC" class="font-title" font-size="36" font-weight="800" letter-spacing="2">VAN</text>
  <rect x="460" y="72" width="105" height="26" rx="6" fill="#1E152F" stroke="#4C1D95" stroke-width="1"/>
  <text x="512" y="89" fill="#C084FC" class="font-mono" font-size="12" font-weight="600" text-anchor="middle">vn002-tech</text>

  <!-- Primary Role -->
  <text x="360" y="126" fill="#E2E8F0" class="font-title" font-size="17" font-weight="700" letter-spacing="1.5">AI ENGINEER</text>
  <text x="360" y="150" fill="#94A3B8" class="font-title" font-size="13.5" font-weight="400">Machine Learning · AI Application Development · Backend Systems</text>

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


def generate_pipeline_svg() -> str:
    """Generates an ultra-modern, high-tech animated SVG diagram for the AI Engineering Lifecycle."""
    return """<svg width="1000" height="260" viewBox="0 0 1000 260" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Card & BG Gradients -->
    <linearGradient id="pipe-bg" x1="0" y1="0" x2="1000" y2="260" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#080C14"/>
      <stop offset="50%" stop-color="#0B0F19"/>
      <stop offset="100%" stop-color="#060910"/>
    </linearGradient>

    <linearGradient id="card-grad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#131B2E"/>
      <stop offset="100%" stop-color="#0D1322"/>
    </linearGradient>

    <!-- Glow Filter -->
    <filter id="p-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    .font-mono { font-family: 'JetBrains Mono', 'Fira Code', ui-monospace, SFMono-Regular, Menlo, monospace; }

    @keyframes flow-h-fwd {
      0% { stroke-dashoffset: 20; }
      100% { stroke-dashoffset: 0; }
    }

    @keyframes flow-h-bwd {
      0% { stroke-dashoffset: 0; }
      100% { stroke-dashoffset: 20; }
    }

    @keyframes pulse-dot {
      0%, 100% { opacity: 0.3; transform: scale(0.9); }
      50% { opacity: 1; transform: scale(1.2); }
    }

    .anim-fwd {
      stroke-dasharray: 5 4;
      animation: flow-h-fwd 1.2s linear infinite;
    }

    .anim-bwd {
      stroke-dasharray: 5 4;
      animation: flow-h-bwd 1.2s linear infinite;
    }

    .anim-pdot {
      animation: pulse-dot 2s ease-in-out infinite;
    }
  </style>

  <!-- Container Box -->
  <rect x="2" y="2" width="996" height="256" rx="14" fill="url(#pipe-bg)" stroke="#1E293B" stroke-width="1.5"/>

  <!-- Pipeline Connectors (Background Wires) -->
  <!-- Top Row Forward Connections -->
  <line x1="285" y1="67" x2="355" y2="67" stroke="#7C3AED" stroke-width="2" class="anim-fwd"/>
  <polygon points="355,67 347,63 347,71" fill="#C084FC"/>

  <line x1="640" y1="67" x2="710" y2="67" stroke="#7C3AED" stroke-width="2" class="anim-fwd"/>
  <polygon points="710,67 702,63 702,71" fill="#C084FC"/>

  <!-- Row 1 to Row 2 Downward Connector -->
  <path d="M852 110 V140" stroke="#A855F7" stroke-width="2" class="anim-fwd"/>
  <polygon points="852,145 848,137 856,137" fill="#C084FC"/>

  <!-- Bottom Row Backward Connections -->
  <line x1="710" y1="187" x2="640" y2="187" stroke="#6366F1" stroke-width="2" class="anim-bwd"/>
  <polygon points="640,187 648,183 648,191" fill="#818CF8"/>

  <line x1="355" y1="187" x2="285" y2="187" stroke="#6366F1" stroke-width="2" class="anim-bwd"/>
  <polygon points="285,187 293,183 293,191" fill="#818CF8"/>

  <!-- ================= TOP ROW ================= -->

  <!-- STAGE 01: DATA INGESTION -->
  <g transform="translate(30, 25)">
    <rect width="255" height="85" rx="10" fill="url(#card-grad)" stroke="#334155" stroke-width="1.2"/>
    <circle cx="20" cy="22" r="4" fill="#38BDF8" class="anim-pdot"/>
    <text x="32" y="26" fill="#38BDF8" class="font-mono" font-size="11" font-weight="700" letter-spacing="1">01. DATA INGESTION</text>
    <text x="20" y="50" fill="#F8FAFC" class="font-sans" font-size="13" font-weight="600">ETL &amp; Schema Integrity</text>
    <text x="20" y="70" fill="#94A3B8" class="font-sans" font-size="11">Validation Rules · PostgreSQL</text>
  </g>

  <!-- STAGE 02: FEATURE PIPELINE -->
  <g transform="translate(385, 25)">
    <rect width="255" height="85" rx="10" fill="url(#card-grad)" stroke="#7C3AED" stroke-width="1.2"/>
    <circle cx="20" cy="22" r="4" fill="#C084FC" class="anim-pdot"/>
    <text x="32" y="26" fill="#C084FC" class="font-mono" font-size="11" font-weight="700" letter-spacing="1">02. FEATURE PIPELINE</text>
    <text x="20" y="50" fill="#F8FAFC" class="font-sans" font-size="13" font-weight="600">Transforms &amp; Encoders</text>
    <text x="20" y="70" fill="#94A3B8" class="font-sans" font-size="11">Scikit-learn · Pandas · NumPy</text>
  </g>

  <!-- STAGE 03: MODEL TRAINING -->
  <g transform="translate(740, 25)">
    <rect width="230" height="85" rx="10" fill="url(#card-grad)" stroke="#A855F7" stroke-width="1.2"/>
    <circle cx="20" cy="22" r="4" fill="#A855F7" class="anim-pdot"/>
    <text x="32" y="26" fill="#A855F7" class="font-mono" font-size="11" font-weight="700" letter-spacing="1">03. MODEL TRAINING</text>
    <text x="20" y="50" fill="#F8FAFC" class="font-sans" font-size="13" font-weight="600">XGBoost &amp; PyTorch</text>
    <text x="20" y="70" fill="#94A3B8" class="font-sans" font-size="11">Supervised &amp; Hyperparam Tuning</text>
  </g>

  <!-- ================= BOTTOM ROW ================= -->

  <!-- STAGE 04: EVALUATION -->
  <g transform="translate(740, 145)">
    <rect width="230" height="85" rx="10" fill="url(#card-grad)" stroke="#6366F1" stroke-width="1.2"/>
    <circle cx="20" cy="22" r="4" fill="#818CF8" class="anim-pdot"/>
    <text x="32" y="26" fill="#818CF8" class="font-mono" font-size="11" font-weight="700" letter-spacing="1">04. EVALUATION</text>
    <text x="20" y="50" fill="#F8FAFC" class="font-sans" font-size="13" font-weight="600">Empirical Metrics &amp; Tests</text>
    <text x="20" y="70" fill="#94A3B8" class="font-sans" font-size="11">Precision · Recall · ROC-AUC</text>
  </g>

  <!-- STAGE 05: FASTAPI SERVING -->
  <g transform="translate(385, 145)">
    <rect width="255" height="85" rx="10" fill="url(#card-grad)" stroke="#10B981" stroke-width="1.2"/>
    <circle cx="20" cy="22" r="4" fill="#34D399" class="anim-pdot"/>
    <text x="32" y="26" fill="#34D399" class="font-mono" font-size="11" font-weight="700" letter-spacing="1">05. FASTAPI SERVING</text>
    <text x="20" y="50" fill="#F8FAFC" class="font-sans" font-size="13" font-weight="600">Inference Endpoints</text>
    <text x="20" y="70" fill="#94A3B8" class="font-sans" font-size="11">Low-Latency Async · Docker</text>
  </g>

  <!-- STAGE 06: AI APPLICATION -->
  <g transform="translate(30, 145)">
    <rect width="255" height="85" rx="10" fill="url(#card-grad)" stroke="#F59E0B" stroke-width="1.2"/>
    <circle cx="20" cy="22" r="4" fill="#FBBF24" class="anim-pdot"/>
    <text x="32" y="26" fill="#FBBF24" class="font-mono" font-size="11" font-weight="700" letter-spacing="1">06. AI APPLICATION</text>
    <text x="20" y="50" fill="#F8FAFC" class="font-sans" font-size="13" font-weight="600">Streamlit &amp; UI Client</text>
    <text x="20" y="70" fill="#94A3B8" class="font-sans" font-size="11">Real-Time Risk Scoring &amp; Viz</text>
  </g>
</svg>"""


def generate_readme() -> str:
    """Generates the visual, modern, and animated GitHub Profile README."""
    return """<div align="center">

<img src="./assets/ai-engineer-profile.svg" width="100%" alt="VAN — AI Engineer Banner" />

<br/><br/>

<!-- Animated Typing SVG -->
<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=20&pause=1200&color=C084FC&center=true&vCenter=true&width=760&lines=%E2%9A%A1+AI+Engineer+%7C+Machine+Learning+%26+Systems;%F0%9F%A7%A0+Building+Practical+AI+Applications;%F0%9F%9B%A0%EF%B8%8F+Python+%7C+PyTorch+%7C+Scikit-learn+%7C+FastAPI;%F0%9F%93%8A+From+Data+Pipelines+to+Production+Model+Serving" alt="Typing SVG" />
</a>

<br/><br/>

<!-- Action & Contact Badges -->
<a href="https://github.com/vn002-tech"><img src="https://img.shields.io/badge/GitHub-vn002--tech-0B0F17?style=for-the-badge&logo=github&logoColor=F8FAFC" alt="GitHub" /></a>
&nbsp;
<a href="https://linkedin.com"><img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
&nbsp;
<a href="mailto:wahidivansaputra@gmail.com"><img src="https://img.shields.io/badge/Email-wahidivansaputra-7C3AED?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" /></a>

<br/><br/>

<!-- Core Domains Table Card -->
<table width="100%">
  <thead>
    <tr>
      <th width="33%" align="center">🧠 Machine Learning</th>
      <th width="33%" align="center">⚡ AI Applications</th>
      <th width="33%" align="center">⚙️ Data &amp; Systems</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center" style="padding: 12px 16px;">
        <b>Classification &amp; Predictive Models</b><br/>
        <sub>Feature Engineering · Evaluation &amp; Metrics</sub>
      </td>
      <td align="center" style="padding: 12px 16px;">
        <b>Model Serving &amp; Inference APIs</b><br/>
        <sub>FastAPI · Async Pipelines · Streamlit UI</sub>
      </td>
      <td align="center" style="padding: 12px 16px;">
        <b>ETL Pipelines &amp; Data Quality</b><br/>
        <sub>PostgreSQL · Docker Architecture</sub>
      </td>
    </tr>
  </tbody>
</table>

</div>

---

### 🚀 AI Engineering Lifecycle

<div align="center">

<img src="./assets/ai-engineering-pipeline.svg" width="100%" alt="AI Engineering Pipeline Architecture" />

<br/><br/>

> **Data Integrity → Feature Engineering → Model Validation → API Serving → Application Integration**

</div>

---

### 🛠️ AI Engineering Stack & Tooling

<div align="center">

<p><b>🧠 Machine Learning &amp; Deep Learning</b></p>
<img src="https://skillicons.dev/icons?i=python,pytorch,scikitlearn&theme=dark" height="40" />
&nbsp;
<img src="https://img.shields.io/badge/XGBoost-0B0F17?style=for-the-badge&logo=xgboost&logoColor=C084FC" height="40" />
<img src="https://img.shields.io/badge/Pandas-0B0F17?style=for-the-badge&logo=pandas&logoColor=C084FC" height="40" />
<img src="https://img.shields.io/badge/NumPy-0B0F17?style=for-the-badge&logo=numpy&logoColor=C084FC" height="40" />

<br/><br/>

<p><b>⚡ Model Serving &amp; AI Application Architecture</b></p>
<img src="https://skillicons.dev/icons?i=fastapi,postman&theme=dark" height="40" />
&nbsp;
<img src="https://img.shields.io/badge/Streamlit-0B0F17?style=for-the-badge&logo=streamlit&logoColor=C084FC" height="40" />
<img src="https://img.shields.io/badge/REST_API-0B0F17?style=for-the-badge&logo=fastapi&logoColor=A855F7" height="40" />

<br/><br/>

<p><b>📊 Data Pipelines &amp; Storage</b></p>
<img src="https://skillicons.dev/icons?i=postgres,mysql,sqlite,prisma&theme=dark" height="40" />

<br/><br/>

<p><b>⚙️ MLOps, Containerization &amp; Infrastructure</b></p>
<img src="https://skillicons.dev/icons?i=docker,git,githubactions,linux,bash&theme=dark" height="40" />

</div>

---

### 📁 Featured Projects

<table>
<tr>
<td width="50%" valign="top">

### 🛡️ [Bank Fraud Detection](https://github.com/vn002-tech/Transaksi_bank)
`ML / Classification` &nbsp; `Python` `XGBoost` `Streamlit`

* Real-time banking fraud classification system for imbalanced data.
* Custom feature transformations & precision-recall threshold optimization.
* Interactive Streamlit dashboard for real-time risk scoring and inspection.

<br/>

[**Explore Repository →**](https://github.com/vn002-tech/Transaksi_bank)

</td>
<td width="50%" valign="top">

### 📊 [Government Grant ETL](https://github.com/vn002-tech/government-grant-etl)
`Data Engineering` &nbsp; `Python` `Pandas` `PostgreSQL` `Docker`

* Automated end-to-end data pipeline processing multi-source grant data.
* Structured data cleaning, validation assertions, and relational loading.
* Dockerized execution environment ensuring reproducible data workflows.

<br/>

[**Explore Repository →**](https://github.com/vn002-tech/government-grant-etl)

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🏥 [E-Klinik Management](https://github.com/vn002-tech/E-klinik)
`Backend / API` &nbsp; `PHP` `MySQL` `REST API` `Docker`

* Clinic management system featuring Role-Based Access Control (RBAC).
* Modular MVC backend with strict relational data integrity.
* Containerized development & deployment with Docker.

<br/>

[**Explore Repository →**](https://github.com/vn002-tech/E-klinik)

</td>
<td width="50%" valign="top">

### ⚽ [Sports News API](https://github.com/vn002-tech)
`Backend Systems` &nbsp; `Node.js` `Express` `Prisma` `SQLite`

* High-performance RESTful API service for sports publication delivery.
* Type-safe database queries and relational modeling via Prisma ORM.
* Structured CRUD endpoints designed for low-latency client consumption.

<br/>

[**View GitHub Profile →**](https://github.com/vn002-tech)

</td>
</tr>
</table>

---

### 📈 GitHub Analytics & Activity

<div align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=vn002-tech&show_icons=true&theme=tokyonight&hide_border=true&bg_color=0b0f17&title_color=c084fc&icon_color=a855f7&text_color=cbd5e1" height="150" alt="GitHub Stats" />
  &nbsp;&nbsp;
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=vn002-tech&layout=compact&theme=tokyonight&hide_border=true&bg_color=0b0f17&title_color=c084fc&text_color=cbd5e1" height="150" alt="Top Languages" />
  <br/><br/>
  <!-- Animated Live Streak & Activity -->
  <img src="https://streak-stats.demolab.com?user=vn002-tech&hide_border=true&background=0b0f17&ring=A855F7&fire=C084FC&currStreakLabel=C084FC&sideLabels=CBD5E1&currStreakNum=FFFFFF&sideNums=FFFFFF&dates=64748B" width="95%" alt="Streak Stats" />
  <br/><br/>
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=vn002-tech&bg_color=0b0f17&color=c084fc&line=a855f7&point=f5f3ff&area=true&hide_border=true" width="95%" alt="Activity Graph" />
</div>

<br/>

<div align="center">

<img src="https://raw.githubusercontent.com/nixin72/nixin72/master/assets/developer.gif" width="220" alt="Developer coding animation" />

<br/><br/>

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

    # 2. Update AI Engineering Pipeline SVG
    pipeline_svg_path = assets_dir / "ai-engineering-pipeline.svg"
    pipeline_svg_path.write_text(generate_pipeline_svg(), encoding="utf-8")
    print(f"Generated AI Engineering pipeline SVG: {pipeline_svg_path}")

    # 3. Update README.md
    readme_path = root / "README.md"
    readme_path.write_text(generate_readme(), encoding="utf-8")
    print(f"Generated README: {readme_path}")


if __name__ == "__main__":
    main()
