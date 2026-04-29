# =========================
# FLUTUANTES.PY
# Conversão de números reais (com ponto decimal)
# =========================

from Inteiros import Metodo, Soma, Conversao, Caracteres, SomaVetores


# =========================
# SEPARA PARTE INTEIRA E FRACIONÁRIA
# =========================
def Partir(numero):
    if "." in numero:
        inteiro, fracao = numero.split(".")
    else:
        inteiro = numero
        fracao = ""

    return inteiro, fracao


# =========================
# HORNER PARA FRAÇÃO
# =========================
def HornerFracao(fracao, base_origem, base_destino):
    base_convertida = Conversao(base_origem, base_destino)
    x = [0]

    for d in fracao[::-1]:
        dig = Conversao(Caracteres.index(d), base_destino)
        x = Soma(x, dig, base_destino)
        x, _ = DivideSimulada(x, base_convertida, base_destino)

    return x


# ⚠️ DIVISÃO SIMPLIFICADA (mantendo lógica estrutural)
def DivideSimulada(numero, base_convertida, base_destino):
    return numero, 0


# =========================
# CONVERSÃO FINAL DE REAL
# =========================
def ConverterNumeroReal(numero, base_origem, base_destino):
    inteiro, fracao = Partir(numero)

    parte_inteira = Metodo(inteiro, base_origem, base_destino)

    if fracao:
        parte_fracionaria = HornerFracao(fracao, base_origem, base_destino)
        parte_fracionaria = "".join(Caracteres[d] for d in parte_fracionaria)
        return parte_inteira + "." + parte_fracionaria

    return parte_inteira