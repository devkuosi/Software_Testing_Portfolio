from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
# Test data
from data.test_data import DROPDOWN_URL  

def test_dropdown_selection():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Navigate to the Dropdown page
        driver.get(DROPDOWN_URL)

        # Select an option from the dropdown
        dropdown = Select(driver.find_element(By.ID, "dropdown"))
        dropdown.select_by_visible_text("Option 1")

        # Verify the selected option
        selected_option = dropdown.first_selected_option.text
        assert selected_option == "Option 1", f"Expected 'Option 1', but found '{selected_option}'"
        print("Test Passed: Dropdown selection works as expected.")

    except NoSuchElementException as e:
        print(f"Test Failed: {e}")
    except AssertionError as e:
        print(f"Test Failed: {e}")
    finally:
        driver.quit()

# Run the test
if __name__ == "__main__":
    test_dropdown_selection()
