import logging  as log

# Configuração para a geração de log [Padrão criado pelo desenvolvedor]
FORMAT = '%(asctime)-15s [%(levelname)s] : %(message)s'
log.basicConfig(filename='../media/registro.log', level=log.DEBUG, format=FORMAT)


class registro:

    def log(self):
        return log
