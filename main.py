import data
import helpers

from pages import UrbanRoutesPage
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities['goog:loggingPrefs'] = {'performance': 'ALL'}
        cls.driver = Chrome()
        cls.driver.implicitly_wait(5)

        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes.")
        else:
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução.")

    def setup_method(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        self.page = UrbanRoutesPage(self.driver)
        self.page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)

    def test_set_route(self):
        assert self.page.get_from_location(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert self.page.get_to_location() == data.ADDRESS_TO


    def test_select_plan(self):
        self.page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.page.click_taxi_option()
        self.page.click_icon_comfort_selected()
        assert self.page.is_comfort_icon_active()


    def test_fill_phone_number(self):
        #Adicionar em S8
        print("funcão criada para definir o número de telefone")
        pass

    def test_fill_card(self):
        # Adicionar em S8
        print("função criada para definir o cartão para pagamento")
        pass

    def test_comment_for_driver(self):
        # Adicionar em S8
        print("função criada para adicionar um comentário ao motorista")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Adicionar em S8
        print("função criada para adicionar cobertor e lenços")
        pass

    def test_order_2_ice_creams(self):
        order_ice_cream = 2
        for count in range(order_ice_cream):
            # Adicionar em S8
            print("função criada para pedir sorvete")
            pass

    def test_car_serarch_model_appears(self):
            # Adicionar em S8
            print("função criada para mostrar o modelo de carro encontrado")
            pass

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()


