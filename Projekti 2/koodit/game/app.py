from flask import Flask, render_template, request, redirect, session
from database import db
from states import intro

app = Flask(__name__)
app.secret_key = "super_secret_key"   # session avain


@app.route("/game", methods=["GET", "POST"])
def game():
    state = int(request.values.get("state", 0))
    answer = request.values.get("answer")
    carry = request.values.get("carry")

    result = intro(state, answer, carry)

    # siirtää valittuun maahan
    if "redirect" in result:
        return redirect(result["redirect"])

    return render_template(
        "scene.html",
        text=result["text"],
        choices=result["choices"],
        next_state=result["next_state"],
        input_type=result.get("input_type"),
        line=result.get("ascii", ""),
        next_url="/game",
        carry=result.get("carry", "")
    )


@app.route("/story/sweden", methods=["GET", "POST"])
def story_sweden():
    from states_sweden import sweden_story

    state = int(request.values.get("state", 0))
    answer = request.values.get("answer")

    result = sweden_story(state, answer)

    return render_template(
        "scene.html",
        text=result["text"],
        choices=result["choices"],
        input_type=result.get("input_type", ""),
        line=result.get("ascii", ""),
        next_state=result["next_state"],
        next_url="/story/sweden",
        carry=""
    )


if __name__ == "__main__":
    app.run(debug=True)
