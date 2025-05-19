from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Test data
from data.test_data import AUTH_URL  # Import test data

def test_basic_auth():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Navigate to the Basic Auth page with credentials in the URL
        driver.get(AUTH_URL)

        # Verify the success message
        success_message = driver.find_element(By.TAG_NAME, "p").text
        assert "Congratulations" in success_message, f"Expected 'Congratulations', but found '{success_message}'"
        print("Test Passed: Basic authentication works as expected.")

    except AssertionError as e:
        print(f"Test Failed: {e}")
    finally:
        driver.quit()

# Run the test
if __name__ == "__main__":
    test_basic_auth()
