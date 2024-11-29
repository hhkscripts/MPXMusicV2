from MPXMusic.core.bot import MPX
from MPXMusic.core.dir import dirr
from MPXMusic.core.git import git
from MPXMusic.core.userbot import Userbot
from MPXMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = MPX()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
