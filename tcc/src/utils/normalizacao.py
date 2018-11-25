from tcc.src.utils.registro import registro
from sklearn.preprocessing  import MinMaxScaler

import pandas

registro = registro()
log = registro.log()

class normalizacao:

    def normalizar(self, data_frame_origin):

        log.debug('Executando normalizacao')

        data_frame = data_frame_origin
        log.info('Definindo a escala para a  normalização')
        escala = MinMaxScaler()

        log.info('Normalizando data_frame')
        data_frame_normalizada = escala.fit_transform(data_frame)

        log.info('Data frame normalizado')
        data_frame_export = pandas.DataFrame.from_records(data_frame_normalizada)

        log.info('Retornando o data frame normalizado')
        return data_frame_export
