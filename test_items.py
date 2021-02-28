

def test_is_add_button_presents(browser):
    browser.get(" http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    browser.find_element_by_class_name('btn-add-to-basket')
