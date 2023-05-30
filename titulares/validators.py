def TitularValidator(titular):
        if titular['Nome'] == None:
            titular['Nome'] = "Campo não pode estar vazio"
            return False, titular
        return True, titular

def EmailValidator(Email):
        if Email['EmailEndereco'] == None:
            Email['EmailEndereco'] = "Campo não pode estar vazio"
            return False, Email
        return True, Email
    
def TelefoneValidator(Telefone):
        e = 0

        for tel in Telefone:
            if Telefone[tel] == None:
                Telefone[tel] = "Campo não pode estar vazio"
                e+=1
        if e > 0:
                return False, Telefone     
        return True, Telefone
    
def EnderecoValidator(Endereco):
    e = 0
    if Endereco['Bairro'] == None:
        Endereco['Bairro'] = "Campo não pode estar vazio"
        e+=1
    if Endereco['CEP'] == None:
        Endereco['CEP'] = "Campo não pode estar vazio"
        e+=1
    if Endereco['Cidade'] == None:
        Endereco['Cidade'] = "Campo não pode estar vazio"
        e+=1
    if Endereco['Numero'] == None:
        Endereco['Numero'] = "Campo não pode estar vazio"
        e+=1      
    if e > 0:
        return False, Endereco
    return True, Endereco
    
def DocumentoValidator(Documento):
    e = 0

    for doc in Documento:
        if Documento[doc] == None:
            Documento[doc] = "Campo não pode estar vazio"
            e+=1
    if e > 0:
            return False, Documento   
    return True, Documento
    
def OutrosValidator(Outros):
    e = 0

    for outr in Outros:
        if Outros[outr] == None:
            Outros[outr] = "Campo não pode estar vazio"
            e+=1
    if e > 0:
            return False, Outros     
    return True, Outros
    
def TermoValidator(Termo):
    e = 0

    for ter in Termo:
        if ter['TermoID'] != None:
            e+=1
    if e > 0:
        return True, Termo
        
    return False, Termo

def Validator(Titular):
        countvalidator = 0
        
        validator, ErrorDic = TitularValidator(Titular['Titular'])

        if validator:
            countvalidator+=1
        else:
            Titular['Titular'] = ErrorDic

        validator, ErrorDic = EmailValidator(Titular['Email'])

        if validator:
            countvalidator+=1
        else:
            Titular['Email'] = ErrorDic

        validator, ErrorDic = TelefoneValidator(Titular['Telefone'])

        if validator:
            countvalidator+=1
        else:
            Titular['Telefone'] = ErrorDic

        validator, ErrorDic = EnderecoValidator(Titular['TitularEndereco'])

        if validator:
            countvalidator+=1
        else:
            Titular['TitularEndereco'] = ErrorDic

        validator, ErrorDic = DocumentoValidator(Titular['Documentos'])

        if validator:
            countvalidator+=1
        else:
            Titular['Documentos'] = ErrorDic
        
        validator, ErrorDic = OutrosValidator(Titular['OutrosDados'])

        if validator:
            countvalidator+=1
        else:
            Titular['OutrosDados'] = ErrorDic

        validator, ErrorDic = TermoValidator(Titular['Termos'])

        if validator == False:
            countvalidator+=1
        
        if countvalidator == 6:
            return True, Titular
        
        return False, Titular