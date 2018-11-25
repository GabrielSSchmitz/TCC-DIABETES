from tcc.src.utils.registro import registro
from apyori import apriori

import pandas

registro = registro()
log = registro.log()

registro.log().debug('Executando Apriori')


class Assosiacao:

    def assosiacao(self, data_frame):

        transacoes = []

        log.info('Convertendo Data Frame para uma lista')
        for i in range(0, int(data_frame.shape[0])):
            transacoes.append([str(data_frame.values[i, j]) for j in range(0, 9)])

        log.info('Aplicando Apriori na Lista')
        regras = apriori(transacoes , min_support=0.0045, min_confidence=0.6 , min_lift=3, min_length=2)

        resultados = list(regras)

        print(len(resultados))

        log.info('Gerando resposta')
        for item in resultados:

            pair = item[0]
            items = [x for x in pair]
            print("Regra: " + items[0] + " -> " + items[1])
            print("Suporte: " + str(item[1]))
            print("Confiança: " + str(item[2][0][2]))
            print("=====================================")

        registro.log().debug('Apriori  Executado')

assosiacao = Assosiacao()

df = pandas.read_csv("../media/pima_indians.csv")
assosiacao.assosiacao(data_frame=df)