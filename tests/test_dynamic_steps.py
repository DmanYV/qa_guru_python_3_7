import allure
from selene import by, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_dynamic_steps_github(open_browser):
    with allure.step('Открываем главную страницу'):
        browser.open('https://github.com/')
    with allure.step('Ищем репозиторий'):
        s('.header-search-input').click()
        s('.header-search-input').send_keys('DmanYV/qa_guru_python_3_7')
        s('.header-search-input').submit()

    with allure.step('Переходим по ссылке репозитория'):
        s(by.link_text('DmanYV/qa_guru_python_3_7')).click()

    with allure.step('Отерываем таб Issues'):
        s('#issues-tab').click()

    with allure.step('Проверяем наличие Issues с номером 1'):
        s(by.partial_text('#1')).should(be.visible)


