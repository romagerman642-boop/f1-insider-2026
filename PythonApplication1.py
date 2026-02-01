from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    next_race_date = "2026-03-01T15:00:00" # Час і дата першої гонки 2026

    # Дані про гонки (можеш додати більше, якщо хочеш)
    races = [
        {"name": "Bahrain GP", "track": "Sakhir", "date": "1 березня", "status": "Tickets Available"},
        {"name": "Saudi Arabian GP", "track": "Jeddah", "date": "8 березня", "status": "Coming Soon"},
        {"name": "Australian GP", "track": "Albert Park", "date": "22 березня", "status": "Coming Soon"}
    ]

    # Розширені дані про пілотів та команди 2026 з їхніми кольорами
    drivers = [
        {"pos": "1", "name": "Max Verstappen", "team": "Red Bull-Ford", "color": "#0600ef"},
        {"pos": "2", "name": "Lewis Hamilton", "team": "Mercedes", "color": "#00d2be"}, # Змінив на Mercedes, бо 2026-02-01
        {"pos": "3", "name": "Charles Leclerc", "team": "Ferrari", "color": "#ef1a2d"},
        {"pos": "4", "name": "Lando Norris", "team": "McLaren", "color": "#ff8700"},
        {"pos": "5", "name": "George Russell", "team": "Mercedes", "color": "#00d2be"} # Змінив на Mercedes, бо 2026-02-01
    ]

    # Технічні зміни 2026
    tech_rules = [
        {"title": "Двигуни", "desc": "Збільшення електричної потужності до 350 кВт та відмова від MGU-H."},
        {"title": "Паливо", "desc": "Перехід на 100% екологічно чисте синтетичне пальне."},
        {"title": "Аеродинаміка", "desc": "Активне аеро (рухомі крила) для зменшення лобового опору на прямих."}
    ]

    return render_template('index.html', races=races, drivers=drivers, next_race=next_race_date, rules=tech_rules)

if __name__ == '__main__':
    app.run(debug=True)
