from main import CepRegister

cep_address = CepRegister().get_cep_data("08150545")
print(cep_address)
#cep_check = CepRegister().check_cep_file("08150545")

#cep_address = CepRegister().delete_cep_file("08150545")

# cep_address = CepRegister().get_cep_data("08150545")
# cep_file = CepRegister().create_cep_file(cep_address)
#print(cep_file)

