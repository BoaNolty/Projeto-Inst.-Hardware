from usuario import Usuario

class SistemaCadastro():
    def __init__(self):
        self._banco_usuarios = []

    def criar_conta(
        self,
        nome: str,
        email: str,
        cpf: str,
        data_nascimento: str,
        login: str,
        senha: str
   ) -> dict:
    
        campos = [("Nome", nome), ("Email", email), ("CPF", cpf), ("Data de Nascimento", data_nascimento), ("Login", login), ("Senha", senha)]
        if any(not str(campo).strip() for _, campo in campos):
            return {
            "sucesso": False,
            "mensagem": "Todos os campos são obrigatórios e não podem estar vazios."
        }
    
        cpf_limpo = "".join(caracter for caracter in cpf if caracter.isdigit())
        for usr in self._banco_usuarios:
            if usr.cpf == cpf_limpo:
                return {
                "sucesso": False,
                "mensagem": "CPF já cadastrado."
            }
        try:
            novo_usuario = Usuario(
                nome=nome.strip(),
                email=email.strip(),
                cpf=cpf,
                data_nascimento=data_nascimento.strip(),
                login=login.strip(),
                senha=senha,
            )

            self._banco_usuarios[novo_usuario.login] = novo_usuario

            return {
                "sucesso": True,
                "mensagem": "Conta criada com sucesso!",
                "dados": novo_usuario.exibir_dados_publicos()
        }
    
        except ValueError as e:
            return {"sucesso": False, "mensagem": str(e)}