import allure

from data import Urls
from pages.feed_page import FeedPage
from pages.main_page import MainPage


@allure.feature('Лента заказов')
class TestOrderFeed:
    @allure.title(
        'После создания заказа счётчик за всё время увеличивается'
    )
    def test_all_time_counter_increases(self, authorized_driver):
        main_page = MainPage(authorized_driver)
        feed_page = FeedPage(authorized_driver)
        main_page.open(Urls.FEED_PAGE)
        counter_before = feed_page.get_all_time_counter()
        main_page.go_to_constructor()
        main_page.wait_for_url(Urls.BASE_URL)

        main_page.create_new_order()
        main_page.go_to_feed()
        main_page.wait_for_url(Urls.FEED_PAGE)

        assert (
            feed_page.wait_all_time_counter_greater_than(counter_before)
            > counter_before
        )

    @allure.title(
        'После создания заказа счётчик за сегодня увеличивается'
    )
    def test_today_counter_increases(self, authorized_driver):
        main_page = MainPage(authorized_driver)
        feed_page = FeedPage(authorized_driver)
        main_page.open(Urls.FEED_PAGE)
        counter_before = feed_page.get_today_counter()
        main_page.go_to_constructor()
        main_page.wait_for_url(Urls.BASE_URL)

        main_page.create_new_order()
        main_page.go_to_feed()
        main_page.wait_for_url(Urls.FEED_PAGE)

        assert (
            feed_page.wait_today_counter_greater_than(counter_before)
            > counter_before
        )

    @allure.title(
        'Номер нового заказа появляется в разделе «В работе»'
    )
    def test_new_order_appears_in_work(self, authorized_driver):
        main_page = MainPage(authorized_driver)
        feed_page = FeedPage(authorized_driver)

        order_number = main_page.create_new_order()
        main_page.go_to_feed()
        main_page.wait_for_url(Urls.FEED_PAGE)

        assert order_number in feed_page.wait_order_in_work(
            order_number
        )
