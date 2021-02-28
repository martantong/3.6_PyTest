def test_is_add_button_presents(browser):
    browser.get(" http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    btn = browser.find_elements_by_class_name('btn-add-to-basket')
    assert btn, "Кнопка не найдена"
