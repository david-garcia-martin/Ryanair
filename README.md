# Ryanair Declined Payment Test

This test suite is designed to automate a booking up to a declined payment on Ryanair website. However, it's written in a way that additional test cases can be added for the different pages that appear in the process of getting this message since this project has only been developed to confirm the declined payment message.

## Structure
* common
	- ***common_functions.py*** includes all functions shared along the project. In addition, all configuration parameters are parsered here. Since Selenium WebDriver is used, sometimes websites takes a little bit longer to load. So an updated version of the methods have been created to wait for the elements to appear.
	- ***html_reports_template.html*** and ***six.py*** are used to generate the html report at the end of the testing.
	- ***Ryanair_config.txt*** consists on a .txt file that stores all configuration variables for the environment and the test cases such as web browser type, credit card information, login information, origing and destination airports, etc. 
* rynair_test
	- This python package includes all the structure for the test cases of Ryanair website. These tests use unittest testing framework (TDD approach) and modelled in a way that each page on the site has it´s own test cases and locators to folllow a page oriented pattern. Thus, there are different python packages for each page on the site: **ryanair_xxx_page**
	- For each package, 3 files are created to simplify the page oriented pattern and follow the best practices for testing:
		- ***xxx_page_features.py*** includes all the test scenarios for that specific page by calling the getters/setters for that specific page. In addition, all assertions would be included here. These test cases will be run in the test_all_xxx.page.py file
		- ***xxx_page_locators.py*** includes the necessary locators and getters/setters for the web elements on each specific page.
		- ***test_all_xxx_page.py*** all test cases will be initiated here by using the setUpClass from unittest framework, all the necessary setup and test clases will be inherit here to easily run the tests of each module on the page.
* ryanair_reports folder includes all the html reports the tests have been run.

## Requirements

### Python 3.x
Instructions to install if if not already done:
```bash
brew update && brew install python
```
Make python3 version as default:
```bash
alias python=/usr/local/bin/python3
```

### HtmlTestRunner: https://github.com/oldani/HtmlTestRunner
```bash
pip install html-testRunner
```

### Selenium 
```bash
pip install selenium
```
Make sure to download the ChromeDriver that matches the current Chrome version: https://sites.google.com/a/chromium.org/chromedriver/downloads.


## Run the tests

### Via Terminal
Make sure to download the code to the desired location and keep track of the location, so that the python path is correctly set:  

```bash
export PYTHONPATH="$PWD/path_to_Ryanair"
```
For example: export PYTHONPATH="$PWD/Desktop/Ryanair"

Run the test_all_payment_page.py test cases:

```bash
python /Users/davidgarcia/Desktop/Ryanair/ryanair_test/ryanair_payment_page/test_all_payment_page.py
```

Once the test is run, the html report will be located under: ryanair_reports.

### Via any IDE
The test can be also run as a unittest in any IDE like PyCharm.


## Edge cases

* Sometimes there's no flight availability for a selected date that appears as available. Due to simplicity this case is not handled.
