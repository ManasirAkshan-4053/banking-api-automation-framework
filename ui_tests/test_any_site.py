def test_playwright_home(page):
    page.goto("https://playwright.dev")

    # Click Get Started using role locator
    page.get_by_role("link", name="Get started").click()

    # Wait for page to load
    page.wait_for_load_state("networkidle")

    # Validate heading instead of title (more stable)
    heading = page.get_by_role("heading", name="Installation")
    assert heading.is_visible()