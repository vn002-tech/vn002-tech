<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,40:1e1b4b,80:0284c7,100:38bdf8&height=230&section=header&text=VN002-TECH%20%E2%9A%A1%20DATA%20ENGINEERING&fontSize=34&fontColor=ffffff&fontAlignY=36&animation=twinkling" width="100%"/>
  
  <br/>

  <!-- ANIMASI TYPING TAGLINE BER-EMOJI (FONT: JetBrains Mono) -->
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=19&pause=1000&color=00F5FF&center=true&vCenter=true&width=700&lines=%E2%9A%A1+Architecting+Scalable+Data+Pipelines;%F0%9F%94%A5+PySpark+%7C+Apache+Airflow+%7C+dbt+%7C+Kafka;%F0%9F%A4%96+MLOps+%26+Real-Time+Data+Warehousing;%F0%9F%93%88+Transforming+Raw+Chaos+Into+Data+Products" alt="Typing SVG" />
  </a>

  <br/><br/>

  <!-- QUICK NAVIGATION BAR (TOMBOL PINTAS) -->
  <a href="#-pipeline_configpy-about-me"><img src="https://img.shields.io/badge/⚡_About_Me-0A192F?style=for-the-badge&logo=python&logoColor=38bdf8" /></a>
  <a href="#️-end-to-end-enterprise-data-architecture"><img src="https://img.shields.io/badge/🏗️_Architecture-0A192F?style=for-the-badge&logo=diagramsdotnet&logoColor=34d399" /></a>
  <a href="#️-data-engineering-tech-stack"><img src="https://img.shields.io/badge/🛠️_Tech_Stack-0A192F?style=for-the-badge&logo=apachespark&logoColor=fbbf24" /></a>
  <a href="#-featured-projects"><img src="https://img.shields.io/badge/🚀_Projects-0A192F?style=for-the-badge&logo=github&logoColor=818cf8" /></a>

  <br/><br/>

  <!-- BADGES CONTACT & PLATFORMS -->
  <a href="https://github.com/vn002-tech"><img src="https://img.shields.io/badge/GitHub-vn002--tech-181717?style=for-the-badge&logo=github&logoColor=white" /></a>
  <a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
  <a href="mailto:your_email@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" /></a>
  <a href="https://kaggle.com"><img src="https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white" /></a>
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
            "Enterprise ETL/ELT Orchestration", 
            "Real-Time Stream Processing", 
            "Cloud Data Lakehouse Architecture"
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

<!-- SECTION 2: EXTENDED ENTERPRISE DATA ARCHITECTURE -->
<img src="https://capsule-render.vercel.app/api?type=rect&color=0A192F&height=45&section=header&text=🏗️%20End-to-End%20Enterprise%20Data%20Architecture&fontSize=17&fontColor=38BDF8&fontAlignY=50&fontAlignX=4" width="100%"/>

```mermaid
flowchart LR
    classDef src fill:#0f172a,stroke:#38bdf8,stroke-width:2px,color:#ffffff;
    classDef ing fill:#1e1b4b,stroke:#818cf8,stroke-width:2px,color:#ffffff;
    classDef proc fill:#311b92,stroke:#a78bfa,stroke-width:2px,color:#ffffff;
    classDef stor fill:#064e3b,stroke:#34d399,stroke-width:2px,color:#ffffff;
    classDef qual fill:#065f46,stroke:#6ee7b7,stroke-width:2px,color:#ffffff;
    classDef serv fill:#451a03,stroke:#fbbf24,stroke-width:2px,color:#ffffff;

    subgraph SG1 ["📥 Data Sources"]
        A1["🗄️ Relational DBs (Postgres/MySQL)"]:::src
        A2["⚡ Real-Time Events (Kafka/RabbitMQ)"]:::src
        A3["🌐 Third-Party APIs & SaaS"]:::src
        A4["📄 Raw Logs (CSV/JSON/Parquet)"]:::src
    end

    subgraph SG2 ["⚙️ Ingestion & Orchestration"]
        B1["🔄 CDC (Debezium / Fivetran)"]:::ing
        B2["⚡ Airflow / Dagster Orchestrator"]:::ing
    end

    subgraph SG3 ["🔥 Data Processing Engine"]
        C1["🚀 PySpark Batch Engine"]:::proc
        C2["🌊 Flink Stream Engine"]:::proc
    end

    subgraph SG4 ["🗄️ Data Lakehouse Layer"]
        D1["☁️ Raw Data Lake (S3 / GCS)"]:::stor
        D2["❄️ Data Warehouse (Snowflake/BigQuery)"]:::stor
        D3["🧬 Delta Lake / Feature Store"]:::stor
    end

    subgraph SG5 ["🔧 Modeling & Data Quality"]
        E1["🔧 dbt Transformations"]:::qual
        E2["🛡️ Great Expectations Quality Checks"]:::qual
    end

    subgraph SG6 ["📊 Data Products & Serving"]
        F1["📊 BI Dashboards (Streamlit / PowerBI)"]:::serv
        F2["🤖 ML Pipelines & Predictive Models"]:::serv
        F3["🔄 Reverse ETL to Operational APIs"]:::serv
    end

    A1 --> B1
    A2 --> B2
    A3 --> B2
    A4 --> B2
    
    B1 --> C1
    B2 --> C1
    B2 --> C2

    C1 --> D1
    C2 --> D2
    C1 --> D3

    D1 --> E1
    D2 --> E1
    E1 --> E2

    E2 --> F1
    E2 --> F2
    E2 --> F3
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
  <img src="https://github-readme-stats.vercel.app/api?username=vn002-tech&show_icons=true&theme=tokyonight&hide_border=true" />
  <br/><br/>
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=vn002-tech&layout=compact&theme=tokyonight&hide_border=true" />
</div>

<br/>

<!-- FOOTER -->
<div align="center">
  <img src="https://komarev.com/ghpvc/?username=vn002-tech&color=38bdf8&style=flat-square&label=Pipeline+Visits" alt="Visitor Count" />
  <br/>
  <sub><i>"In God we trust, all others must bring data." — W. Edwards Deming</i></sub>
</div>
```
