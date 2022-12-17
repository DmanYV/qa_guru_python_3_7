import pytest
from selene.support.shared import browser


@pytest.fixture(scope="class")
def open_browser():
    browser.config.window_height = 1080
    browser.config._window_width = 1920
