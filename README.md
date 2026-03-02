# 🏦 Banking API Automation Framework

A professional REST API Automation Framework built using Python and Pytest.

## 🚀 Project Overview

This framework demonstrates:

- REST API automation using requests
- Pytest-based test execution
- Custom response validation utilities
- Logging implementation
- API chaining (POST → GET dynamic ID)
- Local mock REST server using json-server
- Clean modular framework structure

---

## 🛠 Tech Stack

- Python
- Pytest
- Requests
- JSON Server (Mock API)
- Logging module

---

## 📂 Project Structure

api/ → API request layer  
tests/ → Test cases  
utils/ → Config, logging, validation utilities  

---

## ▶️ How To Run

### 1️⃣ Start Mock API

json-server --watch db.json --port 3000

### 2️⃣ Run Tests

py -m pytest -v

---

## ✅ Sample Test Scenario

✔ Create new banking transaction  
✔ Validate 201 response  
✔ Extract dynamic transaction ID  
✔ Fetch same transaction  
✔ Validate response data  

---

## 🎯 Why This Project Matters

This project demonstrates real-world automation framework design principles:

- Separation of concerns
- Reusable utilities
- Clean architecture
- Scalable structure
- CI/CD ready design

---

## 👨‍💻 Manasir Akshan

Automation Engineer | API Testing | Banking Domain