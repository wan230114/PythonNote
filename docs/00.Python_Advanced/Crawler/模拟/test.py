# %%
from pyppeteer.launcher import Launcher
import asyncio
from pyppeteer import launch

print(' '.join(Launcher().cmd))


async def main():
    # browser = await launch()
    browser = await launch(options={'args': ['--no-sandbox']})
    page = await browser.newPage()
    await page.goto('http://baidu.com')
    print("page.goto")
    await page.screenshot({'path': 'example.png'})
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
