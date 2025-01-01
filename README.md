This script tests the table search functionality on the LambdaTest Table Sort and Search Demo
By searching for "New York" and checking that the search results show 5 entries out of a total of 24
First of all we'll need Python 3.x ,Google Chrome .
And then install Selenium and pytest by running pip install selenium pytest in our terminal.
Then setup and launch chromedriver , finding the elements and writing the codes for that.
Saving the script as qa_selenium_test.py in our project directory, open a terminal,navigate to the directory containing the script,
And run using pytest qa_selenium_test.py.
The script will open Chrome, navigate to the test page, search for "New York" in the search box.
And validates that the search results show 5 entries out of 24 total entries.
If the test passes, it will print a success message.
