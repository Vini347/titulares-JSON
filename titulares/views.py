from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import psycopg2 as pg
from .validators import *
from .DefInserts import *
from django.conf import settings

@csrf_exempt
def retorno_json(request):

    listErrors=[]
    data = request.body.decode('utf-8')
    json_data = json.loads(data)

    connection = pg.connect(
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        database=settings.DB_NAME
    )
    cursor = connection.cursor()

    for Titular in json_data:
        response, dicError = Validator(Titular)
        if response:
            insertTitular(Titular['Titular'])
            
            cursor.execute(f"SELECT titularid FROM titular WHERE titularchavepesquisa = '{Titular['Titular']['TitularChavePesquisa']}'")
            IdTitular = cursor.fetchall()[0][0]
            insertOutros(Titular['OutrosDados'], IdTitular)
            insertDocumento(Titular['Documentos'],  IdTitular)
            insertEndereco(Titular['TitularEndereco'], IdTitular)
            insertTelefone(Titular['Telefone'], IdTitular)
            insertEmail(Titular['Email'], IdTitular)
            insertDadosTitulares(Titular['Termos'], IdTitular)

        else:
            listErrors.append(dicError)
    
    print(listErrors)


    connection.close()
    cursor.close()

    if len(listErrors) == 0:
        return HttpResponse("Nenhum erro encontrado")
    
    return JsonResponse(listErrors, safe=False)