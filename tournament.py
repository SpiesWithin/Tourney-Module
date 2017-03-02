from discord.ext import commands
import discord

"""
For tournament commands i.e. |createTeam
"""
class Tournament():
    def __init__(self, bot): #Setup
        self.bot = bot

    @commands.command(pass_context=True) #Begins tournament creation
    async def createtourney(self, ctx):
        print(dir(self.bot))
        """Creates a tourney."""
        if ctx.message.author.permissions_in(ctx.message.channel).administrator: #Checks if user is an admin.
            await self.bot.say("Beginning the tournament creation!")
            await self.bot.say("To continue.\nPlease type {}tourney name ```TOURNEYNAME```".format(self.bot.command_prefix))
        else:
            await self.bot.say("Sorry! You must have **Administrator** permissions to do that.")

    @commands.group(pass_context=True) #Creates the tourney registration group
    async def tourney(ctx):
        if ctx.invoked_subcommand is None:
            await self.bot.say('Invalid tourney command passed...')

    @tourney.command(pass_context=True)
    async def name(self, ctx, name: str):
        pass
        await self.bot.say("Thanks! I set your tourney name to " + name)
        await self.bot.say("To continue, please type {}tourney ")



def setup(bot): #Exports cog for use by other files.
    bot.add_cog(Tournament(bot))
