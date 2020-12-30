"""
Name:   consts.py
Description:    All the global consts of the project
Creator:    Igal Bibliv
Last Modification:  29/12/2020 - Created
"""
PROTOCOL_VERSION = 1

TABLE_SIZE = 10
SHIPS_NUM = 5

HASH_SIZE = 32


class RequestID:
    GAME_INVITE = 1
    GAME_ACCEPT = 2
    PLACING_INFORM = 3
    TURN = 4
    TURN_RESULT = 5
    PLACEMENT_INFORM = 6


class TableSymbols:
    HIT = "X"
    EMPTY = "."
    SHIP = "S"
