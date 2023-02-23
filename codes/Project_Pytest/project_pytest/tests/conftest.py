import pytest

@pytest.fixture
def cep_invalid() -> str:
    return "0815054v"

@pytest.fixture
def cep_incorrect() -> str:
    return "08150544"

@pytest.fixture
def cep() -> str:
    return "08150545"

@pytest.fixture
def address() -> dict:
    return {"cep":"08150545",
            "address_type":"Rua",
            "address_name":"Frei Fabiano de Cristo",
            "address":"Rua Frei Fabiano de Cristo",
            "state":"SP",
            "district":"Jardim Senice",
            "lat":"-23.5145",
            "lng":"-46.40923",
            "city":"São Paulo",
            "city_ibge":"3550308",
            "ddd":"11"}