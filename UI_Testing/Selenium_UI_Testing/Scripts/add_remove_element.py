from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
#test data
from data.test_data import ADD_REMOVE_URL  # Import test data



def test_add_remove_elements():
    # Initialize the WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Navigate to the Add/Remove Elements page
        driver.get(ADD_REMOVE_URL)

        # Wait for the "Add Element" button to be visible
        add_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "button[onclick='addElement()']"))
        )

        # Click the "Add Element" button 3 times
        for _ in range(3):
            add_button.click()

        # Verify that 3 "Delete" buttons are added
        delete_buttons = driver.find_elements(By.CSS_SELECTOR, "button.added-manually")
        assert len(delete_buttons) == 3, f"Expected 3 delete buttons, but found {len(delete_buttons)}"
        print("Test Passed: Correct number of 'Delete' buttons added.")

        # Click each "Delete" button to remove the elements
        for button in delete_buttons:
            button.click()

        # Verify that all "Delete" buttons are removed
        delete_buttons_after = driver.find_elements(By.CSS_SELECTOR, "button.added-manually")
        assert len(delete_buttons_after) == 0, f"Expected 0 delete buttons, but found {len(delete_buttons_after)}"
        print("Test Passed: All 'Delete' buttons removed successfully.")

    except TimeoutException:
        print("Test Failed: Element not found within the specified timeout.")
    except AssertionError as e:
        print(f"Test Failed: {e}")
    except NoSuchElementException as e:
        print(f"Test Failed: {e}")
    finally:
        # Quit the browser
        driver.quit()

# Run the test
if __name__ == "__main__":
    test_add_remove_elements()
