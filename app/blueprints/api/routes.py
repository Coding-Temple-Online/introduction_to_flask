from flask import render_template, request
import requests
from .import bp as api

@api.route('/ergast', methods=['GET', 'POST'])
def ergast():
    if request.method == 'POST':
        year = request.form.get('year')
        data = requests.get(f'https://ergast.com/api/f1/{year}/5/driverStandings.json').json()['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']
        context = {
            'racers': data
        }
    else:
        context = {
            'racers': []
        }
    return render_template('api/ergast.html', **context)