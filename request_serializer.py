"""
Name:   request_serializer.py
Description:    File contains all the request serializers
Creator:    Igal Bibliv
Last Modification:  29/12/2020 - Created
"""
import requests
from consts import PROTOCOL_VERSION, RequestID, SHIPS_NUM


def serialize_game_invite_request(game_invite_request):
    """
    Creates a game invite request
    :return: A byte array of a game invite request
    """
    return bytes([PROTOCOL_VERSION, game_invite_request.request_type])


def serialize_game_accept_request(game_accept_request):
    """
    Creates a game accept request
    :return: A byte array of a game accept request
    """
    return bytes([PROTOCOL_VERSION, game_accept_request.request_type])


def serialize_pacing_inform_request(placing_inform_request):
    """
    Creates a placing inform request
    :param placing_inform_request: The PlacingInform class
    :return: A byte array of a placing inform request
    """
    return bytes([PROTOCOL_VERSION, placing_inform_request.request_type]) + bytes(placing_inform_request.table_hash)


def serialize_turn_request(turn_request):
    """
    Creates a turn request
    :param turn_request: The TurnRequest class
    :return: A byte array of a turn request
    """
    return bytes([PROTOCOL_VERSION, turn_request.request_type]) + turn_request.attacked_tile


def serialize_turn_result_request(turn_result_request):
    """
    Creates a turn result request
    :param turn_result_request: The TurnResultRequest class
    :return: A byte array of a  turn result request
    """
    return bytes([PROTOCOL_VERSION, turn_result_request.request_type]) + bytes([turn_result_request.is_hit]) \
           + bytes([turn_result_request.ship_sank])


def serialize_placement_inform_request(placement_inform_request):
    """
    Creates a placement inform request
    :param placement_inform_request: The PlacementInformRequest class
    :return: A byte array of the placement inform request
    """
    request_bytes = [PROTOCOL_VERSION, placement_inform_request.request_type]
    for curr_ship in range(SHIPS_NUM):
        request_bytes.append(placement_inform_request.locations[curr_ship])
        request_bytes.append(placement_inform_request.tilts[curr_ship])
    return bytes(request_bytes) + placement_inform_request.nonce.to_bytes(4, byteorder='little')


SERIALIZERS = {RequestID.GAME_INVITE: serialize_game_invite_request,
               RequestID.GAME_ACCEPT: serialize_game_accept_request,
               RequestID.PLACING_INFORM: serialize_pacing_inform_request,
               RequestID.TURN: serialize_turn_request,
               RequestID.TURN_RESULT: serialize_turn_result_request,
               RequestID.PLACEMENT_INFORM: serialize_placement_inform_request}
