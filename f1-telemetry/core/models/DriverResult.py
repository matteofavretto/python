from core.util import Utility

class DriverResult:
    def __init__(self, driver):
        self.driver = driver
        self.lap_times = []
        self.fastest_lap = None
        self.finishing_position = None # Only for race and sprint race
        self.grid_position = None # Only for race and sprint race
        self.completed_laps = None # Only for race and sprint race

    def set_lap_times(self, lap_times):
        for index, lap_time in enumerate(lap_times.Time):
            self.lap_times.append(Utility.format_timedelta(lap_time))

    def set_fastest_lap(self, fastest_lap):
        self.fastest_lap = fastest_lap

    def set_finishing_position(self, finishing_position):
        self.finishing_position = finishing_position

    def set_grid_position(self, grid_position):
        self.grid_position = grid_position

    def set_completed_laps(self, completed_laps):
        self.completed_laps = completed_laps

    def to_dict(self):
        return {
            'driver': self.driver.to_dict(),
            'finishing_position': self.finishing_position,
            'grid_position': self.grid_position
        }