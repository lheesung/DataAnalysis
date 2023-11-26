import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template, send_file, request
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)

# 데이터 로드
temp_data = pd.read_csv('./data/Annual_Surface_Temperature_Change.csv').fillna(0)
co2_data = pd.read_csv('./data/World_Atmospheric_CO2.csv').fillna(0)
sea_level_data = pd.read_csv('./data/Change_in_Mean_Sea_Levels.csv').fillna(0)

def create_plot(data, x_column, y_column, title):
    plt.figure(figsize=(10, 5))
    plt.plot(data[x_column], data[y_column])
    plt.title(title)
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.grid(True)
    plt.savefig('static/plot.png', format='png')
    plt.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
    indicator = request.args.get('indicator')
    if indicator == 'temperature':
        create_plot(temp_data, 'Date', 'Value', 'Annual Surface Temperature Change')
    elif indicator == 'co2':
        create_plot(co2_data, 'Date', 'Value', 'World Atmospheric CO2')
    elif indicator == 'sea_level':
        create_plot(sea_level_data, 'Date', 'Value', 'Change in Mean Sea Levels')
    else:
        return "Invalid indicator", 400

    return send_file('./static/plot.png', mimetype='image/png')

if __name__ == '__main__':
    app.run()
