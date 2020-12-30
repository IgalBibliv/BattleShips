"""
Name:   communicator.py
Description:    The class that is responsible for the communication
Creator:    Igal Bibliv
Last Modification:  29/12/2020 - Created
"""
import requests
import request_serializer
from consts import RequestID, HASH_SIZE, PROTOCOL_VERSION, SHIPS_NUM


class Communicator:
    def __init__(self, sock):
        self.sock = sock

    def recv_game_invite_request(self):
        """
        Function receives a game invite request from the other player and returns it
        :return: A game invite request
        """
        return requests.GameInviteRequest(RequestID.GAME_INVITE)

    def recv_game_accept_request(self):
        """
        Function receives a game accept request from the other player and returns it
        :return: A game accept request
        """
        return requests.GameAcceptRequest(RequestID.GAME_ACCEPT)

    def recv_placing_inform_request(self):
        """
        Function receives a placing inform request from the other player and returns it
        :return: A placing inform request
        """
        new_hash = self.sock.recv(HASH_SIZE)
        return requests.PlacingInfoRequest(RequestID.PLACING_INFORM, new_hash)

    def recv_turn_request(self):
        """
        Function receives a turn request from the other player and returns it
        :return: A turn request
        """
        attacked_tile = self.sock.recv(1)
        return requests.TurnRequest(RequestID.TURN, attacked_tile)

    def recv_turn_result_request(self):
        """
        Function receives a turn result request from the other player and returns it
        :return: A turn result request
        """
        is_hit = bool(self.sock.recv(1))
        ship_sank = self.sock.recv(1)
        return requests.TurnResultRequest(RequestID.TURN_RESULT, is_hit, ship_sank)

    def recv_placement_inform_request(self):
        """
        Function receives a placement inform request from the other player and returns it
        :return: A placement inform request
        """
        locations = []
        tilts = []
        for curr_ship in range(SHIPS_NUM):
            locations.append(self.sock.recv(1))
            tilts.append(self.sock.recv(1))
        nonce = self.sock.recv(4)
        return requests.PlacementInfoRequest(RequestID.PLACEMENT_INFORM, locations, tilts, nonce)

    REQUEST_RECEIVERS = {RequestID.GAME_INVITE: recv_game_invite_request,
                         RequestID.GAME_ACCEPT: recv_game_accept_request,
                         RequestID.PLACING_INFORM: recv_placing_inform_request,
                         RequestID.TURN: recv_turn_request,
                         RequestID.TURN_RESULT: recv_turn_result_request,
                         RequestID.PLACEMENT_INFORM: recv_placement_inform_request}

    def recv_msg(self):
        """
        Function receives a request from the other player and returns it
        :return: The other player's request
        """
        prot_version = self.sock.recv(1)
        if prot_version != PROTOCOL_VERSION:
            return
        request_type = self.sock.recv(1)
        return self.REQUEST_RECEIVERS[request_type]()

    def send_msg(self, curr_request):
        """
        Function sends the request through the socket in byte form
        """
        request_to_send = request_serializer.SERIALIZERS[curr_request.request_type](curr_request)
        self.sock.send(request_to_send)
