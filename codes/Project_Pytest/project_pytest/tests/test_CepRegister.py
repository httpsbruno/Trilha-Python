import pytest
from project_pytest.main import CepRegister

# Api request
@pytest.mark.error
def test_get_cep_data_invalid(cep_invalid: str):
    data = CepRegister().get_cep_data(cep_invalid)
    assert data == {"error": "Invalid CEP!"}

@pytest.mark.error
def test_get_cep_data_incorrect(cep_incorrect: str):
    data = CepRegister().get_cep_data(cep_incorrect)
    assert data == {"error": "CEP not found!"}

def test_get_cep_data(cep: str):
    data = CepRegister().get_cep_data(cep)
    assert data['district'] == "Jardim Senice"

#create a file
def test_create_cep_file(address):
    result = CepRegister().create_cep_file(address)
    assert result == "\n08150545 created!"
    # trying to create another file with the same CEP
    result = CepRegister().create_cep_file(address)
    assert result == "\n08150545 has already been registered!"

# check if the file exist
def test_check_cep_file(cep):
    result = CepRegister().check_cep_file(cep)
    assert result == True

# delete cep file
def test_delete_cep_file(cep):
    result = CepRegister().delete_cep_file(cep)
    assert result == "08150545.txt removed successfully!"
    # trying to delete the file that was deleted
    result = CepRegister().delete_cep_file(cep)
    assert result == "This file doesn't exist!"

# check if the file exist after delete
def test_check_cep_file_after_delete(cep):
    result = CepRegister().check_cep_file(cep)
    assert result == False
