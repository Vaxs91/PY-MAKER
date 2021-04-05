import fortnitepy
import json
import os
import crayons
import FortniteAPIAsync

from fortnitepy.ext import commands


filename = 'config.json'

with open(filename) as f:
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

class client:
    courriel=data['email']
    wordpass=data['password']
    accept_friends=data['accept_friends']
    cid=data['cid']
    eid=data['eid']
    prefix=data['prefix']
    level=data['level']


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

device_auth_details = get_device_auth_details().get(client.courriel, {})
bot = commands.Bot(
    command_prefix=client.prefix,
    auth=fortnitepy.AdvancedAuth(
        email=client.courriel,
        password=client.wordpass,
        prompt_authorization_code=True,
        delete_existing_device_auths=True,
        **device_auth_details
    )
)

fortnite_api_async = FortniteAPIAsync.APIClient()

print(crayons.cyan('PY MAKER BY VAXS RSB YOUTUBE: https://www.youtube.com/channel/UCIK7oxSNPt8MCrphoL5MEPA'))
print(crayons.cyan('IF YOU WONT TO SUPPORT ME USE CODE VAXS-RSB IN THE ITEM SHOP'))

@bot.event()
async def event_ready():
    print('██████╗ ██╗   ██╗     ██████╗  ██████╗ ████████╗')
    print('██╔══██╗╚██╗ ██╔╝     ██╔══██╗██╔═══██╗╚══██╔══╝')
    print('██████╔╝ ╚████╔╝█████╗██████╔╝██║   ██║   ██║   ')
    print('██╔═══╝   ╚██╔╝ ╚════╝██╔══██╗██║   ██║   ██║   ')
    print('██║        ██║        ██████╔╝╚██████╔╝   ██║   ')
    print('╚═╝        ╚═╝        ╚═════╝  ╚═════╝    ╚═╝   ')
    print('----------------')
    print(crayons.green('[PY MAKER, LAUNCHER] BOT READY AS: ' + bot.user.display_name + ", " + bot.user.id))
    print('----------------')
    await bot.set_presence(bot.user.display_name + " BY VAXS RSB")

@bot.event
async def event_device_auth_generate(details, email):
    store_device_auth_details(email, details)


@bot.event
async def event_friend_request(request):
    if client.accept_friends:
        await request.accept()

@bot.event()
async def event_party_member_join(ctx: fortnitepy.ext.commands.Context):
    await bot.party.me.set_outfit(client.cid)
    await bot.party.me.set_emote(client.eid)
    await bot.party.me.set_banner(season_level=int(client.level))
    await bot.party.me.set_banner("InfluencerBanner38")
    await bot.party.send(bot.user.display_name + " BY VAXS RSB")
    await bot.party.send("USE CODE VAXS-RSB IN THE ITEM SHOP")

@bot.command()
async def skin(ctx: fortnitepy.ext.commands.Context, *, item: str):
    try:
        cosmetic = await fortnite_api_async.cosmetics.get_cosmetic(
            lang="en",
            searchLang="en",
            matchMethod="contains",
            name=item,
            backendType="AthenaCharacter"
        )

        await bot.party.me.set_outfit(cosmetic.id)
        await ctx.send("Skin défini sur: " + cosmetic.id + ', ' + cosmetic.name)
        print("Skin défini sur: " + cosmetic.id + ', ' + cosmetic.name)
    except FortniteAPIAsync.exceptions.NotFound:
            ctx.send("Skin introuvable: " + item)
            print("Skin introuvable: " + item)


@bot.command()
async def emote(ctx: fortnitepy.ext.commands.Context, *, item: str):
    try:
        cosmetic_2 = await fortnite_api_async.cosmetics.get_cosmetic(
            lang="en",
            searchLang="en",
            matchMethod="contains",
            name=item,
            backendType="AthenaDance"
        )

        await bot.party.me.set_emote(cosmetic.id_2)
        await ctx.send("Emote défini sur: " + cosmetic_2.id + ', ' + cosmetic_2.name)
        print("Emote défini sur: " + cosmetic_2.id + ', ' + cosmetic_2.name)
    except FortniteAPIAsync.exceptions.NotFound:
            await ctx.send("Emote introuvable: " + item)
            print("Emote introuvable: " + item)




