# CryBot

---

Welcome to CryBot, if you have found this you most certainly enjoy a good cry! 

![cry](Assets/img.jpg)

## Usage

---

CryBot is an object that inherits and extends the functionality of commands.Cog object from the Discord
library. Its primary function is to play a sound on the voice channel based on the text posted in the chat.

A discord application must be registered on the developer Discord website, the generated API key is required
for the program to communicate with Discord and the application must be invited to any Discord server that
it should play sounds on.

```python
bot = commands.Bot(command_prefix='!')
bot.add_cog(CryBot(bot))
bot.run(CryBot.token)
```

To use the code, first instantiate a Bot object from the commands module and specify the command prefix.
Call the bot's add_cog method to add the Cog object and also pass the Bot object through as a parameter.
Finally, call the run method and then pass through the API key as the parameter.


![cord shot](Assets/cord%20scrneeshot.png)

To invoke sounds on the Discord server use the command prefix, and the name of the class method in the
General chat to play the sound file associated with the method. This object takes a parameter after the
command which is then matched to a sound file in the Assets directory and played back in the General
voice channel. In this case `!cri` would invoke the `cri` method and any string after that will be taken
and matched against the sound files.