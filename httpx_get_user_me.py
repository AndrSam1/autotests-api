import httpx  # Импортируем библиотеку HTTPX

# Данные для входа в систему
login_payload = {
    "email": "user@example.com",
    "password": "string"
}

# Выполняем запрос на аутентификацию
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

# Выводим полученные токены
print("Login response:", login_response_data)
print("Status Code:", login_response.status_code)

# Определяем заголовок в объекте Client
client = httpx.Client(headers={"Authorization": f"Bearer {login_response_data["token"]["accessToken"]}"})

# Выполняем запрос к эндпоинту /api/v1/users/me
user_me_response = client.get("http://localhost:8000/api/v1/users/me")
user_me_response_data = user_me_response.json()
client.close()

# Выводим ответ на запрос к эндпоинту /api/v1/users/me
print("Refresh response:", user_me_response_data)
print("Status Code:", user_me_response.status_code)