import Inteiros
import Flutuantes
import Validação



def Calculadora():

    print("Digite 1 se quiser converter")
    print("Digite 2 se quiser somar")
    print("Digite 3 se quiser multiplicar")

    op = int(input())

    if op == 1:
        print("Digite o número que quer converter:")
        numero = input()

        print("Digite a base original:")
        BaseOriginal = int(input())

        print("Digite a base destino:")
        BaseDestino = int(input())

        if Validação.ValidacaoConversao(numero, BaseOriginal, BaseDestino):

            if "." in numero:
                resultado = Flutuantes.ConverterNumeroReal(
                    numero, BaseOriginal, BaseDestino
                )
            else:
                resultado = Inteiros.Metodo(
                    numero, BaseOriginal, BaseDestino
                )

            print("Resultado:", resultado)

    elif op == 2:
        print("Digite o primeiro número:")
        n1 = input()

        print("Digite o segundo número:")
        n2 = input()

        print("Digite a base:")
        base = int(input())

        if Validação.ValidacaoSoma(n1, n2, base):

            
            if "." in n1 or "." in n2:
                resultado = Flutuantes.SomaReais(n1, n2, base)

            else:
                v1 = [Inteiros.Caracteres.index(c) for c in n1]
                v2 = [Inteiros.Caracteres.index(c) for c in n2]

                resultado = Inteiros.SomaVetores(v1, v2, base)
                resultado = "".join(
                    Inteiros.Caracteres[d] for d in resultado
                )

            print("Resultado:", resultado)


    elif op == 3:
        print("Digite o primeiro número:")
        n1 = input()

        print("Digite o segundo número:")
        n2 = input()

        print("Digite a base:")
        base = int(input())

        if Validação.ValidacaoProduto(n1, n2, base):

         
            if "." in n1 or "." in n2:
                resultado = Flutuantes.ProdutoReais(n1, n2, base)

            else:
                v1 = [Inteiros.Caracteres.index(c) for c in n1]
                v2 = [Inteiros.Caracteres.index(c) for c in n2]

                resultado = Inteiros.ProdutoVetores(v1, v2, base)
                resultado = "".join(
                    Inteiros.Caracteres[d] for d in resultado
                )

            print("Resultado:", resultado)

    else:
        print("Opção inválida")

Calculadora()