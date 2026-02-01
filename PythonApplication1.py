from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    next_race_date = "2026-03-01T15:00:00"

    # Повний розклад на 16 етапів з посиланнями на квитки
    races = [
        {"raceName": "Bahrain Grand Prix", "date": "2026-03-01", "Circuit": {"circuitName": "Sakhir"}, "tickets": "https://tickets.formula1.com"},
        {"raceName": "Saudi Arabian GP", "date": "2026-03-08", "Circuit": {"circuitName": "Jeddah"}, "tickets": "https://tickets.formula1.com"},
        {"raceName": "Australian Grand Prix", "date": "2026-03-22", "Circuit": {"circuitName": "Albert Park"}, "tickets": "https://tickets.formula1.com"},
        {"raceName": "Japanese Grand Prix", "date": "2026-04-05", "Circuit": {"circuitName": "Suzuka"}, "tickets": "https://tickets.formula1.com"},
        {"raceName": "Chinese Grand Prix", "date": "2026-04-19", "Circuit": {"circuitName": "Shanghai"}, "tickets": "https://tickets.formula1.com"},
        {"raceName": "Miami Grand Prix", "date": "2026-05-03", "Circuit": {"circuitName": "Miami"}, "tickets": "https://tickets.formula1.com"},
        {"raceName": "Emilia Romagna GP", "date": "2026-05-17", "Circuit": {"circuitName": "Imola"}, "tickets": "https://tickets.formula1.com"},
        {"raceName": "Monaco Grand Prix", "date": "2026-05-24", "Circuit": {"circuitName": "Monte Carlo"}, "tickets": "https://tickets.formula1.com"},
        {"raceName": "Spanish Grand Prix", "date": "2026-06-07", "Circuit": {"circuitName": "Barcelona"}, "tickets": "https://tickets.formula1.com"},
        {"raceName": "Canadian Grand Prix", "date": "2026-06-21", "Circuit": {"circuitName": "Montreal"}, "tickets": "https://tickets.formula1.com"},
        {"raceName": "Austrian Grand Prix", "date": "2026-07-05", "Circuit": {"circuitName": "Red Bull Ring"}, "tickets": "https://tickets.formula1.com"},
        {"raceName": "British Grand Prix", "date": "2026-07-12", "Circuit": {"circuitName": "Silverstone"}, "tickets": "https://tickets.formula1.com"},
        {"raceName": "Belgian Grand Prix", "date": "2026-07-26", "Circuit": {"circuitName": "Spa"}, "tickets": "https://tickets.formula1.com"},
        {"raceName": "Hungarian Grand Prix", "date": "2026-08-02", "Circuit": {"circuitName": "Hungaroring"}, "tickets": "https://tickets.formula1.com"},
        {"raceName": "Dutch Grand Prix", "date": "2026-08-30", "Circuit": {"circuitName": "Zandvoort"}, "tickets": "https://tickets.formula1.com"},
        {"raceName": "Italian Grand Prix", "date": "2026-09-06", "Circuit": {"circuitName": "Monza"}, "tickets": "https://tickets.formula1.com"}
    ]

    # Залік пілотів (Standings)
    drivers = [
        {"position": "1", "points": "0", "Driver": {"familyName": "Verstappen", "givenName": "Max"}, "Constructors": [{"name": "Red Bull"}]},
        {"position": "2", "points": "0", "Driver": {"familyName": "Hamilton", "givenName": "Lewis"}, "Constructors": [{"name": "Ferrari"}]},
        {"position": "3", "points": "0", "Driver": {"familyName": "Leclerc", "givenName": "Charles"}, "Constructors": [{"name": "Ferrari"}]}
    ]

    return render_template('index.html', races=races, drivers=drivers, next_race=next_race_date)

if __name__ == '__main__':
    app.run()
