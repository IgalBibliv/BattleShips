"""
Name:   battle_ships.py
Description:    File represents the whole battleships game
Creator:    Igal Bibliv
Last Modification:  29/12/2020 - Created
"""
import consts
from requests import TurnRequest


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

    def get_players_wanted_attack(self):
        """
        Function returns a wanted attack request from the player
        :return: The chosen tile
        """
        row = input("Enter your wanted row: ")
        column = input("Enter your wanted column: ")
        while not self.is_attack_valid(row, column):
            print("Invalid Input!")
            row = input("Enter your wanted row: ")
            column = input("Enter your wanted column: ")
        return TurnRequest(consts.RequestID.TURN_REQUEST, int(row) * consts.TABLE_SIZE + int(column))
