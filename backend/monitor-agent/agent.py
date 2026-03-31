import requests
import time

API_URL = "http://infra-api:8080/api"
CHECK_INTERVAL = 30


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

    start = time.time()

    try:
        response = requests.get(url, timeout=10)
        is_online = response.status_code < 500
    except requests.exceptions.RequestException:
        is_online = False

    response_time = int((time.time() - start) * 1000)

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