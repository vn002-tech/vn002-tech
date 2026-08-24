#!/usr/bin/env python3
"""
update_readme.py
Programmatic generator for vn002-tech GitHub Profile README and SVG Banner.
Redesigned for modern, visual, high-signal, and professional AI Engineer branding.
"""

from pathlib import Path


def generate_svg_banner() -> str:
    """Generates an ultra-sleek, modern dark-themed SVG banner."""
    return """<svg width="1200" height="280" viewBox="0 0 1200 280" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Background Gradient -->
    <linearGradient id="bg-grad" x1="0" y1="0" x2="1200" y2="280" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#080C14"/>
      <stop offset="50%" stop-color="#0B0F19"/>
      <stop offset="100%" stop-color="#060910"/>
    </linearGradient>

    <!-- Accent Gradient -->
    <linearGradient id="purple-grad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#C084FC"/>
      <stop offset="50%" stop-color="#A855F7"/>
      <stop offset="100%" stop-color="#6366F1"/>
    </linearGradient>

    <!-- Node Glow Filter -->
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3.5" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <style>
    .font-title { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    .font-mono { font-family: 'JetBrains Mono', 'Fira Code', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; }
  </style>

  <!-- Container Box -->
  <rect x="2" y="2" width="1196" height="276" rx="16" fill="url(#bg-grad)" stroke="#1E293B" stroke-width="1.5"/>

  <!-- Ambient Glows -->
  <circle cx="160" cy="140" r="110" fill="#7C3AED" opacity="0.05" filter="url(#glow)"/>
  <circle cx="1060" cy="80" r="100" fill="#6366F1" opacity="0.04" filter="url(#glow)"/>

  <!-- Neural Mesh / Graph Cluster (Left Side) -->
  <g opacity="0.85" transform="translate(40, 35)">
    <!-- Connections -->
    <line x1="30" y1="105" x2="95" y2="50" stroke="#334155" stroke-width="1.5" stroke-dasharray="3 3"/>
    <line x1="30" y1="105" x2="95" y2="160" stroke="#334155" stroke-width="1.5"/>
    <line x1="95" y1="50" x2="170" y2="30" stroke="#475569" stroke-width="1.5"/>
    <line x1="95" y1="50" x2="170" y2="105" stroke="#7C3AED" stroke-width="1.5" stroke-opacity="0.8"/>
    <line x1="95" y1="160" x2="170" y2="105" stroke="#7C3AED" stroke-width="1.5" stroke-opacity="0.8"/>
    <line x1="95" y1="160" x2="170" y2="180" stroke="#475569" stroke-width="1.5"/>
    <line x1="170" y1="30" x2="240" y2="70" stroke="#334155" stroke-width="1.5"/>
    <line x1="170" y1="105" x2="240" y2="70" stroke="#A855F7" stroke-width="1.8"/>
    <line x1="170" y1="105" x2="240" y2="140" stroke="#A855F7" stroke-width="1.8"/>
    <line x1="170" y1="180" x2="240" y2="140" stroke="#334155" stroke-width="1.5"/>

    <!-- Nodes -->
    <circle cx="30" cy="105" r="5" fill="#1E293B" stroke="#64748B" stroke-width="2"/>
    <circle cx="95" cy="50" r="6" fill="#0F172A" stroke="#818CF8" stroke-width="2"/>
    <circle cx="95" cy="160" r="6" fill="#0F172A" stroke="#818CF8" stroke-width="2"/>
    <circle cx="170" cy="30" r="5" fill="#1E293B" stroke="#64748B" stroke-width="2"/>
    <circle cx="170" cy="105" r="9" fill="#581C87" stroke="#C084FC" stroke-width="2.5" filter="url(#glow)"/>
    <circle cx="170" cy="105" r="3" fill="#FFFFFF"/>
    <circle cx="170" cy="180" r="5" fill="#1E293B" stroke="#64748B" stroke-width="2"/>
    <circle cx="240" cy="70" r="6.5" fill="#0F172A" stroke="#A855F7" stroke-width="2"/>
    <circle cx="240" cy="140" r="6.5" fill="#0F172A" stroke="#A855F7" stroke-width="2"/>
  </g>

  <!-- Vertical Divider -->
  <line x1="330" y1="32" x2="330" y2="248" stroke="#1E293B" stroke-width="1.5"/>

  <!-- Right Content Area -->
  <!-- Top Status Badge -->
  <rect x="360" y="32" width="220" height="24" rx="12" fill="#150E28" stroke="#581C87" stroke-width="1"/>
  <circle cx="374" cy="44" r="3.5" fill="#A855F7"/>
  <text x="386" y="48" fill="#D8B4FE" class="font-mono" font-size="11" font-weight="600" letter-spacing="1">AI &amp; ML SYSTEMS</text>

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


def generate_readme() -> str:
    """Generates the visual, modern, and professional GitHub Profile README."""
    return """<div align="center">

<img src="./assets/ai-engineer-profile.svg" width="100%" alt="VAN — AI Engineer Banner" />

