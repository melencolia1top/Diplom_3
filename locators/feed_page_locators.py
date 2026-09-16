from selenium.webdriver.common.by import By


class FeedPageLocators:
    PAGE_TITLE = (By.XPATH, '//h1[text()="Лента заказов"]')
    ALL_TIME_COUNTER = (
        By.XPATH,
        '//p[text()="Выполнено за все время:"]/following-sibling::p',
    )
    TODAY_COUNTER = (
        By.XPATH,
        '//p[text()="Выполнено за сегодня:"]/following-sibling::p',
    )
    ORDERS_IN_WORK = (
        By.XPATH,
        '//p[text()="В работе:"]/following-sibling::ul/li',
    )

