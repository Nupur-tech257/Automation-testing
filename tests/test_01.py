import pytest
from playwright.sync_api import sync_playwright
import os 

BASE_URL = os.getenv("BASE_URL", "http://app:8500")

def test_sql_data_viewer_heading():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(BASE_URL)
        page.wait_for_timeout(4000)
        # Wait for heading to appear
        page.wait_for_selector("text=SQL Data Viewer", timeout=10000)

        assert page.is_visible("text=SQL Data Viewer"), "❌ Heading not found"

        browser.close()
