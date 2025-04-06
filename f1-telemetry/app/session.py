import fastf1

def load_event(year, track):
    return fastf1.get_event(year, track)

def load_session(year, track, qualifier):
    return fastf1.get_session(year, track, qualifier)

