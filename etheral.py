import asyncio
from pyppeteer import launch

async def auto_faucet_ethereal():
    browser = await launch(headless=False, args=['--start-maximized'])
    page = await browser.newPage()
    await page.setViewport({'width': 1920, 'height': 1080})

    # Go to faucet page
    await page.goto('https://register.ethereal.trade/', {'waitUntil': 'networkidle2'})
    print("Page loaded")

    try:
        # Click "Connect Wallet" button - update selector accordingly
        connect_wallet_selector = 'button.connect-wallet'  # <-- Replace with actual selector
        await page.waitForSelector(connect_wallet_selector, timeout=15000)
        await page.click(connect_wallet_selector)
        print("Clicked Connect Wallet button")

        # Wait time for manual wallet approval popup (MetaMask/OKX)
        print("Please approve wallet connection in your wallet extension popup...")
        await asyncio.sleep(30)  # Adjust time as needed for manual approval

        # Click faucet claim button - update selector accordingly
        faucet_claim_selector = 'button.claim-faucet'  # <-- Replace with actual selector
        await page.waitForSelector(faucet_claim_selector, timeout=15000)
        await page.click(faucet_claim_selector)
        print("Clicked Faucet Claim button")

        # Wait for confirmation message or success indicator
        success_selector = '.success-message'  # <-- Replace with actual selector
        await page.waitForSelector(success_selector, timeout=15000)
        print("Faucet claim confirmed")

    except Exception as e:
        print(f"Error during automation: {e}")

    # Take screenshot for verification
    await page.screenshot({'path': 'ethereal_faucet_result.png'})

    await browser.close()

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(auto_faucet_ethereal())
