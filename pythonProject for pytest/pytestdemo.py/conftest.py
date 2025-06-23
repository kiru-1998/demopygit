import os
from datetime import datetime
from email.policy import default
from fileinput import filename

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service



@pytest.fixture(scope="class")
def setup():
    print('execute first')
    yield
    print('execute last')


@pytest.fixture()
def dataLoad():
    print('user profile can be created')
    return['rahul','shetty','rahulshettyacademy']

@pytest.fixture(params=['chrome','firefox','IE'])
def crossBrowser(request):
    return request.param


def pytest_addoption(parser):
    parser.addoption("--Browser_name", action="store",default="Edge",help="Choose browser: Chrome or Edge")


@pytest.fixture()
def BrowserInstance(request):
    Browser_name=request.config.getoption('--Browser_name')

    if Browser_name=='Chrome':
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
    elif Browser_name=='Edge':
        driver=webdriver.Edge()
        driver.implicitly_wait(5)

        yield driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when in ("call", "setup"):
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join(os.path.dirname(__file__), "reports")
            file_name = os.path.join(reports_dir, report.nodeid.replace('::', '_') + ".png")
            print(file_name)
            driver = getattr(item, "driver", None)
            if driver:
                _capture_screenshot(driver, file_name)

                html = (
                    f'<div><img src="{file_name}" alt="screenshot" '
                    f'style="width:304px;height:228px;" '
                    f'onclick="window.open(this.src)" align="right"/></div>'
                )
                extra.append(pytest_html.extras.html(html))
        report.extra = extra



def _capture_screenshot(driver, file_name):
    driver.get_screenshot_as_file(file_name)













