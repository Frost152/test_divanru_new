from pages.main_page import MainPage
from pages.main_page import Catalog
import pages.popups as popups
from pages.filtres import BaseFilters
from pages.cart_page import CartPage


def test_smoke_buy_sofa(browser):
    driver = browser
    mp = MainPage(driver)
    mp.open()
    modal_wrap = popups.ModalWrapper(driver)
    popup_reg = popups.RegionPopup(driver)
    popup_reg.find_close_region_popup()
    mp.click_main_catalog()
    modal_wrap.find_and_close_modal_wrapper()

    catalog = Catalog(driver)
    catalog.go_to_sofas()
    filters = BaseFilters(driver)
    filters.click_all_filters_button()
    filters.open_all_filters()
    filters.move_range_min("Размеры", "Длина,  см", 3)
    fil = ("Банкетка", "Диван угловой", "Голубой", "Еврокнижка", "На низких опорах", "Трехместный", "Двуспальный")
    filters.selecting_multiple_filters(*fil)
    filters.enter_filters(*fil)

    catalog.buying_product_cart()

    cp = CartPage(driver)
    cp.order_confirmation("79995553535", "г Москва, ул Тестовская")

    # Что бы окончательно оформить заказ, необходимо раскомментировать строку 33
    # cp.order_finally()
