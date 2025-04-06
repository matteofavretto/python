from app.session import load_session, load_event
from pick import pick

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

    for i in range(len(options)):
        print(f'{i+1}. {options[i]}')

    identifier = int(input('Select a session: '))
    selected_session = session_dict.get(identifier)

    options = [
        'Display timing sheet'
    ]

    session_object = load_session(year, track, identifier)

    for i in range(len(options)):
        print(f'{i+1}. {options[i]}')

    user_selection = int(input('What would you like to do?'))

def close():
    print('Goodbye!')

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