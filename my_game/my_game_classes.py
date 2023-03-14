"""
Game classes
"""
import random


class Street:
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
        self.apple_tree = False
        self.available_actions = ["вліво", "вправо"]

    def add_apple_tree(self):
        """
        Apple tree
        """
        self.apple_tree = True
        self.available_actions.append("зірвати яблучко")

    def add_available_actions(self, item):
        """
        Add available action
        """
        self.available_actions.append(item)
        return

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
            print_text += value.name + " є " + key + "\n"
        for index, action in enumerate(self.get_available()):
            print_text += f"{index}) Ти можеш : {action}\n"
        print_text = print_text[:-1]
        print(print_text)
        return

    def move(self, command):
        """
        Change room
        """
        return self.linked_sides[command]

    def del_available(self, action):
        """
        Del acction
        """
        self.available_actions = list(
            filter(lambda x: x != action, self.available_actions)
        )

    def get_available(self):
        """
        Available methods
        """

        if self.character:
            if self.character.defeted:
                return self.available_actions
            return [
                action
                for action in self.available_actions
                if (action != "вліво" and action != "вправо")
            ]
        else:
            return self.available_actions


class Character:
    """
    Character class
    """

    def __init__(self, name, desc) -> None:
        """
        Initial method
        """
        self.name = name
        self.description = desc
        self.weakness = ""
        self.words = ""
        self.defeted = False

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
        print(f"{self.name} тут!\n{self.description}")

    def talk(self):
        """
        print enemy words
        """
        if self.words:
            print(f"[{self.name} каже]: {self.words}")

    def get_defeated(self):
        """
        Checks if monsters is defeted
        """
        return self.defeted


class Enemy(Character):
    """
    Enemy class
    """

    def __init__(self, name, desc) -> None:
        self.patience = 0
        super().__init__(name, desc)

    def fight(self, item):
        """
        Fight method
        """
        if self.weakness == item:
            self.defeted = True
            return True
        else:
            return False

    def get_patience(self):
        """
        Patience getter
        """
        return self.patience

    def add_patience(self):
        """
        Patience setter
        """
        self.patience += 1


class MathExam(Enemy):
    """
    Math exam
    """

    def __init__(self, name, desc, complexity) -> None:
        self._complexity = complexity
        super().__init__(name, desc)

    @property
    def complexity(self):
        """
        Complexity property
        """
        return self._complexity

    @complexity.setter
    def complexity(self, value):
        self._complexity = value

    def get_equations(self):
        """
        Return equation
        """
        equations = []
        for _ in range(self.complexity):
            equations.append(
                (
                    random.randint(self.complexity * 100, self.complexity * 200),
                    random.randint(self.complexity * 100, self.complexity * 200),
                )
            )
        return equations


class Item:
    """
    Item class
    """

    def __init__(self, name, description) -> None:
        """
        initial method
        """
        self.name = name
        self.description = description
        self.action = ""

    def set_action(self, action):
        """
        Action setter
        """
        self.action = action

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
