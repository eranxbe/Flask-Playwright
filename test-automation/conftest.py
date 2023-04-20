from typing import Generator
import pytest
from playwright.sync_api import sync_playwright, Playwright, APIRequestContext, BrowserContext
from infra.utils.config import *


@pytest.fixture(scope="session", autouse=True)
def playwright() -> Playwright:
    with sync_playwright() as playwright:
        yield playwright

@pytest.fixture(scope="session")
def browser(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()

@pytest.fixture(scope="session")
def context_web(browser) -> Generator[BrowserContext, None, None]:
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture(scope="session")
def context_api(playwright: Playwright) -> Generator[APIRequestContext, None, None]:
    headers = {
        "content-type": "application/json"
    }
    request_context = playwright.request.new_context(
        extra_http_headers=headers
    )

    yield request_context
    request_context.dispose()

@pytest.fixture
def page(context_web):
    page = context_web.new_page()
    page.goto(FLASK_URL + '/form')
    yield page
    page.close()
