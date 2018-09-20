import random
from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()

code = []
colors = ["BLUE", "GREEN", "PINK", "RED", "VIOLET", "YELLOW"]
history = []
tries = 0


def get_feedback(guess, code):
    feedback = {"black": 0, "white": 0}
    feedback["black"] = sum(a == b for a, b in zip(guess, code))
    feedback["white"] = sum(min(guess.count(color), code.count(color)) for color in colors) - feedback['black']
    return feedback

def finish_game():
    global code, history, tries
    code, history = [], []
    tries = 0

class Game(Resource):
    def get(self):
        global code, tries
        code = random.sample(colors, 4)
        history = []
        tries = 0
        return {"colors": colors}, 201

class Guess(Resource):
    def put(self):
        global history, tries
        if not code:
            return "There's no game being played currently", 400
        guess = request.get_json(force=True)
        if len(guess) is 4:
            feedback = get_feedback(guess, code)
            history.append([str(guess), str(feedback)])
            tries += 1
            if feedback["black"] is 4:
                finish_game()
                return "Won game!"
            if tries is 8:
                finish_game()
                return "All guesses were wrong! The codemaker won!"
            return {"Black key pegs": feedback['black'], "White key pegs": feedback['white']}
        else:
            return "Bad number of colors! (4 colors should be introduced)", 400

class History(Resource):
    def get(self):
        return {"history": history}


api.add_resource(Game, "/new_game")
api.add_resource(History, "/history")
api.add_resource(Guess, "/new_guess")

if __name__ == '__main__':
    app.run(debug=True)
