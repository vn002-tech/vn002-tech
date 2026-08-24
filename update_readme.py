#!/usr/bin/env python3
"""
update_readme.py
Programmatic generator for vn002-tech GitHub Profile README and SVG Banner.
"""

from pathlib import Path


def generate_svg_banner() -> str:
    """Generates a clean, modern, dark-themed SVG banner for the profile."""
    return """<svg width="1200" height="300" viewBox="0 0 1200 300" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Background Gradient -->
    <linearGradient id="bg-grad" x1="0" y1="0" x2="1200" y2="300" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#0B0F17"/>
      <stop offset="60%" stop-color="#080C14"/>
      <stop offset="100%" stop-color="#05080E"/>
    </linearGradient>

    <!-- Node Glow Filter -->
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <style>
    .font-title { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    .font-mono { font-family: 'JetBrains Mono', 'Fira Code', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; }
  </style>

  <!-- Base Container -->
  <rect x="2" y="2" width="1196" height="296" rx="14" fill="url(#bg-grad)" stroke="#1E293B" stroke-width="1.5"/>

  <!-- Subtle Ambient Background Accents -->
  <circle cx="160" cy="150" r="120" fill="#7C3AED" opacity="0.04" filter="url(#glow)"/>
  <circle cx="1080" cy="60" r="90" fill="#6366F1" opacity="0.03" filter="url(#glow)"/>

  <!-- AI / ML Graph Mesh (Left Visual Accent) -->
  <g opacity="0.85" transform="translate(45, 45)">
    <!-- Connection Edges -->
    <line x1="40" y1="105" x2="105" y2="55" stroke="#334155" stroke-width="1.5" stroke-dasharray="3 3"/>
    <line x1="40" y1="105" x2="105" y2="155" stroke="#334155" stroke-width="1.5"/>
    <line x1="105" y1="55" x2="175" y2="35" stroke="#475569" stroke-width="1.5"/>
    <line x1="105" y1="55" x2="175" y2="105" stroke="#7C3AED" stroke-width="1.5" stroke-opacity="0.8"/>
    <line x1="105" y1="155" x2="175" y2="105" stroke="#7C3AED" stroke-width="1.5" stroke-opacity="0.8"/>
    <line x1="105" y1="155" x2="175" y2="175" stroke="#475569" stroke-width="1.5"/>
    <line x1="175" y1="35" x2="235" y2="75" stroke="#334155" stroke-width="1.5"/>
    <line x1="175" y1="105" x2="235" y2="75" stroke="#A855F7" stroke-width="1.8"/>
    <line x1="175" y1="105" x2="235" y2="135" stroke="#A855F7" stroke-width="1.8"/>
    <line x1="175" y1="175" x2="235" y2="135" stroke="#334155" stroke-width="1.5"/>

    <!-- Graph Nodes -->
    <circle cx="40" cy="105" r="5" fill="#1E293B" stroke="#64748B" stroke-width="2"/>
    <circle cx="105" cy="55" r="6" fill="#0F172A" stroke="#818CF8" stroke-width="2"/>
    <circle cx="105" cy="155" r="6" fill="#0F172A" stroke="#818CF8" stroke-width="2"/>
    <circle cx="175" cy="35" r="5" fill="#1E293B" stroke="#64748B" stroke-width="2"/>
    <circle cx="175" cy="105" r="9" fill="#581C87" stroke="#C084FC" stroke-width="2.5" filter="url(#glow)"/>
    <circle cx="175" cy="105" r="3" fill="#FFFFFF"/>
    <circle cx="175" cy="175" r="5" fill="#1E293B" stroke="#64748B" stroke-width="2"/>
    <circle cx="235" cy="75" r="6.5" fill="#0F172A" stroke="#A855F7" stroke-width="2"/>
    <circle cx="235" cy="135" r="6.5" fill="#0F172A" stroke="#A855F7" stroke-width="2"/>
  </g>

  <!-- Vertical Subtle Divider -->
  <line x1="330" y1="36" x2="330" y2="264" stroke="#1E293B" stroke-width="1.5"/>

  <!-- Right Content Area -->
  <!-- Top Badge: Domain / Discipline -->
  <rect x="365" y="36" width="220" height="24" rx="12" fill="#140D24" stroke="#581C87" stroke-width="1"/>
  <circle cx="379" cy="48" r="3.5" fill="#A855F7"/>
  <text x="391" y="52" fill="#D8B4FE" class="font-mono" font-size="11" font-weight="600" letter-spacing="1">AI &amp; ML SYSTEMS</text>

  <!-- Name & Identifier -->
  <text x="365" y="102" fill="#F8FAFC" class="font-title" font-size="38" font-weight="800" letter-spacing="2">VAN</text>
  <rect x="470" y="78" width="105" height="26" rx="6" fill="#1E152F" stroke="#4C1D95" stroke-width="1"/>
  <text x="522" y="95" fill="#C084FC" class="font-mono" font-size="12" font-weight="600" text-anchor="middle">vn002-tech</text>

  <!-- Primary Role & Core Specialization -->
  <text x="365" y="136" fill="#E2E8F0" class="font-title" font-size="18" font-weight="700" letter-spacing="1.5">AI ENGINEER</text>
  <text x="365" y="162" fill="#94A3B8" class="font-title" font-size="14" font-weight="400">Machine Learning · AI Application Development · Backend Systems</text>

  <!-- Tech Stack Pills -->
  <g transform="translate(365, 185)">
    <rect x="0" y="0" width="70" height="24" rx="5" fill="#0F172A" stroke="#334155" stroke-width="1"/>
    <text x="35" y="16" fill="#CBD5E1" class="font-mono" font-size="11" font-weight="500" text-anchor="middle">Python</text>

    <rect x="78" y="0" width="78" height="24" rx="5" fill="#0F172A" stroke="#334155" stroke-width="1"/>
    <text x="117" y="16" fill="#CBD5E1" class="font-mono" font-size="11" font-weight="500" text-anchor="middle">PyTorch</text>

    <rect x="164" y="0" width="102" height="24" rx="5" fill="#0F172A" stroke="#334155" stroke-width="1"/>
    <text x="215" y="16" fill="#CBD5E1" class="font-mono" font-size="11" font-weight="500" text-anchor="middle">Scikit-learn</text>

    <rect x="274" y="0" width="74" height="24" rx="5" fill="#0F172A" stroke="#334155" stroke-width="1"/>
    <text x="311" y="16" fill="#CBD5E1" class="font-mono" font-size="11" font-weight="500" text-anchor="middle">FastAPI</text>

    <rect x="356" y="0" width="94" height="24" rx="5" fill="#0F172A" stroke="#334155" stroke-width="1"/>
    <text x="403" y="16" fill="#CBD5E1" class="font-mono" font-size="11" font-weight="500" text-anchor="middle">PostgreSQL</text>

    <rect x="458" y="0" width="70" height="24" rx="5" fill="#0F172A" stroke="#334155" stroke-width="1"/>
    <text x="493" y="16" fill="#CBD5E1" class="font-mono" font-size="11" font-weight="500" text-anchor="middle">Docker</text>
  </g>

  <!-- Horizontal Separation Line -->
  <line x1="365" y1="225" x2="1140" y2="225" stroke="#1E293B" stroke-width="1"/>

  <!-- Social & Contact Badges -->
  <g transform="translate(365, 238)">
    <rect x="0" y="0" width="180" height="34" rx="6" fill="#090E17" stroke="#1E293B" stroke-width="1"/>
    <path d="M18 17C18 12.58 21.58 9 26 9C30.42 9 34 12.58 34 17C34 20.54 31.7 23.54 28.52 24.6C28.12 24.67 27.97 24.43 27.97 24.21C27.97 24.02 27.98 23.36 27.98 22.56C25.75 23.05 25.28 21.61 25.28 21.61C24.92 20.69 24.39 20.45 24.39 20.45C23.66 19.95 24.45 19.96 24.45 19.96C25.26 20.02 25.68 20.79 25.68 20.79C26.4 22.02 27.56 21.67 28.02 21.46C28.09 20.94 28.3 20.58 28.53 20.38C26.75 20.18 24.88 19.49 24.88 16.42C24.88 15.55 25.19 14.83 25.7 14.27C25.62 14.07 25.35 13.25 25.78 12.16C25.78 12.16 26.45 11.95 27.97 12.98C28.61 12.8 29.29 12.71 29.97 12.71C30.65 12.71 31.33 12.8 31.97 12.98C33.49 11.95 34.16 12.16 34.16 12.16C34.59 13.25 34.32 14.07 34.24 14.27C34.75 14.83 35.06 15.55 35.06 16.42C35.06 19.5 33.18 20.18 31.4 20.37C31.69 20.62 31.95 21.11 31.95 21.87C31.95 22.96 31.94 23.84 31.94 24.21C31.94 24.43 31.79 24.68 31.38 24.6C28.2 23.53 25.9 20.53 25.9 17H18Z" fill="#94A3B8" transform="translate(-10, -3) scale(0.9)"/>
    <text x="40" y="21" fill="#E2E8F0" class="font-mono" font-size="12" font-weight="500">vn002-tech</text>

    <rect x="192" y="0" width="130" height="34" rx="6" fill="#090E17" stroke="#1E293B" stroke-width="1"/>
    <rect x="204" y="9" width="16" height="16" rx="3" fill="#2563EB"/>
    <text x="212" y="21" fill="#FFFFFF" class="font-title" font-size="10" font-weight="800" text-anchor="middle">in</text>
    <text x="228" y="21" fill="#E2E8F0" class="font-title" font-size="12" font-weight="500">LinkedIn</text>

    <rect x="334" y="0" width="250" height="34" rx="6" fill="#090E17" stroke="#1E293B" stroke-width="1"/>
    <path d="M348 11H364C365.1 11 366 11.9 366 13V23C366 24.1 365.1 25 364 25H348C346.9 25 346 24.1 346 23V13C346 11.9 346.9 11 348 11Z" stroke="#A855F7" stroke-width="1.3" fill="none"/>
    <path d="M346 13L356 19L366 13" stroke="#A855F7" stroke-width="1.3" fill="none"/>
    <text x="374" y="21" fill="#E2E8F0" class="font-mono" font-size="11.5" font-weight="500">wahidivansaputra@gmail.com</text>
  </g>

  <!-- Decorative Corner Accents -->
  <line x1="1170" y1="20" x2="1185" y2="20" stroke="#334155" stroke-width="1"/>
  <line x1="1185" y1="20" x2="1185" y2="35" stroke="#334155" stroke-width="1"/>
</svg>"""


