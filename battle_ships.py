"""
Name:   battle_ships.py
Description:    File represents the whole battleships game
Creator:    Igal Bibliv
Last Modification:  30/12/2020 - edited
"""
import communicator
import player_interface
import table_handler


class BattleShips:
    def __init__(self, game_communicator, interface, tables):
        self.game_communicator = game_communicator
        self.interface = interface
        self.tables = tables

    def get_attacked(self):
        """
        Function handles an enemy player's attack
        """
        enemy_request = self.game_communicator.recv_msg()
        attack_result = self.tables.handle_attack(enemy_request)
        self.game_communicator.send_msg(attack_result)

    def attack(self):
        """
        Function handles the current player's attack
        """
        attack_request = self.interface.get_players_wanted_attack()
        self.game_communicator.send_msg(attack_request)
        result = self.game_communicator.recv_msg()
        self.tables.handle_result(attack_request.attacked_tile, result)
