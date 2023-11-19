# Importing necessary components from nextcord.ext.commands
from nextcord.ext.commands import Cog, Bot


# todo: EventCogs

# Define a Cog (nextcord.py extension) for event-related functionality
class __MainEventCog(Cog):

    def __init__(self, bot: Bot):
        """
        Constructor method for the __MainEventCog class.

        Parameters:
        - bot (Bot): An instance of the Discord bot to which this cog will be added.
        """
        self.bot = bot


# Function to register event-related cogs with the Discord bot
def register_event_cogs(bot: Bot) -> None:
    bot.add_cog(__MainEventCog(bot))
