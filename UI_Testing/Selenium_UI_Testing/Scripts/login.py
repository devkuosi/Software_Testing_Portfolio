from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
#test data
from data.test_data import LOGIN_URL, USERNAME, PASSWORD  # Import test data


def test_login():
    # Initialize the WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()  # Optional: Maximize the browser window for better visibility

    try:
        # Navigate to the login page
        driver.get(LOGIN_URL)

        # Wait for the username field to be visible and enter credentials
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(USERNAME)
        driver.find_element(By.ID, "password").send_keys(PASSWORD)

        # Click the login button
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Wait for the success message to appear
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "flash"))
        ).text

        # Assert the success message
        assert "You logged into a secure area!" in success_message
        print("Test Passed: Login functionality works as expected.")

    except TimeoutException:
        print("Test Failed: Element not found within the specified timeout.")
    except NoSuchElementException as e:
        print(f"Test Failed: {e}")
    except AssertionError:
        print("Test Failed: Success message assertion failed.")
    finally:
        # Quit the browser
        driver.quit()

# Run the test
if __name__ == "__main__":
    test_login()
