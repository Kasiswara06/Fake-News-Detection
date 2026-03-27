from flask import Flask, render_template, request

app = Flask(__name__)

# Expanded fake keywords list
fake_keywords = [
    # Sensational words
    "breaking", "shocking", "unbelievable", "exclusive", "urgent",
    "alert", "must read", "viral", "trending", "sensational",

    # Rumor / misinformation
    "rumor", "fake", "hoax", "false claim", "misleading",
    "conspiracy", "exposed", "hidden truth", "leaked", "secret",

    # Emotional manipulation
    "you won't believe", "mind blowing", "what happens next",
    "shocking truth", "can't believe", "watch now", "see what happened",

    # Health scams
    "miracle cure", "instant cure", "100% cure", "no side effects",
    "lose weight fast", "magic pill", "doctor hates this trick",

    # Political misinformation
    "secret plan", "government hiding", "rigged election","death","died"
    "fake vote", "illegal decision", "hidden agenda",

    # Science / extreme claims
    "aliens", "end of world", "time travel", "parallel universe",
    "earth will go dark", "unknown energy", "mysterious object",

    # Social media style
    "forwarded message", "whatsapp forward", "share immediately",
    "spread this", "don’t ignore", "everyone must know",

    # Scam patterns
    "click here", "limited offer", "free money", "win cash now",
    "guaranteed income", "earn money fast"
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    news = request.form['news'].lower()

    # Count keyword matches
    score = sum(1 for word in fake_keywords if word in news)

    # Decision based on score
    if score >= 2:
        prediction = f"⚠️ Fake News (score: {score})"
        color = "red"
    else:
        prediction = f"✅ Real News (score: {score})"
        color = "green"

    return render_template('index.html',
                           prediction_text=prediction,
                           color=color)

if __name__ == "__main__":
    app.run(debug=True)