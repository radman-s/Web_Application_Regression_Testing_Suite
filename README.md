# Web Application Regression Testing Suite

## Introduction
This is a comprehensive Web Application Regression Testing Suite built using Python and Selenium WebDriver. The suite consists of four individual tests to cover various aspects of the web application.

## Test Scenarios
The following test scenarios are included in the suite:

**1. Test Registration Scenario:**

1. Load test data from the JSON file (`pages/test_data_magento.json`).
2. Generate a fake email using the Faker library for registration.
3. Set up the browser driver and initialize the `MagentoPage` object.
4. Verify the homepage title:
   a. Get the actual homepage title.
   b. Get the expected homepage title from the loaded test data.
   c. Compare the actual and expected homepage titles.
   d. If they do not match, raise an assertion error.
5. Register a new account:
   a. Click on the "Create Account" button on the Magento website.
   b. Input the first name, last name, generated email, and password from the test data into their respective input fields.
   c. Confirm the password by inputting it again into the confirmation input field.
   d. Click on the "Create Account" button to complete the registration process.
6. Verify the presence of the confirmation message:
   a. Assert that the confirmation message is displayed on the page.
7. Verify the customer account URL:
   a. Get the actual URL of the current page.
   b. Get the expected customer account URL from the test data.
   c. Compare the actual and expected URLs.
   d. If they do not match, raise an assertion error.
8. Log out from the customer account:
   a. Click on the account link on the page.
   b. Click on the "Log Out" link to log out from the customer account.
9. Verify the sign-out message:
   a. Get the actual sign-out message from the page.
   b. Get the expected sign-out message from the test data.
   c. Compare the actual and expected sign-out messages.
   d. If they do not match, raise an assertion error.
10. Sign in using the registered credentials:
    a. Click on the "Sign In" link on the page.
    b. Input the generated email and password from the test data into their respective input fields.
    c. Click on the "Sign In" button to sign in.
11. Verify the email in the contact information:
    a. Get the expected email from the generated fake email.
    b. Assert that the expected email is present in the contact information on the page.
12. Print "Registration Test passed" if all the steps are executed successfully without any exceptions.



**2. Registration and Login Error Handling Scenario:**

1. Load test data from the JSON file (`pages/test_data_magento.json`).
2. Generate a fake email using the Faker library for registration.
3. Set up the browser driver and initialize the `MagentoPage` object.
4. Navigate to the Magento website.
5. Registration Error Handling:
   a. Click on the "Create Account" button on the Magento website (without filling any details).
   b. Assert that all required fields display the appropriate error message for being left blank.
   c. Enter correct first name and last name.
   d. Enter an invalid email and an invalid password.
   e. Click on the "Create Account" button and assert the error handling for an invalid email and an invalid password.
   f. Clear the invalid credentials and enter a valid email and password but with a different confirmation password.
   g. Click on the "Create Account" button and assert the error handling for mismatching passwords.
   h. Create a valid account with a unique email and log out.
6. Login Error Handling:
   a. Click on the "Sign In" link on the Magento website (without filling any details).
   b. Assert that all required fields on the login page display the appropriate error message for being left blank.
   c. Enter an invalid email format and assert the error handling for an invalid email on the login page.
   d. Enter a valid email and an invalid password.
   e. Click on the "Sign In" button and assert the error handling for an invalid signin.
7. Print "Registration and Login Error Handling Test passed" if all the steps are executed successfully without any exceptions.



**3. Test Purchase Scenario:**

1. Load test data from the JSON file (`pages/test_data_magento.json`).
2. Generate a fake email using the Faker library for registration.
3. Set up the browser driver and initialize the `MagentoPage` object.
4. Verify the homepage title:
   a. Get the actual homepage title.
   b. Get the expected homepage title from the loaded test data.
   c. Compare the actual and expected homepage titles.
   d. If they do not match, raise an assertion error.
5. Verify the product details:
   a. Input the search product into the search input field on the Magento website.
   b. Press the Enter key to search for the product.
   c. Get the name of the first item found.
   d. Click on the first item to open its details page.
   e. Assert that the title of the details page matches the name of the selected product.
   f. Select the size "M" for the item.
   g. Select the first available color option for the item.
   h. Clear the quantity input field and input the desired quantity from the test data.
   i. Click the "Add to Cart" button.
   j. Assert that the shopping cart message displays "You added {product_name} to your shopping cart.".
