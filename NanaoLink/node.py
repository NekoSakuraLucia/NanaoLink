import wavelink

class NodesCreate:
    def __init__(self, identifier: str, uri: str, password: str) -> None:
        self.identifier = identifier
        self.uri = uri
        self.password = password
        self.node = None

    async def connect(self, client, cache_capacity: int = 100):
        self.node = wavelink.Node(identifier=self.identifier, uri=self.uri, password=self.password)
        await wavelink.Pool.connect(nodes=[self.node], client=client, cache_capacity=cache_capacity)