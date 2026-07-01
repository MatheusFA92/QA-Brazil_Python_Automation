from html.parser import commentclose

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

class UrbanRoutesPage:

        #Seção De e Para

        FROM_FIELD = (By.ID, 'from')
        TO_FIELD = (By.ID, 'to')

        #LOCALIZADORES - Solicitação de táxi

        CALL_A_TAXI_BUTTON = (By.XPATH, '//button[text()="Chamar um táxi"]')

        #LOCALIZADORES - Tarifas

        COMFORT_TARIFF_OPTION = (By.XPATH, '//div[@class=tcard-title" and text()="Comfort"]')
        CURRENT_TARIFF        = (By.XPATH, '//div[@class="tcard active"]//div[@class=tcard-title"]')

        #LOCALIZADORES - Telefone

        ADD_PHONE_NUMBER_MAIN_BUTTON = (By.XPATH, '//div[@class="np-button"]//div[contains(text(), "Número de telefone")]')
        PHONE_NUMBER_INPUT_FIELD     = (By.ID,    'phone')
        PHONE_NUMBER_NEXT_BUTTON     = (By.XPATH, '//button[text()="Próximo"]')
        PHONE_CODE_FIELD             = (By.ID,    'code')
        PHONE_NUMBER_CONFIRM_BUTTON  = (By.XPATH, '//button[contains(text(), "Confirmar")]')
        REGISTERED_PHONE_NUMBER      = (By.XPATH, '//div[@contains(@class, "np-text")]')

        def __init__(self, driver):
            self.driver = driver
            self.wait = WebDriverWait(driver, 10)

        # Metodos COR POM

        def _find(self, locator):
                return self.wait.until(EC.visibility_of_element_located(locator))

        def _click(self, locator):
                self.wait.until(EC.element_to_be_clickable(locator)).click()

        def _type(self, locator, text):
                element = self._find(locator)
                element.clear()
                element.send_keys(text)

        # Endereço

        def _get_text(self, locator):
                return self._find(locator).text

        def _get_value(self, locator):
                return self._find(locator).get_attribute('value')

        def enter_locations(self, from_text, to_text):
                self._type(self.from_field, from_text)
                self._type(self.to_field, to_text)

        def get_from_location(self):
                return self._get_value(self.from_field)

        def get_to_location(self):
                return self._get_value(self.to_field)

        #Chamar táxi

        def click_taxi_option(self):
                self.driver.find_element(*self.TAXI_OPTION).click()

        def click_icon_comfort_selected(self):
                self.driver.find_element(*self.COMFORT_ICON).click()

        def is_comfort_icon_active(self):
                try:
                        active_button = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((self.COMFORT_ACTIVE)))
                        return "active" in active_button.get_attribute("class")
                except:
                        return False