6. Verify the shopping cart:
   a. Click on the shopping cart button.
   b. Assert that the item name in the summary is displayed.
   c. Assert that the item name in the summary matches the selected product name.
   d. Click the "Checkout" button.
7. Verify the shipping page:
   a. Input the phone number, first name, last name, company, street, city, and ZIP from the test data into their respective input fields.
   b. Select the country from the dropdown.
   c. Choose the "Flat Rate" shipping option.
   d. Input the generated fake email into the email input field.
   e. Click the "Next" button to proceed to the payment page.
   f. Assert that the checkout URL matches the expected shipping URL from the test data.
8. Verify the payment page:
   a. Assert that the "Place Order" button is displayed.
   b. Assert that the current URL matches the expected payment URL from the test data.
   c. Assert that the first name and last name from the test data are present in the billing details text.
   d. Click the "Place Order" button.
   e. Get the order number text from the page.
   f. Use regular expressions to search for the order number pattern from the test data in the order number text.
   g. If the order number pattern is not found, raise an assertion error.
9. Print "Purchase Test passed" if all the steps are executed successfully without any exceptions.



**4. Filter and Search Test Scenario:**

1. Load test data from the JSON file (`pages/test_data_magento.json`).
2. Set up the browser driver and initialize the `MagentoPage` object.
3. Navigate to the Magento website and verify the homepage title matches the expected title from the test data.
4. Navigate to the jackets section for women.
5. Check product listing by alphabetical order:
   a. Click on the "Sort by" expand icon.
   b. Select "Name" from the sort options.
   c. Retrieve the names of the first 12 jackets listed.
   d. Verify that the names are in alphabetical order.
6. Check product listing by numeric order from lowest to highest:
   a. Click on the "Sort by" expand icon.
   b. Select "Price" from the sort options.
   c. Retrieve the prices of the first 12 jackets listed.
   d. Verify that the prices are in numeric order from lowest to highest.
7. Check filter by price range:
   a. Click on the "Price" expand icon.
   b. Retrieve the price range of the first filter option (`shopping_price_1`).
   c. Click on the first filter option.
   d. Retrieve the prices of the first 12 jackets listed after applying the filter.
   e. Verify that all prices fall within the expected price range.
8. Go back to the previous page.
9. Check filter by another price range:
   a. Click on the "Price" expand icon.
   b. Retrieve the price range of the second filter option (`shopping_price_2`).
   c. Click on the second filter option.
   d. Retrieve the prices of the first 12 jackets listed after applying the filter.
   e. Verify that all prices fall within the expected price range.

10. Print "Filter Test passed" if all the steps are executed successfully without any exceptions.


## How to Run the Tests
To run the tests, you can use the main_script.py provided in the repository. The script allows you to specify which test scenario to run as follows:

python main_script.py test_name
Replace test_name with one of the following options: purchase, registration, filter_search, or error_handling.

Apologies for the oversight. Selenium WebDriver is indeed a requirement for running the Web Application Regression Testing Suite. Here's the updated list of requirements:


**Requirements:**

1. Python 3.x
2. Selenium WebDriver
3. Chrome WebDriver (compatible with your Chrome browser version)
4. Faker library
5. Requests library
6. JSON library
7. argparse library
8. Chrome WebDriver: Since the test suite is designed to work with Google Chrome, you need to download the Chrome WebDriver executable compatible with your Chrome browser version. 
   To download and set up Chrome WebDriver, follow the instructions provided in the official Selenium documentation: https://sites.google.com/a/chromium.org/chromedriver/downloads

Please ensure you have installed all these libraries in your Python environment to successfully execute the tests in the Web Application Regression Testing Suite.


**Installation**
1. Clone this repository to your local machine.
2. Install the required Python packages using pip:
- pip install selenium 
- pip install requests
- pip install Faker


**Feedback and Contributions**
Feedback and contributions to this testing suite are welcome! Feel free to open an issue or submit a pull request.


**License**
This project is licensed under the MIT License.
