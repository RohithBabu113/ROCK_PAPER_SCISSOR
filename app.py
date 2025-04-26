from flask import Flask, render_template, request
import random

app = Flask(__name__)

options = {
    'ROCK': 1,
    'PAPER': 2,
    'SCISSOR': 3
}

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    user_choice = ""
    computer_choice = ""
    
    if request.method == "POST":
        user_choice = request.form['choice']
        user_value = options[user_choice]
        computer_choice = random.choice(list(options.keys()))
        computer_value = options[computer_choice]

        # Determine winner
        if user_value == computer_value:
            result = " It's a Draw!"
        elif (user_value, computer_value) in [(1, 3), (2, 1), (3, 2)]:
            result = "🥳 You Win!"
        else:
            result = "🤖 Computer Wins!"

    return render_template("index.html", result=result,
                           user_choice=user_choice,
                           computer_choice=computer_choice)

if __name__ == "__main__":
    app.run(debug=True,port=5000)
