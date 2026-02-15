import requests

class PetstoreClient:
    BASE_URL = "https://petstore.swagger.io/v2"

    def create_pet(self, pet_id, name):
        """CREATE - Skapar ett nytt husdjur"""
        payload = {
            "id": pet_id,
            "name": name,
            "status": "available"
        }
        return requests.post(f"{self.BASE_URL}/pet", json=payload)
    #
    def get_pet(self, pet_id):
        """READ - Hämtar ett husdjur baserat på ID"""
        return requests.get(f"{self.BASE_URL}/pet/{pet_id}")

    def update_pet(self, pet_id, new_name):
        """UPDATE - Uppdaterar namnet på ett befintligt husdjur"""
        payload = {
            "id": pet_id,
            "name": new_name,
            "status": "sold"
        }
        return requests.put(f"{self.BASE_URL}/pet", json=payload)

    def delete_pet(self, pet_id):
        """DELETE - Tar bort ett husdjur"""
        return requests.delete(f"{self.BASE_URL}/pet/{pet_id}"  )