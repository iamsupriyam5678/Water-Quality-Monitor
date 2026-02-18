from flask import Flask, render_template, request

app = Flask(__name__)

# Store all submitted values here
saved_results = []


def check_water_quality(ph, turbidity, temp):
    if 6.5 <= ph <= 8.5 and turbidity <= 5 and 0 <= temp <= 35:
        return "Water Quality is GOOD"
    else:
        return "Water Quality is BAD"


@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        ph = float(request.form["ph"])
        turbidity = float(request.form["turbidity"])
        temp = float(request.form["temp"])


        result = check_water_quality(ph, turbidity, temp)

        # Save record
        saved_results.append({"ph": ph,
            "turbidity": turbidity,
            "temp": temp,
            "result": result
        })

    return render_template("index.html", result=result)


# New page to show all saved results
@app.route("/results")
def results():
    return render_template("results.html", data=saved_results)


if __name__ == "__main__":
    app.run(debug=True)
