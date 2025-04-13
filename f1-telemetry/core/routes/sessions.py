from flask import Blueprint, jsonify, request
import fastf1
from core.models.Session import Session
from core.models.Driver import Driver
from core.models.DriverResult import DriverResult
from core.util import Utility
import pandas as pd

from core.models.SessionResult import SessionResult

sessions_bp = Blueprint('sessions', __name__)

@sessions_bp.route('/sessions', methods=['GET'])
def get_session():
    args = request.args
    track = args.get('track')
    year = args.get('year', type=int)
    session_id = args.get('sessionId')

    try:
        session_resource = fastf1.get_session(year, track, session_id)
    except ValueError:
        return jsonify({"error": "Session not found for the specified parameters"}), 404

    session_resource.load()

    session = Session(track, year, session_id)

    drivers_abbrevs = pd.Series(dict(session_resource.results.Abbreviation))
    drivers_full_names = pd.Series(dict(session_resource.results.BroadcastName))
    drivers_teams = pd.Series(dict(session_resource.results.TeamName))
    drivers_grid_position = pd.Series(dict(session_resource.results.GridPosition))
    drivers_race_position = pd.Series(dict(session_resource.results.Position))

    drivers_results = []

    for number in drivers_abbrevs.index:
        driver = Driver(drivers_abbrevs[number])
        driver.set_race_number(number)
        driver.set_full_name(drivers_full_names[number])
        driver.set_team(drivers_teams[number])
        driver_result = DriverResult(driver)
        driver_result.set_lap_times(session_resource.laps.pick_driver(driver.abbreviation))
        driver_result.set_fastest_lap(Utility.format_timedelta(session_resource.laps.pick_driver(driver.abbreviation).pick_fastest().Time))
        driver_result.set_grid_position(drivers_grid_position[number])
        driver_result.set_finishing_position(drivers_race_position[number])
        drivers_results.append(driver_result)

    session_results = SessionResult(session_id, drivers_results)

    return session_results.to_dict()