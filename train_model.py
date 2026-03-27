from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

# Global model
vectorizer = None
model = None

@app.route('/')
def home():
    return render_template('index.html')


# 🔹 Train model using user input
@app.route('/train', methods=['POST'])
def train():
    global vectorizer, model

    fake_text = request.form['fake_text'].split('\n')
    real_text = request.form['real_text'].split('\n')

    texts = fake_text + real_text
    labels = [0]*len(fake_text) + [1]*len(real_text)

    # Train
    vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1,2))
    X = vectorizer.fit_transform(texts)

    model = LogisticRegression(max_iter=1000)
    model.fit(X, labels)

    return render_template('index.html', message="✅ Model trained successfully!")


# 🔹 Predict
@app.route('/predict', methods=['POST'])
def predict():
    global vectorizer, model

    if model is None:
        return render_template('index.html', prediction_text="⚠️ Train model first!")

    news = request.form['news']
    data = vectorizer.transform([news])
    result = model.predict(data)[0]

    if result == 0:
        prediction = "⚠️ Fake News"
        color = "red"
    else:
        prediction = "✅ Real News"
        color = "green"

    return render_template('index.html',
                           prediction_text=prediction,
                           color=color)


if __name__ == "__main__":
    app.run(debug=True)