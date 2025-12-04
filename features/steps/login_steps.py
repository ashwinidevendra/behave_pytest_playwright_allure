from behave import given, when, then
from pages.login_page import LoginPage
import time
import allure

@allure.feature('Feature1')
@allure.story('Story1')
@allure.step(1)
@given("the application is opened")
def step_open_app(context):
    base = context.config_data.get("base_url")
    context.page.goto(base)
    context.login_page = LoginPage(context.page)
    
@allure.step(2)
@when("I login with valid credentials")
def step_login_valid(context):
    cfg = context.config_data
    user = cfg.get("valid_user")
    pwd = cfg.get("valid_password")
    if user == "CHANGE_ME" or pwd == "CHANGE_ME":
        # if placeholders are not changed, continue but this will likely fail assertion below
        print("WARNING: valid_user/valid_password are placeholders. Update config.json for a real run.")
    context.login_page.login(user, pwd)
    # small wait for navigation
    time.sleep(1)

@when("I login with invalid credentials")
def step_login_invalid(context):
    cfg = context.config_data
    user = cfg.get("invalid_user")
    pwd = cfg.get("invalid_password")
    context.login_page.login(user, pwd)
    time.sleep(1)

@then("I should see the dashboard or a logged-in indicator")
def step_assert_logged_in(context):
    assert context.login_page.is_logged_in(), "Expected to be logged in but wasn't. Check credentials/selectors."

@then("I should see an error message")
def step_assert_error(context):
    assert context.login_page.get_error_message() is not None, "Expected an error message for invalid login."
