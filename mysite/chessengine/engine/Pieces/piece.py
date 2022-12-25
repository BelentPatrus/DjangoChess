from abc import ABC, abstractmethod
class Piece(ABC):
    def __init__(self, team):
        self.team = team

    @abstractmethod
    def validMove(self):
        pass
    
    

