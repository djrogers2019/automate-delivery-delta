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

    '''Repeatable block of code, this can be used per episode'''

    # Select specific episode
    episode = "Pelmeni Panic S1E204"
    page.get_by_role("row", name=episode).locator("i").nth(3).click()

    # Wait for Image tab to load before interacting
    page.locator("span:has-text('Image')").wait_for(state="visible")
    page.locator("span").filter(has_text="Image").click()

    # ✅ **Wait for Manual Upload**
    print("Please manually upload your images. The script will wait for you to click 'Mark as Done'...")

    # Wait for the "Done Mark as done" button to appear, then ensure it's visible
    done_button = page.get_by_role("button", name="Done Mark as done")
    done_button.wait_for(state="visible")  # Wait for the button to be visible

    # Wait for the user to manually click the "Mark as Done" button
    input("Press Enter once you've finished uploading images and clicked 'Mark as Done'...")

    # After you press Enter, click the "Mark as Done" button to complete the process
    done_button.click()

    print("Uploads completed! Closing script...")

    # Close the browser after upload is done
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
