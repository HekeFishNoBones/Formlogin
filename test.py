from python_imagesearch.imagesearch import imagesearch
from python_imagesearch.imagesearch import imagesearch_loop
import pyautogui
import os
from selenium import webdriver
from form_fill import start_au
import subprocess

# Opening VPN
#subprocess.Popen(["C:\\Program Files (x86)\\Cisco\\Cisco AnyConnect Secure Mobility Client\\vpnui.exe"])
def start_vpn(login, password):
    """THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    vpn_screen = os.path.join(THIS_FOLDER, 'ready_to_connect.png')
    image_pos = imagesearch_loop(vpn_screen, 3, 0.9)

    pyautogui.click(image_pos)
    pyautogui.press('enter')

    password_window = os.path.join(THIS_FOLDER, 'password_window.png')
    image_pos = imagesearch_loop(password_window, 3, 0.9)
    pyautogui.write(password)"""

    start_au(login, password)

    return 0
