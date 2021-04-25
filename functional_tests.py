from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # The user goes to the homepage for our site
        self.browser.get('http://localhost:8000')

        # The user notices that the page title mentions to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # User can enter item into list right away

        # User types "Purchase laundry detergent" into text box

        # User hits enter, page updates, page shows entered task

        # Text box present for another entry

        # page updates again, shows both items

        # website creates unique URL to remember her list

        # user visits URL and list is still there


if __name__ == '__main__':
    unittest.main()
