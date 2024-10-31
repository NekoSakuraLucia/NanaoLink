import discord.ext.commands
import wavelink
import discord
from typing import Optional, Union
from .filters import Nightcore

import discord.ext

class Nanao_Player(wavelink.Player):
    def __init__(self, *args, guild: discord.Guild, **kwargs):
        super().__init__(*args, **kwargs)
        self._guild = guild
        self.voice_channel = None
        self._filters = self.create_filters()

    @property
    def guild(self):
        return self._guild
    
    @property
    def filters(self):
        return self._filters

    @property
    def nightcore(self):
        return Nightcore(self)
    
    def create_filters(self):
        return wavelink.Filters()

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
        if not player or not player.connected:
            try:
                player = await voice_channel.connect(cls=wavelink.Player, self_deaf=True)
                self.voice_channel = voice_channel
            except Exception as e:
                raise RuntimeError(f"Failed to connect to the voice channel: {str(e)}")
            
        return player
    
    async def TrackSearch(self, query: str):
        tracks: wavelink.Playable = await wavelink.Playable.search(query)
        if not tracks:
            return None
        
        if isinstance(tracks, wavelink.Playlist):
            await self.queue.put_wait(tracks)
            return tracks
        else:
            track: wavelink.Playable = tracks[0]
            await self.queue.put_wait(track)
            return [track]
        
    def QueueGet(self):
        track = self.queue.get()
        return track if track else None

    async def playTrack(self, track: wavelink.Playable, volume: int = 60):
        if track is None:
            raise ValueError("Track cannot be None")
        
        player: Optional[wavelink.Player] = self.guild.voice_client 
        if player is None or not player.connected:
            raise RuntimeError("Player is not connected to a voice channel")
        
        await self.play(track)
        await player.set_volume(volume)