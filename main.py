from flask import Flask, render_template
from playSound import play # custom lib

app = Flask(__name__)

states = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka",
    "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram",
    "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana",
    "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands",
    "Chandigarh", "Dadra and Nagar Haveli and Daman and Diu", "Lakshadweep", "Delhi", "Puducherry"
]

@app.route('/')
def index():
    return render_template('index.html', states=states)

@app.route('/play_sound/<state>')
def play_sound(state):
    play(state)
    return "Sound played for {}".format(state)

if __name__ == '__main__':
    app.run(debug=True)
