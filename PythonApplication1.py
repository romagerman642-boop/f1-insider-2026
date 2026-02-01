from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Дата першої гонки для таймера
    next_race_date = "2026-03-01T15:00:00"

    # Дані розкладу гонок
    races = [
        {"raceName": "Bahrain Grand Prix", "date": "2026-03-01", "Circuit": {"circuitName": "Sakhir"}},
        {"raceName": "Saudi Arabian GP", "date": "2026-03-08", "Circuit": {"circuitName": "Jeddah"}},
        {"raceName": "Australian Grand Prix", "date": "2026-03-22", "Circuit": {"circuitName": "Albert Park"}}
    ]

    # Дані пілотів
    drivers = [
        {"position": "1", "points": "0", "Driver": {"familyName": "Verstappen", "givenName": "Max"}, "Constructors": [{"name": "Red Bull"}]},
        {"position": "2", "points": "0", "Driver": {"familyName": "Hamilton", "givenName": "Lewis"}, "Constructors": [{"name": "Ferrari"}]},
        {"position": "3", "points": "0", "Driver": {"familyName": "Leclerc", "givenName": "Charles"}, "Constructors": [{"name": "Ferrari"}]}
    ]

    return render_template('index.html', races=races, drivers=drivers, next_race=next_race_date)

if __name__ == '__main__':
    app.run()
