from flask import Flask, render_template, request
import random

app = Flask(__name__)

coffee_data = {
    "happy": [
        {"name": "Vanilla Latte", "recipe": "Espresso + steamed milk + vanilla syrup"},
        {"name": "Caramel Cappuccino", "recipe": "Espresso + milk foam + caramel drizzle"}
    ],
    "tired": [
        {"name": "Double Espresso", "recipe": "Two strong espresso shots"},
        {"name": "Black Coffee", "recipe": "Hot brewed coffee, no sugar"}
    ],
    "stressed": [
        {"name": "Honey Latte", "recipe": "Espresso + milk + honey"},
        {"name": "Chamomile Coffee", "recipe": "Light coffee + chamomile infusion"}
    ],
    "lazy": [
        {"name": "Cold Brew", "recipe": "Coffee soaked overnight, served chilled"},
        {"name": "Iced Latte", "recipe": "Espresso + cold milk + ice"}
    ],
    "adventurous": [
        {"name": "Mocha", "recipe": "Espresso + chocolate + milk"},
        {"name": "Spiced Coffee", "recipe": "Coffee + cinnamon + nutmeg"}
    ]
}

all_coffee = [item for sublist in coffee_data.values() for item in sublist]

@app.route("/", methods=["GET", "POST"])
def home():
    coffee = None

    if request.method == "POST":
        mood = request.form.get("mood")
        surprise = request.form.get("surprise")

        if surprise:
            coffee = random.choice(all_coffee)
        elif mood:
            coffee = random.choice(coffee_data.get(mood))

    return render_template("index.html", coffee=coffee)

if __name__ == "__main__":
    app.run(debug=True)