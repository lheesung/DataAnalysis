from flask import Flask, jsonify, request
import pandas as pd
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

temp_data = pd.read_csv('data/Annual_Surface_Temperature_Change.csv')
co2_data = pd.read_csv('data/World_Atmospheric_CO2.csv')
sea_level_data = pd.read_csv('data/Change_in_Mean_Sea_Levels.csv')

@app.route('/data', methods=['GET'])
@cross_origin()

def get_data():
    country = request.args.get('country')
    indicator = request.args.get('indicator')
    if indicator == 'temperature':
        data = temp_data[temp_data['Country'] == country]
    elif indicator == 'co2':
        data = co2_data[co2_data['Country'] == country]
    elif indicator == 'sea_level':
        data = sea_level_data[sea_level_data['Country'] == country]
    else:
        return jsonify({'error': 'Invalid indicator'}), 400

    return jsonify(data.to_dict(orient='records'))

if __name__ == '__main__':
    app.run()
