import pytest
from petstore_client import PetstoreClient  # <-- Ändra detta till ditt faktiska filnamn/klassnamn

@pytest.fixture
def pet_api():
    # Din kod för att initiera API-klienten
    return PetstoreClient()

@pytest.fixture
def random_pet_id():
    return 123  # Eller din logik för ID

@pytest.fixture
def fake_person(faker):
    """Skapar en fejkad person med hjälp av faker-pluginen"""
    return {
        "first_name": faker.first_name(),  # Här lägger vi till den specifika nyckeln
        "last_name": faker.last_name(),
        "email": faker.email(),
        "address": faker.address()
    }