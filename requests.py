"""
Name:   requests.py
Description:    File contains all the request classes
Creator:    Igal Bibliv
Last Modification:  29/12/2020 - Created
"""


class IRequest:
    def __init__(self, request_type):
        self.request_type = request_type
