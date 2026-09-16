import allure

from data import Urls
from pages.feed_page import FeedPage
from pages.main_page import MainPage


@allure.feature('Основная функциональность')
class TestMainFunctionality:
    @allure.title('Переход по клику на «Конструктор»')
    def test_go_to_constructor(self, driver):
        page = MainPage(driver)
        page.open(Urls.FEED_PAGE)

        page.go_to_constructor()
        page.wait_for_url(Urls.BASE_URL)

        assert page.current_url() == Urls.BASE_URL

    @allure.title('Переход по клику на «Лента заказов»')
    def test_go_to_feed(self, driver):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        main_page.open(Urls.BASE_URL)

        main_page.go_to_feed()
        main_page.wait_for_url(Urls.FEED_PAGE)

        assert main_page.current_url() == Urls.FEED_PAGE
        assert feed_page.title_is_visible()

    @allure.title('При клике на ингредиент открывается окно с деталями')
    def test_ingredient_details_open(self, driver):
        page = MainPage(driver)
        page.open(Urls.BASE_URL)

        page.open_ingredient_details()

        assert page.ingredient_details_are_visible()

    @allure.title('Окно с деталями ингредиента закрывается по крестику')
    def test_ingredient_details_close(self, driver):
        page = MainPage(driver)
        page.open(Urls.BASE_URL)
        page.open_ingredient_details()

        page.close_ingredient_details()

        assert page.ingredient_details_are_closed()

    @allure.title('После добавления ингредиента его счётчик увеличивается')
    def test_ingredient_counter_increases(self, driver):
        page = MainPage(driver)
        page.open(Urls.BASE_URL)
        counter_before = page.get_ingredient_counter()

        page.add_ingredient_to_order()

        assert page.get_ingredient_counter() > counter_before

