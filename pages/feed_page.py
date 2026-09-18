import allure

from locators.feed_page_locators import FeedPageLocators
from pages.base_page import BasePage


class FeedPage(BasePage):
    @allure.step('Проверить, что заголовок ленты заказов отображается')
    def title_is_visible(self):
        return self.find(FeedPageLocators.PAGE_TITLE).is_displayed()

    @allure.step('Получить счётчик выполненных заказов за всё время')
    def get_all_time_counter(self):
        return int(self.get_text(FeedPageLocators.ALL_TIME_COUNTER))

    @allure.step('Получить счётчик выполненных заказов за сегодня')
    def get_today_counter(self):
        return int(self.get_text(FeedPageLocators.TODAY_COUNTER))

    @allure.step('Дождаться увеличения счётчика «Выполнено за всё время»')
    def wait_all_time_counter_greater_than(self, old_value):
        self.wait.until(lambda _: self.get_all_time_counter() > old_value)
        return self.get_all_time_counter()

    @allure.step('Дождаться увеличения счётчика «Выполнено за сегодня»')
    def wait_today_counter_greater_than(self, old_value):
        self.wait.until(lambda _: self.get_today_counter() > old_value)
        return self.get_today_counter()

    @allure.step('Получить номера заказов в разделе «В работе»')
    def get_in_work_order_numbers(self):
        elements = self.find_all(FeedPageLocators.ORDERS_IN_WORK)
        numbers = []
        for element in elements:
            text = element.text.strip().lstrip('#')
            if text.isdigit():
                numbers.append(int(text))
        return numbers

    @allure.step('Дождаться номера заказа в разделе «В работе»')
    def wait_order_in_work(self, order_number):
        self.wait.until(lambda _: order_number in self.get_in_work_order_numbers())
        return self.get_in_work_order_numbers()