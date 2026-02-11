import requests # Se der erro aqui, rode: pip install requests
import time
import random

# O endereço que apareceu no seu terminal do C#
URL_API = "http://localhost:5105/api/eventos"

cores = ["Vermelho", "Verde", "Amarelo"]
cameras = ["CAM_ENTRADA_01", "CAM_SAIDA_02"]

def enviar_deteccao():
    # Simulando os dados que o seu grupo vai gerar
    dados = {
        "cameraId": random.choice(cameras),
        "color": random.choice(cores)
    }

    print(f" tentando enviar: {dados}...")

    try:
        # Envia o POST para o seu Controller C#
        response = requests.post(URL_API, json=dados)
        
        if response.status_code == 200:
            print(" Sucesso! O C# recebeu e salvou no SQLite.")
        else:
            print(f" Erro {response.status_code}: {response.text}")
            
    except Exception as e:
        print(f" Erro de conexão: Verifique se o C# está rodando! \n{e}")

# Simular 5 detecções
for i in range(5):
    enviar_deteccao()
    time.sleep(2) # Espera 2 segundos entre um envio e outro