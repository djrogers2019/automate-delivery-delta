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

    # Define File Paths Dynamically
    base_path = "/home/josh/Downloads/IMAGES"  # Change this to your actual image directory
    image_formats = ["16x9_notitle", "16x9_withtitle", "3x4", "4x3"]
    
    uploaded_files = 0  # Counter to check if files were uploaded

    for index, format in enumerate(image_formats):
        file_name = f"{episode}_{format}.jpg"
        file_path = os.path.join(base_path, file_name)

    if os.path.exists(file_path):
        print(f"Uploading: {file_path}")  # Debugging

        # Find the real input[type=file] field instead of clicking "Browse"
        file_input = page.locator("input[type='file']").nth(index)

        # Wait for the input field to be available
        file_input.wait_for(state="attached")

        # Upload the file directly to the input field
        file_input.set_input_files(file_path)

    if uploaded_files == 0:
        print("No matching image files found. Skipping upload.")
        return  # Stop the script if no files are available

    # Wait for the Upload button to become enabled
    upload_button = page.get_by_role("button", name="Upload")
    upload_button.wait_for(state="visible")
    upload_button.wait_for(state="enabled")  # Ensure it's clickable
    upload_button.click()

    # Wait for the upload to finish (Adjust selector if needed)
    page.wait_for_timeout(5000)  # Wait for 5 seconds (increase if needed)

    # Wait for the "Done Mark as done" button to be visible and click it
    done_button = page.get_by_role("button", name="Done Mark as done")
    done_button.wait_for(state="visible")
    done_button.click()

    # Keep the browser open until manually closed
    input("Press Enter to close the browser...")  

    # Close the browser when done
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
