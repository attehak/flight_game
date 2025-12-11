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
    
    if state == 0:
        session.clear()  # puhdas alku jos restart

    result = intro(state, answer, carry)

    if "redirect" in result:
        return redirect(result["redirect"])

    return render_template(
        "scene.html",
        text=result["text"],
        choices=result.get("choices", []),
        next_state=result["next_state"],
        option_texts=result.get("option_texts", []),
        input_type=result.get("input_type"),
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
        choices=result.get("choices", []),
        option_texts=result.get("option_texts", []),
        input_type=result.get("input_type", ""),
        line=result.get("ascii", ""),
        next_state=result["next_state"],
        next_url="/story/sweden",
        carry=""
    )



if __name__ == "__main__":
    app.run(debug=True)
