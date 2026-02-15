import pytest

def test_pet_full_lifecycle(pet_api, random_pet_id, fake_person):
    pet_name = fake_person['first_name']
    updated_name = f"{pet_name}_Updated"

    # 1. CREATE
    create_res = pet_api.create_pet(random_pet_id, pet_name)
    assert create_res.status_code == 200
    assert create_res.json()["name"] == pet_name

    # 2. READ
    read_res = pet_api.get_pet(random_pet_id)
    assert read_res.status_code == 200
    assert read_res.json()["id"] == random_pet_id

    # 3. UPDATE - Se till att din klient tar emot namnet korrekt
    update_res = pet_api.update_pet(random_pet_id, updated_name)
    assert update_res.status_code == 200
    assert update_res.json()["name"] == updated_name

    # 4. DELETE
    assert pet_api.delete_pet(random_pet_id).status_code == 200

    # 5. VERIFY DELETED
    final_get = pet_api.get_pet(random_pet_id)
    assert final_get.status_code == 404