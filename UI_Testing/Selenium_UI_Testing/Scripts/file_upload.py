from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
#test data
from data.test_data import FILE_UPLOAD_URL, FILE_PATH  # Import test data


def test_file_upload():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Navigate to the File Upload page
        driver.get(FILE_UPLOAD_URL)

        # Upload the file
        upload_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "file-upload"))
        )
        upload_input.send_keys(FILE_PATH)

        # Click the "Upload" button
        driver.find_element(By.ID, "file-submit").click()

        # Verify the uploaded file name
        uploaded_file = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "uploaded-files"))
        ).text
        assert "file.txt" in uploaded_file, f"Expected 'file.txt', but found '{uploaded_file}'"
        print("Test Passed: File uploaded successfully.")

    except TimeoutException:
        print("Test Failed: Element not found within the specified timeout.")
    except AssertionError as e:
        print(f"Test Failed: {e}")
    finally:
        driver.quit()

# Run the test
if __name__ == "__main__":
    test_file_upload()
