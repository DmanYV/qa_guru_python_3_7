import allure
from selene import by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_decorator_steps_github(open_browser):
    open_main_page()
    search_for_repository('DmanYV/qa_guru_python_3_7')
    go_to_repository('DmanYV/qa_guru_python_3_7')
    open_issues_tab()
    shold_see_issues_with_number('#1')


@allure.step('Открываем главную страницу')
def open_main_page():
    browser.open('https://github.com/')


@allure.step('Ищем репозиторий {repo}')
def search_for_repository(repo):
    s('.header-search-input').click()
    s('.header-search-input').send_keys('DmanYV/qa_guru_python_3_7')
    s('.header-search-input').submit()

@allure.step('переходим по ссылке репозитория {repo}')
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step('Открываем там Issues')
def open_issues_tab():
    s('#issues-tab').click()


@allure.step('Проверяем наличие Issues с номером {number}')
def shold_see_issues_with_number(number):
    s(by.partial_text(number)).click()
