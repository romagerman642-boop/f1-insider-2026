from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    next_race_date = "2026-03-01T15:00:00"

    # ПОВНИЙ РОЗКЛАД СЕЗОНУ 2026 (усі основні етапи)
    races = [
        {"raceName": "Bahrain Grand Prix", "date": "2026-03-01", "Circuit": {"circuitName": "Sakhir"}},
        {"raceName": "Saudi Arabian GP", "date": "2026-03-08", "Circuit": {"circuitName": "Jeddah"}},
        {"raceName": "Australian Grand Prix", "date": "2026-03-22", "Circuit": {"circuitName": "Albert Park"}},
        {"raceName": "Japanese Grand Prix", "date": "2026-04-05", "Circuit": {"circuitName": "Suzuka"}},
        {"raceName": "Chinese Grand Prix", "date": "2026-04-19", "Circuit": {"circuitName": "Shanghai"}},
        {"raceName": "Miami Grand Prix", "date": "2026-05-03", "Circuit": {"circuitName": "Miami"}},
        {"raceName": "Emilia Romagna GP", "date": "2026-05-17", "Circuit": {"circuitName": "Imola"}},
        {"raceName": "Monaco Grand Prix", "date": "2026-05-24", "Circuit": {"circuitName": "Monte Carlo"}},
        {"raceName": "Spanish Grand Prix", "date": "2026-06-07", "Circuit": {"circuitName": "Barcelona"}},
        {"raceName": "Canadian Grand Prix", "date": "2026-06-21", "Circuit": {"circuitName": "Montreal"}},
        {"raceName": "Austrian Grand Prix", "date": "2026-07-05", "Circuit": {"circuitName": "Red Bull Ring"}},
        {"raceName": "British Grand Prix", "date": "2026-07-12", "Circuit": {"circuitName": "Silverstone"}},
        {"raceName": "Belgian Grand Prix", "date": "2026-07-26", "Circuit": {"circuitName": "Spa"}},
        {"raceName": "Hungarian Grand Prix", "date": "2026-08-02", "Circuit": {"circuitName": "Hungaroring"}},
        {"raceName": "Dutch Grand Prix", "date": "2026-08-30", "Circuit": {"circuitName": "Zandvoort"}},
        {"raceName": "Italian Grand Prix", "date": "2026-09-06", "Circuit": {"circuitName": "Monza"}}
    ]

    drivers = [
        {"position": "1", "points": "0", "Driver": {"familyName": "Verstappen", "givenName": "Max"}, "Constructors": [{"name": "Red Bull"}]},
        {"position": "2", "points": "0", "Driver": {"familyName": "Hamilton", "givenName": "Lewis"}, "Constructors": [{"name": "Ferrari"}]},
        {"position": "3", "points": "0", "Driver": {"familyName": "Leclerc", "givenName": "Charles"}, "Constructors": [{"name": "Ferrari"}]}
    ]

    return render_template('index.html', races=races, drivers=drivers, next_race=next_race_date)

if __name__ == '__main__':
    app.run()
