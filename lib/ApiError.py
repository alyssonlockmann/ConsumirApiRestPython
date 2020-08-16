class ApiError(Exception):
    #Trata erro da API.

    def __init__(self, status):
        self.status = status

    def __str__(self):
        return "Erro ao obter retorno do serviço! status={}".format(self.status)
