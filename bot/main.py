# Importing necessary components from nextcord
from nextcord import Intents
from nextcord.ext.commands import Bot

# Importing configuration and setup functions
from bot.misc import Env, Config
from bot.cogs import register_all_cogs
from bot.database.models import register_models


def start_bot():
    """
    Function to initialize and start the Discord bot.

    This function performs the following steps:
    1. Configures the bot's intents, enabling message content tracking.
    2. Creates an instance of the Bot class, using the command prefix from the Config class
       and the configured intents.
    3. Registers all cogs using the register_all_cogs function.
    4. Registers database models using the register_models function.
    5. Initiates the bot's connection to the Discord server using the TOKEN from the Env class.
    """

    # Configure intents to track message content
    intents = Intents.default()
    intents.message_content = True

    # Create a Bot instance with the specified command prefix and intents
    bot = Bot(Config.CMD_PREFIX, intents=intents)

    # Register all cogs with the bot
    register_all_cogs(bot)

    # Register database models
    register_models()

    # Start the bot by connecting to the Discord server using the provided TOKEN
    bot.run(Env.TOKEN)
