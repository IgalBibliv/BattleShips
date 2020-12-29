"""
Name:   communicator.py
Description:    The class that is responsible for the communication
Creator:    Igal Bibliv
Last Modification:  29/12/2020 - Created
"""
import requests
import request_serializer


class Communicator:
    def __init__(self, sock):
        self.sock = sock
