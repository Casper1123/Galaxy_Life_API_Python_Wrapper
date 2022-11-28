class planet:
    def __init__(self, json: dict):
        self.ownerid = json["OwnerId"]
        self.hqlevel = json["HQLevel"]


class user:
    def __init__(self, json: dict):
        self.id = int(json["Id"])
        self.name = json["Name"]
        self.avatar = json["Avatar"]
        self.online = json["Online"]
        self.experience = json["Experience"]
        self.allianceid = json["AllianceId"]
        self.planets = [planet(i) for i in json["Planets"]]
        from GL_API_PY_WRAPPER import get_user_stats
        self.stats = get_user_stats(self.id)
