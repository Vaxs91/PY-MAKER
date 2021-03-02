import fortnitepy
import json
import os
import crayons
import BenBotAsync
import aiohttp
import psutil
import FortniteAPIAsync

from fortnitepy.ext import commands


filename = 'config.json'

with open('config.json') as f:
    data = json.load(f)

if data['debug']:
    logger = logging.getLogger('fortnitepy.http')
    logger.setLevel(level=logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter('\u001b[36m %(asctime)s:%(levelname)s:%(name)s: %(message)s \u001b[0m'))
    logger.addHandler(handler)

    logger = logging.getLogger('fortnitepy.xmpp')
    logger.setLevel(level=logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter('\u001b[35m %(asctime)s:%(levelname)s:%(name)s: %(message)s \u001b[0m'))
    logger.addHandler(handler)


def get_device_auth_details():
    if os.path.isfile(filename):
        with open(filename, 'r') as fp:
            return json.load(fp)
    return {}

def store_device_auth_details(email, details):
    existing = get_device_auth_details()
    existing[email] = details

    with open(filename, 'w') as fp:
        json.dump(existing, fp)

device_auth_details = get_device_auth_details().get(data['email'], {})
bot = commands.Bot(
    command_prefix="!",
    auth=fortnitepy.AdvancedAuth(
        email=data['email'],
        password=data['password'],
        prompt_authorization_code=True,
        delete_existing_device_auths=True,
        **device_auth_details
    )
)

FortniteAPI = FortniteAPIAsync.APIClient()


@bot.event
async def event_device_auth_generate(details, email):
    store_device_auth_details(email, details)

@bot.event
async def event_ready():
    print('██████╗ ██╗   ██╗     ██████╗  ██████╗ ████████╗')
    print('██╔══██╗╚██╗ ██╔╝     ██╔══██╗██╔═══██╗╚══██╔══╝')
    print('██████╔╝ ╚████╔╝█████╗██████╔╝██║   ██║   ██║   ')
    print('██╔═══╝   ╚██╔╝ ╚════╝██╔══██╗██║   ██║   ██║   ')
    print('██║        ██║        ██████╔╝╚██████╔╝   ██║   ')
    print('╚═╝        ╚═╝        ╚═════╝  ╚═════╝    ╚═╝   ')
    print('----------------')
    print('Bot connecté !')
    print(bot.user.display_name)
    print(bot.user.id)
    print('----------------')
    await bot.party.me.platform(bot.platform)


@bot.event()
async def event_friend_request(request):
    await request.accept()

@bot.event()
async def event_party_member_join(ctx):
    await bot.party.send("BOT BY VAXS RSB")
    await bot.party.send("SUPPORT ME CODE VAXS-RSB IN THE ITEM SHOP !")
    await bot.party.me.set_outfit("CID_028_Athena_Commando_F")
    await bot.party.me.set_emote("EID_KPopDance03")
    await bot.party.me.set_banner(season_level=int(999))
    await bot.party.me.set_banner("InfluencerBanner38")



@bot.command()
async def level(ctx: fortnitepy.ext.commands.Context, content: str) -> None:
    await ctx.send("LEVEL DÉFINI SUR: " + content)
    await bot.party.me.set_banner(season_level=int(content))

@bot.command()
async def skin(ctx: fortnitepy.ext.commands.Context, *, content: str) -> None:
    try:
        cosmetic = await FortniteAPI.cosmetics.get_cosmetic(
            lang="en",
            searchLang="en",
            matchMethod="contains",
            name=content,
            backendType="AthenaCharacter"
        )

        await ctx.send(f'Skin mis sur: {cosmetic.id}.')
        print(f"Skin remplacer par: {cosmetic.id}.")
        await bot.party.me.set_outfit(cosmetic.id)

    except FortniteAPIAsync.exceptions.NotFound:
        await ctx.send(f"Erreur avec le skin: {content}.")
        print(f"Skin introuvable: {content}.")

@bot.command(
    description="[Cosmetic] Sets the emote of the client using the emotes name.",
    help="Sets the emote of the client using the emotes name.\n"
         "Example: !emote Windmill Floss"
)
async def emote(ctx: fortnitepy.ext.commands.Context, *, content: str) -> None:
    try:
        cosmetic = await FortniteAPI.cosmetics.get_cosmetic(
            lang="en",
            searchLang="en",
            matchMethod="contains",
            name=content,
            backendType="AthenaDance"
        )

        await ctx.send(f'Je fait cette emote: {cosmetic.id}.')
        print(f"Je fait l'emote: {cosmetic.id}.")
        await bot.party.me.clear_emote()
        await bot.party.me.set_emote(cosmetic.id)

    except FortniteAPIAsync.exceptions.NotFound:
        await ctx.send(f"Erreur je ne peux pas trouvé cette danse: {content}.")
        print(f"Erreur pas de emote avec le nom: {content}.")

@bot.command()
async def scenario(ctx: fortnitepy.ext.commands.Context):
    await ctx.send("#FREE SCENARIO")
    await bot.party.me.set_emote("EID_KPopDance03")



@bot.command()
async def stop(ctx):
    await ctx.send("OK STOP")
    await bot.party.me.clear_emote()


@bot.event
async def event_party_invite(invite: fortnitepy.ReceivedPartyInvitation) -> None:
    await invite.accept()
    print(f'Le bot à rejoind un group {invite.sender.display_name}.')











bot.run()
