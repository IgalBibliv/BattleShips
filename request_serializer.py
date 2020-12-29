import requests
from consts import PROTOCOL_VERSION, RequestID


def serialize_game_invite_request():
    """
    Creates a game invite request
    :return: A byte array of a game invite request
    """
    return bytes([PROTOCOL_VERSION, RequestID.GAME_INVITE])


def serialize_game_accept_request():
    """
    Creates a game accept request
    :return: A byte array of a game accept request
    """
    return bytes([PROTOCOL_VERSION, RequestID.GAME_ACCEPT])


def serialize_pacing_inform_request(placing_inform_request):
    """
    Creates a game invite request
    :return: A byte array of a game invite request
    """
    return bytes([PROTOCOL_VERSION, RequestID.PLACING_INFORM]) + bytes(placing_inform_request.table_hash)


def serialize_turn_request(turn_request):
    """
    Creates a game invite request
    :return: A byte array of a game invite request
    """
    return bytes([PROTOCOL_VERSION, RequestID.TURN]) + turn_request.attacked_tile
