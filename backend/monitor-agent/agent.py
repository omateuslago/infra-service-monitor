import requests
import time
import os

API_URL = os.getenv("API_URL", "http://localhost:5232/api")
CHECK_INTERVAL = 60


def get_services():
    try:
        response = requests.get(f"{API_URL}/services", timeout=10)

        print(f"GET /services -> {response.status_code}")
        print("Resposta:", response.text)

        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print("Erro ao buscar serviços:", e)
        return []
    except ValueError:
        print("Resposta não é JSON válido")
        return []


def send_check(data):
    try:
        response = requests.post(f"{API_URL}/checks", json=data, timeout=10)
        print(f"POST /checks -> {response.status_code}")
        print("Resposta:", response.text)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Erro ao enviar check:", e)


def check_service(service):
    url = service["url"]
    service_id = service["id"]

    headers = {
        "User-Agent": "InfraServiceMonitor/1.0"
    }

    start = time.perf_counter()

    try:
        response = requests.head(
            url,
            timeout=10,
            allow_redirects=True,
            headers=headers
        )

        is_online = 200 <= response.status_code < 500

    except requests.exceptions.RequestException:
        is_online = False

    response_time = int((time.perf_counter() - start) * 1000)

    return {
        "serviceId": service_id,
        "isOnline": is_online,
        "responseTimeMs": response_time
    }


while True:
    print("Buscando serviços...")

    services = get_services()

    if not services:
        print("Nenhum serviço encontrado ou API indisponível.")
    else:
        for service in services:
            result = check_service(service)
            print("Resultado:", result)
            send_check(result)

    print("Aguardando próximo ciclo...")
    time.sleep(CHECK_INTERVAL)