import fastf1
from flask import Flask, request, jsonify
from models.Session import Session

app = Flask(__name__)

@app.route('/sessions')
def get_session():
    args = request.args
    track = args.get('track')
    year = args.get('year', type=int)
    session_id = args.get('sessionId')

    session = fastf1.get_session(year, track, session_id)
    session.load()

    session_obj = Session.create_from_session(Session(), session)
    return session_obj

if __name__ == "__main__":
    app.run(debug=True)


