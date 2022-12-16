import json

import requests as _r   # When importing this file I don't want you to take this with you
from entities import *


#API Call functions, just import these lol
def get_alliance(alliance: str) -> classes.alliance.alliance or None:
    try:
        return classes.alliance.alliance(_r.get(f"https://api.galaxylifegame.net/alliances/get?name={alliance}").json())
    except json.JSONDecodeError:
        return None


def get_server_status() -> classes.serverstatus.serverstatus or None:
    try:
        return classes.serverstatus.serverstatus(_r.get(f"https://api.galaxylifegame.net/status").json())
    except json.JSONDecodeError:
        return None


def get_user(user: str or int, steam=False) -> classes.user.user or None:
    try:
        if not steam:
            if isinstance(user, int):
                return classes.user.user(_r.get(f"https://api.galaxylifegame.net/users/get?id={user}").json())

            else:
                try:
                    return classes.user.user(_r.get(f"https://api.galaxylifegame.net/users/get?id={int(user)}").json())
                except ValueError:
                    return classes.user.user(_r.get(f"https://api.galaxylifegame.net/users/name?name={user}").json())
                # Handles ID's being put in as strings.
        else:
            return classes.user.user(_r.get(f"https://api.galaxylifegame.net/users/steam?steamId={user}").json())
    except json.JSONDecodeError:
        return None


def search_user(user: str or int) -> list[classes.user.user] or None:
    try:
        if isinstance(user, int):
            return [classes.user.user(i) for i in _r.get(f"https://api.galaxylifegame.net/users/get?id={user}").json()]
        else:
            try:
                return [classes.user.user(i) for i in _r.get(f"https://api.galaxylifegame.net/users/get?id={int(user)}").json()]
            except ValueError:
                return [classes.user.user(i) for i in _r.get(f"https://api.galaxylifegame.net/users/name?name={user}").json()]
            # Handles ID's being put in as strings.
    except json.JSONDecodeError:
        return None


def get_user_stats(userID: int or str) -> classes.userstats.userstats or None:
    try:
        return classes.userstats.userstats(_r.get(f"https://api.galaxylifegame.net/users/stats?id={userID}").json())
    except json.JSONDecodeError:
        return None



if __name__ == "__main__":
    # Example code here

    print(get_user("Casper1123").stats.coinsspent)

    # entities.classes.user imports this file, therefore code is run twice outside of this statement.
    # This is because it needs to import get_user_stats :)