"""GHOUL ROSE"""
@bot.command()
async def pink_ghoul(ctx: fortnitepy.ext.commands.Context):
    pink_ghoul_variants = bot.party.me.create_variant(
        material=3
    )
    await bot.party.me.set_outfit(
        asset="CID_029_Athena_Commando_F_Halloween",
        variants=pink_ghoul_variants
    )

    await ctx.send("Tâche terminé")
    print("Tâche terminer")

@bot.command()
async def sac(ctx: fortnitepy.ext.commands.Context, *, item: str):
    try:
        cosmetic_3 =  await fortnite_api_async.cosmetics.get_cosmetic(
            lang="en",
            searchLang="en",
            matchMethod="contains",
            name=item,
            backendType="AthenaBackpack"
        )

        await bot.party.me.set_backpack(cosmetic_3.id)
        await ctx.send("Sac à dos défini sur: " + cosmetic_3.id + ', ' + cosmetic_3.name)
        print("Sac à dos défini sur: " + cosmetic_3.id + ', ' + cosmetic_3.name)
    except FortniteAPIAsync.exceptions.NotFound:
            await ctx.send("Sac à dos introuvable: " + item)
            print("Sac à dos introuvable: " + item)


@bot.command()
async def pioche(ctx: fortnitepy.ext.commands.Context, *, item: str):
    try:
        cosmetic_4 = await fortnite_api_async.cosmetics.get_cosmetic(
            lang="en",
            searchLang="en",
            matchMethod="contains",
            name=content,
            backendType="AthenaPickaxe"
        )

        await bot.party.me.set_pickaxe(cosmetic_4.id)
        await ctx.send("Pioche défini sur: " + cosmetic_4.id + ", " + cosmetic_4.name)
        print("Pioche défini sur: " + cosmetic_4.id + ", " + cosmetic_4.name)
    except FortniteAPIAsync.exceptions.NotFound:
            await ctx.send("Pioche introuvable: " + item)
            print("Pioche introuvable: " + item)

@bot.command()
async def purpleskull(ctx: fortnitepy.ext.commands.Context):
    purple_variante = bot.party.me.create_variant(
        material=2
    )

    await bot.party.me.set_outfit(
        asset="CID_030_Athena_Commando_M_Halloween",
        variants=purple_variante
    )

    await ctx.send("Tâche terminer")
    print("Tâche terminer")



@bot.command()
async def variant(ctx: fortnitepy.ext.commands.Context, item: str, number: str):
    try:
        cosmetic_5 = await fortnite_api_async.cosmetics.get_cosmetic(
            lang="en",
            searchLang="en",
            matchMethod="contains",
            name=item,
            backendType="AthenaCharacter"
        )

        skin_varient = await bot.party.me.create_variant(
            material=number
        )

        await bot.party.me.set_outfit(
            asset=cosmetic_5.id,
            variants=skin_varient
        )

        await ctx.send("Skin varient: " + cosmetic_5.id + ', ' + cosmetic_5.name)
        print("Skin varient: " + cosmetic_5.id + ', ' + cosmetic_5.name)
    except FortniteAPIAsync.exceptions.NotFound:
        await ctx.send("Varient de skin introuvalble: " + item + ' (' + number + ')')
        print("Varient de skin introuvalble: " + item + ' (' + number + ')')



@bot.command()
async def cadeau(ctx: fortnitepy.ext.commands.Context):
    await bot.party.me.set_emote("EID_NeverGonna")
    await ctx.send("Fake commande (troll)")


@bot.command()
async def scenario(ctx: fortnitepy.ext.commands.Context):
    await bot.party.me.clear_emote()
    await bot.party.me.set_emote("EID_KPopDance03")
    await ctx.send("#FREE SCENARIO")
    print("Emote défini sur:  EID_KPopDance03, Scenario")


@bot.command()
async def stop(ctx: fortnitepy.ext.commands.Context):
    await bot.party.me.clear_emote()
    await ctx.send("Emote arrêter!")
    print("Emote arrêter!")


bot.run()
