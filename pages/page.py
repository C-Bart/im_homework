from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

from locators.symptomate_locator import SymptomateLocator


class BasePage(object):
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def accept_cookies_policy(self):
        cookies_policy = self.driver.find_element_by_id("cky-btn-accept")
        if cookies_policy:
            cookies_policy.click()


class SymptomatePage(BasePage):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.url = "https://symptomate.com/{}/diagnosis/"

    def open(self, language='pl'):
        self.driver.get(self.url.format(language))
        self.accept_cookies_policy()

    def change_language(self, language):
        language_dropdown = self.driver.find_element(*SymptomateLocator.LANGUAGE_DROPDOWN)
        action = ActionChains(self.driver)
        action.move_to_element(language_dropdown).perform()
        self.wait.until(EC.element_to_be_clickable((
            SymptomateLocator.SELECTED_LANGUAGE[0],
            SymptomateLocator.SELECTED_LANGUAGE[1].format(language)))
        ).click()
        self.wait.until(EC.visibility_of_element_located(SymptomateLocator.FOOTER))

    def is_correct_language(self, expected_language):
        html = self.driver.find_element(*SymptomateLocator.HTML)
        assert html.get_attribute("lang") == expected_language
        url = self.driver.current_url.split('/')
        assert url[3] == expected_language
        assert self._get_active_language().get_attribute("data-lang-code") == expected_language

    def _get_active_language(self):
        return self.wait.until(EC.presence_of_element_located(SymptomateLocator.ACTIVE_LANGUAGE))
