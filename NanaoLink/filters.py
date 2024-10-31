import wavelink

class Nightcore:
    def __init__(self, player: wavelink.Player) -> None:
        self.player = player
    
    async def set(self, speed=1.2, pitch=1.2, rate=1):
        filters: wavelink.Filters = self.player.filters
        filters.timescale.set(speed=speed, pitch=pitch, rate=rate)
        await self.player.set_filters(filters)