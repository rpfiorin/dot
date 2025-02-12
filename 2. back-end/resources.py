# Lib para requsicoes em API
import requests
# Lib para valores aleatorios
from faker import Faker

class Resource:
    # Construtor com atributos da entidade
    def __init__(self, user_id, id, title, body):
        self.user_id = user_id
        self.id = id
        self.title = title
        self.body = body

class ResourceService:
    def get_response(self, typed_id):
        # Valida entrada do usuario
        if (typed_id == ''):
            raise ValueError("O ID não foi digitado!")
        
        # Apos validado, chama endpoint, interpolando id do recurso (de item I)
        url = f"https://jsonplaceholder.typicode.com/posts/{typed_id}"
        response = requests.get(url)

        if (response.status_code == 200):
            # Se obtiver sucesso, popula as propriedades JSON nos atributos
            data = response.json()

            if (int(data["userId"]) is None):
                # Trata se fkey estiver sem valor
                user_id = "null"
                id = int(data["id"])
                title = data["title"]
                body = data["body"]
            else:
                user_id = int(data["userId"])
                id = int(data["id"])
                title = data["title"]
                body = data["body"]

            # Cria instancia de Resource passando o body retornado
            return Resource(user_id, id, title, body)
        else:
            return None

    def print_response(self, resource: Resource) -> dict:
        try:
            dictionary = resource.__dict__
            
            return dictionary  
        except:
            # Trata exception se nao for possivel converter o recurso em dict
            raise TypeError("Erro ao converter o retorno da requisição!\n"+
                            "Verifique se o recurso existe e tente novamente.")
        
    def post_request(self) -> object:
        fake = Faker()

        # Gera massa de teste aleatoria (de item II)
        f_title = fake.sentence()
        f_body = fake.text()
        f_user_id = fake.random.randint(1,10)
        
        # Atribui massa gerada a um objeto
        resource_obj = {
            "title": f_title,
            "body": f_body,
            "userId": f_user_id
        }

        url = f"https://jsonplaceholder.typicode.com/posts"
        # Envia requisicao passando objeto criado como payload
        response = requests.post(url, json=resource_obj)

        if (response.status_code == 201):
            # Trata resultado da postagem
            data = response.json()
            return data
        else:
            response.raise_for_status()
            
