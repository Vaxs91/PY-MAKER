from EpicHandler.epicHandler import EpicOAuthHandler
import asyncio
import fortnitepy

from fortnitepy.ext import commands

async def main():
    handler = EpicOAuthHandler()
    login = await handler.generate_login_link()
    print(login.verification_uri_complete)
    await asyncio.sleep(10)
    device_auth_details = await handler.get_device_auth_details(login.device_code)
    bot = commands.Bot(
    command_prefix='!',
    auth=fortnitepy.DeviceAuth(
        account_id=f"{device_auth_details.accountId}",
        device_id=f"{device_auth_details.deviceId}",
        secret=f"{device_auth_details.secret}"
        )
        )        
    await asyncio.sleep(1)    
    bot.run()
    print(f"Device ID: {device_auth_details.deviceId}")
    print(f"Account ID: {device_auth_details.accountId}")
    print(f"Secret: {device_auth_details.secret}")

    @bot.event
    async def event_ready():
            print('Well Done')



loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.run_forever()
