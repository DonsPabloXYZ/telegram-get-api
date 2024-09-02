from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import Fore, Style, init
import time
import random
import string
init(autoreset=True)
hitam = Fore.LIGHTBLACK_EX
hijau = Fore.LIGHTGREEN_EX
putih = Fore.LIGHTWHITE_EX
kuning = Fore.LIGHTYELLOW_EX
biru = Fore.LIGHTBLUE_EX
merah = Fore.LIGHTRED_EX
muda = Fore.LIGHTCYAN_EX
reset = Style.RESET_ALL
ungu = Fore.LIGHTMAGENTA_EX
line = putih + "~" * 50

init(autoreset=True)

print(
    f"""
{muda} ++--------------------------------------------++
{kuning}        AUTO GET API_ID & API_HASH TELEGRAM
{muda} ++--------------------------------------------++    
{biru}  ╔╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╗
{biru}  ╟┼┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┼╢
{muda}  ╟┤██████╗  ██████╗ ███╗   ██╗███████╗    ██╗├╢
{muda}  ╟┤██╔══██╗██╔═══██╗████╗  ██║██╔════╝   ██╔╝├╢
{muda}  ╟┤██║  ██║██║   ██║██╔██╗ ██║███████╗  ██╔╝ ├╢
{muda}  ╟┤██║  ██║██║   ██║██║╚██╗██║╚════██║ ██╔╝  ├╢
{muda}  ╟┤██████╔╝╚██████╔╝██║ ╚████║███████║██╔╝██╗├╢
{muda}  ╟┤╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝ ╚═╝├╢
{muda}  ╟┼┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┼╢
{biru}  ╚╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╝
{muda} ++--------------------------------------------++
{kuning}              FREE NOT FOR SALE !!
{muda} ++--------------------------------------------++ 
""")

CHROME_DRIVER_PATH = "C:/cromed/chrome-win32/chromedriver.exe"  # Ganti dengan path yang benar

def generate_random_string(length=10):
    """Generate a random string of fixed length."""
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--log-level=3')  # Set log level to ERROR
chrome_options.add_argument('--disable-gpu')  # Optional: Disable GPU acceleration

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
chrome_options.add_argument(f'user-agent={USER_AGENT}')

service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    print(Fore.CYAN + Style.BRIGHT + "Proses Get API_ID & API_HASH...")
    driver.get("https://my.telegram.org/auth")

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#my_login_phone"))
    )

    PHONE_NUMBER = input(Fore.YELLOW + "Input Your Phone Number (With Country Code. Ex +628xx): ")
    
    phone_input = driver.find_element(By.CSS_SELECTOR, "#my_login_phone")
    phone_input.send_keys(PHONE_NUMBER)

    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#my_send_form > div.support_submit > button"))
    ).click()

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#my_password"))
    )

    PASSWORD = input(Fore.YELLOW + "Input Your OTP: ")
    password_input = driver.find_element(By.CSS_SELECTOR, "#my_password")
    password_input.send_keys(PASSWORD)

    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#my_login_form > div.support_submit > button"))
    ).click()

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.tl_page_wrap > div.container.tl_page_container > div > div > div > div > div.col-md-8 > div > ul > li:nth-child(1) > a"))
    )

    element_to_click = driver.find_element(By.CSS_SELECTOR, "body > div.tl_page_wrap > div.container.tl_page_container > div > div > div > div > div.col-md-8 > div > ul > li:nth-child(1) > a")
    element_to_click.click()

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#app_title"))
    )

    app_title_input = driver.find_element(By.CSS_SELECTOR, "#app_title")
    app_title_input.send_keys(generate_random_string())

    app_shortname_input = driver.find_element(By.CSS_SELECTOR, "#app_shortname")
    app_shortname_input.send_keys(generate_random_string())

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#app_create_form > div:nth-child(6) > div > div:nth-child(1)"))
    )
    
    div_to_click = driver.find_element(By.CSS_SELECTOR, "#app_create_form > div:nth-child(6) > div > div:nth-child(1)")
    div_to_click.click()

    app_desc_input = driver.find_element(By.CSS_SELECTOR, "#app_desc")
    app_desc_input.send_keys(generate_random_string(50))  # Mengisi deskripsi dengan 50 karakter acak

    save_button = driver.find_element(By.CSS_SELECTOR, "#app_save_btn")
    save_button.click()

    time.sleep(5)

    api_id_element = driver.find_element(By.CSS_SELECTOR, "#app_edit_form > div:nth-child(3) > div.col-md-7 > span")
    api_id = api_id_element.text

    api_hash_element = driver.find_element(By.CSS_SELECTOR, "#app_edit_form > div:nth-child(4) > div.col-md-7 > span")
    api_hash = api_hash_element.text

    with open("data.txt", "w") as file:
        file.write(f"ACCOUNT INFO : {PHONE_NUMBER}\n")
        file.write(f"API_ID : {api_id}\n")
        file.write(f"API_HASH : {api_hash}\n")

    print(Fore.GREEN + Style.BRIGHT + "The information has been saved in data.txt")

except Exception as e:
    print(Fore.RED + Style.BRIGHT + f"Eror: {e}")

finally:
    driver.quit()
