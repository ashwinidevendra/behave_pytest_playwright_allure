# Playwright + Behave Automation Framework (POM) for practice.qabrains

This project is a starter, robust and scalable automation framework using:
- Playwright (Python sync API)
- Behave (BDD)
- Page Object Model
- Allure reporting (via `allure-behave` formatter)
- GitHub Actions CI workflow

**What is included**
- `features/` — Behave feature file, environment hooks and step implementations
- `pages/` — Page Object Model classes
- `requirements.txt` — Python dependencies
- `.github/workflows/ci.yml` — GitHub Actions CI to run tests and publish allure-results as artifact
- `run_behave.sh` — helper script to run tests locally and produce Allure results
- `config.json` — credentials and base_url (update before running)
- `behave.ini` — behave configuration

**IMPORTANT**
- Selectors used in page objects are reasonable guesses but may need adjustment if the page's HTML differs. Update `pages/login_page.py` accordingly.
- You must provide valid credentials in `config.json` for the *positive* test to pass.
- To view Allure report locally after running:
  1. `pip install allure-commandline` (or use the Allure Docker image)
  2. `allure serve allure-results`

