from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result')
def result():
    df = pd.read_csv('clustered_data.csv', index_col=0)
    return render_template('result.html', data=df)

if __name__ == '__main__':
    app.run(debug=True)
