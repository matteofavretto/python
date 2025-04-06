from datetime import timedelta

def format_timedelta(td: timedelta):
    total_seconds = td.total_seconds()
    minutes = int(total_seconds // 60)
    seconds = int(total_seconds % 60)
    milliseconds = int((total_seconds - int(total_seconds)) * 1000)
    return f'{minutes:02}:{seconds:02}.{milliseconds:03}'
