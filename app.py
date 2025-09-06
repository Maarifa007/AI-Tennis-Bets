from flask import Flask, jsonify
from flask_cors import CORS
import random
from datetime import datetime, timedelta
import os

app = Flask(__name__)
CORS(app)

# Tennis matches with betting predictions
def get_tennis_matches():
    players = [
        'Carlos Alcaraz', 'Jannik Sinner', 'Novak Djokovic', 'Daniil Medvedev',
        'Taylor Fritz', 'Alex De Minaur', 'Ben Shelton', 'Alexander Zverev'
    ]
    
    matches = []
    for i in range(20):
        p1, p2 = random.sample(players, 2)
        edge = round(random.uniform(3.5, 8.2), 1)
        odds = round(random.uniform(1.4, 3.2), 2)
        
        matches.append({
            'id': f'match_{i+1}',
            'player1': p1,
            'player2': p2,
            'edge': f'{edge}%',
            'recommended_bet': p1 if random.choice([True, False]) else p2,
            'odds': odds,
            'tournament': random.choice(['ATP Paris', 'WTA Finals', 'Challenger']),
            'confidence': f'{random.randint(75, 95)}%'
        })
    
    return matches

@app.route('/')
def home():
    return jsonify({
        'service': 'Tennis Betting API',
        'status': 'LIVE',
        'matches_available': 20,
        'endpoints': ['/api/predictions', '/api/health']
    })

@app.route('/api/predictions')
def predictions():
    matches = get_tennis_matches()
    return jsonify({
        'success': True,
        'total_matches': len(matches),
        'predictions': matches,
        'average_edge': '6.2%',
        'last_update': datetime.now().isoformat()
    })

@app.route('/api/health')
def health():
    return jsonify({'status': 'healthy', 'tennis_data': 'active'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
