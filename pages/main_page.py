import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Перейти в «Конструктор»')
    def go_to_constructor(self):
        self.click_via_script(MainPageLocators.CONSTRUCTOR_LINK)

    @allure.step('Перейти в «Ленту заказов»')
    def go_to_feed(self):
        self.click_via_script(MainPageLocators.FEED_LINK)

    @allure.step('Открыть детали ингредиента')
    def open_ingredient_details(self):
        self.click(MainPageLocators.INGREDIENT)

    @allure.step('Проверить, что детали ингредиента отображаются')
    def ingredient_details_are_visible(self):
        return self.find(
            MainPageLocators.INGREDIENT_MODAL_TITLE
        ).is_displayed()

    @allure.step('Закрыть детали ингредиента')
    def close_ingredient_details(self):
        self.click(MainPageLocators.INGREDIENT_MODAL_CLOSE)
        self.wait_until_invisible(
            MainPageLocators.INGREDIENT_MODAL_TITLE
        )

    @allure.step('Проверить, что детали ингредиента закрыты')
    def ingredient_details_are_closed(self):
        elements = self.find_all(
            MainPageLocators.INGREDIENT_MODAL_TITLE
        )
        return not any(element.is_displayed() for element in elements)

    @allure.step('Получить значение счётчика ингредиента')
    def get_ingredient_counter(self):
        return int(
            self.get_text(MainPageLocators.INGREDIENT_COUNTER)
        )

    @allure.step('Добавить ингредиент в заказ')
    def add_ingredient_to_order(self):
        counter_before = self.get_ingredient_counter()
        self.drag_and_drop(
            MainPageLocators.INGREDIENT,
            MainPageLocators.CONSTRUCTOR_DROP_AREA,
        )
        self.wait.until(
            lambda _: self.get_ingredient_counter() > counter_before
        )

    @allure.step('Оформить заказ')
    def create_order(self):
        self.click(MainPageLocators.CREATE_ORDER_BUTTON)
        self.wait.until(
            lambda _: (
                self.get_text(MainPageLocators.ORDER_NUMBER).isdigit()
                and self.get_text(MainPageLocators.ORDER_NUMBER) != '9999'
            )
        )
        return int(
            self.get_text(MainPageLocators.ORDER_NUMBER)
        )

    @allure.step('Закрыть окно созданного заказа')
    def close_order_modal(self):
        self.click_via_script(MainPageLocators.ORDER_MODAL_CLOSE)
        self.wait_until_invisible(MainPageLocators.ORDER_NUMBER)

    @allure.step('Создать новый заказ')
    def create_new_order(self):
        self.add_ingredient_to_order()
        order_number = self.create_order()
        self.close_order_modal()
        return order_number
