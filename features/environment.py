from playwright.sync_api import sync_playwright
import json, os

def before_all(context):
    # load config
    cfg_path = os.path.join(os.path.dirname(__file__), "..", "config.json")
    with open(cfg_path, "r") as f:
        context.config_data = json.load(f)

    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False ,slow_mo=500)
    # create a single browser context for isolation per feature / scenario if needed
    context.context = context.browser.new_context()
    context.page = context.context.new_page()

def after_all(context):
    try:
        context.page.close()
        context.context.close()
        context.browser.close()
        context.playwright.stop()
    except Exception:
        pass
