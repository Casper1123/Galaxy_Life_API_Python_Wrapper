from json import JSONDecodeError
import requests as _r   # When importing this file I don't want you to take this with you


# Classes
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
        self.stats = get_user_stats(self.id)


class userstats:
    def __init__(self, json: dict):
        self.playtime = json["TotalPlayTimeInMs"]
        self.npcsattacked = json["NpcsAttacked"]
        self.playersattacked = json["PlayersAttacked"]
        self.timesattacked = json["TimesAttacked"]
        self.starbasesdestroyed = json["StarbasesDestroyed"]
        self.buildingsdestroyed = json["BuildingsDestroyed"]
        self.damagedone = json["DamageDoneInAttacks"]
        self.obstaclesrecycled = json["ObstaclesRecycled"]
        self.coinsspent = json["CoinsSpent"]
        self.mineralsspent = json["MineralsSpent"]
        self.chipsspent = json["ChipsSpent"]
        self.coinloot = json["CoinsFromAttacks"]
        self.mineralloot = json["MineralsFromAttacks"]
        self.scoreloot = json["ScoreFromAttacks"]
        self.utilitiesused = json["UtilityUsed"]
        self.nukesused = json["NukesUsed"]
        self.troopstrained = json["TroopsTrained"]
        self.troopsizedonated = json["TroopSizesDonated"]
        self.helpclicksused = json["FriendsHelped"]
        self.giftsreceived = json["GiftsReceived"]
        self.giftssent = json["GiftsSent"]
        self.coloniesmoved = json["ColoniesMoved"]
        self.starsvisited = json["StarsVisited"]


class serverstatussingle:
    def __init__(self, json: dict):
        self.name = json["Name"]
        self.isonline = json["IsOnline"]
        self.ping = json["Ping"]


class serverstatus:
    def __init__(self, listy: list):
        self.servers = [serverstatussingle(i) for i in listy]
        
        
class emblem:
    def __init__(self, json: dict):
        self.shape = json["Shape"]
        self.pattern = json["Pattern"]
        self.icon = json["Icon"]

    def ToString(self):
        self.shape = {0: "Circle", 1: "Diamond",
                      2: "Badge",
                      3: "Cross",
                      4: "Shield"}[self.shape]

        self.pattern = {
            0: "CrackedBlue",
            1: "CrackedRed",
            2: "CrackedGreen",
            3: "CrackedBlack",
            4: "CrackedPink",
            5: "Blue",
            6: "Red",
            7: "Green",
            8: "Black",
            9: "Pink",
            10: "DualBlue",
            11: "DualRed",
            12: "DualGreen",
            13: "DualBlack",
            14: "DualPink"
        }[self.pattern]

        self.icon = {
            0: "Rabbit",
            1: "Skull",
            2: "Viking",
            3: "Octopus",
            4: "Devil",
            5: "Angel",
            6: "Gladiator",
            7: "NativeAmerican",
            8: "Soldier",
            9: "Pilot",
            10: "Starlinator",
            11: "Fists",
            12: "Ufo2",
            13: "Gun",
            14: "Orange"
        }[self.icon]

    def __str__(self):
        return f"{self.shape}, {self.pattern}, {self.icon}"


class alliancerolec:
    def __init__(self, number: int):
        self.raw = number
        self.full = {0: "Leader", 1: "Admin", 2: "Regular"}[number]


class member:
    def __init__(self, json: dict):
        self.id = json["Id"]
        self.name = json["Name"]
        self.avatar = json["Avatar"]
        self.alliancerole = alliancerolec(json["AllianceRole"])
        self.totalwarpoints = json["TotalWarPoints"]


class alliance:
    def __init__(self, json: dict):
        self.id = json["Id"]
        self.name = json["Name"]
        self.description = json["Description"]
        self.emblem = emblem(json["Emblem"])
        self.alliancelevel = json["AllianceLevel"]
        self.warpoints = json["WarPoints"]
        self.warswon = json["WarsWon"]
        self.warslost = json["WarsLost"]
        self.members = [member(i) for i in json["Members"]]
        

#API Call functions, just import these lol
def get_alliance(allianceID: str) -> alliance or None:
    try:
        return alliance(_r.get(f"https://api.galaxylifegame.net/alliances/get?name={allianceID}").json())
    except JSONDecodeError:
        return None


def get_server_status() -> serverstatus or None:
    try:
        return serverstatus(_r.get(f"https://api.galaxylifegame.net/status").json())
    except JSONDecodeError:
        return None


def get_user(userID: str or int, steam=False) -> user or None:
    try:
        if not steam:
            if isinstance(user, int):
                return user(_r.get(f"https://api.galaxylifegame.net/users/get?id={userID}").json())

            else:
                try:
                    return user(_r.get(f"https://api.galaxylifegame.net/users/get?id={int(userID)}").json())
                except ValueError:
                    return user(_r.get(f"https://api.galaxylifegame.net/users/name?name={userID}").json())
                # Handles ID's being put in as strings.
        else:
            return user(_r.get(f"https://api.galaxylifegame.net/users/steam?steamId={userID}").json())
    except JSONDecodeError:
        return None


def search_user(userID: str or int) -> list[user] or None:
    try:
        if isinstance(user, int):
            return [user(i) for i in _r.get(f"https://api.galaxylifegame.net/users/get?id={userID}").json()]
        else:
            try:
                return [user(i) for i in _r.get(f"https://api.galaxylifegame.net/users/get?id={int(userID)}").json()]
            except ValueError:
                return [user(i) for i in _r.get(f"https://api.galaxylifegame.net/users/name?name={userID}").json()]
            # Handles ID's being put in as strings.
    except JSONDecodeError:
        return None


def get_user_stats(userID: int or str) -> userstats or None:
    try:
        return userstats(_r.get(f"https://api.galaxylifegame.net/users/stats?id={userID}").json())
    except JSONDecodeError:
        return None




if __name__ == "__main__":
    # Example code here

    print(get_user("Casper1123").stats.coinsspent)

    # entities.classes.user imports this file, therefore code is run twice outside of this statement.
    # This is because it needs to import get_user_stats :)
