matriz_num = [
    ['', 'um', 'dois', 'três', 'quatro','cinco', 'seis', 'sete', 'oito', 'nove'],
    ['', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove'],
    ['', '', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa'],
    ['', 'cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos', 'oitocentos', 'novecentos']
]

def get_unidade(inteiro_str):
    return matriz_num[0][int(inteiro_str)]
    
def get_dezena(inteiro_str):
    if inteiro_str[0] == '0':
        return '', False

    if inteiro_str[0] != '1':
        dezena = inteiro_str[0]
        dezena = int(dezena)
        return matriz_num[2][dezena], False
    else:
        unidade = inteiro_str[1]
        unidade = int(unidade)
        return matriz_num[1][unidade - 10], True

def get_centena(inteiro_str):
    if inteiro_str == '100':
        return 'cem', True
    else:
        return matriz_num[3][int(inteiro_str[0])], False

def get_milhar(inteiro_str):
    return get_extenso(inteiro_str) + ' mil'

def get_milhao(inteiro_str):
    inteiro = int(inteiro_str)
    if inteiro == 1:
        return 'um milhão'
    return verifica_extenso(inteiro) + ' milhoes'

def get_extenso(inteiro_str):
    num = 0
    antes_numeros = ''
    if inteiro_str.startswith('-'):
        antes_numeros = 'menos '
        inteiro_str = inteiro_str[1:]
    inteiro_str = str(int(inteiro_str))
    tamanho_inteiro = len(inteiro_str)
    
    if inteiro_str == '0':
        return antes_numeros + 'zero'

    if tamanho_inteiro == 1:
        return antes_numeros + get_unidade(inteiro_str)

    elif tamanho_inteiro == 2 :
        dezena, toda = get_dezena(inteiro_str)
        nums_str = []
        nums_str.append(dezena)
        if not toda:
            unidade = get_unidade(inteiro_str[1])
            if unidade != '':
                nums_str.append(unidade)
        return antes_numeros + ' e '.join(nums_str)

    elif tamanho_inteiro == 3:
        centena, todo = get_centena(inteiro_str)
        nums_str = []
        if todo:
            return centena
        if centena != '':
            nums_str.append(centena)
        dezena, toda = get_dezena(inteiro_str[-2:])
        if dezena != '':
            nums_str.append(dezena)
        if not toda:
            unidade = get_unidade(inteiro_str[-1])
            if unidade != '':
                nums_str.append(unidade)
        return antes_numeros + ' e '.join(nums_str)

    else:
        nums_str = []
        mil = get_milhar(inteiro_str[:-3])
        nums_str.append(mil)
        centena, todo = get_centena(inteiro_str[-3:])
        if todo:
            return centena
        if centena != '':
            nums_str.append(centena)
        dezena, toda = get_dezena(inteiro_str[-2:])
        if dezena != '':
            nums_str.append(dezena)
        if not toda:
            unidade = get_unidade(inteiro_str[-1])
            if unidade != '':
                nums_str.append(unidade)
        return antes_numeros + ' e '.join(nums_str)


    return num 