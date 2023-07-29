import argparse  # Importing the argparse module to handle command-line arguments
from test_purchase_item import TestPurchaseScenario
from test_user_registration import TestRegistrationScenario
from test_filter_search import FilterSearchScenario
from test_registration_login_error_handling import RegistrationLoginErrorHandlingScenario

if __name__ == "__main__":
    # Creating an ArgumentParser object to handle command-line arguments
    parser = argparse.ArgumentParser(description="Web Application Regression Testing Suite")

    # Adding a positional argument 'test' to specify which test to run
    parser.add_argument("test", choices=["purchase", "registration", "filter_search", "error_handling"],
                        help="Specify which test to run: purchase, registration, filter_search, error_handling")

    # Parsing the command-line arguments
    args = parser.parse_args()

    # Checking the value of 'test' and executing the corresponding test scenario
    if args.test == "purchase":
        test = TestPurchaseScenario()
        test.run_test()

    elif args.test == "registration":
        test = TestRegistrationScenario()
        test.run_test()

    elif args.test == "filter_search":
        test = FilterSearchScenario()
        test.run_test()

    elif args.test == "error_handling":
        test = RegistrationLoginErrorHandlingScenario()
        test.test_registration_error_handling()

    else:
        # If an invalid test name is provided, display an error message
        print("Invalid test name. Please choose from: purchase, registration, filter_search, error_handling")
