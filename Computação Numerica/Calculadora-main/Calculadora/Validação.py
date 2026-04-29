

from Inteiros import Caracteres


def ValidacaoBases(b1, b2):
    if b1 < 2 or b2 < 2:
        print("Base deve ser >= 2")
        return False

    if b1 > len(Caracteres) or b2 > len(Caracteres):
        print("Base maior que permitido")
        return False

    return True


def ValidacaoNumero(numero, base):
    numero = numero.upper()

    for c in numero:
        if c == ".":
            continue

        if c not in Caracteres:
            print("Caractere inválido")
            return False

        if Caracteres.index(c) >= base:
            print("Dígito não pertence à base")
            return False

    return True



def ValidacaoConversao(numero, b1, b2):
    return ValidacaoBases(b1, b2) and ValidacaoNumero(numero, b1)


def ValidacaoSoma(n1, n2, base):
    return (
        ValidacaoBases(base, base)
        and ValidacaoNumero(n1, base)
        and ValidacaoNumero(n2, base)
    )


def ValidacaoProduto(n1, n2, base):
    return ValidacaoSoma(n1, n2, base)