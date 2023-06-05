import psycopg2 as pg
from django.conf import settings

def insertTitular(Titular):
    conn = pg.connect(
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        database=settings.DB_NAME
    )
    cursor = conn.cursor()
    nome = Titular['Nome']
    nacionalidade = Titular['Nacionalidade']
    naturalidade = Titular['Naturalidade']
    nomedopai = Titular['NomePai']
    nomedamae = Titular['NomeMae']
    datanasc = Titular['DataNascimento']
    pessoapoliticamenteexposta = Titular['PessoaPoliticamenteExposta']
    menoridade = Titular['MenorIdade']
    responsavellegal = Titular['ResponsavelLegal']
    titularchavepesquisa = Titular['TitularChavePesquisa']

    query = f"""select titularnome from titular where titularnome = '{nome}'"""
    cursor.execute(query)
    resultados = cursor.fetchall()
    encontrado = 0
    for x in resultados:
        encontrado = 1
        break
    if encontrado == 0:
        sql = "INSERT INTO titular(titularnome, titularnacionalidade, titularnaturalidade, titularnomepai, titularnomemae, titulardtnasc, titularpolitexposta, titularmenoridade, titularrespleal, titularchavepesquisa) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (nome, nacionalidade, naturalidade, nomedopai, nomedamae, datanasc, pessoapoliticamenteexposta, menoridade, responsavellegal, titularchavepesquisa))
        conn.commit()
        return ('Titular cadastrado com sucesso')
    
def insertDocumento(Titular, id):
    conn = pg.connect(
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        database=settings.DB_NAME
    )
    
    cursor = conn.cursor()
    tipo_doc = Titular['TipoDoc']
    valor_doc = Titular['ValorDoc']
    validade_doc = Titular['ValidadeDoc']

    query = f"""select titulardocumentoconteudo from titulardocumento where titulardocumentoconteudo = '{valor_doc}'"""
    cursor.execute(query)
    resultados = cursor.fetchall()
    encontrado = 0
    for x in resultados:
        encontrado = 1
        break
    if encontrado == 0:
        
        sql = "INSERT INTO titulardocumento(titulardocumentotipodocumentopessoal, titulardocumentoconteudo, titulardocumentovalidade,titularid) VALUES(%s, %s, %s,%s)"
        cursor.execute(sql, (tipo_doc, valor_doc, validade_doc, id))
        conn.commit()
        return ('Documento cadastrado com sucesso')
    
def insertEndereco(Titular, id):
    conn = pg.connect(
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        database=settings.DB_NAME
    )

    cursor = conn.cursor()
    categoriaend = Titular['Categoria']
    endereco = Titular['Endereco']
    numerolocal = Titular['Numero']
    complemento = Titular['Complemento']
    bairro = Titular['Bairro']
    cep = Titular['CEP']
    cidade = Titular['Cidade']
    unidadefederal = Titular['UF']
    pais = Titular['Pais']

    query = f"""select titularid from titularendereco where titularid = '{id}'"""
    cursor.execute(query)
    resultados = cursor.fetchall()
    encontrado = 0
    for x in resultados:
        encontrado = 1
        break
    if encontrado == 0:

        sql = "INSERT INTO titularendereco(titularenderecocategoriaendereco, titularenderecorua, titularendereconro, titularenderecocomplemento, titularenderecobairro, titularenderecocep, titularenderecocidade, titularenderecouf, titularenderecopais, titularid) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (categoriaend, endereco, numerolocal, complemento, bairro, cep, cidade, unidadefederal, pais, id))
        conn.commit()
        return('Endereço cadastrado com sucesso')

def insertTelefone(Titular, id):
    conn = pg.connect(
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        database=settings.DB_NAME
    )

    cursor = conn.cursor()
    TelDDI = Titular['DDI']
    TelDDD = Titular['DDD']
    TelNro = Titular['Nro']

    query = f"""select titulartelefonenro from titulartelefone where titulartelefonenro = '{TelNro}'"""
    cursor.execute(query)
    resultados = cursor.fetchall()
    encontrado = 0
    for x in resultados:
        encontrado = 1
        break
    if encontrado == 0:

        sql = "INSERT INTO titulartelefone(titulartelefoneinternacional, titulartelefoneDDD, titulartelefonenro, titularid) VALUES(%s, %s, %s, %s)"
        cursor.execute(sql, (TelDDI, TelDDD, TelNro, id))
        conn.commit()
        return('Telefone cadastrado com sucesso')

def insertEmail(Titular, id):
    conn = pg.connect(
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        database=settings.DB_NAME
    )

    cursor = conn.cursor()
    emailcategoria = Titular['Categoria']
    emailendereco = Titular['EmailEndereco']

    query = f"""select titularemailemail from titularemail where titularemailemail = '{emailendereco}'"""
    cursor.execute(query)
    resultados = cursor.fetchall()
    encontrado = 0
    for x in resultados:
        encontrado = 1
        break
    if encontrado == 0:

        sql = "INSERT INTO titularemail(titularemailcategoriaemail, titularemailemail, titularid) VALUES(%s, %s, %s)"
        cursor.execute(sql, (emailcategoria, emailendereco, id))
        conn.commit()
        return('Telefone cadastrado com sucesso')

def insertOutros(Titular, id):
    conn = pg.connect(
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        database=settings.DB_NAME
    )

    cursor = conn.cursor()
    tipo_dado = Titular['TipoDado']
    titulo_dado  = Titular['TituloDado']
    valor_dado = Titular['ValorDado']

    query = f"""select titularid from titularoutros where titularid = '{id}'"""
    cursor.execute(query)
    resultados = cursor.fetchall()
    encontrado = 0
    for x in resultados:
        encontrado = 1
        break
    if encontrado == 0:

        sql = "INSERT INTO titularoutros(titularoutrosdadotipo, titularoutrostitulo, titularoutrosvalor, titularid) VALUES(%s, %s, %s, %s)"
        cursor.execute(sql, (tipo_dado, titulo_dado, valor_dado, id))
        conn.commit()
        return('Dados titulares cadastrados com sucesso')
    
def insertDadosTitulares(Titular, id):
    conn = pg.connect(
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        database=settings.DB_NAME
    )
    cursor = conn.cursor()
     
    cursor.execute(f"select titulardocumentoid from titulardocumento where titularid = {id}")
    IdDocumento = cursor.fetchall()[0][0]

    cursor.execute(f"select titularEnderecoid from titularEndereco where titularid = {id}")
    IdEndereco = cursor.fetchall()[0][0]

    cursor.execute(f"select titularemailid from titularemail where titularid = {id}")
    IdEmail = cursor.fetchall()[0][0]

    cursor.execute(f"select titularTelefoneid from titularTelefone where titularid = {id}")
    IdTelefone = cursor.fetchall()[0][0]
  
    for termo in Titular:
        cursor.execute(f"select sg_titularid, sg_termoid from dadostitulares where sg_titularid = {id} and sg_termoid = {termo['TermoID']}")
        resultados = cursor.fetchall()
        encontrado = 0
        for x in resultados:
            encontrado = 1
            break
        if encontrado == 0:

            sql = "insert into dadostitulares(sg_termoid, sg_titularid, titulardocumentoid,titularemailid,titularenderecoid, titulartelefoneid) values(%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql,(termo['TermoID'],id,IdDocumento, IdEmail, IdEndereco, IdTelefone))
            conn.commit()
    
    cursor.close()
    conn.close()
    return('Dados titulares cadastrados com sucesso')