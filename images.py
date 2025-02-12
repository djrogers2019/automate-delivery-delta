import os
from playwright.sync_api import Playwright

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Navigate and Login
    page.goto("https://delta.stockholmstream.net/spa/brand/192cec3d-3f30-4c01-b842-debf835aef0a/rights")
    page.get_by_role("textbox", name="Enter Email...").fill("douglas@yippee.tv")
    page.get_by_role("textbox", name="Enter Password...").fill("Alvinman1!")
    page.get_by_role("button", name="Login").click()

    # Enter confirmation code
    page.get_by_role("textbox", name="Enter Confirmation Code...").fill("480771")
    page.get_by_role("button", name="Login").click()

    # Navigate to Series and Search
    page.get_by_text("Series", exact=True).click()
    search_box = page.get_by_role("row", name="Filter... Start End Type").get_by_role("searchbox").first
    search_box.click()
    search_box.fill("super wings")
    page.get_by_text("Show all 240 episodes").click()

    # Select specific episode
    episode = "Fire Drill Heroes S1E203"
    page.get_by_role("row", name=episode).locator("i").nth(3).click()
    page.get_by_role("button", name="Start").click()
    page.get_by_text("Show all 240 episodes").click()
    page.get_by_role("row", name=episode).get_by_role("link").nth(2).click()

    # Navigate to Image Upload Section
    page.locator("span").filter(has_text="Image").click()

    # Define File Paths Dynamically
    base_path = "path_to_your_images_folder"  # Change this to your actual image directory
    formats = [
        ("16x9_notitle", 0),
        ("16x9_withtitle", 1),
        ("3x4", 2),
        ("4x3", 3),
        ("16x9_withtitle", 4),
    ]

    for format, index in formats:
        file_path = os.path.join(base_path, f"{episode}_{format}.jpg")
        if os.path.exists(file_path):
            page.get_by_role("button", name="Browse").nth(index).click()
            page.get_by_role("button", name="Browse").nth(index).set_input_files(file_path)

    # Upload and Mark as Done
    page.get_by_role("button", name="Upload").click()
    page.get_by_role("button", name="Done Mark as done").click()
