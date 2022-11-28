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
