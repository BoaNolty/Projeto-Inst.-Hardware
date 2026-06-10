from datetime import datetime

class Usuario():
    def __init__(self, nome: str, email: str, cpf: str, data_nascimento: str, login: str, senha: str):
        self.nome = nome
        self.email = email
        self.cpf = self._limpar_cpf(cpf)
        self.data_nascimento = self._converter_data(data_nascimento)
        self.login = login
        self._senha = senha

    def _limpar_cpf(self, cpf: str) -> str:
        return "".join(caracter for caracter in cpf if caracter.isdigit())

    def _converter_data(self, data_str: str) -> datetime.date:
        try:
            return datetime.strptime(data_str, "%d/%m/%Y").date()
        except ValueError:
            raise ValueError("Formato de data inválido. Use DD/MM/AAAA")
        
    def verificar_senha(self, senha_digitada: str) -> bool:
        return self._senha == senha_digitada
    
    def exibir_dados_publicos(self) -> dict:
        return {
            "Nome": self.nome,
            "Email": self.email,
            "CPF": self.cpf,
            "Data de Nascimento": self.data_nascimento.strftime("%d/%m/%Y"),
            "Login": self.login
            }