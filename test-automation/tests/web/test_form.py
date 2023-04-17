
from infra.pages.form_page import FormPage
from infra.pages.after_form_page import AfterFormPage
import pytest

class TestFormPage:
    @pytest.mark.usefixtures('page')
    def test_form_page(self, page):
        form_page = FormPage(page)
        after_form_page = AfterFormPage(page)
        form_page.fill_name("John Doe")
        form_page.fill_email("gustavo@gmail.org")
        form_page.fill_age("18")
        form_page.select_gender("Male")
        form_page.click_submit()
        assert after_form_page.header_thank_you.is_visible()

    @pytest.mark.usefixtures('page')
    def test_form_page2(self, page):
        form_page = FormPage(page)
        after_form_page = AfterFormPage(page)
        form_page.fill_name("John Doeyyyyy")
        form_page.fill_email("gustavo@gmail.orgffff")
        form_page.fill_age("182")
        form_page.select_gender("Male")
        form_page.select_interests("Music")
        form_page.select_country("Canada")
        form_page.fill_comments("this was f**king hard but I did it!")
        form_page.click_submit()
        assert after_form_page.header_thank_you.is_visible()    
