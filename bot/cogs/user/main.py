# Importing necessary components from nextcord.ext.commands
from nextcord.ext.commands import Cog, Bot


# todo: UserCogs
# Define a Cog (nextcord.py extension) for user-related functionality
class __MainUserCog(Cog):

    def __init__(self, bot: Bot):
        """
        Constructor method for the __MainUserCog class.

        Parameters:
        - bot (Bot): An instance of the Discord bot to which this cog will be added.
        """
        self.bot = bot


# Function to register user-related cogs with the Discord bot
def register_user_cogs(bot: Bot) -> None:
    bot.add_cog(__MainUserCog(bot))
