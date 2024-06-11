import pandas
import data.EnviarEmail as ee

def Gerenciamento(caminho, linhaI, linhaF, email):

    # Le o arquivo
    arquivo = pandas.read_excel(caminho)

    # Define "selecionadas" como as linhas escolhidas
    selecionadas = arquivo.iloc[linhaI-2:linhaF-1]

    # Copia as linhas escolhidas em outro arquivo
    selecionadas.to_excel('arquivo_copiado.xlsx', index=False, header=False)

    # Chama a função EnviarEmail
    ee.send(email,"arquivo_copiado.xlsx")

    # Deleta arquivo copiado (a biblioteca os já foi importada em EnviarEmail)
    ee.os.remove("arquivo_copiado.xlsx")

    print("operação sucesso")
