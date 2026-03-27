import requests
import time

API_URL = "http://infra-api:8080/api"
CHECK_INTERVAL = 30


def get_services():
    response = requests.get(f"{API_URL}/services")
    return response.json()


def send_check(data):
    requests.post(f"{API_URL}/checks", json=data)


def check_service(service):

    url = service["url"]
    service_id = service["id"]

    start = time.time()

    try:
        response = requests.get(url, timeout=10)
        is_online = response.status_code < 500
    except:
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

    for service in services:

        result = check_service(service)

        print("Resultado:", result)

        send_check(result)

    print("Aguardando próximo ciclo...")

    time.sleep(CHECK_INTERVAL)