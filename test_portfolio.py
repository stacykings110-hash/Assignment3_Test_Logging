from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
import time

logging.basicConfig(
    filename="Logs/test_log.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

driver = webdriver.Chrome()

driver.get(r"C:\Users\BBG Ltd\Assignment\index.html")

logging.info("RUN START")

time.sleep(2)

# TEST 1 - ABOUT
try:
    start = time.time()

    driver.find_element(
        By.LINK_TEXT,
        "ABOUT"
    ).click()

    time.sleep(3)

    duration = round(time.time() - start, 2)

    logging.info(
        f"TC-01 PASS | ABOUT | {duration}s"
    )

except Exception as e:

    logging.error(
        f"TC-01 FAIL | ABOUT | {e}"
    )

# TEST 2 - SERVICES
try:
    start = time.time()

    driver.find_element(
        By.LINK_TEXT,
        "SERVICES"
    ).click()

    time.sleep(3)

    duration = round(time.time() - start, 2)

    logging.info(
        f"TC-02 PASS | SERVICES | {duration}s"
    )

except Exception as e:

    logging.error(
        f"TC-02 FAIL | SERVICES | {e}"
    )

    # TEST 3 - PORTFOLIO
try:
    start = time.time()

    driver.find_element(
        By.LINK_TEXT,
        "PORTFOLIO"
    ).click()

    time.sleep(3)

    duration = round(time.time() - start, 2)

    logging.info(
        f"TC-03 PASS | PORTFOLIO | {duration}s"
    )

except Exception as e:

    logging.error(
        f"TC-03 FAIL | PORTFOLIO | {e}"
    )

    # TEST 4 - PAGES
try:
    start = time.time()

    driver.find_element(
        By.LINK_TEXT,
        "PAGES"
    ).click()

    time.sleep(3)

    duration = round(time.time() - start, 2)

    logging.info(
        f"TC-04 PASS | PAGES | {duration}s"
    )

except Exception as e:

    logging.error(
        f"TC-04 FAIL | PAGES | {e}"
    )

    # TEST 5 - CONTACT
try:
    start = time.time()

    driver.find_element(
        By.LINK_TEXT,
        "CONTACT"
    ).click()

    time.sleep(3)

    duration = round(time.time() - start, 2)

    logging.info(
        f"TC-05 PASS | CONTACT | {duration}s"
    )

except Exception as e:

    logging.error(
        f"TC-05 FAIL | CONTACT | {e}"
    )

    # TEST 6 - NEGATIVE TEST
try:

    driver.find_element(
        By.LINK_TEXT,
        "DOES_NOT_EXIST"
    ).click()

    logging.info(
        "TC-06 PASS"
    )

except Exception:

    logging.error(
        "TC-06 FAIL | Negative Test | Link not found"
    )

driver.quit()