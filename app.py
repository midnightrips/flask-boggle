from boggle import Boggle
from flask import Flask, render_template, redirect, request, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'
app.debug = True
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

boggle_game = Boggle()

@app.route('/')
def show_board():
    board = boggle_game.make_board()
    session['BOARD'] = board
    return render_template('board.html', board=board)


@app.route('/guess', methods=['POST'])
def valid_word():
    guess = request.form.get('guess')
    board = session['BOARD']

    # if guess in boggle_game.words:
    result = boggle_game.check_valid_word(board, guess)
    info = {"result": result}
    JSON =  jsonify(info)

    return redirect('/', JSON=JSON)
