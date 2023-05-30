import psycopg2 as pg

def insertTitular(Titular):
    conn = pg.connect(
        host="localhost",
        port="5432",
        database="Eagle2",
        user="postgres",
        password="SDNA@2022"
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
    
def insertDocumento(Titular, Chave):
    conn = pg.connect(
        host="localhost",
        port="5432",
        database="Eagle2",
        user="postgres",
        password="SDNA@2022"
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
    
        cursor.execute(f"SELECT titularid FROM titular WHERE titularchavepesquisa = '{Chave}'")
        selectchave = cursor.fetchall()
        
        sql = "INSERT INTO titulardocumento(titulardocumentotipodocumentopessoal, titulardocumentoconteudo, titulardocumentovalidade,titularid) VALUES(%s, %s, %s,%s)"
        cursor.execute(sql, (tipo_doc, valor_doc, validade_doc,selectchave[0][0]))
        conn.commit()
        return ('Documento cadastrado com sucesso')
    
def insertEndereco(Titular, Chave):
    conn = pg.connect(
        host="localhost",
        port="5432",
        database="Eagle2",
        user="postgres",
        password="SDNA@2022"
    )

    cursor = conn.cursor()
    categoriaend = Titular['Habitacao']
    endereco = Titular['Endereco']
    numerolocal = Titular['Numero']
    complemento = Titular['Complemento']
    bairro = Titular['Bairro']
    cep = Titular['CEP']
    cidade = Titular['Cidade']
    unidadefederal = Titular['UF']
    pais = Titular['Pais']

    cursor.execute(f"SELECT titularid FROM titular WHERE titularchavepesquisa = '{Chave}'")
    selectchave = cursor.fetchall()

    query = f"""select titularid from titularendereco where titularid = '{selectchave[0][0]}'"""
    cursor.execute(query)
    resultados = cursor.fetchall()
    encontrado = 0
    for x in resultados:
        encontrado = 1
        break
    if encontrado == 0:

        sql = "INSERT INTO titularendereco(titularenderecocategoriaendereco, titularenderecorua, titularendereconro, titularenderecocomplemento, titularenderecobairro, titularenderecocep, titularenderecocidade, titularenderecouf, titularenderecopais, titularid) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (categoriaend, endereco, numerolocal, complemento, bairro, cep, cidade, unidadefederal, pais, selectchave[0][0]))
        conn.commit()
        return('Endereço cadastrado com sucesso')

def insertTelefone(Titular, Chave):
    conn = pg.connect(
        host="localhost",
        port="5432",
        database="Eagle2",
        user="postgres",
        password="SDNA@2022"
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

        cursor.execute(f"SELECT titularid FROM titular WHERE titularchavepesquisa = '{Chave}'")
        selectchave = cursor.fetchall()

        sql = "INSERT INTO titulartelefone(titulartelefoneinternacional, titulartelefoneDDD, titulartelefonenro, titularid) VALUES(%s, %s, %s, %s)"
        cursor.execute(sql, (TelDDI, TelDDD, TelNro, selectchave[0][0]))
        conn.commit()
        return('Telefone cadastrado com sucesso')

def insertEmail(Titular, Chave):
    conn = pg.connect(
        host="localhost",
        port="5432",
        database="Eagle2",
        user="postgres",
        password="SDNA@2022"
    )

    cursor = conn.cursor()
    emailcategoria = Titular['EmailCategoria']
    emailendereco = Titular['EmailEndereco']

    query = f"""select titularemailemail from titularemail where titularemailemail = '{emailendereco}'"""
    cursor.execute(query)
    resultados = cursor.fetchall()
    encontrado = 0
    for x in resultados:
        encontrado = 1
        break
    if encontrado == 0:

        cursor.execute(f"SELECT titularid FROM titular WHERE titularchavepesquisa = '{Chave}'")
        selectchave = cursor.fetchall()

        sql = "INSERT INTO titularemail(titularemailcategoriaemail, titularemailemail, titularid) VALUES(%s, %s, %s)"
        cursor.execute(sql, (emailcategoria, emailendereco, selectchave[0][0]))
        conn.commit()
        return('Telefone cadastrado com sucesso')

def insertOutros(Titular, Chave):
    conn = pg.connect(
        host="localhost",
        port="5432",
        database="Eagle2",
        user="postgres",
        password="SDNA@2022"
    )

    cursor = conn.cursor()
    tipo_dado = Titular['TipoDado']
    titulo_dado  = Titular['TituloDado']
    valor_dado = Titular['ValorDado']

    cursor.execute(f"SELECT titularid FROM titular WHERE titularchavepesquisa = '{Chave}'")
    selectchave = cursor.fetchall()
    print(selectchave)

    sql = "INSERT INTO titularoutros(titularoutrosdadotipo, titularoutrostitulo, titularoutrosvalor, titularid) VALUES(%s, %s, %s, %s)"
    cursor.execute(sql, (tipo_dado, titulo_dado, valor_dado, selectchave[0][0]))
    conn.commit()
    return('Dados titulares cadastrados com sucesso')
    
def insertTermosIDs(Titular):
    conn = pg.connect(
        host="localhost",
        port="5432",
        database="Eagle2",
        user="postgres",
        password="SDNA@2022"
    )
    cursor = conn.cursor()
    cursor.execute('SELECT titularid as "titularid", titulardocumentoid as "titulardocumentoid", titularemailid as "titularemailid", titularenderecoid as "titularenderecoid", titulartelefoneid as "titulartelefoneid" FROM titulares_ids')
    titulares_ids = cursor.fetchall()
    sql = "INSERT INTO dadostitulares(sg_titularid, titulardocumentoid, titularemailid, titularenderecoid)"
    cursor.close()
    conn.close()
    return('Dados titulares cadastrados com sucesso')