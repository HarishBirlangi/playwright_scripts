import re
import asyncio
from playwright.async_api import expect, async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless = False)
        context = await browser.new_context()
        # await context.tracing.start(screenshots = True, snapshots = True, sources = True)
        page = await context.new_page()

        await page.goto('https://authtest.gridlex.com/login/')

        await page.fill('#email_id', 'harish.b@gridlex.com')
        await page.fill('#password', 'Harish@123')
        await page.click('#login')

        await page.wait_for_load_state('networkidle')


        await page.goto("https://gotest.gridlex.com/a/711/c/ep/1004/en/73/contract-create/")

        await page.fill('input[name="contract_name"]' ,'Created using playwright 1')

        await page.fill('input[id="signature_date_id"]', '2023-01-12')

        # await page.fill('textarea[class="select2-search__field"]', 'Pulsar Bike')

        # await page.click('select[name="items"]')

        # await page.type('input.select2-search__field', "Pulsar Bike")

        # await page.selectOption('select')


        # await page.press('input.select2-search__field', 'Enter')
        # await page.select_option('ul.select2-results__options li.select2-results__option', label='Pulsar Bike')

        await page.click('button[id="submit"]')

        await page.wait_for_load_state('networkidle')

        # await page.screenshot(path='screenshot.png')

        await browser.close()


asyncio.run(main())
