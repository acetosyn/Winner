from flask import Flask, request
import name_test

app = Flask(__name__)

@app.route("/")
def get_name():
    num_str = request.args.get("num")
    if not num_str:
        return 'Please add a number to the URL, like /?num=5'
    
    num = int(num_str)
    winner = name_test.pick_at_random(num)
    return f'The name of the winner is "{winner.upper()}"'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
