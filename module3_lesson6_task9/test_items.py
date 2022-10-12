from selenium.webdriver.common.by import By


class TestLanguage:
    def test_check_button(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        assert browser.find_elements(By.CLASS_NAME, 'btn-add-to-basket'), 'button not found'
