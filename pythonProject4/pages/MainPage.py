class MainPage():
    def __init__(self, driver):
        self.driver = driver

        self.search_field_id = 'ts_input'
        self.eng_btn = '//*[@id="bottom_nav"]/div[3]/a[3]'
        self.login_field = '//*[@id="index_email"]'
        self.password_field = '//*[@id="index_pass"]'
        self.reset_pass_btn = '//*[@id="index_forgot"]'
        self.reset_pass_field = '//*[@id="reset"]/div/section/div[1]/div/form/div/div[1]/div/input'
        self.all_prod_btn = '//*[@id="content"]/div[1]/div[1]/div/div[1]/a'

    def enter_search(self, search):
        self.driver.find_element_by_id(self.search_field_id).send_keys(search)

    def eng_lang(self):
        self.driver.find_element_by_xpath(self.eng_btn).click()

    def enter_login(self, login):
        self.driver.find_element_by_xpath(self.login_field).send_keys(login)

    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.password_field).send_keys(password)

    def reset_password(self):
        self.driver.find_element_by_xpath(self.reset_pass_btn).click()

    def enter_reset(self, reset):
        self.driver.find_element_by_xpath(self.reset_pass_field).send_keys(reset)

    def all_prod (self):
        self.driver.find_element_by_xpath(self.all_prod_btn).click()