def generate_readme() -> str:
    """Generates the clean, technical, high-signal GitHub Profile README."""
    return """<div align="center">

<img src="./assets/ai-engineer-profile.svg" width="100%" alt="VAN — AI Engineer">

<p align="center">
  <a href="https://github.com/vn002-tech">
    <img src="https://img.shields.io/badge/GitHub-vn002--tech-0B0F17?style=flat-square&logo=github&logoColor=F8FAFC&labelColor=1E293B" alt="GitHub" />
  </a>
  <a href="https://linkedin.com">
    <img src="https://img.shields.io/badge/LinkedIn-Connect-0B0F17?style=flat-square&logo=linkedin&logoColor=38BDF8&labelColor=1E293B" alt="LinkedIn" />
  </a>
  <a href="mailto:wahidivansaputra@gmail.com">
    <img src="https://img.shields.io/badge/Email-wahidivansaputra%40gmail.com-0B0F17?style=flat-square&logo=gmail&logoColor=C084FC&labelColor=1E293B" alt="Email" />
  </a>
</p>

</div>

---

## About

I am an **AI Engineer** with a background in Informatics Engineering, focused on building reliable machine learning systems and AI-powered applications.

My engineering practice combines **machine learning, backend systems, and data engineering** to transform models from experimental notebooks into robust software architectures. I focus on feature engineering, empirical validation, performant REST APIs, and reproducible data workflows.

---

## Core Technical Focus

### Machine Learning
- **Predictive Modeling & Classification**: Developing supervised models, classification systems, and anomaly detection pipelines.
- **Feature Engineering**: Designing domain-specific transformations, data preprocessing routines, and statistical feature pipelines.
- **Model Evaluation**: In-depth empirical validation using Precision, Recall, F1-Score, ROC-AUC, and Confusion Matrices.

### AI Application Development
- **Model Integration & Serving**: Embedding machine learning models into responsive, service-oriented architectures.
- **API Development**: Designing high-throughput, low-latency RESTful APIs using FastAPI and Node.js.
- **Application Architecture**: Structuring modular backends for asynchronous inference workflows and user-facing dashboards.

### ML & Data Engineering Foundations
- **Automated ETL Pipelines**: Building resilient data ingestion and transformation pipelines with data quality assertions.
- **Relational Databases**: Data modeling, query optimization, and schema integrity with PostgreSQL, MySQL, and SQLite.
- **Reproducibility & Infrastructure**: Packaging containerized runtime environments with Docker for consistent deployments.

---

## Technology Stack

| Category | Technologies |
| :--- | :--- |
| **Languages** | Python, Go, JavaScript, SQL, Bash |
| **Machine Learning & Data** | PyTorch, Scikit-learn, XGBoost, Pandas, NumPy, Streamlit |
| **Backend & APIs** | FastAPI, Node.js, Express.js, REST APIs |
| **Databases & Storage** | PostgreSQL, MySQL, SQLite, Prisma ORM |
| **Engineering & Tools** | Docker, Git, GitHub Actions, Linux |

---

## AI Engineering Workflow

```text
┌─────────────────┐       ┌──────────────────────┐       ┌──────────────────┐
│    RAW DATA     │  ───> │ FEATURE ENGINEERING  │  ───> │  MODEL TRAINING  │
│ Ingestion & ETL │       │ Cleaning & Encoders  │       │ Baseline & Tuning│
└─────────────────┘       └──────────────────────┘       └──────────────────┘
                                                                   │
                                                                   ▼
┌─────────────────┐       ┌──────────────────────┐       ┌──────────────────┐
│ AI APPLICATION  │  <─── │   FASTAPI BACKEND    │  <─── │ MODEL EVALUATION │
│ Client & UI     │       │ Serving & Validation │       │ Metrics & Error  │
└─────────────────┘       └──────────────────────┘       └──────────────────┘
```

The engineering objective is to understand and manage the complete system lifecycle:  
**Data Integrity → Feature Pipelines → Model Validation → API Serving → Application Integration → Monitoring**

---

## Featured Projects

### [Bank Fraud Detection System](https://github.com/vn002-tech/Transaksi_bank)
> **Domain:** Machine Learning · Classification  
> **Stack:** `Python` · `XGBoost` · `Scikit-learn` · `Pandas` · `Streamlit`

* **Problem:** Detecting fraudulent financial transactions in highly imbalanced datasets while minimizing false positive disruptions.
* **Engineering Approach:** Engineered domain-specific features from transaction metadata, balanced class distributions, tuned tree-based classifiers (XGBoost/Scikit-learn), and evaluated decision thresholds using Precision-Recall trade-offs.
* **Interface:** Integrated an interactive Streamlit exploration dashboard for real-time risk assessment and score inspection.
* **Link:** [`github.com/vn002-tech/Transaksi_bank`](https://github.com/vn002-tech/Transaksi_bank)

---

### [Government Grant ETL Pipeline](https://github.com/vn002-tech/government-grant-etl)
> **Domain:** Data Engineering · ETL  
> **Stack:** `Python` · `Pandas` · `PostgreSQL` · `Docker`

* **Problem:** Ingesting, cleaning, and standardizing multi-source government grant proposal submissions for analytics and reporting.
* **Engineering Approach:** Built an end-to-end automated ETL pipeline featuring automated data ingestion, validation rules, type conversions, and structured loading into PostgreSQL.
* **Reliability:** Packaged with Docker for reproducible containerized execution and consistent schema assertions.
* **Link:** [`github.com/vn002-tech/government-grant-etl`](https://github.com/vn002-tech/government-grant-etl)

---

### [E-Klinik Management System](https://github.com/vn002-tech/E-klinik)
> **Domain:** Backend Engineering · REST API  
> **Stack:** `PHP` · `MySQL` · `REST API` · `Docker`

* **Problem:** Managing clinical operational workflows, electronic medical records, and role-sensitive access securely.
* **Engineering Approach:** Implemented a structured MVC backend architecture with Role-Based Access Control (RBAC), relational database integrity constraints, and RESTful API endpoints.
* **Deployment:** Containerized development environment using Docker to ensure environment parity.
* **Link:** [`github.com/vn002-tech/E-klinik`](https://github.com/vn002-tech/E-klinik)

---

### [Sports News API Service](https://github.com/vn002-tech)
> **Domain:** Backend Engineering  
> **Stack:** `Node.js` · `Express.js` · `Prisma ORM` · `SQLite`

* **Problem:** Providing structured content delivery and filtering for sports publications and article feeds.
* **Engineering Approach:** Developed a REST API service utilizing Express.js and Prisma ORM for type-safe database queries, relational data modeling, and predictable CRUD operations.
* **Link:** [`github.com/vn002-tech`](https://github.com/vn002-tech)

---

## Engineering Principles

- **Data Integrity First** — Model performance is strictly bounded by data quality, feature design, and pipeline reliability.
- **Evidence-Driven** — Validate model behavior through quantitative metrics, baseline comparisons, and rigorous error analysis.
- **Production Mindset** — Design beyond experimental notebooks: prioritize latency, fault tolerance, and clean API contracts.
- **Reproducibility** — Maintain deterministic transformations, versioned artifacts, and isolated runtime environments.
- **Modular Architecture** — Decouple data extraction, model inference, and backend presentation layers for long-term maintainability.

---

## GitHub Activity

<div align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=vn002-tech&show_icons=true&theme=tokyonight&hide_border=true&bg_color=0b0f17&title_color=c084fc&icon_color=a855f7&text_color=cbd5e1" height="150" alt="GitHub Stats" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=vn002-tech&layout=compact&theme=tokyonight&hide_border=true&bg_color=0b0f17&title_color=c084fc&text_color=cbd5e1" height="150" alt="Top Languages" />
</div>

---

<div align="center">
  <sub><b>VAN (vn002-tech)</b> · AI Engineer</sub><br>
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
