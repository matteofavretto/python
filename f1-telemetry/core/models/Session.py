class Session:
    def __init__(self):
        self.year = None
        self.track = None
        self.identifier = None
        self.drivers = None

    def create_with_data(self, year, track, identifier, drivers):
        self.year = year
        self.track = track
        self.identifier = identifier
        self.drivers = drivers
        return self

    def create_from_session(self, session):
        self.year = session.event.year
        self.track = session.event.Location
        self.drivers = session.results.BroadcastName.iloc[1:].tolist()
        return self.to_dict()

    def to_dict(self):
        return {
            'track': self.track,
            'year': self.year,
            'session_id': self.identifier,
            'drivers': self.drivers
        }