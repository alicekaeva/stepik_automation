import time
import math
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.parametrize('urls', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
class TestAliens:
    def test_stepik_aliens(self, browser, urls):
        link = f"https://stepik.org/lesson/{urls}/step/1"
        browser.get(link)
        browser.implicitly_wait(10)
        area = browser.find_element(By.CSS_SELECTOR, 'textarea')
        area.send_keys(str(math.log(int(time.time()))))
        button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
        )
        button.click()
        txt = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'smart-hints__hint'))
        )
        ans = txt.text
        assert "Correct!" == ans
