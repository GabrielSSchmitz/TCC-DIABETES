from tcc.src.utils.registro import registro

registro = registro()
log = registro.log()

class verificaArquivo:

    def verificaArquivo(self, data_frame_origin):

        log.debug("Executando validador de arquivo")

        data_frame = data_frame_origin

        colunas_CSV = str(data_frame.columns)
        log.info('Coletando as colunas do Data Frame')

        COLUNAS = ['gravidez',
                   'glucose',
                   'pressao_sanguinea',
                   'espessura_da_pele',
                   'insulina',
                   'bmi',
                   'funcao_de_pedigree_de_diabetes',
                   'idade',
                   'resultado']

        colunas = ""

        for x in range(0, 8):
            colunas = colunas + " (" + str(COLUNAS[x]) + ")"

        log.info('Colunas de verificacao ' + colunas)

        for x in range(0, 8):
            if colunas_CSV.find(COLUNAS[x]) > 0:
                log.info('[OK] ' + COLUNAS[x])
            else:
                log.error(COLUNAS[x] + ':' + 'Codigo parado por arquivo não atender as pré definições')
                exit()

        return True
