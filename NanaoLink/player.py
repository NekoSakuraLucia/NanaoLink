import discord.ext.commands
import wavelink
import discord
from typing import Optional, Union

import discord.ext

class Nanao_Player(wavelink.Player):
    async def VoiceConnect(self, source: Union[discord.ext.commands.Context, discord.Interaction]):
        """
        Connects the bot to the user's voice channel.
        Raises errors for users to handle them externally.
        """
        if isinstance(source, discord.ext.commands.Context):
            author = source.author
            voice_channel = author.voice.channel if author.voice else None
        elif isinstance(source, discord.Interaction):
            author = source.user
            voice_channel = author.voice.channel if author.voice else None
        else:
            raise TypeError("Invalid source type. Expected Context or Interaction.")

        if not voice_channel:
            raise AttributeError("User is not connected to a voice channel.")
        
        player: Optional[wavelink.Player] = source.guild.voice_client
        if not player:
            player = await voice_channel.connect(cls=wavelink.Player, self_deaf=True)
        return player