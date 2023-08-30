class AfterFormPage:
    def __init__(self, page):
        self.page = page

    ### elements ###    

    @property
    def header_thank_you(self):
        return self.page.locator('h1[id="thanks"]')
    
    def verify_header_thank_you(self):
        assert self.header_thank_you.is_visible()