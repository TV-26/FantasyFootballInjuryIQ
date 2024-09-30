import datetime
class InjuryReport:
    def __init__(self, injury: str, league: str):
        self.injury = injury
        self.league = league

    def display_report(self):
        return f"Injury: {self.injury}, League: {self.league}"

# Child class for game-related injury
class GameInjuryReport(InjuryReport):
    def __init__(self, season: int, game_type: str, team: str, week: int, report_primary_injury: str, report_secondary_injury: str, 
                 report_status: str, practice_primary_injury: str, practice_secondary_injury: str, 
                 practice_status: str, injured_in_game: bool):
        # Call the parent class constructor with the correct arguments
        super().__init__(report_primary_injury, "NFL")  # Only 2 arguments: injury and league

        # Assigning all other attributes for GameInjuryReport
        self.season = season
        self.game_type = game_type
        self.team = team
        self.week = week
        self.report_secondary_injury = report_secondary_injury
        self.report_status = report_status
        self.practice_primary_injury = practice_primary_injury
        self.practice_secondary_injury = practice_secondary_injury
        self.practice_status = practice_status
        self.injured_in_game = injured_in_game


    def display_report(self):
        report = super().display_report()
        return (f"{report}, Season: {self.season}, Team: {self.team}, Week: {self.week}, "
                f"Game Type: {self.game_type}, "
                f"Primary Injury: {self.injury}, Secondary Injury: {self.report_secondary_injury}, "
                f"Practice Status: {self.practice_status}")

# Child class for detailed injury
class DetailedInjuryReport(InjuryReport):
    def __init__(self, date: datetime, injury: str, league: str, details: str):
        super().__init__(injury, league)
        self.details = details
        self.date = date

    def display_report(self):
        report = super().display_report()
        return f"{report}, Details: {self.details}, Date: {self.date}"
