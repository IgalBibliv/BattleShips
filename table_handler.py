"""
Name:   table_handler.py
Description:    Class that is responsible for the table management
Creator:    Igal Bibliv
Last Modification:  30/12/2020 - Created
"""
from consts import TABLE_SIZE, RequestID, TableSymbols
import requests
import ship


def create_empty_table():
    """
    Function returns an empty table
    :return: An empty table
    """
    return [TableSymbols.EMPTY] * pow(TABLE_SIZE, 2)


def print_table(table):
    """
    Function prints a given game table
    """
    for row in range(TABLE_SIZE):
        for column in range(TABLE_SIZE):
            print(table[row * TABLE_SIZE + column], end=" ")
        print()


class TableHandler:
    def __init__(self, my_table, my_ships):
        self.my_ships = my_ships
        self.my_table = my_table
        self.enemy_table = create_empty_table()
        self.ships_sank = 0

    def print_tables(self):
        """
        Function prints both the player's and the other player's tables
        """
        print("My table: ")
        print_table(self.my_table)
        print("Enemy table: ")
        print_table(self.enemy_table)

    def handle_attack(self, turn_request):
        """
        Function handles an attack request and returns a turn result request
        :return: The turn result request
        """
        is_hit = False
        ship_sank = 0
        for curr_ship in self.my_ships:
            if curr_ship.is_hit(turn_request.attacked_tile):
                is_hit = True
                self.my_table[turn_request.attacked_tile] = TableSymbols.HIT
                if curr_ship.is_sank():
                    ship_sank = curr_ship.ship_id
        return requests.TurnResultRequest(RequestID.TURN_RESULT, is_hit, ship_sank)

    def handle_result(self, attack_cord, turn_result):
        """
        Function handles the ship result request
        """
        if turn_result.is_hit:
            self.enemy_table[attack_cord] = TableSymbols.HIT
            if turn_result.ship_sank:
                self.enemy_table[attack_cord] = TableSymbols.SANK
                self.ships_sank += 1
        else:
            self.enemy_table[attack_cord] = TableSymbols.NONE

