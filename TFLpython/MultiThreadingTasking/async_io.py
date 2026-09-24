import asyncio

async def download_policy():
    print("Downloading...")
    await asyncio.sleep(3)
    print("Downloaded")

async def send_email():
    print("Sending Email..")
    await asyncio.gather(download_policy(), send_email())

async def main():
    asyncio.run(main())