from core.util import Utility

class SessionResult:
    def __init__(self, session_id, driver_results):
        self.session_id = session_id # FP1, FP2, FP3, Q1, Q2, Q3, SQ, SR, R
        self.driver_results = driver_results # List of drivers who started the session

    def to_dict(self):
        session_result_dict = {
            'session_id': Utility.map_session_id(self.session_id)
        }
        for driver_result in self.driver_results:
            session_result_dict[driver_result.driver.abbreviation] = driver_result.to_dict()
        return session_result_dict