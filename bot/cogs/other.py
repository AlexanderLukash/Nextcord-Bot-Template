# Importing necessary components from nextcord.ext.commands
from nextcord.ext.commands import Bot, Cog, Context


# todo: OtherCogs
# Define a Cog (nextcord.py extension) for other functionality
class __MainOtherCog(Cog):

    def __init__(self, bot: Bot):
        """
        Constructor method for the __MainOtherCog class.

        Parameters:
        - bot (Bot): An instance of the Discord bot to which this cog will be added.
        """
        self.bot = bot

    @Cog.listener()
    async def on_ready(self) -> None:
        """
        Event listener method triggered when the bot is ready.

        Prints a message indicating that the bot is ready.
        """
        print('Bot ready!')


# Function to register other cogs with the Discord bot
def register_other_cogs(bot: Bot) -> None:
    bot.add_cog(__MainOtherCog(bot))
