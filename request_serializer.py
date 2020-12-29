import requests
from consts import PROTOCOL_VERSION, RequestID


def serialize_game_invite_request():
    """
    Creates a game invite request
    :return: A byte array of a game invite request
    """
    return bytes([PROTOCOL_VERSION, RequestID.GAME_INVITE])
