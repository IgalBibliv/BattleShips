"""
Name:   requests.py
Description:    File contains all the request classes
Creator:    Igal Bibliv
Last Modification:  29/12/2020 - Created
"""


class ShipIndexes:
    """
    The ship indexes in the PlacementInfoRequest
    """
    LONGEST_SHIP = 0  # length: 5
    BIG_SHIP = 1  # length: 4
    FIRST_SHORT_SHIP = 2  # length: 3
    SECOND_SHORT_SHIP = 3  # length: 3
    SHORTEST_SHIP = 4  # length: 2


class IRequest:
    """
    The request interface
    """
    def __init__(self, request_type):
        self.request_type = request_type


class GameInviteRequest(IRequest):
    """
    Request that represents a game invite
    """
    def __init__(self, request_type):
        super().__init__(request_type)


class GameAcceptRequest(IRequest):
    """
    Request that represents a game accept
    """
    def __init__(self, request_type):
        super().__init__(request_type)


class PlacingInfoRequest(IRequest):
    """
    Request that represents the placement info, for validity check in the end
    """
    def __init__(self, request_type, table_hash):
        super().__init__(request_type)
        self.table_hash = table_hash


class TurnRequest(IRequest):
    """
    Request that represents a players turn
    """
    def __init__(self, request_type, attacked_tile):
        super().__init__(request_type)
        self.attacked_tile = attacked_tile


class TurnResultRequest(IRequest):
    """
    Request that represents a turn response
    """
    def __init__(self, request_type, is_hit, ship_sank):
        super().__init__(request_type)
        self.is_hit = is_hit
        self.ship_sank = ship_sank


class PlacementInfoRequest(IRequest):
    """
    Not my idea.
    Used for calculating the validity of the table in the endgame.
    """
    def __init__(self, request_type, locations, tilts, nonce):
        super().__init__(request_type)

        self.longest_ship_loc = locations[ShipIndexes.LONGEST_SHIP]
        self.big_ship_loc = locations[ShipIndexes.BIG_SHIP]
        self.first_short_ship_loc = locations[ShipIndexes.FIRST_SHORT_SHIP]
        self.second_short_ship_loc = locations[ShipIndexes.SECOND_SHORT_SHIP]
        self.shortest_ship_loc = locations[ShipIndexes.SHORTEST_SHIP]

        self.longest_ship_tilt = tilts[ShipIndexes.LONGEST_SHIP]
        self.big_ship_tilt = tilts[ShipIndexes.BIG_SHIP]
        self.first_short_ship_tilt = tilts[ShipIndexes.FIRST_SHORT_SHIP]
        self.second_short_ship_tilt = tilts[ShipIndexes.SECOND_SHORT_SHIP]
        self.shortest_ship_tilt = tilts[ShipIndexes.SHORTEST_SHIP]

        self.nonce = nonce
