import os
import time
import random
import audioread
import discord
from discord.ext import commands


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
    async def ri(self, ctx, soundbite):
        """
        Disturb the General channel and emit an unwanted noise.
        :param ctx: discord context parameter
        :param soundbite: the value sent after the command will be the soundbite to play from the Assets directory
        :return: Bad bad sounds.
        """
        voice_channel = discord.utils.get(ctx.guild.voice_channels, name='General')
        await voice_channel.connect()
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)

        soundbite_lower = soundbite.casefold()
        if soundbite_lower == 'random':
            file = self._get_random_file(soundbite_lower)
        else:
            file = self._get_file(soundbite_lower)

        try:
            voice.play(discord.FFmpegPCMAudio(f"Assets/{file}"))
        except PermissionError:
            await ctx.send('Wait for the current sound to end, scrote.')
            return

        duration = self._get_audio_duration(f"Assets/{file}")
        time.sleep(duration)
        if voice.is_connected():
            await voice.disconnect()

    @staticmethod
    def _get_file(soundbite):
        """
        Find the audio file that is associated with the given parameter.
        :param soundbite: The audio file to find.
        :return: String object representing the file path of the audio file
        """
        assets_dir = os.listdir('Assets')
        file_name = [name for name in assets_dir if soundbite in name]
        return file_name[0]

    @staticmethod
    def _get_random_file(soundbite):
        """
        Find the audio file that is associated with the given parameter.
        :param soundbite: The audio file to find.
        :return: String object representing the file path of the audio file
        """
        assets_dir = os.listdir('Assets')
        print(random.choice(assets_dir))
        return random.choice(assets_dir)

    @staticmethod
    def _get_audio_duration(filepath: str):
        """
        Get the duration of the audio file.
        :param filepath: the location of the audio file.
        :return: int value of the duration of the audio file in seconds.
        """
        with audioread.audio_open(filepath) as audio_file:
            duration = audio_file.duration
        return duration


bot = commands.Bot(command_prefix='c')
bot.add_cog(CryBot(bot))
bot.run(CryBot.token)
