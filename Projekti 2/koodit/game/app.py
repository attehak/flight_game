from flask import Flask, render_template, request, redirect, session
from database import db
from states import intro
from states_australia import australia_story
from states_china import china_story
from states_usa import usa_story
from states_sweden import sweden_story

THE_END_ART = r"""
████████╗██╗  ██╗███████╗     ███████╗███╗   ██╗██████╗ 
╚══██╔══╝██║  ██║██╔════╝     ██╔════╝████╗  ██║██╔══██╗
   ██║   ███████║█████╗       █████╗  ██╔██╗ ██║██║  ██║
   ██║   ██╔══██║██╔══╝       ██╔══╝  ██║╚██╗██║██║  ██║
   ██║   ██║  ██║███████╗     ███████╗██║ ╚████║██████╔╝
   ╚═╝   ╚═╝  ╚═╝╚══════╝     ╚══════╝╚═╝  ╚═══╝╚═════╝ 
Prototype by: Aleksi, Atte, Eetu, Juuso ja Nipa
"""

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


@app.route("/story/australia", methods=["GET", "POST"])
def story_australia_route():
    state = int(request.values.get("state", 0))
    answer = request.values.get("answer")
    carry = request.values.get("carry", "")

    print("STATE:", state, "ANSWER:", repr(answer))

    result = australia_story(state, answer, carry)
    print("RESULT:", result)

    if "redirect" in result:
        return redirect(result["redirect"])

    return render_template(
        "scene.html",
        text=result["text"],
        choices=result["choices"],
        input_type=result.get("input_type", ""),
        line=result.get("ascii", ""),
        next_state=result["next_state"],
        next_url="/story/australia",
        carry=result.get("carry", "")
    )

@app.route("/story/china", methods=["GET", "POST"])
def story_china_route():
    state = int(request.values.get("state", 0))
    answer = request.values.get("answer")
    carry = request.values.get("carry", "")

    print("STATE:", state, "ANSWER:", repr(answer))

    result = china_story(state, answer, carry)
    print("RESULT:", result)

    if "redirect" in result:
        return redirect(result["redirect"])

    return render_template(
        "scene.html",
        text=result["text"],
        choices=result["choices"],
        input_type=result.get("input_type", ""),
        line=result.get("ascii", ""),
        next_state=result["next_state"],
        next_url="/story/china",
        carry=result.get("carry", "")
    )

@app.route("/story/usa", methods=["GET", "POST"])
def story_usa_route():
    state = int(request.values.get("state", 0))
    answer = request.values.get("answer")
    carry = request.values.get("carry", "")

    print("STATE:", state, "ANSWER:", repr(answer))

    result = usa_story(state, answer, carry)
    print("RESULT:", result)

    if "redirect" in result:
        return redirect(result["redirect"])

    return render_template(
        "scene.html",
        text=result["text"],
        choices=result["choices"],
        input_type=result.get("input_type", ""),
        line=result.get("ascii", ""),
        next_state=result["next_state"],
        next_url="/story/usa",
        carry=result.get("carry", "")
    )

@app.route("/story/germany", methods=["GET", "POST"])
def story_germany_route():
    from states_germany import germany_story

    state = int(request.values.get("state", 0))
    answer = request.values.get("answer")
    carry = request.values.get("carry", "")

    print("STATE:", state, "ANSWER:", repr(answer))

    result = germany_story(state, answer, carry)
    print("RESULT:", result)

    if "redirect" in result:
        return redirect(result["redirect"])

    return render_template(
        "scene.html",
        text=result["text"],
        choices=result["choices"],
        input_type=result.get("input_type", ""),
        line=result.get("ascii", ""),
        next_state=result["next_state"],
        next_url="/story/germany",
        carry=result.get("carry", "")
    )

@app.route("/story/sweden", methods=["GET", "POST"])
def story_sweden_route():
    state = int(request.values.get("state", 0))
    answer = request.values.get("answer")
    carry = request.values.get("carry", "")

    print("STATE:", state, "ANSWER:", repr(answer))

    result = sweden_story(state, answer, carry)
    print("RESULT:", result)

    if "redirect" in result:
        return redirect(result["redirect"])

    return render_template(
        "scene.html",
        text=result["text"],
        choices=result["choices"],
        input_type=result.get("input_type", ""),
        line=result.get("ascii", ""),
        next_state=result["next_state"],
        next_url="/story/sweden",
        carry=result.get("carry", "")
    )

print(app.url_map)

if __name__ == "__main__":
    app.run(debug=True)
