# Manual Testing of E-Commerce Website

## Scope 

The testing will cover :
	- Functional Testing
	- UI/UX Testing
	- Compatibility Testing
	- Database Testing
	- Security Testing (basic level)
	- Regression Testing

## Project Details

	Application Name: ShopEase
	Domain: E-commerce
	Modules to Test:
		User Authentication
		Product Search
		Product Details Page
		Shopping Cart
		Checkout Process
		Order History

## Test Plan

### Functional Requirements:

- User should be able to log in and log out.
- Users can search for products by name, category, or price.
- Product details page should display accurate product information.
- Users can add, update, or remove items in the shopping cart.
- Checkout process should handle payments securely and accurately.
- Users can view their past orders in the "Order History" section.

### Non-Functional Requirements:

- Website should load within 3 seconds.
- The website should be compatible with major browsers (Chrome, Firefox, Edge).
- Database queries should be executed efficiently.


## Test Scenarios

### Module 1: User Authentication
	Verify login with valid credentials.
	Verify login with invalid credentials.
	Verify password recovery functionality.
	Verify logout functionality.

### Module 2: Product Search
	Verify searching with exact product names.
	Verify searching with partial product names.
	Verify sorting and filtering of search results.

### Module 3: Product Details Page
	Verify product description, price, and stock availability.
	Verify "Add to Cart" button functionality.
	Verify that images are displayed properly.

### Module 4: Shopping Cart
	Verify items can be added to the cart.
	Verify items can be removed from the cart.
	Verify the cart updates total price correctly.

### Module 5: Checkout Process
	Verify users can enter shipping information.
	Verify users can select payment methods.
	Verify payment gateway integration works correctly.

### Module 6: Order History
	Verify past orders are displayed correctly.
	Verify order details are accurate.

## Test Cases

### Test Case 1: Login with Valid Credentials
- **Test Case ID:** TC_Auth_01
- **Module:**  User Authentication.
- **Steps:**
1. Navigate to the login page.
  2. Enter a valid email and password.
  3. Click on the "Login" button.
- **Expected Result:** User should be redirected to the homepage and greeted with a welcome message.

### Test Case 2: Login with Invalid Credentials
- **Test Case ID:** TC_Auth_02
- **Module:**  User Authentication.
- **Steps:**
1. Navigate to the login page.
  2. Enter a invalid email and/or password.
  3. Click on the "Login" button.
- **Expected Result:** User should be see an error message telling that the credentials are incorrect.

### Test Case 3: Password Recovery
- **Test Case ID:** TC_Auth_03
- **Module:**  User Authentication.
- **Steps:**
1. Navigate to the login page.
  2. Click on the "Forgot Password" link.
  3. Enter a valid email address.
  4. Click on the "Recover Password" button.
- **Expected Result:** User should receive an email with instructions to reset the password.

### Test Case 4: Logout
- **Test Case ID:** TC_Auth_04
- **Module:**  User Authentication.
- **Pre-condition:**  User should be logged in.
- **Steps:**
1. Click on the "Logout" button.
- **Expected Result:** User should be redirected to the login page.

### Test Case 5: Search by Product Name
- **Test Case ID:** TC_Search_01
- **Module:**  Product Search.
- **Steps:**
1. Enter a product name in the search bar.
  2. Click on the "Search" button.
- **Expected Result:** Products with matching names should be displayed.

### Test Case 6: Search by Category
- **Test Case ID:** TC_Search_02
- **Module:**  Product Search.
- **Steps:**
1. Select a category from the dropdown menu.
  2. Click on the "Search" button.
- **Expected Result:** Products from the selected category should be displayed.

### Test Case 7: Search by Price Range
- **Test Case ID:** TC_Search_03
- **Module:**  Product Search.
- **Steps:**
1. Enter a price range in the search bar.
  2. Click on the "Search" button
- **Expected Result:** Products within the specified price range should be displayed.
- **Note:** The price range should be in the format "min-max" (e.g., 10-50).
- **Note:** The search results should include products with prices equal to the min or max values.

### Test Case 8: Product Details
- **Test Case ID:** TC_Product_01
- **Module:**  Product Details Page.
- **Steps:**
1. Navigate to a product's details page.
- **Expected Result:** The product details should include the name, description, price, and images.
- **Note:** The product details should be accurate and up-to-date.


