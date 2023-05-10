from flask import Flask, jsonify, request, abort

app = Flask(__name__)

player_data = {
    "Dhoni": [180, 75, 123, 85, 90],
    "Sachin": [385, 100, 89, 24, 99]
}


app = Flask(__name__)

API_KEYS = {
    'wannahack': 'My_Secret_Key',
}

@app.before_request
def check_api_key():
    api_key = request.args.get('api_key')
    if api_key not in API_KEYS:
        abort(401, 'Invalid API key')
        
# API endpoint
@app.route('/v1/get_player_average/', methods=['GET'])

def get_player_average():
    response_data = {}
    for player, scores in player_data.items():
        avg_score = sum(scores[-5:]) / 5  # Calculating average of last 5 scores
        response_data[player] = avg_score
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True,port=int("8000"))
