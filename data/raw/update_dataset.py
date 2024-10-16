import requests

#Função para buscar o dataset da página original. 

def download_dataset(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verificar se houve um erro na requisição

        with open(filename, 'wb') as file:
            file.write(response.content)
        
        print(f"Dataset atualizado: {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar o dataset: {e}")

if __name__ == "__main__":
    dataset_url = "https://raw.githubusercontent.com/atlantico-academy/datasets/refs/heads/main/diamonds.csv"
    local_filename = "/mnt/c/Users/Isabel/Documents/bootcamp_CDD/avanti-bootcamp-cdd/data/raw/diamonds.csv"
    
    download_dataset(dataset_url, local_filename)