import battle_ships
import communicator
import player_interface
import table_handler
import ship
import socket
import consts


def start_listening():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((consts.MY_IP, consts.GAME_PORT))
    sock.listen()
    conn, addr = sock.accept()
    return sock


def bind_to_other_player():
    target_ip = input("Enter the other player's ip: ")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((target_ip, consts.GAME_PORT))
    return sock


def create_utils():
    interface = player_interface.PlayerInterface()
    player_ships = interface.get_player_ships()
    player_table = create_table_from_ships(player_ships)
    players_table_handler = table_handler.TableHandler(player_table, player_ships)
    return interface, players_table_handler


def create_table_from_ships(ships):
    new_table = [consts.TableSymbols.NONE] * pow(consts.TABLE_SIZE, 2)
    for curr_ship in ships:
        for cord in curr_ship.ship_cords:
            new_table[cord] = consts.TableSymbols.SHIP
    return new_table


def create_connecting_player():
    sock = bind_to_other_player()
    print("Connected to target")
    player_communicator = communicator.Communicator(sock)
    interface, players_table_handler = create_utils()
    player_game = battle_ships.BattleShips(player_communicator, interface, players_table_handler, False)
    return player_game


def create_hosting_player():
    sock = start_listening()
    print("Connected")
    player_communicator = communicator.Communicator(sock)
    interface, players_table_handler = create_utils()
    player_game = battle_ships.BattleShips(player_communicator, interface, players_table_handler, True)
    return player_game


def game_runner():
    choice = input("Press 1 to host a game and 2 to connect to a game: ")
    if choice == "1":
        player_game = create_hosting_player()
    else:
        player_game = create_connecting_player()
    return player_game


def main():
    game_runner()


if __name__ == '__main__':
    main()
