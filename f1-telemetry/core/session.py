import fastf1

from core.models.Session import Session


def load_event(year, track):
    return fastf1.get_event(year, track)

def load_session(year, track, qualifier):
    session_object = fastf1.get_session(year, track, qualifier)
    session_object.load()
    drivers = {}
    for driver_number in session_object.drivers:
        drivers[driver_number] = session_object.get_driver(driver_number)
    return Session(year, track, qualifier, drivers)

