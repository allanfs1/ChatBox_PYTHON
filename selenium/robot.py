from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import socket
delay = 5

#st = open("conversas/conversa.txt",'w')
#st.write(txt)
try:
    st = open("conversas/conversa.txt",'r')
    message_text=st.read() # message
except Exception as e:
    print("Erro ao Abri o Arquivo")
    exit()


execult=2 # no. of time
moblie_no_list=[5511975512897] # list of phone number


def element_presence(by,xpath,time):
    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)


def is_connected():
    try:
        socket.setdefaulttimeout(100)
        timeout = socket.getdefaulttimeout()
        print("System has default timeout of {0} for create_connection".format(timeout))
        socketInstance = socket.create_connection(("localhost",35491))
        return True
    except :
        is_connected()


driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("http://web.whatsapp.com")
sleep(delay) #wait time to scan the code in second

def send_whatsapp_msg(phone_no,text):
    driver.get("https://web.whatsapp.com/send?phone={0}&source=&data=#".format(phone_no))
    try:
        driver.switch_to_alert().accept()
    except Exception as e:
        pass

    try:
        element_presence(By.XPATH,'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]',30)
        txt_box=driver.find_element(By.XPATH , '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        global execult
        for x in range(execult):
            txt_box.send_keys("Bot-1.0.1:"+text)
            txt_box.send_keys("\n")

    except Exception as e:
        print("Numero de Telefone Invalido:"+str(phone_no))

for moblie_no in moblie_no_list:
    try:
        send_whatsapp_msg(moblie_no,message_text)

    except Exception as e:
        sleep(delay)
        is_connected()
