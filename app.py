from flask import Flask, render_template, request
from model import predict_car_value

app = Flask(__name__)
@app.route('/')
@app.route('/index.html')
def home():
    return render_template('index.html')
@app.route('/about.html')
def about():
    return render_template('about.html')

# Example prediction route (optional)
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Example: collect form data
        car_data = {
            'make': request.form['make'],
            'model': request.form['model'],
            'year': int(request.form['year']),
            'mileage': float(request.form['mileage'])
        }
        predicted_price = predict_car_value(car_data)
        return render_template('index.html', prediction=predicted_price)

if __name__ == '__main__':
    app.run(debug=True)