### Test Case 9: Add Product to Cart
- **Test Case ID:** TC_Cart_01
- **Module:**  Shopping Cart.
- **Pre-condition:**  User should be logged in.
- **Steps:**
1. Navigate to a product's details page.
2. Click on the "Add to Cart" button.
3. Go to the cart page.
- **Expected Result:**The product should appear in the cart with correct details (name, price, quantity).

### Test Case 10: Remove Product from Cart
- **Test Case ID:** TC_Cart_02
- **Module:**  Shopping Cart.
- **Pre-condition:**  User should have at least one item in the cart.
- **Steps:**
1. Navigate to the cart page.
2. Click on the "Remove" button next to a product.
3. Confirm the removal.
4. Verify that the product is no longer in the cart.
5. Verify that the total price is updated.

- **Expected Result:** The product should be removed from the cart, and the total price should be updated accordingly.

### Test Case 11: Update Product Quantity in Cart
- **Test Case ID:** TC_Cart_03
- **Module:**  Shopping Cart.
- **Pre-condition:**  User should have at least one item in the cart.
- **Steps:**
1. Navigate to the cart page.
2. Change the quantity of a product.
3. Verify that the total price is updated.
4. Click on the "Update" button.
5. Verify that the quantity is updated.
6. Verify that the total price is updated.

- **Expected Result:** The quantity of the product should be updated, and the total price should be recalculated.

### Test Case 12: Checkout Process
- **Test Case ID:** TC_Checkout_01
- **Module:**  Checkout Process.
- **Pre-condition:**  User must have at least one item in the cart.
- **Steps:**
1. Navigate to the cart page.
2. Click on "Checkout."
3. Enter valid shipping and payment information.
4. Submit the order.
5. Verify that the order is placed successfully.

- **Expected Result:** The order should be placed successfully, and a confirmation message should appear.
- **Note:** The order details should be saved in the database.

### Test Case 13: View Order History
- **Test Case ID:** TC_Order_01
- **Module:**  Order History.
- **Pre-condition:**  User should have at least one order placed.
- **Steps:**
1. Navigate to the order history page.
2. Verify that the past orders are displayed.
3. Click on an order to view the details.
4. Verify that the order details are accurate.
5. Verify that the order status is correct.
6. Verify that the total price is correct.
7. Verify that the shipping address is correct.
8. Verify that the payment method is correct.

- **Expected Result:** The past orders should be displayed with accurate details.

### Test Case 14: Website Loading Time
- **Test Case ID:** TC_NFR_01
- **Module:**  Non-Functional Requirements.
- **Steps:**
1. Access the website.
2. Measure the time taken to load the homepage.
3. Repeat the test multiple times.
4. Calculate the average loading time.
5. Compare the average loading time with the requirement.
6. Record the results.
7. Analyze the results.
8. Report any discrepancies.

- **Expected Result:** The website should load within 3 seconds on average.


### Test Case 15: Browser Compatibility
- **Test Case ID:** TC_NFR_02
- **Module:**  Non-Functional Requirements.
- **Steps:**
1. Access the website using Chrome.
2. Access the website using Firefox.
3. Access the website using Edge.
4. Verify that the website is displayed correctly in each browser.
5. Verify that all features are functional in each browser.
6. Record any discrepancies.
7. Report any issues.

- **Expected Result:** The website should be compatible with major browsers (Chrome, Firefox, Edge).

### Test Case 16: Database Query Performance
- **Test Case ID:** TC_NFR_03
- **Module:**  Non-Functional Requirements.
- **Steps:**
1. Perform a search operation.
2. Perform an insert operation.
3. Perform an update operation.
4. Perform a delete operation.
5. Measure the time taken for each operation.
6. Repeat the test multiple times.
7. Calculate the average time for each operation.
8. Compare the average times with the requirement.
9. Record the results.
10. Analyze the results.
11. Report any discrepancies.

- **Expected Result:** Database queries should be executed efficiently.

### Test Case 17: Security Testing
- **Test Case ID:** TC_NFR_04
- **Module:**  Non-Functional Requirements.
- **Steps:**
1. Verify that the website uses HTTPS.
2. Verify that user passwords are encrypted.
3. Verify that sensitive information is not stored in cookies.
4. Verify that the website is protected against SQL injection.
5. Verify that the website is protected against cross-site scripting (XSS).
6. Verify that the website is protected against cross-site request forgery (CSRF).
7. Verify that the website is protected against session hijacking.
8. Verify that the website is protected against clickjacking.
9. Verify that the website is protected against brute force attacks.
10. Verify that the website is protected against DDoS attacks.

- **Expected Result:** The website should meet basic security standards.