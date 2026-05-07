from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.actions = ActionChains(driver)

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].click();", element)

    def get_text(self, locator):
        return self.find_element(locator).text

    def is_displayed(self, locator):
        return self.find_element(locator).is_displayed()

    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_current_url(self):
        return self.driver.current_url

    def wait_for_url(self, url_part):
        self.wait.until(EC.url_contains(url_part))

    def open_url(self, url):
        self.driver.get(url)

    def delete_all_cookies(self):
        self.driver.delete_all_cookies()

    def refresh_page(self):
        self.driver.refresh()

    def drag_and_drop(self, source, target):
        source_elem = self.find_element(source)
        target_elem = self.find_element(target)
        self.driver.execute_script("""
            var source = arguments[0];
            var target = arguments[1];
            var dataTransfer = new DataTransfer();
            var dragStartEvent = new DragEvent('dragstart', {
                dataTransfer: dataTransfer,
                bubbles: true,
                cancelable: true
            });
            var dropEvent = new DragEvent('drop', {
                dataTransfer: dataTransfer,
                bubbles: true,
                cancelable: true
            });
            source.dispatchEvent(dragStartEvent);
            target.dispatchEvent(dropEvent);
        """, source_elem, target_elem)
