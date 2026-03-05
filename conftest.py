import pytest
from pathlib import Path


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page", None)

        if page:
            screenshots_dir = Path("screenshots")
            screenshots_dir.mkdir(exist_ok=True)

            screenshot_file = screenshots_dir / f"{item.name}.png"
            page.screenshot(path=str(screenshot_file))

            print(f"\nScreenshot saved: {screenshot_file}")