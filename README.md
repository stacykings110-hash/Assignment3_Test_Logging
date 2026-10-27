# Assignment 3: Test Logging and Reporting with Selenium

## Student Information

- **Name:** Stella Matutina Uwamahoro
- **Module:** ITLDO801

## Overview

This project uses Python and Selenium WebDriver to automate checks on a portfolio website. It exercises the website's main navigation links and writes timestamped test results to a log file.

The assignment demonstrates:

- Test planning and execution
- Browser automation with Selenium
- Positive and negative test scenarios
- Logging test outcomes and execution times

## Test Cases

| ID | Scenario |
|---|---|
| TC-01 | Click the **ABOUT** navigation link |
| TC-02 | Click the **SERVICES** navigation link |
| TC-03 | Click the **PORTFOLIO** navigation link |
| TC-04 | Click the **PAGES** navigation link |
| TC-05 | Click the **CONTACT** navigation link |
| TC-06 | Look for a link that should not exist (`DOES_NOT_EXIST`) |

## Requirements

- Python 3
- Google Chrome
- The Selenium Python package
- The portfolio website files used by the tests

## Setup

Open a terminal in this project folder and install Selenium:

```bash
python -m pip install selenium
```

Before running the tests, open `test_portfolio.py` and update the path in `driver.get(...)` to point to the portfolio site's `index.html` file on your computer. The script currently uses a machine-specific path, so it must be changed if that file is not available at that location.

## Run the Tests

From the project folder, run:

```bash
python test_portfolio.py
```

Chrome will open and the script will attempt each navigation check. Keep the browser available until the run finishes.

## Logs and Results

The script writes timestamped messages to `Logs/test_log.log`. Successful navigation checks are logged with `PASS`; exceptions are logged with `FAIL` and an error message. The positive checks also record their elapsed time.

The `Screenshots` folder is present in the project, but the current script does not save screenshots.

> **Note about TC-06:** The script currently logs the expected missing-link exception as `FAIL`. This reflects the current implementation; it does not yet report the negative test as a passing check when the link is absent.