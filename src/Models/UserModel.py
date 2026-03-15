from pydantic import EmailStr

class User:
    def __init__(
        self,
        nome_completo: str,
        cpf: str,
        data_nascimento: str,
        nome_pais: str,
        rg: str,
        rg_emissor: str,
        rg_uf: str,
        email: EmailStr,
        celular: str,
        nacionalidade: str,
        estado_civil: str,
        sexo: str,
        cep: str,
        endereco: str,
        estado: str,
        pais: str,
        ocupacao: str = "",
        salario: str = ""
    ):
        # Campos obrigatórios
        self.nome_completo = nome_completo
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.nome_pais = nome_pais
        self.rg = rg
        self.rg_emissor = rg_emissor
        self.rg_uf = rg_uf
        self.email = email
        self.celular = celular
        self.nacionalidade = nacionalidade
        self.estado_civil = estado_civil
        self.sexo = sexo
        self.cep = cep
        self.endereco = endereco
        self.estado = estado
        self.pais = pais

        # Campos opcionais
        self.ocupacao = ocupacao
        self.salario = salario
        self.cpf_validator()

    # Método para converter para dicionário
    def to_dict(self):
        return self.__dict__

    def cpf_validator(self):
        if  not len(self.cpf) == 11 and not self.cpf.isdigit() and not self.cpf != "00000000000":
            raise Exception("CPF Inválido!")