"""
Name:   ship.py
Description:    class represents a basic ship
Creator:    Igal Bibliv
Last Modification:  29/12/2020 - Created
"""


class Ship:
    def __init__(self, ship_id, ship_cords):
        self.ship_id = ship_id
        self.ship_cords = ship_cords
        self.hits = 0

    def get_len(self):
        """
        Function returns the ship's length
        :return: The ships length
        """
        return len(self.ship_cords)

    def is_hit(self, attack_cord):
        """
        Function checks if a hit occurred, if True adds 1 to the hits and returns the result
        :return: True if the ship got hit, else False
        """
        if attack_cord in self.ship_cords:
            self.hits += 1
            return True
        return False

    def is_sank(self):
        """
        Function checks if a ship sank or not
        :return: True if it sank, else False
        """
        return self.hits >= self.get_len()
