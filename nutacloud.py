from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Inisialisasi driver Chrome
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Buka halaman web
driver.get("https://www.nutacloud.com/authentication/loginv2")

#Test Case Login
# Input Nama Perusahaan
perusahaan_input = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Nama Perusahaan']")
perusahaan_input.send_keys("Rizki'sHouse")

#Input Username
username_input = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Username']")
username_input.send_keys("Rizki Hernawan Wicaksono")

#Input Password
password_input = driver.find_element(By.CSS_SELECTOR, "#input-password")
password_input.send_keys("no123456")

#Klik Login
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

import time
time.sleep(10)  # Menunggu 10 detik sebelum menutup browser

# Cek apakah elemen "Penjualan Hari ini" muncul
penjualan_hari_ini = driver.find_element(By.XPATH, "//span[@id='caption-penjualan-hari-ini']")
penjualan_text = penjualan_hari_ini.text

# Lakukan assertion pada teks elemen
expected_text = "Penjualan Hari ini"  # Ganti dengan teks yang kamu harapkan muncul
assert penjualan_text == expected_text, f"Teks penjualan tidak sesuai: '{penjualan_text}' != '{expected_text}'"

print("Assertion passed: Teks penjualan sesuai.")

driver.quit()
