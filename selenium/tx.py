from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import socket

phone = [5511975512897]


try:
    st = open("conversas/conversa.txt",'r')
    message_text=st.read() # message
except Exception as e:
    print("Erro ao Abri o Arquivo")
    exit()



driver = webdriver.Chrome(executable_path="chromedriver.exe")
sleep(2)
driver.get("http://web.whatsapp.com")


def send_whatsapp_msg(phone,text):
    driver.get("https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no))
    try:
       driver.switch_to_alert().accept()
    except Exception as e:
       pass


def reconect():
    try:
        socket.setdefaulttimeout(10)
        timeout = socket.getdefaulttimeout()
        print("System has default timeout of {0} for create_connection".format(timeout))
        socketInstance = socket.create_connection(("www.google.com",35491))
    except Exception as e:
        reconect()

    try:
        element_presence(By.XPATH,'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]',30)
        txt_box=driver.find_element(By.XPATH , '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        global no_of_message
        for x in range(no_of_message):
            txt_box.send_keys(text)
            txt_box.send_keys("\n")

    except Exception as e:
        print("invailid phone no :"+str(phone_no))


while len(phone):
  try:
     send_whatsapp_msg(phone,message_text)
  except:
     reconect()
