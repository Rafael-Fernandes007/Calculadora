from Inteiros import Metodo, Soma, Conversao, Caracteres, SomaVetores, ProdutoVetores



def Partir(numero):
    if "." in numero:
        inteiro, fracao = numero.split(".")
    else:
        inteiro = numero
        fracao = ""

    return inteiro, fracao



def HornerFracao(fracao, base_origem, base_destino):
    base_convertida = Conversao(base_origem, base_destino)
    x = [0]

    for d in fracao[::-1]:
        dig = Conversao(Caracteres.index(d), base_destino)
        x = Soma(x, dig, base_destino)
        x, _ = DivideSimulada(x, base_convertida, base_destino)

    return x



def DivideSimulada(numero, base_convertida, base_destino):
    base = base_convertida[0] 

    resultado = []
    resto = 0

    for d in numero:
        atual = resto * base_destino + d

        quociente = atual // base
        resto = atual % base

        resultado.append(quociente)

    while len(resultado) > 1 and resultado[0] == 0:
        resultado.pop(0)

    return resultado, resto


def ConverterNumeroReal(numero, base_origem, base_destino):
    inteiro, fracao = Partir(numero)

    parte_inteira = Metodo(inteiro, base_origem, base_destino)

    if fracao:
        parte_fracionaria = HornerFracao(fracao, base_origem, base_destino)
        parte_fracionaria = "".join(Caracteres[d] for d in parte_fracionaria)
        return parte_inteira + "." + parte_fracionaria

    return parte_inteira


def SomaReais(n1, n2, base):
    i1, f1 = Partir(n1)
    i2, f2 = Partir(n2)


    max_len = max(len(f1), len(f2))
    f1 = f1.ljust(max_len, '0')
    f2 = f2.ljust(max_len, '0')

    v_f1 = [Caracteres.index(c) for c in f1] if f1 else []
    v_f2 = [Caracteres.index(c) for c in f2] if f2 else []

    soma_frac = SomaVetores(v_f1, v_f2, base) if v_f1 or v_f2 else []

   
    carry = 0
    if len(soma_frac) > max_len:
        carry = soma_frac[0]
        soma_frac = soma_frac[1:]


    v_i1 = [Caracteres.index(c) for c in i1]
    v_i2 = [Caracteres.index(c) for c in i2]

    soma_int = SomaVetores(v_i1, v_i2, base)

    if carry:
        soma_int = SomaVetores(soma_int, [carry], base)

    int_str = "".join(Caracteres[d] for d in soma_int)

    if max_len > 0:
        frac_str = "".join(Caracteres[d] for d in soma_frac).ljust(max_len, '0')
        return int_str + "." + frac_str

    return int_str



def ProdutoReais(n1, n2, base):
    i1, f1 = Partir(n1)
    i2, f2 = Partir(n2)

    num1 = i1 + f1
    num2 = i2 + f2

    casas = len(f1) + len(f2)

    v1 = [Caracteres.index(c) for c in num1]
    v2 = [Caracteres.index(c) for c in num2]

    produto = ProdutoVetores(v1, v2, base)

    produto_str = "".join(Caracteres[d] for d in produto)

    if casas > 0:
        if len(produto_str) <= casas:
            produto_str = "0" * (casas - len(produto_str) + 1) + produto_str

        produto_str = produto_str[:-casas] + "." + produto_str[-casas:]

    return produto_str