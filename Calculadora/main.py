# =========================
# MAIN.PY
# Interface principal da calculadora
# =========================

import Inteiros
import Flutuantes
import Validação


# =========================
# FUNÇÃO PRINCIPAL
# =========================
def Calculadora():

    print("Digite 1 se quiser converter")
    print("Digite 2 se quiser somar")
    print("Digite 3 se quiser multiplicar")

    op = int(input())

    # =====================
    # CONVERSÃO DE BASES
    # =====================
    if op == 1:
        print("Digite o número que quer converter:")
        numero = input()

        print("Digite a base original:")
        BaseOriginal = int(input())

        print("Digite a base destino:")
        BaseDestino = int(input())

        if Validação.ValidacaoConversao(numero, BaseOriginal, BaseDestino):

            if "." in numero:
                resultado = Flutuantes.ConverterNumeroReal(numero, BaseOriginal, BaseDestino)
            else:
                resultado = Inteiros.Metodo(numero, BaseOriginal, BaseDestino)

            print("Resultado:", resultado)

    # =====================
    # SOMA
    # =====================
    elif op == 2:
        print("Digite o primeiro número:")
        n1 = input()

        print("Digite o segundo número:")
        n2 = input()

        print("Digite a base:")
        base = int(input())

        if Validação.ValidacaoSoma(n1, n2, base):

            v1 = [Inteiros.Caracteres.index(c) for c in n1]
            v2 = [Inteiros.Caracteres.index(c) for c in n2]

            resultado = Inteiros.SomaVetores(v1, v2, base)

            print("Resultado:", "".join(Inteiros.Caracteres[d] for d in resultado))

    # =====================
    # MULTIPLICAÇÃO
    # =====================
    elif op == 3:
        print("Digite o primeiro número:")
        n1 = input()

        print("Digite o segundo número:")
        n2 = input()

        print("Digite a base:")
        base = int(input())

        if Validação.ValidacaoProduto(n1, n2, base):

            v1 = [Inteiros.Caracteres.index(c) for c in n1]
            v2 = [Inteiros.Caracteres.index(c) for c in n2]

            resultado = Inteiros.ProdutoVetores(v1, v2, base)

            print("Resultado:", "".join(Inteiros.Caracteres[d] for d in resultado))

    else:
        print("Opção inválida")


# =========================
# EXECUÇÃO
# =========================
Calculadora()