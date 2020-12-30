"""
Name:   table_handler.py
Description:    Class that is responsible for the table management
Creator:    Igal Bibliv
Last Modification:  30/12/2020 - Created
"""
from consts import TABLE_SIZE
import requests


def create_empty_table():
    """
    Function returns an empty table
    :return: An empty table
    """
    return ["."] * pow(TABLE_SIZE, 2)


def print_table(table):
    """
    Function prints a given game table
    """
    for row in range(TABLE_SIZE):
        for column in range(TABLE_SIZE):
            print(table[row * TABLE_SIZE + column], end=" ")
        print()


class TableHandler:
    def __init__(self, my_table):
        self.my_table = my_table
        self.enemy_table = create_empty_table()

    def print_tables(self):
        """
        Function prints both the player's and the other player's tables
        """
        print("My table: ")
        print_table(self.my_table)
        print("enemy table: ")
        print_table(self.enemy_table)

    def handle_attack(self, turn_request):
        pass
