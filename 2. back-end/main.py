# Inclui arquivo 'resources.py'
import resources
# Lib para reproducao de testes
import unittest

if __name__ == "__main__":
    # Instancia classe de servico da entidade Resource e solicita o id a buscar
    service = resources.ResourceService()
    resource_id = input("Digite o ID do recurso que deseja buscar: ")
    resource = service.get_response(resource_id)

    # Exibe o JSON retornado na busca do recurso em um dicionario
    print("Dados do recurso: "+str(service.print_response(resource)))

    # Executa requisicao da criacao de recurso (de item II)
    new_resource = service.post_request()
    
    print("Executando os testes...")
    class TestMethods(unittest.TestCase):
        def test_get_valid_resource(self):
            # Valida se recurso foi encontrado (de item I)
            self.assertIsNotNone(resource)

        def test_resource_has_minimal_properties_filled(self):
            parameters = ['id', 'title', 'body']        
            # Valida se propriedades exclusivas do recurso foram retornadas    
            for prop in parameters:
                self.assertTrue(hasattr(resource, prop))

        def test_resource_properties_are_not_empty(self):
            # Valida se propriedades do recurso possuem algum valor
            self.assertNotEqual(resource.user_id, '')
            self.assertNotEqual(resource.id, '')
            self.assertNotEqual(resource.title, '')
            self.assertNotEqual(resource.body, '')

        def test_created_resource_id(self):
            print("Recurso enviado: "+str(new_resource))
            # Valida se retorno contem id unico (de item III)
            unique_resource_id = list(new_resource.keys()).count('id')
            self.assertTrue(unique_resource_id, 1)

# Dispara classe de testes
unittest.main()
