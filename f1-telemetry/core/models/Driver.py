class Driver:
    def __init__(self, abbreviation):
        self.team = None
        self.race_number = None
        self.full_name = None
        self.abbreviation = abbreviation

    def set_full_name(self, full_name):
        self.full_name = full_name

    def set_race_number(self, number):
        self.race_number = number

    def set_team(self, team):
        self.team = team

    def to_dict(self):
        return {
            'full_name': self.full_name,
            'team': self.team,
            'race_number': self.race_number,
            'abbreviation': self.abbreviation
        }