'''Modul'''
class Action:
    '''Action class'''
    action_values = {"Rock": 0, "Sciccors": 1, "Paper": 2}
    action_names = {val: name for name, val in action_values.items()}

    def __init__(self, value):
        if isinstance(value, str):
            value = self.action_values[value]
        assert isinstance(value, int) & (value >= 0) & (value < 3)
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __gt__(self, other):
        return (self.value + 1) % 3 == other.value

    def __str__(self):
        return self.action_names[self.value]

    def who_beats_me(self):
        '''method for counter attack'''
        return (self.value + 2) % 3
