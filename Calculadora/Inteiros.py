# =========================
# INTEIROS.PY
# Funções de manipulação de números inteiros em diferentes bases
# =========================

# Tabela de caracteres usada para representar valores em bases maiores que 10
Caracteres = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$&"


# =========================
# CONVERSÃO DE BASE (DIVISÕES SUCESSIVAS)
# Ex: decimal -> outra base
# =========================
def Conversao(numero, base):
    """
    Converte um número inteiro (decimal) para outra base.
    Retorna um vetor de dígitos.
    """
    restos = []

    while numero > 0:
        restos.append(numero % base)
        numero = numero // base

    restos.reverse()

    return restos if restos else [0]


# =========================
# SOMA DE VETORES EM BASE
# =========================
def Soma(a, b, base):
    a = a[::-1]
    b = b[::-1]

    carry = 0
    resultado = []

    for i in range(max(len(a), len(b))):
        da = a[i] if i < len(a) else 0
        db = b[i] if i < len(b) else 0

        s = da + db + carry
        resultado.append(s % base)
        carry = s // base

    if carry:
        resultado.append(carry)

    return resultado[::-1]


# =========================
# MULTIPLICAÇÃO DE VETORES
# =========================
def Multiplica(a, b, base):
    resultado = [0]

    for i in range(len(b)):
        temp = []
        carry = 0

        for d in a[::-1]:
            val = d * b[-1 - i] + carry
            temp.append(val % base)
            carry = val // base

        if carry:
            temp.append(carry)

        temp = temp[::-1] + [0] * i
        resultado = Soma(resultado, temp, base)

    return resultado


# =========================
# HORNER PARA BASES
# =========================
def Horner(digitos_convertidos, base_convertida, base_destino):
    x = [0]

    for d in digitos_convertidos:
        x = Multiplica(x, base_convertida, base_destino)
        x = Soma(x, d, base_destino)

    return x


# =========================
# CONVERSÃO GERAL DE NÚMEROS EM BASE
# =========================
def Metodo(numero, base_origem, base_destino):
    base_convertida = Conversao(base_origem, base_destino)

    digitos_convertidos = []

    for d in numero:
        valor = Caracteres.index(d)
        digitos_convertidos.append(Conversao(valor, base_destino))

    resultado = Horner(digitos_convertidos, base_convertida, base_destino)

    return "".join(Caracteres[d] for d in resultado)


# =========================
# SOMA E MULTIPLICAÇÃO AUXILIAR (EXPORTADAS)
# =========================
def SomaVetores(v1, v2, base):
    i = len(v1) - 1
    j = len(v2) - 1
    carry = 0
    resultado = []

    while i >= 0 or j >= 0:
        d1 = v1[i] if i >= 0 else 0
        d2 = v2[j] if j >= 0 else 0

        s = d1 + d2 + carry
        resultado.append(s % base)
        carry = s // base

        i -= 1
        j -= 1

    if carry:
        resultado.append(carry)

    resultado.reverse()
    return resultado


def ProdutoVetores(v1, v2, base):
    resultado = [0]

    for i in range(len(v2)):
        temp = []
        carry = 0

        for d in v1[::-1]:
            val = d * v2[-1 - i] + carry
            temp.append(val % base)
            carry = val // base

        if carry:
            temp.append(carry)

        temp = temp[::-1] + [0] * i
        resultado = SomaVetores(resultado, temp, base)

    return resultado