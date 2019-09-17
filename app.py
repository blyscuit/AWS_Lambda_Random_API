import logging
from flask import Flask, jsonify, render_template
import random
import math

app = Flask(__name__)
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

@app.route('/dice', methods=['GET', 'POST'])
def dice(event=None, context=None):
    rr = random.randint(1,6)*1
    return jsonify({'result': rr})

@app.route('/coin', methods=['GET', 'POST'])
def coin(event=None, context=None):
    rr = random.randint(1,2)*1
    return jsonify({'result': rr})

@app.route('/card', methods=['GET', 'POST'])
def card(event=None, context=None):
    rr = random.randint(0,51)*1
    cc = (rr%13) + 1
    suit = math.floor(rr/13)
    rank = "K" if cc == 13 else "Q" if cc == 12 else "J" if cc == 11 else str(cc)
    suits = ["Spade", "Heart", "Diamond", "Clover"]
    return jsonify({'result': {"letter":rank, "rank": cc, "suit": suits[suit]}})

@app.route('/', methods=['GET', 'POST'])
def aaaa(event=None, context=None):
    logger.info('Lambda function invoked index()')

    
    return render_template('index.html', message="message")

if __name__ == '__main__':
    app.run(debug=True)
