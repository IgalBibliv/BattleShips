"""
Name:   game_creator.py
Description:    The functions that initialize the game and let the player to start playing
Creator:    Igal Bibliv
Last Modification:  30/12/2020 - Created
"""
import battle_ships
import communicator
import player_interface
import table_handler
import socket
import consts


def start_listening():
    """
    Function starts listening to an enemy connection
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1000)
    sock.bind((consts.MY_IP, consts.GAME_PORT))
    sock.listen()
    conn, addr = sock.accept()
    return conn


def bind_to_other_player():
    """
    Function connects to the enemy player
    """
    target_ip = input("Enter the other player's ip: ")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((target_ip, consts.GAME_PORT))
    return sock


def create_utils():
    """
    Function creates and returns the table_handler and player interface for the game
    :return: The table_handler and player interface
    """
    interface = player_interface.PlayerInterface()
    player_ships = interface.get_player_ships()
    player_table = create_table_from_ships(player_ships)
    players_table_handler = table_handler.TableHandler(player_table, player_ships)
    return interface, players_table_handler


def create_table_from_ships(ships):
    """
    Function creates the game table for the table, from the ships
    :param ships: The player's chosen ships
    :return: The new configured table
    """
    new_table = [consts.TableSymbols.NONE] * pow(consts.TABLE_SIZE, 2)
    for curr_ship in ships:
        for cord in curr_ship.ship_cords:
            new_table[cord] = consts.TableSymbols.SHIP
    return new_table


def create_connecting_player():
    """
    Function creates a player via connecting to a listening one
    :return: The BattleShips class of the player
    """
    sock = bind_to_other_player()
    player_communicator = communicator.Communicator(sock)
    interface, players_table_handler = create_utils()
    player_game = battle_ships.BattleShips(player_communicator, interface, players_table_handler, False)
    return player_game


def create_hosting_player():
    """
    Function creates a player via listening to a connection
    :return: The BattleShips class of the player
    """
    sock = start_listening()
    player_communicator = communicator.Communicator(sock)
    interface, players_table_handler = create_utils()
    player_game = battle_ships.BattleShips(player_communicator, interface, players_table_handler, True)
    return player_game


def game_runner():
    """
    Function creates a BattleShips class by the player's choices and starts playing
    """
    choice = input("Press 1 to host a game and 2 to connect to a game: ")
    if choice == "1":
        player_game = create_hosting_player()
    else:
        player_game = create_connecting_player()
    player_game.initialize_game()
    player_game.play()


def main():
    game_runner()


if __name__ == '__main__':
    main()
