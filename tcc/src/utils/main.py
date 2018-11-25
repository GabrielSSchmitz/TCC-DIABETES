import pandas

from tcc.src.utils.verificaArquivo import verificaArquivo
from tcc.src.utils.normalizacao import normalizacao
from tcc.src.classificador.svm import SVM
from tcc.src.utils.registro import registro

registro = registro()
log = registro.log()

log.debug("====== INICIALIZANDO ======")

data_frame = pandas.read_csv('../media/pima_indians.csv')

# verificaArquivo
verificaArquivo = verificaArquivo()
verificaArquivo.verificaArquivo(data_frame)

resultados = []

normalizacao = normalizacao()
SVM = SVM()

print(data_frame)
log.debug("\n")
for i in range(5):
    log.debug("====== Treinamento: " + str(i) + " ======\n")
    # normalizacao
    data_frame_normalizada = normalizacao.normalizar(data_frame)
    print(data_frame_normalizada)

    # SVM
    precisao = SVM.classificar(data_frame_origin=data_frame_normalizada, target=8)
    resultados.append(precisao)
    log.debug("====== Fim do treinamento: " + str(i) + " ======\n")

pandas.DataFrame(list(resultados)).to_csv("../Media/precisao.csv")
log.debug("====== FINALIZANDO ======\n")
