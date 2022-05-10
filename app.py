import flask
from flask import request, jsonify
import pandas as pd
from datetime import datetime as dt
from flask_cors import CORS, cross_origin
import openpyxl

app = flask.Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    fecha = request.args['fecha']
    year = fecha[:4]
    mes = fecha[5:7]
    dia = fecha[8:10]

    if mes[:1] == '0':
        m = mes[1:2]
        mes = m
        print('0 deleted mes', m)

    if dia[:1] == '0':
        d = dia[1:2]
        dia = d
        print('0 deleted dia', d)    

    
    if mes == '1':
        mes = 'A'
    elif mes == '2':
        mes = 'B'
    elif mes == '3':
        mes = 'C'
    elif mes == '4':
        mes = 'D'        
    elif mes == '5':
        mes = 'E'
    elif mes == '6':
        mes = 'F'
    elif mes == '7':
        mes = 'G'
    elif mes == '8':
        mes = 'H'
    elif mes == '9':
        mes = 'I'
    elif mes == '10':
        mes = 'J'
    elif mes == '11':
        mes = 'K' 
    else:
        mes = 'L'    
    d = int(dia) - 1

    print(year, mes, dia)
    path= f'{year}.xlsx'
    #leemos el excel usando pandas
    valor = pd.read_excel(path, usecols= mes, header= d, nrows=0, index_col=None)
    data = valor.columns.values[0]
   
    return jsonify({"respuesta":data})

# if __name__ == '__app__':
# app.run( debug=True, port=7774)