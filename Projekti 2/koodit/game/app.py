from flask import Flask, render_template, request, redirect
from database import db
from states import intro

app = Flask(__name__)


@app.route("/game", methods=["GET", "POST"])
def game():
    state = int(request.values.get("state", 0))
    answer = request.values.get("answer")

    result = intro(state, answer)

    if "redirect" in result:
        return redirect(result["redirect"])

    return render_template(
        "scene.html",
        text=result["text"],
        choices=result["choices"],
        next_state=result["next_state"],
        input_type=result.get("input_type")
    )

if __name__ == "__main__":
    app.run(debug=True)
    
@app.route("/story/sweden", methods=["GET", "POST"])
def story_sweden():
    from states_sweden import sweden_story

    state = request.values.get("state", "0")
    answer = request.values.get("answer")

    try:
        state = int(state)
    except:
        pass

    result = sweden_story(state, answer)

    return render_template(
        "scene.html",
        text=result["text"],
        choices=result["choices"],
        next_state=result["next_state"]
    )

@app.route("/choose_country", methods=["GET", "POST"])
def choose_country():
    if request.method == "POST":
        country = request.form.get("country", "").upper()

        allowed = ["US", "DE", "SE", "CN", "AU"]
        if country not in allowed:
            return "Invalid country", 400

        airport = get_random_large_airport(country)

        if not airport:
            return f"No large airports found in {country}."

        # Säilöö sessionissa
        session["country"] = country
        session["airport_name"] = airport[0]
        session["airport_country"] = airport[1]

        return redirect("/story/start")

    return render_template("choose_country.html")

@app.route("/story/start")
def story_start():
    name = session.get("player_name", "Traveler")
    airport = session.get("airport_name")
    country = session.get("airport_country")

    if not airport:
        return redirect("/choose_country")

    return render_template(
        "scene.html",
        text=[
            f"Welcome {name}!",
            f"You are flying to: {airport} ({country})"
        ],
        choices=["Continue"],
        next_state="/story/sweden" if country == "SE" else "/story/not_ready"
    )
