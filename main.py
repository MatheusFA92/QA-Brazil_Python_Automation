import data
import helpers


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print(
                "Não foi possível conectar ao Urban Routes. "
                "Verifique se o servidor está ligado e ainda em execução."
            )

    def test_set_route(self):
        # Adicionar na Sprint S8
        pass
        print("função criada para definir a rota")

    def test_select_plan(self):
        # Adicionar na Sprint S8
        pass
        print("função criada para selecionar o plano")

    def test_fill_phone_number(self):
        # Adicionar na Sprint S8
        pass
        print("função criada para preencher o número de telefone")

    def test_fill_card(self):
        # Adicionar na Sprint S8
        pass
        print("função criada para preencher os dados do cartão")

    def test_comment_for_driver(self):
        # Adicionar na Sprint S8
        pass
        print("função criada para adicionar comentário ao motorista")

    def test_order_blanket_and_handkerchiefs(self):
        # Adicionar na Sprint S8
        pass
        print("função criada para solicitar cobertor e guardanapos")

    def test_order_2_ice_creams(self):
        numbers_of_ice_creams = 2

        for count in range(numbers_of_ice_creams):
            #Adicionar na Sprint S8
            print("função criada para pedir quantidade de sorvetes")
        pass

    def test_car_search_model_appears(self):
        # Adicionar na Sprint S8
        print("função criada para verificar o modelo do carro")
        pass

    def test_add_2_ice_creams(self):
        number_of_ice_creams = 2

        for count in range(number_of_ice_creams):
            print("função criada para adicionar a quantidade de sorvetes")

        pass