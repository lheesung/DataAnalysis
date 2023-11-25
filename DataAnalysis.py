import pandas as pd
from flask import Flask, render_template, jsonify

# 데이터 로드
climate_data = pd.read_csv('./data/Annual_Surface_Temperature_Change.csv')

# 불필요한 열 제거
columns_to_drop = ['ObjectId', 'ISO2', 'ISO3', 'CTS_Code', 'Source', 'CTS_Name', 'CTS_Full_Descriptor']
data = climate_data.drop(columns=columns_to_drop)
