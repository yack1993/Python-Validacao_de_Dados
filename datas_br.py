from datetime import datetime, timedelta

class Datas:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_data()

    def mes_cadastro(self):
        meses_do_ano = ["Janeiro", "Fevereiro", "Março", "Abril",
                        "Maio", "Junho","Julho", "Agosto", "Setembro",
                        "Outubro", "Novembro","Dezembro"]
        mes_cadastro = self.momento_cadastro.month - 1
        #print(mes_cadastro)
        return meses_do_ano[mes_cadastro]

    def dia_semana(self):
        dias_semana = ["Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sábado","Domingo"]
        dia_semana = self.momento_cadastro.weekday()
        #print(dia_semana)
        return dias_semana[dia_semana]

    def format_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada

    def tempo_cadastro(self):
        tempo_cadastro = (datetime.today() + timedelta(days=30)) - self.momento_cadastro
        return tempo_cadastro