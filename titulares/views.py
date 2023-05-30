from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import psycopg2 as pg
import json
from .validators import *
from .definserts import *


@csrf_exempt
def retorno_json(request):
    conn = pg.connect(
        host="localhost",
        port="5432",
        database="Eagle2",
        user="postgres",
        password="SDNA@2022"
    )
    cursor = conn.cursor()
    listErrors = []

    if request.method == 'POST':
        data = request.body.decode('utf-8')
        json_data = json.loads(data)

        for Titular in json_data:
            response, dicError = Validator(Titular)
            if response:
                insertTitular(Titular['Titular'])
                insertDocumento(Titular['Documentos'], Titular['Titular']['TitularChavePesquisa'])
                insertEndereco(Titular['TitularEndereco'], Titular['Titular']['TitularChavePesquisa'])
                insertTelefone(Titular['Telefone'], Titular['Titular']['TitularChavePesquisa'])
                insertEmail(Titular['Email'], Titular['Titular']['TitularChavePesquisa'])
                insertOutros(Titular['OutrosDados'], Titular['Titular']['TitularChavePesquisa'])
                insertTermosIDs(Titular['Termos'])
            else:
                listErrors.append(dicError)

        print(listErrors)
        cursor.close()
        conn.close()

    return JsonResponse(listErrors, safe=False)