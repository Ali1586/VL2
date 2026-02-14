import requests


def test_that_country_is_US():
    # Anropar API:et för ett specifikt postnummer i USA
    url = "http://api.zippopotam.us/us/90210"
    response = requests.get(url)

    # Kontrollera att anropet lyckades (Statuskod 200)
    assert response.status_code == 200, f"API-anropet misslyckades med status: {response.status_code}"

    response_body = response.json()

    # Validera datan i JSON-svaret
    assert response_body["country"] == "United States"
    assert response_body["places"][0]["place name"] == "Beverly Hills"