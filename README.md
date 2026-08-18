<!-- HEADER BANNER UTAMA -->
<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,50:203a43,100:2c5364&height=220&section=header&text=VN002-TECH%20%7C%20DATA%20ENGINEERING&fontSize=34&fontColor=ffffff&fontAlignY=36&animation=fadeIn" width="100%"/>
  
  <!-- TYPING EFFECT TAGLINE -->
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&pause=1000&color=38BDF8&center=true&vCenter=true&width=650&lines=Data+Engineer+%26+MLOps+Specialist;Scalable+ETL+%2F+ELT+Data+Pipelines;Big+Data+Architect+%26+Stream+Processing;Fraud+Detection+%26+Real-Time+Analytics" alt="Typing SVG" />
  </a>
</div>

<br/>

<!-- BADGES CONTACT & SOCIALS -->
<div align="center">
  <a href="https://github.com/vn002-tech"><img src="https://img.shields.io/badge/GitHub-vn002--tech-181717?style=for-the-badge&logo=github&logoColor=white" /></a>
  <a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
  <a href="mailto:your_email@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" /></a>
</div>

<br/>

---

<!-- ABOUT ME IN DATA PIPELINE / PYTHON STYLE -->
<img src="https://capsule-render.vercel.app/api?type=rounded&color=0:0f2027,50:203a43,100:38bdf8&height=50&section=header&text=⚡%20pipeline_config.py%20(About%20Me)&fontSize=18&fontColor=ffffff&fontAlignY=50&fontAlignX=5" width="100%"/>

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
            "PostgreSQL", "Docker", "Streamlit"
        ]
        
    def get_mission(self):
        return "Building robust, scalable data pipelines to transform high-volume transactional data into actionable insights."

if __name__ == "__main__":
    engineer = DataEngineer()
    print(engineer.get_mission())
```

<br/>

<!-- DATA ARCHITECTURE FLOW (MERMAID DIAGRAM) -->
<img src="https://capsule-render.vercel.app/api?type=rounded&color=0:0f2027,50:203a43,100:38bdf8&height=50&section=header&text=🏗️%20My%20Standard%20Data%20Pipeline%20Architecture&fontSize=18&fontColor=ffffff&fontAlignY=50&fontAlignX=5" width="100%"/>

```mermaid
flowchart LR
    subgraph Ingestion["📥 Data Ingestion"]
        A[(Bank Transactions)] 
        B[API / Webhooks]
        C[CSV / Parquet Logs]
    end

    subgraph Processing["⚙️ Orchestration & Processing"]
        D[Apache Kafka] --> E[PySpark Batch / Stream]
        A --> F[Apache Airflow]
        B --> F
        C --> F
        F --> E
    end

    subgraph Storage["🗄️ Storage & Transformation"]
        E --> G[(Feature Store / Postgres)]
        G --> H[dbt Data Modeling]
    end

    subgraph Serving["📊 Analytics & ML Serving"]
        H --> I[Streamlit Fraud Dashboard]
        H --> J[Anomaly Detection Model]
    end

    style Ingestion fill:#1e293b,stroke:#38bdf8,color:#fff
    style Processing fill:#0f172a,stroke:#818cf8,color:#fff
    style Storage fill:#1e293b,stroke:#34d399,color:#fff
    style Serving fill:#0f172a,stroke:#fbbf24,color:#fff
```

<br/>

<!-- TECH STACK -->
<img src="https://capsule-render.vercel.app/api?type=rounded&color=0:0f2027,50:203a43,100:38bdf8&height=50&section=header&text=🛠️%20Data%20Engineering%20Tech%20Stack&fontSize=18&fontColor=ffffff&fontAlignY=50&fontAlignX=5" width="100%"/>

<div align="center">
  <h3>Languages & Databases</h3>
  <img src="https://skillicons.dev/icons?i=python,postgres,mysql,mongodb,bash" />
  
  <h3>Big Data, ETL & Orchestration</h3>
  <img src="https://skillicons.dev/icons?i=kafka,docker,kubernetes,git,github" />
  <p><i>Python, PySpark, Apache Airflow, dbt, Apache Kafka</i></p>

  <h3>Infrastructure, DevOps & Cloud</h3>
  <img src="https://skillicons.dev/icons?i=aws,gcp,docker,kubernetes,linux" />
</div>

<br/>

<!-- FEATURED PROJECTS -->
<img src="https://capsule-render.vercel.app/api?type=rounded&color=0:0f2027,50:203a43,100:38bdf8&height=50&section=header&text=🚀%20Featured%20Projects&fontSize=18&fontColor=ffffff&fontAlignY=50&fontAlignX=5" width="100%"/>

| Project | Stack | Description |
| :--- | :--- | :--- |
| 🛡️ **[Bank Fraud Detection & Anomaly System](https://github.com/vn002-tech/Transaksi_bank)** | `Python` `Scikit-Learn` `Streamlit` `PostgreSQL` | Machine Learning pipeline & interactive dashboard for transaction fraud detection. |
| ⚡ **[Real-Time Transaction Ingestion](https://github.com/vn002-tech)** | `PySpark` `Kafka` `Docker` | High-throughput streaming data pipeline for bank transaction logs. |
| ☁️ **[Automated ETL Orchestration](https://github.com/vn002-tech)** | `Airflow` `dbt` `PostgreSQL` | End-to-end automated data transformation & data warehousing model. |

<br/>

<!-- GITHUB STATS CARDS -->
<img src="https://capsule-render.vercel.app/api?type=rounded&color=0:0f2027,50:203a43,100:38bdf8&height=50&section=header&text=📈%20GitHub%20Metrics&fontSize=18&fontColor=ffffff&fontAlignY=50&fontAlignX=5" width="100%"/>

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
