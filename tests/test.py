import pytest
from playwright.sync_api import sync_playwright

BASE_URL = "http://localhost:8501"

def test_sql_data_viewer_heading():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(BASE_URL)

        # Wait for heading to appear
        page.wait_for_selector("text=SQL Data Viewer", timeout=10000)

        assert page.is_visible("text=SQL Data Viewer"), "❌ Heading not found"

        browser.close()
