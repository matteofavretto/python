from datetime import timedelta

session_full_names = {
    'FP1': 'Free Practice 1',
    'FP2': 'Free Practice 2',
    'FP3': 'Free Practice 3',
    'Q': 'Qualifying',
    'SQ': 'Sprint Qualifying',
    'R': 'Race',
    'SR': 'Sprint Race'
}

def format_timedelta(td: timedelta):
    total_seconds = td.total_seconds()
    minutes = int(total_seconds // 60)
    seconds = int(total_seconds % 60)
    milliseconds = int((total_seconds - int(total_seconds)) * 1000)
    return f'{minutes:02}:{seconds:02}.{milliseconds:03}'

def map_session_id(session_id):
    return session_full_names[session_id]
