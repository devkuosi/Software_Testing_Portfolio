# test_data.py

import os


URL = "https://the-internet.herokuapp.com"
AUTH_URL = "https://admin:admin@the-internet.herokuapp.com/basic_auth"
FILE_PATH = os.path.abspath("UI_Testing/Selenium_UI_Testing/Scripts/data/file.txt")
# Test data for various test cases
LOGIN_URL = f"{URL}/login" 
ADD_REMOVE_URL = f"{URL}/add_remove_elements/"
FILE_UPLOAD_URL = f"{URL}/upload"
DROPDOWN_URL = f"{URL}/dropdown"
CHECKBOX_URL = f"{URL}/checkboxes"
USERNAME = "tomsmith"
PASSWORD = "SuperSecretPassword!"