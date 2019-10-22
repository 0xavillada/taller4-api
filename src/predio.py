from flask import Flask, request, render_template
from flask_cors import CORS
from datetime import datetime
import json
from conection import db_find,db_save

app = Flask(__name__, template_folder='../templates/')
#CORS(app)

predios_list = [{ 'codigo':'1234', 'latitud': 123453.75 , 'terreno':'Desértico', 'longitud': 123453.75, 'area': 23.32 }]

terrenos_list = ['Planicie', 'Ladera', 'Cenagoso', 'Desértico']

@app.route('/createPredio/', methods=['GET'])
def addPredio():
    return render_template('createPredio.html', terrenos= terrenos_list)

@app.route('/listPredio/', methods=['GET'])
def listPredio():
    find_response = find_predios()
    predios_list.clear()
    for x in find_response:
        predios_list.append(x)
    return render_template('listPredio.html', predios= predios_list)

@app.route('/addPredio', methods=['POST'])
def pushOne():
    vals = request.values
    #print(request.values)
    #print(vals)
    #predios_list.append(v)
    if float(vals['area']) > 0:
        #---------------------------------------------------------------------
        data = {'codigo':vals['codigo'],'latitud':vals['latitud'], 'terreno':vals['terreno'],'longitud':vals['longitud'],'area':vals['area'], 'imagen':vals['imagen']}
        db_save("predios", data)
        #---------------------------------------------------------------------
        find_response = find_predios()
        predios_list.clear()
        for x in find_response:
            predios_list.append(x)

        #predios_list.append({'codigo':vals['codigo'],'latitud':vals['latitud'], 'terreno':vals['terreno'],'longitud':vals['longitud'],'area':vals['area']})
        return render_template('listPredio.html', predios= predios_list)
    else:
        return 'El area debe ser un valor positivo!'

def find_predios():
    find_response = db_find("predios")
    return(find_response)

app.run(port=5000, debug=True)