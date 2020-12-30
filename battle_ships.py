"""
Name:   battle_ships.py
Description:    File represents the whole battleships game
Creator:    Igal Bibliv
Last Modification:  30/12/2020 - edited
"""
import communicator
import player_interface
import table_handler
import requests
import consts


class BattleShips:
    def __init__(self, game_communicator, interface, tables, is_playing):
        self.game_communicator = game_communicator
        self.interface = interface
        self.tables = tables
        self.is_playing = is_playing

    def initialize_game(self):
        if self.is_playing:
            self.game_communicator.recv_msg()
            self.game_communicator.send_msg(requests.GameAcceptRequest(consts.RequestID.GAME_ACCEPT))
        else:
            self.game_communicator.send_msg(requests.GameAcceptRequest(consts.RequestID.GAME_INVITE))
            self.game_communicator.recv_msg()

    def get_attacked(self):
        """
        Function handles an enemy player's attack
        """
        print("\nGetting attacked!\n")
        enemy_request = self.game_communicator.recv_msg()
        attack_result = self.tables.handle_attack(enemy_request)
        self.game_communicator.send_msg(attack_result)

    def attack(self):
        """
        Function handles the current player's attack
        """
        print("\nAttacking!\n")
        attack_request = self.interface.get_players_wanted_attack()
        self.game_communicator.send_msg(attack_request)
        result = self.game_communicator.recv_msg()
        self.tables.handle_result(attack_request.attacked_tile, result)

    def play(self):
        while True:
            self.tables.print_tables()
            if self.is_playing:
                self.attack()
            else:
                self.get_attacked()
            self.is_playing = not self.is_playing
