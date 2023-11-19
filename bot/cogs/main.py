# Importing necessary components from nextcord.ext.commands
from nextcord.ext.commands import Bot

# Importing functions to register specific types of cogs from their respective modules
from bot.cogs.admin import register_admin_cogs
from bot.cogs.events import register_event_cogs
from bot.cogs.other import register_other_cogs
from bot.cogs.user import register_user_cogs


# Function to register all types of cogs with the Discord bot
def register_all_cogs(bot: Bot) -> None:
    """
   Function to register all types of cogs with the provided Discord bot.

   Parameters:
   - bot (Bot): An instance of the Discord bot.
   """

    # Create a tuple containing functions to register different types of cogs
    cogs = (
        register_user_cogs,
        register_admin_cogs,
        register_other_cogs,
        register_event_cogs,
    )

    # Iterate over the tuple and call each cog registration function
    for cog in cogs:
        cog(bot)
