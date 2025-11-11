from flask import Flask, render_template_string
import secrets

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Secure Dice Roller</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 50px;
            background-color: #f0f0f0;
        }
        .container {
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            display: inline-block;
            min-width: 600px;
            margin: 0 auto;
        }
        button {
            padding: 15px 30px;
            font-size: 18px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            margin: 20px 0;
        }
        button:hover {
            background-color: #45a049;
        }
        #result {
            margin-top: 20px;
            font-size: 24px;
            color: #333;
        }
        .dice-container {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 20px;
            margin: 30px 0;
            flex-wrap: nowrap;
        }
        .dice {
            width: 100px;
            height: 100px;
            background-color: #f8f8f8;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }
        .dice-emoji {
            font-size: 36px;
            margin-bottom: 0px; /* Reduced spacing */
            line-height: 1;
        }
        .dice-value {
            font-size: 36px;
            font-weight: bold;
            line-height: 1;
        }
        .total-container {
            font-size: 36px;
            font-weight: bold;
            color: #2196F3;
            min-width: 120px;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100px;
        }
        .operator {
            font-size: 36px;
            color: #777;
            font-weight: bold;
        }
        h1 {
            margin-top: 0;
            margin-bottom: 20px;
        }
        .summary {
            font-size: 20px;
            margin-top: 20px;
            padding: 15px;
            background-color: #f8f9fa;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🔒 Secure Dice Roller</h1>
        <form method="POST" action="/roll">
            <button type="submit">Roll Two Dice</button>
        </form>
        <div id="result">
            {% if dice1 and dice2 %}
                <div class="dice-container">
                    <div class="dice">
                        <div class="dice-emoji">🎲</div>
                        <div class="dice-value">{{ dice1 }}</div>
                    </div>
                    <div class="operator">+</div>
                    <div class="dice">
                        <div class="dice-emoji">🎲</div>
                        <div class="dice-value">{{ dice2 }}</div>
                    </div>
                    <div class="operator">=</div>
                    <div class="total-container">{{ total }}</div>
                </div>
                <div class="summary">
                    Individual rolls: {{ dice1 }} and {{ dice2 }} | Total: <strong>{{ total }}</strong>
                </div>
            {% else %}
                <p>Click the button to roll two dice!</p>
            {% endif %}
        </div>
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/roll', methods=['POST'])
def roll_dice():
    # Cryptographically secure random number
    dice_roll_1 = secrets.randbelow(6) + 1  # Returns 1-6
    dice_roll_2 = secrets.randbelow(6) + 1  # Returns 1-6
    total_roll = dice_roll_1 + dice_roll_2
    return render_template_string(HTML_TEMPLATE, total=total_roll, dice1=dice_roll_1, dice2=dice_roll_2)

if __name__ == '__main__':
    # Enable SSL with ad-hoc certificates, edit when actual production begins
    app.run(host='0.0.0.0', port=443, ssl_context='adhoc', debug=True)