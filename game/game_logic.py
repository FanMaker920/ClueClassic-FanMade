import random
from game.player import Player
from game.ai import AILogic
import json

class Game:
    def __init__(self, board):
        self.board = board
        self.players = [Player("You"), Player("AI 1", True), Player("AI 2", True)]
        self.load_cards()
        self.solution = self.deal_cards()

    def load_cards(self):
        with open("assets/cards/suspects.json") as f:
            self.suspects = json.load(f)
        with open("assets/cards/rooms.json") as f:
            self.rooms = json.load(f)
        with open("assets/cards/weapons.json") as f:
            self.weapons = json.load(f)

    def deal_cards(self):
        suspect = random.choice(self.suspects)
        room = random.choice(self.rooms)
        weapon = random.choice(self.weapons)
        solution = (suspect, room, weapon)

        remaining = [s for s in self.suspects if s != suspect] + \
                    [r for r in self.rooms if r != room] + \
                    [w for w in self.weapons if w != weapon]
        random.shuffle(remaining)

        while remaining:
            for player in self.players:
                if remaining:
                    player.cards.append(remaining.pop())

        return solution

    def update(self):
        # Placeholder for game logic updates (turns, suggestions, etc.)
        pass
