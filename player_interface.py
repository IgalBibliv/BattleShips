"""
Name:   battle_ships.py
Description:    File represents the whole battleships game
Creator:    Igal Bibliv
Last Modification:  29/12/2020 - Created
"""
import consts
from requests import TurnRequest
import ship

SHIP_LENGTH_TO_ID = [(5, 1), (4, 2), (3, 3), (3, 4), (2, 5)]
LEN_LOC = 0
ID_LOC = 1


def get_ship_coordinates(ship_len, is_horizontal, start_coordinate):
    """
    Function gets the top left ship coordinate, it's tile and it's len and returns all the rest of the ship coordinates
    :param ship_len: The ships length
    :param is_horizontal: The ships tilt
    :param start_coordinate: The ships top left coordinate
    """
    coordination = []
    for curr_coordination in range(ship_len):
        if is_horizontal:
            coordination.append(start_coordinate + 1 * curr_coordination)
        else:
            coordination.append(start_coordinate + 10 * curr_coordination)
    return coordination


class PlayerInterface:
    def __init__(self):
        pass

    def is_attack_valid(self, row, column):
        """
        Function checks weather an wanted tile is valid or not
        :param row: The tile's row
        :param column: The tile's column
        :return: True if the tile is valid, else False
        """
        return row.isdigit() and column.isdigit() and \
               0 <= int(row) < consts.TABLE_SIZE and \
               0 <= int(column) < consts.TABLE_SIZE

    def get_coordinates(self):
        """
        Function gets a coordinate from a player
        :return: A valid coordinate
        """
        row = input("Enter your wanted row: ")
        column = input("Enter your wanted column: ")
        while not self.is_attack_valid(row, column):
            print("Invalid Input!")
            row = input("Enter your wanted row: ")
            column = input("Enter your wanted column: ")
        return int(row) * consts.TABLE_SIZE + int(column)

    def get_players_wanted_attack(self):
        """
        Function returns a wanted attack request from the player
        :return: The chosen tile
        """
        tile_to_attack = self.get_coordinates()
        return TurnRequest(consts.RequestID.TURN, tile_to_attack)

    def get_player_ships(self):
        """
        Function gets the wanted ship locations from a player
        :return: The player's chosen ship locations
        """
        player_ships = []
        for curr_ship in SHIP_LENGTH_TO_ID:
            print(f"Enter the top left coordinate of ship with len {curr_ship[LEN_LOC]}")
            ship_first_coordinate = self.get_coordinates()
            is_tilted = input("Press 1 if the ship is horizontal, else 2: ")
            ship_cords = get_ship_coordinates(curr_ship[LEN_LOC], is_tilted == "1", ship_first_coordinate)
            player_ships.append(ship.Ship(curr_ship[ID_LOC], ship_cords))
        return player_ships
