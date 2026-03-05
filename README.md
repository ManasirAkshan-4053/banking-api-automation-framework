# Banking API Automation Framework

# Banking API Automation Framework

![API Tests](https://github.com/ManasirAkshan-4053/banking-api-automation-framework/actions/workflows/ci.yml/badge.svg)

![UI Tests](https://github.com/ManasirAkshan-4053/banking-api-automation-framework/actions/workflows/ui-tests.yml/badge.svg)

# 🏦 Banking API Automation Framework

A professional REST API Automation Framework built using Python and Pytest.

## 🚀 Project Overview

This project is a professional-grade API Automation Framework built using Python and Pytest, designed to simulate real-world banking transaction workflows.

It validates core banking operations such as:

Account validation

Transaction creation

Balance verification

API response validation

Negative scenario handling

The framework is designed following industry best practices and includes:

Structured test architecture

Mock banking API using json-server

Allure reporting integration

CI/CD pipeline using GitHub Actions

This project demonstrates production-ready automation design aligned with Banking, Cards, ATM, and Payments domain testing.

---

## 🏗 Architecture

The framework follows a clean layered structure:

Tests Layer
    ↓
API Client Layer
    ↓
Mock Banking API (json-server)

Key Design Principles

Separation of concerns

Reusable API utility functions

Configurable test execution

Scalable folder structure

CI-ready implementation

---

## 🛠 Tech Stack

| Tool           | Purpose              |
| -------------- | -------------------- |
| Python 3.11    | Programming Language |
| Pytest         | Test Framework       |
| Requests       | API Interaction      |
| Allure         | Reporting            |
| JSON Server    | Mock Banking API     |
| GitHub Actions | CI/CD                |
| Git            | Version Control      |


---

## 📂 Project Structure

api/ → API request layer  
tests/ → Test cases  
utils/ → Config, logging, validation utilities  

---

### ▶️ How To Run

### 1️⃣ Clone Repository

git clone https://github.com/ManasirAkshan-4053/banking-api-automation-framework.git

cd banking-api-automation-framework

### 2️⃣ Install Dependencies

pip install -r requirements.txt

### 3️⃣ Start Mock Banking API

json-server --watch db.json --port 3000

### 4️⃣ Execute Tests

py -m pytest --alluredir=allure-results

### 5️⃣ Generate Allure Report

allure serve allure-results

This opens an interactive HTML report in your browser.

---

## ✅ Sample Test Scenario

✔ Create new banking transaction  
✔ Validate 201 response  
✔ Extract dynamic transaction ID  
✔ Fetch same transaction  
✔ Validate response data  

---

## 📊 Allure Reporting

The framework integrates Allure Reporting for:

Detailed test steps

Request/Response visibility

Failure diagnostics

Test categorization (Feature/Story)

Execution timeline

This mirrors reporting standards used in enterprise QA environments.

---

## 🔄 CI/CD Integration

CI pipeline is configured using GitHub Actions.

Triggered On:

Push to main

Pull Request creation

CI Workflow Includes:

Code checkout

Python setup

Dependency installation

Automated test execution

This ensures continuous validation and professional DevOps alignment.

---

## 📂 Folder Structure

banking-api-automation-framework
│
├── api/                      # API client layer
├── tests/                    # Test cases
├── utils/                    # Reusable utilities
├── db.json                   # Mock banking data
├── pytest.ini                # Pytest configuration
├── requirements.txt          # Project dependencies
├── README.md                 # Project documentation
└── .github/
    └── workflows/
        └── ci.yml            # CI pipeline

---

## 🚀 Future Enhancements

Planned improvements to elevate this framework further:

Dockerized execution

Environment configuration (DEV / QA / PROD)

Parallel test execution

Logging framework integration

Data-driven testing support

API coverage metrics

Performance testing integration

Authentication token management

---

## 💼 Professional Context

This framework reflects hands-on automation design aligned with:

Banking & Payments domain testing

API validation strategies

Enterprise QA best practices

CI/CD integration workflows

It demonstrates capability in transitioning from Manual Testing to Advanced API Automation Engineering.

## 📬 Author

Manasir Akshan Ayubkhan,
Software Test Engineer | Banking & Payments Domain,
API Automation | CI/CD | Test Architecture