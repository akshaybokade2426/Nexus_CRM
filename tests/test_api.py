import time

import pytest
import requests
from config.environment import Environment

class TestContacts:
    env = Environment()
    base_url = env.get_base_url()

    def test_login(self):
        resource_path = "/users/login"
        payload = {
                    "email": "akshaybokade007@gmail.com",
                    "password": "Admin@123"
                    }

        response = requests.post(self.base_url+resource_path, json=payload)

        assert response.status_code == 200, f"The status code should be 200 but got {response.status_code}"
        bearer_token  = response.json()["token"]
        headers = {"Authorization": f"Bearer {bearer_token}",
                   "Content-Type": "application/json"}
        return headers

    def test_add_contact(self):
        resource_path = "/contacts"
        payload ={
                    "firstName": "John",
                    "lastName": "Doe",
                    "birthdate": "1970-01-01",
                    "email": "jdoe@fake.com",
                    "phone": "8005555555",
                    "street1": "1 Main St.",
                    "street2": "Apartment A",
                    "city": "Anytown",
                    "stateProvince": "KS",
                    "postalCode": "12345",
                    "country": "USA"
                }
        headers = self.test_login()

        response = requests.post(self.base_url + resource_path, json=payload, headers=headers)
        assert response.status_code == 201, f"The status code should be 201 but got {response.status_code}"
        print(response.json())
        return response.json()["_id"]

    def test_get_contact_list(self):
        resource_path = "/contacts"
        headers = self.test_login()

        response = requests.get(self.base_url + resource_path, headers=headers)
        assert response.status_code == 200, f"The status code should be 200 but got {response.status_code}"

    def test_get_contact(self):
        resource_path = "/contacts/"
        headers = self.test_login()

        response = requests.get(self.base_url + resource_path, headers=headers)
        assert response.status_code == 200, f"The status code should be 200 but got {response.status_code}"
        print(response.json())

    def test_update_contact(self):
        id = self.test_add_contact()
        resource_path = f"/contacts/{id}"
        headers = self.test_login()
        payload = {
                    "firstName": "Amy",
                    "lastName": "Miller",
                    "birthdate": "1992-02-02",
                    "email": "amiller@fake.com",
                    "phone": "8005554242",
                    "street1": "13 School St.",
                    "street2": "Apt. 5",
                    "city": "Washington",
                    "stateProvince": "QC",
                    "postalCode": "A1A1A1",
                    "country": "Canada"
                }
        response = requests.put(self.base_url + resource_path, json=payload, headers=headers)
        assert response.status_code == 200, f"The status code should be 200 but got {response.status_code}"

    def test_patch_update_contact(self):
        id = self.test_add_contact()
        resource_path = f"/contacts/{id}"
        headers = self.test_login()
        payload = {"firstName": "Anna"}

        response = requests.patch(self.base_url + resource_path, json=payload, headers=headers)
        assert response.status_code == 200, f"The status code should be 200 but got {response.status_code}"
        print(response.json())

    @pytest.mark.skip
    def test_delete_contact(self):
        resource_path = "/contacts/69ca27f2f70609001540319b"
        headers = self.test_login()
        response = requests.delete(self.base_url + resource_path, headers=headers)
        assert response.status_code == 200, f"The status code should be 200 but got {response.status_code}"


class TestUser:
    env = Environment()
    base_url = env.get_base_url()
    unique_email = f"test_user_{int(time.time())}@fake.com"

    def test_1_add_user(self):
        resource_path = "/users"
        payload = {
            "firstName": "Akshay",
            "lastName": "Sanjay",
            "email": self.unique_email,  # Assuming this is generated in setup
            "password": "myPassword"
        }

        response = requests.post(self.base_url + resource_path, json=payload)
        # 1. Check for success and print error if it fails
        assert response.status_code == 201, f"User creation failed: {response.text}"
        # 2. Extract the token
        bearer_token = response.json()["token"]
        # 3. Save to 'self' so other methods in this class can use it
        headers = {
            "Authorization": f"Bearer {bearer_token}",
            "Content-Type": "application/json"
        }
        return headers

        print(f"User created and token stored for: {payload['email']}")

    def test_2_get_user_profile(self):
        resource_path = "/users/me"

        headers = self.test_1_add_user()
        response = requests.get(self.base_url + resource_path, headers=headers)
        assert response.status_code == 200, f"Failed to fetch profile: {response.text}"

        user_data = response.json()

        assert "email" in user_data
        print(f"Successfully retrieved profile for: {user_data['email']}")
        print(response.json())
        return user_data

    def test_3_update_user_profile(self):
        resource_path = "/users/me"
        headers = self.test_1_add_user()
        email =self.unique_email
        password = "myNewPassword"

        payload = {
                    "firstName": "Akshay",
                    "lastName": "Bokade",
                    "email": email,
                    "password": password
                }
        response = requests.patch(self.base_url + resource_path, json=payload, headers=headers)
        assert response.status_code == 200, f"Failed to update profile: {response.text}"
        return email, password

    def test_4_post_logout_user(self):
        resource_path = "/users/logout"
        headers = self.test_1_add_user()
        response = requests.post(self.base_url + resource_path, headers=headers)
        assert response.status_code == 200, f"Failed to logout user: {response.text}"

    def test_5_login_user(self):
        resource_path = "/users/login"
        email, password = self.test_3_update_user_profile()
        payload = {
            "email": email,
            "password": password
        }
        response = requests.post(self.base_url + resource_path, json=payload)
        assert response.status_code == 200, f"Failed to login user: {response.text}"

    @pytest.mark.skip
    def test_6_delete_user(self):
        resource_path = "/users/me"
        headers = self.test_1_add_user()

        response = requests.delete(self.base_url + resource_path, headers=headers)
        assert response.status_code == 200, f"Failed to delete user: {response.text}"


