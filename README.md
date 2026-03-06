# 🏦 Banking API & UI Automation Framework

![Python](https://img.shields.io/badge/Python-3.11-blue)
![PyTest](https://img.shields.io/badge/PyTest-Test%20Framework-green)
![Playwright](https://img.shields.io/badge/Playwright-UI%20Automation-brightgreen)

![API Tests](https://github.com/ManasirAkshan-4053/banking-api-automation-framework/actions/workflows/api-tests.yml/badge.svg)

![UI Tests](https://github.com/ManasirAkshan-4053/banking-api-automation-framework/actions/workflows/ui-tests.yml/badge.svg)


![License](https://img.shields.io/badge/License-MIT-yellow)
![Stars](https://img.shields.io/github/stars/ManasirAkshan-4053/banking-api-automation-framework?style=social)

Enterprise-level **Test Automation Framework** built using **Python, PyTest, Playwright, and GitHub Actions**.

This project demonstrates modern QA automation practices including:

* API Automation
* UI Automation
* Data-driven testing
* Faker-based dynamic test data
* JSON schema validation
* Response time SLA validation
* Page Object Model (POM)
* CI/CD with GitHub Actions
* Allure reporting
* Screenshot capture on failure

---

# Tech Stack

Python 3.11
PyTest
Playwright (UI Automation)
Requests (API Testing)
Faker (Dynamic Test Data)
JSONSchema (Response Validation)
Allure Reports
GitHub Actions (CI/CD)

---

# Project Structure

project/
│
├── api/
│   └── transaction_api.py
│
├── utils/
│   ├── validators.py
│   └── data_factory.py
│
├── tests/
│   └── test_transactions.py
│
├── ui_tests/
│   ├── pages/
│   │   └── playwright_home_page.py
│   │
│   └── test_playwright_home.py
│
├── config/
│   └── dev.json
│
├── db.json
├── pytest.ini
├── requirements.txt
│
└── .github/
└── workflows/
├── api-tests.yml
└── ui-tests.yml

---

# Features Implemented

API Automation

Create Transaction API testing

JSON Schema validation

Negative testing

Dynamic test data using Faker

Response time SLA validation

UI Automation

Playwright with Python

Page Object Model (POM)

Headed and headless execution

Screenshot capture on failure

CI/CD

Automated pipelines using GitHub Actions

Separate workflows for API and UI tests

Tests automatically run on every push

---

# Running Tests Locally

API Tests

pytest tests -v

Start mock server before running tests:

npx json-server --watch db.json --port 3000

UI Tests

pytest ui_tests -v

Run with browser visible:

pytest ui_tests -v --headed

---

# Allure Reporting

Generate report:

pytest --alluredir=allure-results

Open report:

allure serve allure-results

---

# CI Pipelines

API Tests Pipeline

![API Tests](https://github.com/ManasirAkshan-4053/banking-api-automation-framework/workflows/api-tests.yml/badge.svg)

UI Tests Pipeline

![UI Tests](https://github.com/ManasirAkshan-4053/banking-api-automation-framework/workflows/ui-tests.yml/badge.svg)

---

# Future Enhancements

Dockerized test environment

Test parallelization

Cross-browser testing

Integration with TestRail

Cloud execution using GitHub runners

---

# Author

Manasir Akshan Ayubkhan, QA Automation Engineer

Specialized in:

API Testing

Payments / Banking domain

Automation Framework Design

CI/CD Test Automation

