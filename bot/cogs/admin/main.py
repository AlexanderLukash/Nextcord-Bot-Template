# Importing necessary components from nextcord.ext.commands
from nextcord.ext.commands import Cog, Bot


# todo: AdminCogs

# Define a Cog (nextcord.py extension) for admin-related functionality
class __MainAdminCog(Cog):

    def __init__(self, bot: Bot):
        """
        Constructor method for the __MainAdminCog class.

        Parameters:
        - bot (Bot): An instance of the Discord bot to which this cog will be added.
        """
        self.bot = bot


# Function to register admin cogs with the Discord bot
def register_admin_cogs(bot: Bot) -> None:
    bot.add_cog(__MainAdminCog(bot))
