from selenium.webdriver.common.by import By


class SymptomateLocator:
    LANGUAGE_DROPDOWN = (By.XPATH, "//div[contains(@class,'language-dropdown')]")
    SELECTED_LANGUAGE = (By.XPATH, "//div[contains(@class,'language-dropdown')]//a[@data-lang-code='{}']")
    FOOTER = (By.CLASS_NAME, "footer-links")
    ACTIVE_LANGUAGE = (By.XPATH, "//div[contains(@class,'language-dropdown')]//a[contains(@class,'active')]")
    HTML = (By.TAG_NAME, "html")
