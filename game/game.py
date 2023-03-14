"""
Game classes
"""


class Room:
    """
    Room class
    """

    def __init__(self, name) -> None:
        """
        Intial method
        """
        self.name = name
        self.linked_sides = {}
        self.character = None
        self.item = None
        self.description = ""

    def set_description(self, desc):
        """
        Setter description
        """
        self.description = desc

    def link_room(self, another_room, side):
        """
        Link one room to another
        """
        self.linked_sides[side] = another_room

    def set_character(self, character):
        """
        Setter for character
        """
        self.character = character

    def get_character(self):
        """
        Getter for character
        """
        return self.character

    def set_item(self, item):
        """
        Setter for item
        """
        self.item = item

    def get_item(self):
        """
        Getter for item
        """
        return self.item

    def get_details(self):
        """
        Print details about room
        """
        print_text = ""
        print_text += f"{self.name}\n--------------------\n{self.description}\n"
        for key, value in self.linked_sides.items():
            print_text += value.name + " is " + key + "\n"
        print_text = print_text[:-1]
        print(print_text)
        return

    def move(self, command):
        """
        Change room
        """
        return self.linked_sides[command]

class Character:
    def __init__(self, name, desc) -> None:
        """
        Initial method
        """
        self.name = name
        self.description = desc
        self.weakness = ""
        self.words = ""

    def set_conversation(self, words):
        """
        Setter conversation
        """
        self.words = words

    def set_weakness(self, weakness):
        """
        Setter weakness
        """
        self.weakness = weakness

    def describe(self):
        """
        Print info about enemy
        """
        print(f"{self.name} is here!\n{self.description}")

    def talk(self):
        """
        print enemy words
        """
        print(f"[{self.name} says]: {self.words}")

class Enemy(Character):
    """
    Enemy class
    """
    defeted = 0
    def fight(self, item):
        """
        Fight method
        """
        if self.weakness == item:
            Enemy.defeted += 1
            return True
        else:
            return False

    def get_defeated(self):
        """
        Checks if monsters is defeted
        """
        return Enemy.defeted

class Friend(Character):
    """
    Friend
    """
    def __init__(self, name, desc) -> None:
        """
        """
        self.friend=True
        super().__init__(name, desc)
class Item:
    """
    Item class
    """

    def __init__(self, name) -> None:
        """
        initial method
        """
        self.name = name
        self.description = ""

    def set_description(self, desc):
        """
        Setter for description
        """
        self.description = desc

    def describe(self):
        """
        Print info about item
        """
        print(f"The [{self.name}] is here - {self.description}")

    def get_name(self):
        """
        Getter for name
        """
        return self.name
