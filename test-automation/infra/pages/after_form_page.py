from infra.utils.config import FLASK_URL

class AfterFormPage:
    def __init__(self, page):
        self.page = page

    ### elements ###    

    @property
    def header_thank_you(self):
        return self.page.locator('h1[name="thanks"]')