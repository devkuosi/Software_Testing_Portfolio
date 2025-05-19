from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
# Test data
from data.test_data import CHECKBOX_URL  

def test_checkbox_selection():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Navigate to the Checkboxes page
        driver.get(CHECKBOX_URL)

        # Locate the checkboxes
        checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

        # Select the first checkbox if not already selected
        if not checkboxes[0].is_selected():
            checkboxes[0].click()

        # Verify the first checkbox is selected
        assert checkboxes[0].is_selected(), "Test Failed: First checkbox is not selected."

        # Deselect the second checkbox if selected
        if checkboxes[1].is_selected():
            checkboxes[1].click()

        # Verify the second checkbox is deselected
        assert not checkboxes[1].is_selected(), "Test Failed: Second checkbox is still selected."

        print("Test Passed: Checkbox selection and deselection work as expected.")

    except NoSuchElementException as e:
        print(f"Test Failed: {e}")
    except AssertionError as e:
        print(f"Test Failed: {e}")
    finally:
        driver.quit()

# Run the test
if __name__ == "__main__":
    test_checkbox_selection()
