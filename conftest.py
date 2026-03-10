import pytest
import allure
from pathlib import Path

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        page = item.funcargs.get("page")

        if page:

            screenshot_path = f"screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path)

            allure.attach.file(
                screenshot_path,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )

            video_dir = Path("videos")

            if video_dir.exists():
                for video in video_dir.rglob("*.webm"):
                    allure.attach.file(
                        str(video),
                        name="Test Video",
                        attachment_type=allure.attachment_type.WEBM
                    )