Automation Architecture

                +---------------------+
                |     GitHub Repo     |
                +----------+----------+
                           |
                           v
                 +-------------------+
                 | GitHub Actions CI |
                 +---------+---------+
                           |
        ------------------------------------------
        |                                        |
        v                                        v
+---------------------+              +----------------------+
| API Automation      |              | UI Automation        |
| PyTest Framework    |              | Playwright + PyTest  |
| Faker Data          |              | Page Object Model    |
| Schema Validation   |              | Screenshot on Fail   |
+----------+----------+              | Video Recording      |
           |                         +----------+-----------+
           v                                    |
     +-------------+                           v
     | API Server  |                   +------------------+
     | Banking API |                   | Web Applications |
     +-------------+                   +------------------+

Outputs:
- Allure Reports
- CI Artifacts
- Logs