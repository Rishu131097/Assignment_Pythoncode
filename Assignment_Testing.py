import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#Launch the chrome Browser
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

# Navigate to the FitPeo Homepage
driver.get('https://www.fitpeo.com/')
time.sleep(2) # Wait for the page to load
driver.maximize_window()
time.sleep(2)

# Navigate to the Revenue Calculator Page
Revenue_Calculator = driver.find_element(By.XPATH, '//div[text()="Revenue Calculator"]')
Revenue_Calculator.click()
time.sleep(2)

# Scroll Down to the Slider section
slider = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, "//h4[text()='Medicare Eligible Patients']"))  # Adjust as per the slider's actual ID or locator
    )
driver.execute_script("arguments[0].scrollIntoView();", slider)

slider_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[2]/div/div/span[1]/span[3]")
time.sleep(5)
# Adjust the Slider

ActionChains(driver).drag_and_drop_by_offset(slider_element,94,0).perform()
time.sleep(4)
text_field = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'MuiInputBase-root') and contains(@class, 'MuiOutlinedInput-root') and contains(@class, 'css-129j43u')]//input[@id=':r0:' and @type='number']")))
time.sleep(1)
for _ in range(5):
    text_field.send_keys(Keys.BACKSPACE)
time.sleep(4)

#Update the Text Field

input_value ="560"
text_field.send_keys(input_value)
time.sleep(3)
#Validate Part
#WebDriverWait(driver, 100).until(EC.text_to_be_present_in_element_value((By.XPATH, "//div[contains(@class, 'MuiInputBase-root') and contains(@class, 'MuiOutlinedInput-root') and contains(@class, 'css-129j43u')]//input[@id=':r0:' and @type='number']"), "820"))
slider_value = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//p[text()="560"]')))
slider_value_text = slider_value.text
#Validate Slider Value
print(f" slider value: {slider_value_text}")

# Scroll Down furthur to CPT
cpt_section = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, "//p[text()='CPT-99091']"))  # Adjust as per the slider's actual ID or locator
    )
driver.execute_script("arguments[0].scrollIntoView();", cpt_section)

cpt_99091 = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[1]/label/span[1]/input")
cpt_99091.click()
cpt_99453 = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/label/span[1]/input")
cpt_99453.click()
cpt_99454 = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[3]/label/span[1]/input")
cpt_99454.click()
cpt_99474 = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[8]/label/span[1]/input")
cpt_99474.click()

for _ in range(5):
    text_field.send_keys(Keys.BACKSPACE)
time.sleep(4)
input_value ="820"
text_field.send_keys(input_value)
time.sleep(10)
# 8. Validate Total Recurring Reimbursement
# Verify that the total recurring reimbursement is displayed correctly
reimbursement_header =  WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/header/div/p[4]/p"))) # Replace with the correct element ID or selector
assert reimbursement_header.text == "$110700", f"Expected total reimbursement to be $110700 but got {reimbursement_header.text}"