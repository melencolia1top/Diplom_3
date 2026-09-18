import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as conditions
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step('Открыть страницу {url}')
    def open(self, url):
        self.driver.get(url)

    def current_url(self):
        return self.driver.current_url

    @allure.step('Дождаться адреса страницы {url}')
    def wait_for_url(self, url):
        self.wait.until(conditions.url_to_be(url))

    def find(self, locator):
        return self.wait.until(conditions.visibility_of_element_located(locator))

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        self.wait.until(conditions.element_to_be_clickable(locator)).click()

    def click_via_script(self, locator):
        element = self.find(locator)
        self.driver.execute_script('arguments[0].click();', element)

    def enter_text(self, locator, text):
        element = self.wait.until(conditions.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text

    def wait_until_invisible(self, locator):
        self.wait.until(conditions.invisibility_of_element_located(locator))

    def drag_and_drop(self, source_locator, target_locator):
        source = self.find(source_locator)
        target = self.find(target_locator)

        if self.driver.name == 'firefox':
            self.driver.execute_script(
                """
                const source = arguments[0];
                const target = arguments[1];
                const dataTransfer = new DataTransfer();
                const options = {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer,
                };

                source.dispatchEvent(new DragEvent('dragstart', options));
                target.dispatchEvent(new DragEvent('dragenter', options));
                target.dispatchEvent(new DragEvent('dragover', options));
                target.dispatchEvent(new DragEvent('drop', options));
                source.dispatchEvent(new DragEvent('dragend', options));
                """,
                source,
                target,
            )
            return

        (
            ActionChains(self.driver)
            .move_to_element(source)
            .click_and_hold(source)
            .pause(0.5)
            .move_by_offset(5, 0)
            .pause(0.5)
            .move_to_element(target)
            .pause(1)
            .release()
            .perform()
        )