import pandas as pd

from core.session import load_session, load_event
from core.models import Driver, Session
from core.util import Utility
import datetime

session_names = {
    'FP1': 'Free Practice 1',
    'FP2': 'Free Practice 2',
    'FP3': 'Free Practice 3',
    'FP': 'Free Practice',
    'Q': 'Qualifying',
    'R': 'Race',
    'SQ': 'Sprint Qualifying',
    'SR': 'Sprint Race'
}

def get_event():
    year = int(input('Input the year: '))
    track = input('Input the track: ')
    event = load_event(year, track)
    is_sprint_weekend = True
    try:
        event.get_sprint()
    except ValueError:
        is_sprint_weekend = False
    if is_sprint_weekend:
        options = ['FP', 'SQ', 'SR', 'Q', 'R']
    else:
        options = ['FP1', 'FP2', 'FP3', 'Q', 'R']

    session_dict = {}

    for index, session_id in enumerate(options):
        session_dict[index] = session_id

    print('Select a session: ')
    for i in range(len(options)):
        print(f'{i+1}. {options[i]}')
    identifier = int(input(''))

    selected_session = session_dict.get(identifier)

    options = [
        'Display timing sheet'
    ]

    session = load_session(year, track, identifier)

    print('What would you like to do?')
    for i in range(len(options)):
        print(f'{i+1}. {options[i]}')
    user_selection = int(input(''))

    options = [
        'Q1',
        'Q2',
        'Q3'
    ]

    print('Select the session:')
    for i in range(len(options)):
        print(f'{i+1}. {options[i]}')
    selected_session = input('')

    display_timing_sheet(session, selected_session)

def close():
    print('Goodbye!')

class DriverSessionResult:
    def __init__(self, driver, fastest_lap):
        self.driver = driver
        self.fastest_lap = fastest_lap

def display_timing_sheet(session, selected_session):
    driver_results = {}
    for index, driver_num in enumerate(session.drivers):
        driver = session.drivers[driver_num]
        abbreviation = driver.Abbreviation
        if selected_session == '1':
            fastest_lap = driver.Q1
        elif selected_session == '2':
            fastest_lap = driver.Q2
        else:
            fastest_lap = driver.Q3
        driver_results[abbreviation] = fastest_lap

    sorted_drivers_results = sorted(driver_results.items(), key=lambda item: item[1])
    for index, driver_result in enumerate(sorted_drivers_results):
        abbreviation = driver_result[0]
        fastest_lap = driver_result[1]
        if fastest_lap is pd.NaT:
            fastest_lap = 'NO TIME'
        else:
            fastest_lap = Utility.format_timedelta(fastest_lap)
        print(f'{index+1}. {abbreviation} - {fastest_lap}')


# Instead of using switch-case to handle the different possible user selections,
# create a dictionary of functions to call depending on user selection

menu_actions = {
    '1': get_event,
    '2': close
}

def user_menu():
    user_selection = input('Welcome! Select an option:\n1. Display session information\n2. Quit\n')
    action = menu_actions.get(user_selection)
    if action:
        action()
    else:
        print('Please select an option from the menu!')