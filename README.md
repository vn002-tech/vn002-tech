<!-- 1. TOP BANNER -->
<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=F59E0B&height=180&section=header&text=⚙️%20DATA%20ENGINEERING%20LAB&fontSize=32&fontColor=000000&fontAlignY=50" width="100%" />
  
  <br/><br/>
  
  <h2>👨‍💻 VAN (vn002-tech)</h2>
  <p><b>Data Engineer & MLOps Specialist</b> | Python · PySpark · Apache Airflow · dbt · PostgreSQL</p>
  
  <br/>
  
  <div>
    <a href="https://github.com/vn002-tech"><img src="https://img.shields.io/badge/GitHub-vn002--tech-181717?style=for-the-badge&logo=github&logoColor=white" /></a>
    <a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
    <a href="mailto:your_email@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" /></a>
  </div>
  <br/>
  <div>
    <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/PySpark-E25A1C?style=flat-square&logo=apachespark&logoColor=white" />
    <img src="https://img.shields.io/badge/Airflow-017CEE?style=flat-square&logo=apacheairflow&logoColor=white" />
    <img src="https://img.shields.io/badge/dbt-FF6B4A?style=flat-square&logo=dbt&logoColor=white" />
    <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white" />
    <img src="https://img.shields.io/badge/Kafka-231F20?style=flat-square&logo=apachekafka&logoColor=white" />
  </div>
</div>

<br/>

---

<!-- 2. GITHUB STATS -->
<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=0:D97706,50:DC2626,100:9333EA&height=60&section=header&text=GitHub%20Stats&fontSize=24&fontColor=ffffff&fontAlignY=50" width="100%" />
</div>

<br/>

<div align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=vn002-tech&show_icons=true&theme=tokyonight&hide_border=true" height="170" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=vn002-tech&layout=compact&theme=tokyonight&hide_border=true" height="170" />
</div>

<br/><br/>

<!-- 3. ABOUT ME -->
<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=0:7C3AED,100:6366F1&height=60&section=header&text=About%20Me&fontSize=24&fontColor=ffffff&fontAlignY=50" width="100%" />
</div>

<br/>

