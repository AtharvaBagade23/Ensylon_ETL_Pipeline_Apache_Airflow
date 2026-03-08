# ETL Weather Data Pipeline using Apache Airflow

## 📌 Project Overview

This project demonstrates the design and implementation of an **ETL (Extract, Transform, Load) data pipeline** using **Apache Airflow**.
The pipeline extracts weather data from an external API, performs data cleaning and preprocessing, and loads the processed data into a database for further analysis.

The goal of this project is to understand **data engineering workflows, pipeline orchestration, and data preprocessing techniques** used in real-world ETL systems.

---

# ⚙️ Tech Stack

* Python
* Apache Airflow
* Docker
* SQLite
* Pandas
* Weather API
* Git & GitHub

---

# 📂 Project Structure

```
.
├── dags/
│   └── weather_etl_dag.py
│
├── tests/
│   └── dags/
│
├── Dockerfile
├── requirements.txt
├── packages.txt
├── .gitignore
├── .dockerignore
└── README.md
```

**Folder Description**

| Folder/File      | Description                                  |
| ---------------- | -------------------------------------------- |
| dags             | Contains Airflow DAG files for ETL pipelines |
| tests            | Contains test scripts for validating DAGs    |
| Dockerfile       | Container configuration for running Airflow  |
| requirements.txt | Python dependencies                          |
| packages.txt     | System dependencies                          |
| README.md        | Project documentation                        |

---

# 🔄 ETL Pipeline Workflow

## 1️⃣ Extract

Weather data is extracted from an external API using Python.
The API returns structured data containing:

* Timestamp
* Temperature
* Humidity
* Weather conditions

The data is fetched periodically through an **Airflow DAG scheduler**.

---

## 2️⃣ Transform

The transformation stage focuses on **data cleaning and preprocessing**.

Transformations performed:

* Handling missing values
* Removing duplicate records
* String normalization (e.g., city names like *Hyd → Hyderabad*)
* Data formatting
* Data validation

Libraries used:

* **Pandas**
* **NumPy**

---

## 3️⃣ Load

After cleaning the dataset, the processed data is stored in a **SQLite database** for analysis.

Benefits of storing the data:

* Easy querying
* Structured storage
* Data analysis capability

---

# 🚀 How the Pipeline Runs

1. Airflow scheduler triggers the DAG.
2. The **Extract task** pulls weather data from the API.
3. The **Transform task** cleans and processes the data.
4. The **Load task** stores the data in the SQLite database.
5. Airflow logs and monitors each step.

---

# 📚 What I Learned

During this project, I learned:

* How **ETL pipelines work in real-world data engineering systems**
* How to use **Apache Airflow for orchestration**
* Writing **DAGs and scheduling workflows**
* Handling **missing data and inconsistencies**
* Data preprocessing using **Pandas**
* Managing dependencies using **Docker**
* Using **Git and GitHub for version control**

---

# ⚠️ Challenges Faced

### 1️⃣ Missing Values in Dataset

Some API responses had missing values for certain fields.

**Solution**

* Applied data cleaning techniques using Pandas
* Replaced missing values with appropriate defaults or removed invalid rows.

---

### 2️⃣ Duplicate Records

Duplicate entries appeared when data was fetched multiple times.

**Solution**

* Implemented duplicate removal using:

```
drop_duplicates()
```

---

### 3️⃣ String Inconsistencies

City names appeared in different formats such as:

```
Hyd
Hyderabad
HYD
```

**Solution**

Implemented **string normalization and fuzzy matching** techniques to standardize city names.

---

### 4️⃣ Pipeline Debugging

Initial DAG execution errors occurred due to dependency and environment issues.

**Solution**

* Checked Airflow logs
* Fixed dependency issues in `requirements.txt`
* Used Docker to maintain a consistent environment

---

# 📊 Outcome

The project successfully demonstrates a **fully functional ETL pipeline** with the following outcomes:

* Automated data extraction
* Clean and structured dataset
* Scheduled workflow using Apache Airflow
* Reliable data storage in SQLite
* Reproducible and scalable pipeline design

This project provides a **strong foundation for building production-grade data pipelines**.

---

# 📈 Future Improvements

Possible improvements include:

* Integrating **cloud storage (AWS S3 / GCP)**
* Adding **data visualization dashboards**
* Using **PostgreSQL instead of SQLite**
* Implementing **real-time streaming pipelines**
* Adding more advanced **data validation checks**

---

# 👨‍💻 Author

**Atharva Bagade**

Data Engineering & AI Enthusiast

---

# ⭐ Acknowledgement

This project was built as part of a **data engineering learning exercise to understand ETL pipelines and workflow orchestration using Apache Airflow**.
