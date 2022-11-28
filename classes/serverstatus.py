class serverstatussingle:
    def __init__(self, json: dict):
        self.name = json["Name"]
        self.isonline = json["IsOnline"]
        self.ping = json["Ping"]


class serverstatus:
    def __init__(self, listy: list):
        self.servers = [serverstatussingle(i) for i in listy]