<br/><br/>

<a href="https://github.com/vn002-tech"><img src="https://img.shields.io/badge/GitHub-vn002--tech-0B0F17?style=for-the-badge&logo=github&logoColor=F8FAFC" alt="GitHub" /></a>
&nbsp;
<a href="https://linkedin.com"><img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
&nbsp;
<a href="mailto:wahidivansaputra@gmail.com"><img src="https://img.shields.io/badge/Email-wahidivansaputra-7C3AED?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" /></a>

<br/><br/>

<table>
  <tr>
    <td align="center" width="33%" style="padding: 14px;">
      <b>🧠 Machine Learning</b><br/>
      <sub>Classification · Predictive Models<br/>Feature Pipelines · Empirical Validation</sub>
    </td>
    <td align="center" width="33%" style="padding: 14px;">
      <b>⚡ AI Applications</b><br/>
      <sub>Model Serving · FastAPI<br/>REST APIs · Async Workflows</sub>
    </td>
    <td align="center" width="33%" style="padding: 14px;">
      <b>⚙️ Data &amp; Systems</b><br/>
      <sub>ETL Pipelines · Data Quality<br/>PostgreSQL · Docker Architecture</sub>
    </td>
  </tr>
</table>

</div>

---

### 🚀 AI Engineering Lifecycle

```text
┌──────────────┐      ┌─────────────────────┐      ┌────────────────┐
│   RAW DATA   │ ───> │ FEATURE ENGINEERING │ ───> │ MODEL TRAINING │
│ ETL & Schema │      │ Preprocessing & PCA │      │ XGBoost / ML   │
└──────────────┘      └─────────────────────┘      └────────────────┘
                                                           │
                                                           ▼
┌──────────────┐      ┌─────────────────────┐      ┌────────────────┐
│  AI CLIENT   │ <─── │   FASTAPI BACKEND   │ <─── │   EVALUATION   │
│ UI Dashboard │      │ Inference Endpoints │      │ Metrics & Test │
└──────────────┘      └─────────────────────┘      └────────────────┘
```

> **Data Integrity → Feature Pipelines → Model Validation → API Serving → Application Integration**

---

### 🛠️ Tech Stack & Tooling

<div align="center">

<p><b>AI &amp; Machine Learning</b></p>
<img src="https://skillicons.dev/icons?i=python,pytorch,scikitlearn&theme=dark" height="38" />
&nbsp;
<img src="https://img.shields.io/badge/XGBoost-0B0F17?style=for-the-badge&logo=xgboost&logoColor=C084FC" height="38" />
<img src="https://img.shields.io/badge/Pandas-0B0F17?style=for-the-badge&logo=pandas&logoColor=C084FC" height="38" />
<img src="https://img.shields.io/badge/NumPy-0B0F17?style=for-the-badge&logo=numpy&logoColor=C084FC" height="38" />
<img src="https://img.shields.io/badge/Streamlit-0B0F17?style=for-the-badge&logo=streamlit&logoColor=C084FC" height="38" />

<br/><br/>

<p><b>Backend &amp; Data Engineering</b></p>
<img src="https://skillicons.dev/icons?i=fastapi,nodejs,express,go,postgres,mysql,sqlite,prisma&theme=dark" height="38" />

<br/><br/>

<p><b>Infrastructure &amp; Tooling</b></p>
<img src="https://skillicons.dev/icons?i=docker,git,github,githubactions,linux,bash,postman,vscode&theme=dark" height="38" />

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

### 📈 GitHub Metrics

<div align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=vn002-tech&show_icons=true&theme=tokyonight&hide_border=true&bg_color=0b0f17&title_color=c084fc&icon_color=a855f7&text_color=cbd5e1" height="150" alt="GitHub Stats" />
  &nbsp;&nbsp;
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=vn002-tech&layout=compact&theme=tokyonight&hide_border=true&bg_color=0b0f17&title_color=c084fc&text_color=cbd5e1" height="150" alt="Top Languages" />
  <br/><br/>
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=vn002-tech&bg_color=0b0f17&color=c084fc&line=a855f7&point=f5f3ff&area=true&hide_border=true" width="100%" alt="Activity Graph" />
</div>

---

<div align="center">
  <sub><b>VAN (vn002-tech)</b> · AI Engineer</sub><br/>
  <sub><i>Building reliable AI systems from data to application.</i></sub>
</div>
"""


def main():
    root = Path(__file__).resolve().parent
    assets_dir = root / "assets"
    assets_dir.mkdir(parents=True, exist_ok=True)

    # 1. Update SVG Banner
    svg_path = assets_dir / "ai-engineer-profile.svg"
    svg_path.write_text(generate_svg_banner(), encoding="utf-8")
    print(f"Generated SVG banner: {svg_path}")

    # 2. Update README.md
    readme_path = root / "README.md"
    readme_path.write_text(generate_readme(), encoding="utf-8")
    print(f"Generated README: {readme_path}")


if __name__ == "__main__":
    main()
