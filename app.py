from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

def predict_emotion(text):
    return model.predict([text])[0]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text_input = request.form['textInput']
    prediction = predict_emotion(text_input)  # Call your prediction function
    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
