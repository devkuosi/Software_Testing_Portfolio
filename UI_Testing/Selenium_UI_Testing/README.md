
- **Scripts/**: Contains Python scripts for Selenium-based UI tests.
- **data/**: Stores test data such as URLs and credentials used by the test scripts.

## Example Test: Basic Authentication

The `Scripts/basic_auth.py` script demonstrates how to automate a basic authentication flow:

- Launches a Chrome browser using Selenium WebDriver.
- Navigates to a protected URL with credentials.
- Verifies that the login was successful by checking for a success message on the page.
- Handles assertion failures and ensures the browser is closed after the test.

## How to Run the Tests

1. **Install dependencies**  
   Make sure you have Python and Selenium installed.
   Download the appropriate ChromeDriver for your Chrome version and ensure it is in your system PATH.

2. **Configure test data** 
   Edit `data/test_data.py` to set the correct `AUTH_URL` and any other required test data.

3. **Run the test script**  

## Best Practices

- Keep test data separate from test logic for maintainability.
- Use assertions to validate expected UI outcomes.
- Always close the browser in a `finally` block to ensure resources are released.

## Extending

You can add more test scripts in the `Scripts/` directory following the same pattern. For more complex scenarios, consider using Selenium’s Page Object Model and integrating with test runners like `pytest` for better organization and reporting.

---

**This folder demonstrates how to automate and validate web UI flows using Selenium, providing a foundation for robust end-to-end testing.**