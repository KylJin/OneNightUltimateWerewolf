from .base import BaseRole


class Troublemaker(BaseRole):
    role_name = "Troublemaker"

    def __init__(self, name: str):
        super().__init__(name=name)

        self.role_description = f"""You are {self.name}, the Troublemaker at the first place. 
As a Troublemaker, you may switch the roles of two other players during the Night phase, but you will not know their roles.
Those players will become the new role after your switch, even though they do not know what that is until the end of the game.
Remember, you are on Team Village. Your goal is to help other teammates to find out who are the actual Werewolves.\n""" + self.role_description
    
    def get_night_prompt(self):
        action_prompt = f"""Now it is your turn, {self.name}.
Please think about your acting strategy and choose whether to swap roles between two other players. If swap, please give the two different players you want to swap. 
You can only choose two different players from the following options: [{', '.join(self.current_players)}].
You must return your response in a JSON format that can be parsed by Python `json.loads`. Here is the Response Format:
{{
    "thought": <your acting strategy and the reason why you act in this way>,
    "swap": <`true` or `false`, whether to swap roles between two other players>,
    "player_1": <the first player to swap>,
    "player_2": <the second player to swap>
}}
"""
        return action_prompt