from Injury import InjuryReport
class Player:
    def __init__(self, first_name: str, last_name: str, position: str):
        """
        Initialize the Player class.
        
        Args:
        - name (str): The player's name.
        - position (str): The player's position (e.g., quarterback, striker).
        """
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.injuries = []
        
    def add_injury(self, injury: InjuryReport):
        """
        Add an injury to the player's injury list.
        
        Args:
        - injury (Injury): An instance of the Injury class.
        """
        self.injuries.append(injury)

    def list_injuries(self):
        """
        List all injuries for the player.
        """
        return [str(injury) for injury in self.injuries]
