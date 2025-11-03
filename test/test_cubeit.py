from playwright.sync_api import Page, expect

url = "http://127.0.0.1:8000/cubeit/2-index.html"

def test_cube(page: Page):
    page.goto(url)

    input = page.get_by_placeholder('enter number')
    input.fill("2")

    btn_cube = page.get_by_role("button", name='CUBE')
    btn_cube.click()

    result = page.locator('css=p#result')

    expect(result).to_contain_text('8')

def test_empty_input(page: Page):
    page.goto(url)

    input = page.get_by_placeholder('enter number')
    input.fill("")

    btn_cube = page.get_by_role("button", name='CUBE')
    btn_cube.click()

    result = page.locator('css=p#result')

    expect(result).to_have_text("Enter something!")