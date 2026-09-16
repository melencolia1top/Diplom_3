from selenium.webdriver.common.by import By

from data import Ingredients


class MainPageLocators:
    CONSTRUCTOR_LINK = (By.XPATH, '//p[text()="Конструктор"]')
    FEED_LINK = (By.XPATH, '//p[text()="Лента Заказов"]')

    INGREDIENT = (By.CSS_SELECTOR, f'a[href="/ingredient/{Ingredients.BUN_ID}"]')
    INGREDIENT_COUNTER = (
        By.XPATH,
        f'//a[@href="/ingredient/{Ingredients.BUN_ID}"]'
        '//p[contains(@class,"counter__num")]',
    )
    CONSTRUCTOR_DROP_AREA = (
        By.XPATH,
        '//section[contains(@class,"BurgerConstructor_basket")]',
    )

    INGREDIENT_MODAL_TITLE = (By.XPATH, '//h2[text()="Детали ингредиента"]')
    INGREDIENT_MODAL_CLOSE = (
        By.XPATH,
        '//section[.//h2[text()="Детали ингредиента"]]//button',
    )

    CREATE_ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')
    ORDER_NUMBER = (
        By.XPATH,
        '//p[text()="идентификатор заказа"]/preceding-sibling::h2',
    )
    ORDER_MODAL_CLOSE = (
        By.XPATH,
        '//section[.//p[text()="идентификатор заказа"]]//button',
    )

