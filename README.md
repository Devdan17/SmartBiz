# SmartBiz: Cloud-Based Business Analytics & Project Management System

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-Flask-green.svg)](https://flask.palletsprojects.com/)
[![Database](https://img.shields.io/badge/Database-MySQL-orange.svg)](https://www.mysql.com/)
[![Deployment](https://img.shields.io/badge/Deployment-Railway%20%2F%20AWS-blueviolet.svg)](https://railway.app/)

SmartBiz is a centralized, cloud-enabled web platform designed to streamline enterprise project management, automate business operations, and deliver interactive performance analytics. Developed during an internship at Edutainer (PAT Technologies), it combines relational database workflows with data science libraries to replace disconnected spreadsheets with real-time, data-driven business intelligence.

---

## 📌 Features

- **📊 Centralized Business Analytics Dashboard:** Real-time KPI monitoring, including monthly revenue analytics, active project counts, and user distribution visualizations powered by Pandas and Matplotlib.
- **📁 Project & Task Management:** Complete CRUD workflows to create projects, assign statuses (e.g., Ongoing, Completed), schedule deadlines, and monitor completion timelines.
- **🔐 Authentication & Access Control:** Secure user signup, credential validation, session handling, and role-based interface access.
- **☁️ Cloud & Database Architecture:** Multi-tier system architecture deployed on Railway/AWS backed by MySQL relational storage.

---

## 🏗️ System Architecture

SmartBiz is organized into a 5-layer modular architecture:
┌────────────────────────────────────────────────────────┐
│        Presentation Layer (HTML5, CSS3, Bootstrap)     │
└───────────────────────────┬────────────────────────────┘
│
┌───────────────────────────▼────────────────────────────┐
│      Application Layer (Flask Web Framework / Python)   │
└─────────────┬────────────────────────────┬─────────────┘
│                            │
┌─────────────▼───────────────┐ ┌──────────▼─────────────┐
│  Database Layer (MySQL)     │ │ Analytics Layer        │
│  - Users, Projects, Tasks   │ │ - Pandas & Matplotlib  │
└─────────────┬───────────────┘ └────────────────────────┘
│
┌─────────────▼──────────────────────────────────────────┐
│      Cloud Layer (Railway & AWS Cloud Infrastructure)  │
└────────────────────────────────────────────────────────┘


```markdown
# SmartBiz: Cloud-Based Business Analytics & Project Management System

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-Flask-green.svg)](https://flask.palletsprojects.com/)
[![Database](https://img.shields.io/badge/Database-MySQL-orange.svg)](https://www.mysql.com/)
[![Deployment](https://img.shields.io/badge/Deployment-Railway%20%2F%20AWS-blueviolet.svg)](https://railway.app/)

SmartBiz is a centralized, cloud-enabled web platform designed to streamline enterprise project management, automate business operations, and deliver interactive performance analytics[cite: 1]. Developed during an internship at Edutainer (PAT Technologies), it combines relational database workflows with data science libraries to replace disconnected spreadsheets with real-time, data-driven business intelligence[cite: 1].

---

## 📌 Features

- **📊 Centralized Business Analytics Dashboard:** Real-time KPI monitoring, including monthly revenue analytics, active project counts, and user distribution visualizations powered by Pandas and Matplotlib[cite: 1].
- **📁 Project & Task Management:** Complete CRUD workflows to create projects, assign statuses (e.g., Ongoing, Completed), schedule deadlines, and monitor completion timelines[cite: 1].
- **🔐 Authentication & Access Control:** Secure user signup, credential validation, session handling, and role-based interface access[cite: 1].
- **☁️ Cloud & Database Architecture:** Multi-tier system architecture deployed on Railway/AWS backed by MySQL relational storage[cite: 1].

---

## 🏗️ System Architecture

SmartBiz is organized into a 5-layer modular architecture[cite: 1]:


```

┌────────────────────────────────────────────────────────┐
│        Presentation Layer (HTML5, CSS3, Bootstrap)     │
└───────────────────────────┬────────────────────────────┘
│
┌───────────────────────────▼────────────────────────────┐
│      Application Layer (Flask Web Framework / Python)   │
└─────────────┬────────────────────────────┬─────────────┘
│                            │
┌─────────────▼───────────────┐ ┌──────────▼─────────────┐
│  Database Layer (MySQL)     │ │ Analytics Layer        │
│  - Users, Projects, Tasks   │ │ - Pandas & Matplotlib  │
└─────────────┬───────────────┘ └────────────────────────┘
│
┌─────────────▼──────────────────────────────────────────┐
│      Cloud Layer (Railway & AWS Cloud Infrastructure)  │
└────────────────────────────────────────────────────────┘

```

---

## 🛠️ Tech Stack

- **Backend:** Python (Flask), Flask-MySQLdb[cite: 1]
- **Frontend:** HTML5, CSS3, Bootstrap, JavaScript[cite: 1]
- **Analytics Engine:** Pandas, Matplotlib[cite: 1]
- **Database:** MySQL[cite: 1]
- **Cloud & Deployment:** Railway / AWS, Gunicorn[cite: 1]

---

## 📂 Repository Structure

```text
SmartBiz/
├── analytics/           # Analytics modules & visualization logic
├── database/
│   └── schema.sql       # MySQL database schemas and tables
├── static/
│   ├── css/             # Stylesheets & Bootstrap
│   └── js/              # Client-side scripts
├── templates/
│   ├── index.html       # Landing page
│   ├── login.html       # User authentication (Login)
│   ├── signup.html      # Account creation (Signup)
│   ├── dashboard.html   # Main analytics & KPI dashboard
│   ├── projects.html    # Project management overview
│   └── edit_project.html# Project update & edit view
├── app.py               # Application entry point & core routing
├── requirements.txt     # Project dependencies
└── README.md            # Documentation

```

---

## 🚀 Getting Started

### Prerequisites

* Python 3.7+ installed


* MySQL Server running locally or on a cloud provider


* Git

### Installation & Setup

1. **Clone the Repository:**
```bash
git clone [https://github.com/Devdan17/SmartBiz.git](https://github.com/Devdan17/SmartBiz.git)
cd SmartBiz

```


2. **Create and Activate a Virtual Environment:**
```bash
# macOS/Linux:
python3 -m venv venv
source venv/bin/activate

# Windows:
python -m venv venv
venv\Scripts\activate

```


3. **Install Required Packages:**
```bash
pip install -r requirements.txt

```


4. **Database Configuration:**
* Import the database schema into MySQL:
```bash
mysql -u <your_mysql_user> -p < database/schema.sql

```


* Configure your MySQL connection parameters inside `app.py` (or load them from a `.env` file):
```python
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'smartbiz_db'

```




5. **Run the Application:**
```bash
python app.py

```


Open your browser and navigate to `http://127.0.0.1:5000/`.

---

## 🌐 Cloud Deployment (Railway / AWS)

1. Push your repository to GitHub.
2. Link your repository to **Railway** or an **AWS EC2** instance.


3. Provision a **MySQL database** service and connect the environment variables (`MYSQL_HOST`, `MYSQL_USER`, `MYSQL_PASSWORD`, `MYSQL_DB`).
4. Define the production start command:
```bash
gunicorn app:app

```



---

## 🔮 Future Enhancements

* Integration of machine learning models for automated sales forecasting and predictive churn analysis.


* Development of companion mobile applications for iOS and Android.


* Integration of advanced BI tools such as Tableau and Power BI for enterprise reporting.


* Multi-factor authentication (MFA) and fine-grained role-based access control (RBAC).



---

## 👤 Author

**Devdan Cornelius**

Department of Computer Science & Engineering, MVJ College of Engineering

*Internship Project carried out at Edutainer (PAT Technologies Private Limited)*

```

```
