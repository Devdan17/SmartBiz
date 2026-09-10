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
