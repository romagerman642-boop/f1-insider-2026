from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_data(url, backup_data):
    try:
        response = requests.get(url, timeout=5)
        return response.json()
    except:
        return backup_data

@app.route('/')
def home():
    # Дата першої гонки 2026
    next_race_date = "2026-03-01T15:00:00"

    # Отримуємо розклад
    race_data = get_data('https://ergast.com/api/f1/2026.json', {})
    races = race_data.get('MRData', {}).get('RaceTable', {}).get('Races', [
        {"raceName": "Bahrain Grand Prix", "date": "2026-03-01", "Circuit": {"circuitName": "Sakhir"}},
        {"raceName": "Saudi Arabian GP", "date": "2026-03-08", "Circuit": {"circuitName": "Jeddah"}},
        {"raceName": "Australian Grand Prix", "date": "2026-03-22", "Circuit": {"circuitName": "Albert Park"}}
    ])

    # Отримуємо пілотів
    standings_data = get_data('https://ergast.com/api/f1/2026/driverStandings.json', {})
    try:
        drivers = standings_data['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']
    except:
        drivers = [
            {"position": "1", "points": "0", "Driver": {"familyName": "Verstappen", "givenName": "Max"}, "Constructors": [{"name": "Red Bull"}]},
            {"position": "2", "points": "0", "Driver": {"familyName": "Hamilton", "givenName": "Lewis"}, "Constructors": [{"name": "Ferrari"}]},
            {"position": "3", "points": "0", "Driver": {"familyName": "Leclerc", "givenName": "Charles"}, "Constructors": [{"name": "Ferrari"}]}
        ]

    return render_template('index.html', races=races, drivers=drivers, next_race=next_race_date)

if __name__ == '__main__':
    app.run(debug=True)
