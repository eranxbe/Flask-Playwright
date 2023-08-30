
from infra.utils.test_enums import CountryEnum, GenderEnum, InterestsEnum
from infra.pages.form_page import FormPage
from infra.pages.after_form_page import AfterFormPage
from infra.utils.config import FLASK_URL
import pytest
import time

@pytest.fixture
def setup(page):
    form_page = FormPage(page)
    after_form_page = AfterFormPage(page)
    page.goto(FLASK_URL + '/form/fill-tha-form')
    yield form_page, after_form_page

class TestFormPage:

    def test_form_page(self, setup):
        form_page, after_form_page = setup
        name = 'John Doe'
        email = 'gustavo@gmail.org'
        age = '18'
        gender = 'male'
        form_page.fill_name(name)
        form_page.fill_email(email)
        form_page.fill_age(age)
        form_page.select_gender(gender)
        time.sleep(1)
        form_page.click_submit()
        time.sleep(1)
        after_form_page.verify_header_thank_you()
        '''test ready'''

    def test_form_page2(self, setup):
        form_page, after_form_page = setup
        name = 'John Doeyyyyy'
        email = 'gustavo@gmail.orgffff'
        age = '12'
        comment = 'this was freaking hard but I did it!'
        form_page.fill_name(name)
        form_page.fill_email(email)
        form_page.fill_age(age)
        form_page.select_gender(GenderEnum.MALE)
        form_page.select_interests(InterestsEnum.MUSIC)
        form_page.select_interests(InterestsEnum.BOOKS)
        form_page.select_country(CountryEnum.ISRAEL)
        form_page.fill_comments(comment)
        form_page.click_submit()
        time.sleep(1)
        after_form_page.verify_header_thank_you()
        '''test ready'''  
