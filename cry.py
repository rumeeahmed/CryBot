import os
import time
import discord
from discord.ext import commands, tasks


class CryBot(commands.Cog):
    """
    Bot object that handles actions on Discord.
    """
    token = os.environ.get('DISCORD_KEY')

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """
        Print to the console to indicate the bot is now active.
        :return:
        """
        print('Bot online')

    @commands.command()
    async def cmd(self, ctx, soundbite):
        """
        Announce judgment to the voice channel.
        :param ctx: discord context parameter
        :param soundbite: the value sent after the command will be the soundbite to play from the Assets directory
        :return: JUDGMENT!
        """
        voice_channel = discord.utils.get(ctx.guild.voice_channels, name='General')
        await voice_channel.connect()
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        file = self._get_file(soundbite)

        try:
            voice.play(discord.FFmpegPCMAudio(f"Assets/{file}"))
        except PermissionError:
            await ctx.send('Wait for the current playing music to end or use the stop command')
            return

        time.sleep(2)
        if voice.is_connected():
            await voice.disconnect()

    @staticmethod
    def _get_file(soundbite):
        assets_dir = os.listdir('Assets')
        file_name = [name for name in assets_dir if soundbite.casefold() in name]
        return file_name[0]


bot = commands.Bot(command_prefix='!')
bot.add_cog(CryBot(bot))
bot.run(CryBot.token)