```python
class DataEngineer:
    def __init__(self):
        self.username = "vn002-tech"
        self.role = "Data Engineer & MLOps Specialist"
        self.focus_areas = [
            "Enterprise ETL/ELT Pipeline Orchestration", 
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

<br/><br/>

<!-- 4. TECH STACK -->
<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=0:4F46E5,100:2563EB&height=60&section=header&text=Tech%20Stack&fontSize=24&fontColor=ffffff&fontAlignY=50" width="100%" />
</div>

<br/>

<div align="center">
  <h3>Languages & Databases</h3>
  <img src="https://skillicons.dev/icons?i=python,postgres,mysql,mongodb,bash" />
  <h3>Big Data, ETL & Orchestration</h3>
  <img src="https://skillicons.dev/icons?i=kafka,kubernetes,git,github" />
  <p><i>Python · PySpark · Apache Airflow · dbt · Apache Kafka</i></p>
  <h3>Infrastructure & Cloud</h3>
  <img src="https://skillicons.dev/icons?i=aws,gcp,kubernetes,linux" />
</div>

<br/><br/>

<!-- 5. ARCHITECTURE: MESH NETWORK DATA PIPELINE -->
<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=0:059669,100:0D9488&height=60&section=header&text=🕸️%20Data%20Mesh%20Architecture&fontSize=24&fontColor=ffffff&fontAlignY=50" width="100%" />
</div>

<br/>

```mermaid
graph LR
    classDef src fill:#0b192c,stroke:#00f5ff,stroke-width:2px,color:#fff
    classDef ing fill:#1e1b4b,stroke:#818cf8,stroke-width:2px,color:#fff
    classDef proc fill:#1a1a4e,stroke:#a78bfa,stroke-width:2px,color:#fff
    classDef stor fill:#064e3b,stroke:#34d399,stroke-width:2px,color:#fff
    classDef qual fill:#065f46,stroke:#6ee7b7,stroke-width:2px,color:#fff
    classDef serv fill:#451a03,stroke:#fbbf24,stroke-width:2px,color:#fff
    classDef ml   fill:#4c1d95,stroke:#c084fc,stroke-width:2px,color:#fff

    A1["🗄️ PostgreSQL / MySQL"]:::src
    A2["📡 REST APIs / SaaS"]:::src
    A3["⚡ Kafka Event Stream"]:::src
    A4["📂 CSV / JSON / Parquet"]:::src
    A5["🌐 Web Scraping / IoT"]:::src

    B1["🔄 Debezium CDC"]:::ing
    B2["🔌 Airbyte / Fivetran"]:::ing
    B3["📥 Batch Loader"]:::ing

    C1["⚙️ Apache Airflow"]:::proc
    C2["⚡ Dagster / Prefect"]:::proc

    D1["🚀 PySpark Batch"]:::proc
    D2["🌊 Apache Flink Stream"]:::proc
    D3["🐼 Pandas / Polars"]:::proc

    E1["☁️ AWS S3 / GCS Bucket"]:::stor
    E2["❄️ Snowflake DWH"]:::stor
    E3["🏠 Delta Lake / Iceberg"]:::stor
    E4["🐘 PostgreSQL OLAP"]:::stor

    F1["🔧 dbt Core Models"]:::qual
    F2["🛡️ Great Expectations"]:::qual
    F3["📊 Data Catalog"]:::qual

    G1["📊 Streamlit Dashboard"]:::serv
    G2["📈 PowerBI / Tableau"]:::serv
    G3["🤖 Fraud Detection ML"]:::ml
    G4["🧠 MLflow + Feature Store"]:::ml
    G5["🔄 Reverse ETL → API"]:::serv

    A1 --> B1
    A1 --> B2
    A2 --> B2
    A2 --> B3
    A3 --> B1
    A3 --> D2
    A4 --> B3
    A5 --> B2
    A5 --> B3

    B1 --> C1
    B2 --> C1
    B2 --> C2
    B3 --> C1
    B3 --> C2

    C1 --> D1
    C1 --> D3
    C2 --> D1
    C2 --> D2

    D1 --> E1
    D1 --> E3
    D2 --> E2
    D2 --> E3
    D3 --> E4
    D3 --> E1

    E1 --> F1
    E2 --> F1
    E3 --> F1
    E4 --> F2
    F1 --> F2
    F1 --> F3
    F2 --> F3

    F3 --> G1
    F3 --> G2
    F3 --> G3
    F3 --> G5
    G3 --> G4
    G4 --> G5
    E2 --> G2
    E4 --> G1
```

<br/><br/>

<!-- 6. FEATURED PROJECTS -->
<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=0:059669,100:0D9488&height=60&section=header&text=🚀%20Featured%20Projects&fontSize=24&fontColor=ffffff&fontAlignY=50" width="100%" />
</div>

<br/>

| Project | Stack | Description |
| :--- | :--- | :--- |
| 🛡️ **[Bank Fraud Detection System](https://github.com/vn002-tech/Transaksi_bank)** | `Python` `Scikit-Learn` `Streamlit` `PostgreSQL` | ML pipeline & dashboard for transaction fraud detection. |
| ⚡ **[Real-Time Transaction Ingestion](https://github.com/vn002-tech)** | `PySpark` `Kafka` `PostgreSQL` | High-throughput streaming data pipeline for bank logs. |
| ☁️ **[Automated ETL Orchestration](https://github.com/vn002-tech)** | `Airflow` `dbt` `PostgreSQL` | End-to-end automated data transformation & warehousing. |

<br/>

<!-- FOOTER -->
<div align="center">
  <img src="https://skillicons.dev/icons?i=vscode,postgres,bash,linux" height="50" />
  <br/><br/>
  <img src="https://komarev.com/ghpvc/?username=vn002-tech&color=F59E0B&style=flat-square&label=Pipeline+Visits" />
</div>
```

Diagram sekarang berbentuk **jaring-jaring (mesh network)** sesungguhnya — setiap source bisa masuk ke multiple ingestion path, setiap processing engine bisa mengirim ke multiple storage, dan setiap output bercabang ke berbagai serving layer! 🕸️🚀
