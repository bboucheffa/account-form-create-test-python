from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from manageData.read_data import ReadData

URL = "https://sendform.nicepage.io/?version=13efcba7-1a49-45a5-9967-c2da8ebdd189&uid=f7bd60f0-34c8-40e3-8e2c-06cc19fcb730"

read_data = ReadData()

def test_homme(driver):
    client = read_data.read_Client("Client1")
    #wait = WebDriverWait(driver, 100)

    driver.get(URL)

    driver.find_element(By.ID, "field-2688").click()
    Select(driver.find_element(By.ID, "select-9648")).select_by_value("FR")

    #breakpoint()
    driver.find_element(By.ID, "email-c6a3").send_keys(client["email"])
    driver.find_element(By.ID, "name-c6a3").send_keys(client["name"])
    driver.find_element(By.ID, "phone-84d9").send_keys(client["phone"])
    driver.find_element(By.ID, "address-be2d").send_keys(client["adresse"])
    driver.find_element(By.ID, "message-c6a3").send_keys(client["message"])

    Select(driver.find_element(By.ID, "select-c283")).select_by_value("mot")

    driver.execute_script(
        "arguments[0].scrollIntoView(true);",
        driver.find_element(By.ID, "checkbox-8214")
    )
    driver.find_element(By.ID, "checkbox-8214").click()

    driver.find_element(By.CSS_SELECTOR, "form a").click()

