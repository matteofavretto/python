# import fastf1
#
# fastf1.Cache.enable_cache('cache')
#
# session = fastf1.get_session(2021, 'Abu Dhabi', 'R')
# session.load()
#
# laps = session.laps.pick_fastest()
# print(laps[['Driver', 'LapTime']])

from app.menu import user_menu

def main():
    user_menu()

if __name__ == '__main__':
    main()
