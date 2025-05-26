class Player:
    def __init__(self, name, is_ai=False):
        self.name = name
        self.is_ai = is_ai
        self.cards = []
        self.position = (0, 0)  # Can be used for movement later

    def take_turn(self):
        pass  # Future logic goes here
