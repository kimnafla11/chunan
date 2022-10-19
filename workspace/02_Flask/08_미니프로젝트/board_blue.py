from flask import Blueprint, render_template, request

boardBlue = Blueprint('board_blue',__name__)

@boardBlue.route('/board_main')
def board_main() :
    html = render_template('board/board_main.html')
    return html
