from infra.utils.config import FLASK_URL

class FormPage:
    def __init__(self, page):
        self.page = page

    ### elements ###    

    @property
    def text_name(self):
        return self.page.locator('input[id="name"]')

    @property
    def text_email(self):
        return self.page.locator('input[id="email"]')
    
    @property
    def text_age(self):
        return self.page.locator('input[id="age"]')
    
    @property
    def radio_gender(self):
        return self.page.locator('input[name="gender"]')
    
    @property
    def checkbox_interests(self):
        return self.page.locator('input[name="interests"]')
    
    @property
    def dropdown_country(self):
        return self.page.locator('select[name="country"]')
    
    @property
    def textarea_comments(self):
        return self.page.locator('textarea[name="comments"]')

    @property
    def button_submit(self):
        return self.page.locator('input[type="submit"]')
    
    ### actions ###

    def navigate(self):
        self.page.goto(FLASK_URL + '/form')

    def fill_name(self, name: str):
        self.text_name.fill(name)


    def fill_email(self, email: str):
        self.text_email.fill(email)


    def fill_age(self, age: str):
        self.text_age.fill(age)


    def select_gender(self, gender: str):
        options = self.radio_gender.all()
        for option in options:
            if option.get_attribute('value') == gender.lower():
                option.click(force=True)    

    def select_interests(self, interest: str):
        options = self.checkbox_interests.all()
        for option in options:
            if option.get_attribute('id') == interest.lower():
                option.click()


    def select_country(self, country: str):
        self.dropdown_country.select_option(country.lower())


    def fill_comments(self, comments: str):
        self.textarea_comments.fill(comments)


    def click_submit(self):
        self.button_submit.click()

