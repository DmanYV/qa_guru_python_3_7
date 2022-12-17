from selene import by, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_github(open_browser):
    browser.open('https://github.com/')

    s('.header-search-input').click()
    s('.header-search-input').send_keys('DmanYV/qa_guru_python_3_7')
    s('.header-search-input').submit()

    s(by.link_text('DmanYV/qa_guru_python_3_7')).click()

    s('#issues-tab').click()

    s(by.partial_text('#1')).should(be.visible)