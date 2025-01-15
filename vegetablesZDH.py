import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.locator("body").click()
    page.goto("http://127.0.0.1:5000/")
    # page.get_by_placeholder("请输入蔬菜名称").click()
    # page.get_by_placeholder("请输入蔬菜名称").fill("香蕉")
    # page.get_by_placeholder("请输入单价").click()
    # page.get_by_placeholder("请输入单价").fill("2.99")
    # page.once("dialog", lambda dialog: dialog.dismiss())
    # page.get_by_role("button", name="添加蔬菜").click()
    page.get_by_role("list").get_by_text("记录销售").click()
    page.locator("#vegSelect").select_option("9")
    page.get_by_placeholder("请输入销售数量").click()
    page.get_by_placeholder("请输入销售数量").fill("66")
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="记录销售").click()
    page.get_by_placeholder("请输入销售数量").click()
    page.get_by_placeholder("请输入销售数量").fill("2")
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="记录销售").click()
    page.get_by_role("list").get_by_text("销售统计").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
