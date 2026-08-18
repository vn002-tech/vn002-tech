<!-- HEADER BANNER UTAMA -->
<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=0A192F&height=200&section=header&text=VN002-TECH%20%7C%20DATA%20ENGINEERING&fontSize=34&fontColor=ffffff&fontAlignY=40&animation=fadeIn" width="100%"/>
  
  <!-- TYPING EFFECT TAGLINE (FONT: JetBrains Mono) -->
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=20&pause=1000&color=38BDF8&center=true&vCenter=true&width=650&lines=Data+Engineer+%26+MLOps+Specialist;Scalable+ETL+%2F+ELT+Data+Pipelines;Big+Data+Architect+%26+Stream+Processing;Fraud+Detection+%26+Real-Time+Analytics" alt="Typing SVG" />
  </a>
</div>

<br/>

<!-- BADGES CONTACT & SOCIALS -->
<div align="center">
  <a href="https://github.com/vn002-tech"><img src="https://img.shields.io/badge/GitHub-vn002--tech-0A192F?style=for-the-badge&logo=github&logoColor=white" /></a>
  <a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
  <a href="mailto:your_email@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" /></a>
</div>

<br/>

---

<!-- SECTION 1: ABOUT ME -->
<img src="https://capsule-render.vercel.app/api?type=rect&color=0A192F&height=45&section=header&text=⚡%20pipeline_config.py%20(About%20Me)&fontSize=17&fontColor=38BDF8&fontAlignY=50&fontAlignX=4" width="100%"/>

```python
class DataEngineer:
    def __init__(self):
        self.username = "vn002-tech"
        self.role = "Data Engineer & MLOps Specialist"
        self.focus_areas = [
            "ETL/ELT Pipeline Orchestration", 
            "Fraud Detection & Anomaly Systems", 
            "Cloud Data Warehousing"
        ]
        self.current_stack = [
            "PySpark", "Apache Airflow", "dbt", 
            "PostgreSQL", "Streamlit"
        ]
        
    def get_mission(self):
        return "Building robust, scalable data pipelines to transform high-volume transactional data into actionable insights."

if __name__ == "__main__":
    engineer = DataEngineer()
    print(engineer.get_mission())
```

<br/>

<!-- SECTION 2: DATA ARCHITECTURE -->
<img src="https://capsule-render.vercel.app/api?type=rect&color=0A192F&height=45&section=header&text=🏗️%20My%20Standard%20Data%20Pipeline%20Architecture&fontSize=17&fontColor=38BDF8&fontAlignY=50&fontAlignX=4" width="100%"/>

```mermaid
graph LR
    classDef ingestion fill:#0f172a,stroke:#38bdf8,stroke-width:2px,color:#ffffff;
    classDef processing fill:#1e1b4b,stroke:#818cf8,stroke-width:2px,color:#ffffff;
    classDef storage fill:#064e3b,stroke:#34d399,stroke-width:2px,color:#ffffff;
    classDef serving fill:#451a03,stroke:#fbbf24,stroke-width:2px,color:#ffffff;

    subgraph 📥 Data Ingestion
        A[(💳 Bank Transactions)]:::ingestion
        B[(📄 Logs / APIs)]:::ingestion
    end

    subgraph ⚙️ Processing & ETL
        C[⚡ Apache Airflow]:::processing
        D[🚀 PySpark Engine]:::processing
    end

    subgraph 🗄️ Storage & Modeling
        E[(🗄️ Postgres / S3)]:::storage
        F[🔧 dbt Data Models]:::storage
    end

    subgraph 📊 Analytics & Serving
        G[📊 Streamlit Dashboard]:::serving
        H[🤖 Fraud Detection ML]:::serving
    end

    A --> C
    B --> C
    C --> D
    D --> E
    E --> F
    F --> G
    F --> H
```

<br/>

<!-- SECTION 3: TECH STACK -->
<img src="https://capsule-render.vercel.app/api?type=rect&color=0A192F&height=45&section=header&text=🛠️%20Data%20Engineering%20Tech%20Stack&fontSize=17&fontColor=38BDF8&fontAlignY=50&fontAlignX=4" width="100%"/>

<div align="center">
  <h3>Languages & Databases</h3>
  <img src="https://skillicons.dev/icons?i=python,postgres,mysql,mongodb,bash" />
  
  <h3>Big Data, ETL & Orchestration</h3>
  <img src="https://skillicons.dev/icons?i=kafka,kubernetes,git,github" />
  <p><i>Python, PySpark, Apache Airflow, dbt, Apache Kafka</i></p>

  <h3>Infrastructure & Cloud</h3>
  <img src="https://skillicons.dev/icons?i=aws,gcp,kubernetes,linux" />
</div>

<br/>

<!-- SECTION 4: FEATURED PROJECTS -->
<img src="https://capsule-render.vercel.app/api?type=rect&color=0A192F&height=45&section=header&text=🚀%20Featured%20Projects&fontSize=17&fontColor=38BDF8&fontAlignY=50&fontAlignX=4" width="100%"/>

| Project | Stack | Description |
| :--- | :--- | :--- |
| 🛡️ **[Bank Fraud Detection & Anomaly System](https://github.com/vn002-tech/Transaksi_bank)** | `Python` `Scikit-Learn` `Streamlit` `PostgreSQL` | Machine Learning pipeline & interactive dashboard for transaction fraud detection. |
| ⚡ **[Real-Time Transaction Ingestion](https://github.com/vn002-tech)** | `PySpark` `Kafka` `PostgreSQL` | High-throughput streaming data pipeline for bank transaction logs. |
| ☁️ **[Automated ETL Orchestration](https://github.com/vn002-tech)** | `Airflow` `dbt` `PostgreSQL` | End-to-end automated data transformation & data warehousing model. |

<br/>

<!-- SECTION 5: GITHUB METRICS -->
<img src="https://capsule-render.vercel.app/api?type=rect&color=0A192F&height=45&section=header&text=📈%20GitHub%20Metrics&fontSize=17&fontColor=38BDF8&fontAlignY=50&fontAlignX=4" width="100%"/>

<div align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=vn002-tech&show_icons=true&theme=tokyonight&hide_border=true&count_private=true" height="170" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=vn002-tech&layout=compact&theme=tokyonight&hide_border=true" height="170" />
</div>

<br/>

<div align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=vn002-tech&theme=tokyonight&hide_border=true" />
</div>

<br/>

<!-- FOOTER -->
<div align="center">
  <img src="https://komarev.com/ghpvc/?username=vn002-tech&color=38bdf8&style=flat-square&label=Pipeline+Visits" alt="Visitor Count" />
  <br/>
  <sub><i>"In God we trust, all others must bring data." — W. Edwards Deming</i></sub>
</div>
```
