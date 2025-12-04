from .base_page import BasePage
import time

class LoginPage(BasePage):
    # NOTE: selectors below are reasonable guesses. Adjust if the site's HTML differs.
    USER_INPUT = 'input[name="username"]'
    PASS_INPUT = 'input[name="password"]'
    LOGIN_BUTTON = 'button[type="submit"]'
    ERROR_SELECTOR = '.alert, .error, .invalid-feedback'
    LOGGED_IN_INDICATOR = 'text=Logout'  # text selector; adjust to site-specific indicator

    def __init__(self, page):
        super().__init__(page)

    def login(self, username, password):
        # ensure fields are visible/ready
        try:
            if self.page.query_selector(self.USER_INPUT):
                self.fill(self.USER_INPUT, username)
            else:
                # fallback: find first input[type=text] or input
                first_input = self.page.query_selector('input[type="text"]') or self.page.query_selector('input')
                if first_input:
                    first_input.fill(username)
            if self.page.query_selector(self.PASS_INPUT):
                self.fill(self.PASS_INPUT, password)
            else:
                # fallback: use the second input
                inputs = self.page.query_selector_all('input')
                if len(inputs) > 1:
                    inputs[1].fill(password)
            # click submit
            if self.page.query_selector(self.LOGIN_BUTTON):
                self.click(self.LOGIN_BUTTON)
            else:
                # press Enter as a fallback
                self.page.keyboard.press('Enter')
        except Exception as e:
            print('Login action had an exception:', e)
        time.sleep(0.5)

    def get_error_message(self):
        el = self.page.query_selector(self.ERROR_SELECTOR)
        if el:
            return el.text_content().strip()
        return None

    def is_logged_in(self):
        # tries multiple heuristics for being logged in
        # 1) presence of a logout link/button
        if self.page.query_selector(self.LOGGED_IN_INDICATOR):
            return True
        # 2) URL changed or contains dashboard
        if 'dashboard' in self.page.url or 'profile' in self.page.url:
            return True
        return False
