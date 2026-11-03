# Python Playwright UI Automation

This project uses Python, Playwright, pytest, and the Page Object Model (POM).

## Setup

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
pip install -r requirements.txt
playwright install
```

## Run tests

```bash
pytest
pytest -m smoke
```

The `pages` package contains page objects, `tests` contains test scenarios, and
`conftest.py` provides reusable Playwright fixtures.

## Configuration and framework base classes

Runtime settings are kept in `config/config.properties`:

```properties
base_url=https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
username=Admin
password=admin123
browser=chromium
headless=false
```

Use `BASE_URL`, `ORANGEHRM_USERNAME`, `ORANGEHRM_PASSWORD`,
`PLAYWRIGHT_BROWSER`, and `PLAYWRIGHT_HEADLESS` environment variables to
override these values without changing source code. `framework/driver_factory.py`
owns browser creation and cleanup. Class-based tests can inherit from
`tests.base_test.BaseTest` to receive `self.page` and `self.settings`.

## OrangeHRM login

The login test uses the public OrangeHRM demo account by default:

```bash
pytest tests/test_orangehrm_login.py
```

The default configuration opens Chromium visibly and shows logs in the terminal.
To run headless for CI, override the configuration property:

```bash
PLAYWRIGHT_HEADLESS=true pytest tests/test_orangehrm_login.py
```

You can override the credentials without changing source code:

```bash
ORANGEHRM_USERNAME=Admin ORANGEHRM_PASSWORD=admin123 \
pytest tests/test_orangehrm_login.py
```
