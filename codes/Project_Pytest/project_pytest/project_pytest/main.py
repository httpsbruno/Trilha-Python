# Classe que recebe um número CEP e cria um arquivo com o endereço deste
# número. Utilizando a api: https://cep.awesomeapi.com.br/json/{cep};
# O arquivo só é criado se o resultado for válido, caso o CEP já tenha sido digitado
# retorna "CEP já foi registrado".
# Se digitar letras ou caracteres especiais: "CEP inválido";
# Se digitar números mas não tiver CEP: "CEP não encontrado".

import requests
import os
from requests.exceptions import HTTPError


class CepRegister:

    def __init__(self):
        self.url = "https://cep.awesomeapi.com.br/json/"
        self.headers = {"Accept": "application/json"}

    def get_cep_data(self,  cep: str) -> dict:
        try:
            response = requests.get(self.url + cep, headers=self.headers)
            response.raise_for_status()
            result = response.json()
        except HTTPError as err:
            code = str(err).split(' ')[0]

            if code == "400":
                result = {"error": "Invalid CEP!"}
            elif code == "404":
                result = {"error": "CEP not found!"}
            else:
                result = {"error": str(err).split(' ')[0]}

        return result  # response.json()  ["cep"]

    def create_cep_file(self, address: dict):
        cep_file_path = self.get_file_path(address['cep'])
        exist = self.check_cep_file(address['cep'])
        if not exist:
            with open(cep_file_path, "w") as file:
                file.write(str(
                    f"{ address['address'] }, { address['district'] }, { address['city'] } - { address['state'] }"))
            return f"\n{address['cep']} created!"
        else:
            return f"\n{address['cep']} has already been registered!"

    def check_cep_file(self, cep: str):
        cep_file_path = self.get_file_path(cep)
        if os.path.exists(cep_file_path):
            return True
        else:
            return False

    def delete_cep_file(self, cep):
        exist = self.check_cep_file(cep)
        if exist:
            cep_file_path = self.get_file_path(cep)
            os.remove(cep_file_path)

            return f"{cep}.txt removed successfully!"
        else:
            return f"This file doesn't exist!"
    
    def get_file_path(self, file):
        file_extension = f"{file}.txt"
        dir_path = os.path.dirname(os.path.realpath(__file__))
        cep_path = os.path.join(dir_path, "ceps")
        cep_file_path = os.path.join(cep_path, file_extension)

        return cep_file_path
