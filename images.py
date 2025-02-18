import os
from playwright.sync_api import sync_playwright

def run(playwright):
    # Define the path to your Firefox user data directory
    user_data_dir = "/home/josh/.mozilla/firefox/profile1"  # Update this to your actual Firefox profile path
    
    # Launch Firefox with persistent context
    browser = playwright.firefox.launch_persistent_context(user_data_dir, headless=False)
    
    # Create a new page
    page = browser.new_page()
    page.goto("https://delta.stockholmstream.net/spa/brand/192cec3d-3f30-4c01-b842-debf835aef0a/rights")

    # Navigate to Series and Search
    page.get_by_text("Series", exact=True).click()
    search_box = page.get_by_role("row", name="Filter... Start End Type").get_by_role("searchbox").first
    search_box.click()
    search_box.fill("super wings")
    page.get_by_text("Show all 240 episodes").click()

    import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://delta.stockholmstream.net/")
    page.get_by_role("link", name="Log in").click()
    page.get_by_role("textbox", name="Enter Email...").click()
    page.get_by_role("textbox", name="Enter Email...").fill("douglas@yippee.tv")
    page.get_by_role("textbox", name="Enter Email...").press("Tab")
    page.get_by_role("textbox", name="Enter Password...").fill("Alvinman1!")
    page.get_by_role("textbox", name="Enter Password...").press("Enter")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("textbox", name="Enter Confirmation Code...").click()
    page.get_by_role("textbox", name="Enter Confirmation Code...").press("Alt+z")
    page.locator("div").filter(has_text="LoginConfirmation Code*").nth(2).click()
    page.get_by_role("textbox", name="Enter Confirmation Code...").click()
    page.get_by_role("textbox", name="Enter Confirmation Code...").fill("936109")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="Rights").click()
    page.get_by_text("Series", exact=True).click()
    page.get_by_role("row", name="Filter... Start End Type").get_by_role("searchbox").first.click()
    page.get_by_role("row", name="Filter... Start End Type").get_by_role("searchbox").first.fill("super wings")
    page.get_by_text("Show all 240 episodes").click()
    page.get_by_role("button", name="mediation").click()
    page.get_by_role("row", name="Pelmeni Panic S1E204 Janson").get_by_role("link").nth(2).click()
    page.get_by_role("button", name="Browse").first.click()
    page.get_by_role("button", name="Browse").first.set_input_files("Pelmeni Panic S1E204_16x9_withtitle.jpg")
    page.get_by_role("button", name="Upload").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)



    with sync_playwright() as playwright:
        run(playwright)