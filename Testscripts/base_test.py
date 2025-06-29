from Pages.base_page import BaseTest

class TestBase(BaseTest):
    def test_base_page_valid(self):
        assert self.driver.title == "OrangeHRM", "Title does not match"
        print("\n\nBase page test passed!")
        assert self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", "URL does not match"
        print("\n\nBase page URL test passed!")
        