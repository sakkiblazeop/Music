from callsmusic.bot import InnexiaBot
from InnexiaMusic.core.dir import dirr
from InnexiaMusic.core.git import git
from callsmusic.userbot import Userbot
from InnexiaMusic.misc import dbb, heroku, sudo
from aiohttp import ClientSession

from .logging import LOGGER


dirr()

git()

dbb()

heroku()

sudo()

# Clients
app = InnexiaBot()

userbot = Userbot()


from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()

aiohttpsession = ClientSession()
