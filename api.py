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
    return feedback


class Game(Resource):
    def get(self):
        global code, tries
        code = random.sample(colors, 4)
        return {"colors": colors}, 201

class Guess(Resource):
    def put(self):
        global history, tries
        guess = request.get_json(force=True)
        if len(guess) is 4:
            feedback = get_feedback(guess, code)
            history.append([str(guess), str(feedback)])
            tries += 1
            if feedback["black"] is 4:
                # restart everything
                return {"Won game!"}
            if tries is 8:
                # restart everything
                return {"All guesses were wrong! The codemaker won!"}
            return {"Black key pegs": feedback['black'], "White key pegs": feedback['white']}
        else:
            return {"Bad number of colors! (4 colors should be introduced)"}, 400


api.add_resource(Game, "/new_game")
api.add_resource(Guess, "/new_guess")
