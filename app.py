from boggle import Boggle
from flask import Flask, render_template, redirect, request, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = '12345'
app.debug = True
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

boggle_game = Boggle()

@app.route('/')
def show_board():
    """Creates and shows boggle board"""

    board = boggle_game.make_board()
    session['BOARD'] = board
    return render_template('board.html', board=board)


@app.route('/guess')
def valid_word(): #checks if word exists and returns JSON
    """Checks if word exists and returns JSON"""

    guess = request.args['guess']
    board = session['BOARD']
    print(guess)

    result = boggle_game.check_valid_word(board, guess)

    return jsonify({'result': result})
