from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time, pyautogui, os, csv, datetime
import pandas as pd


chrome_options = Options()
chrome_options.add_argument("--kiosk-printing")
driver = webdriver.Chrome(chrome_options)
driver.get("https://data.castoredc.com")
time.sleep(60)
os.chdir('path')
n = 0
today = datetime.date.today()
today = str(today)
study_id = 'study_id' 
with open('file.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
                n=n+1
                file_name=(str(row[0]))
                URL = "https://data.castoredc.com/print-multiple-crf-instance/"+study_id+"?withHelpText=0&withAdditionalInfo=0&includeCalculationTemplates=0&includeHiddenCalculationFields=0&stepsOnSeparatePages=1&shouldPrintAllOptions=0&recordInfo=[{%22recordId%22:%22"+str(row[0])+"%22}]"
                if n>1:
                        print(URL)
                        print(n)
                        driver.get(URL)
                        time.sleep(10)
                        pyautogui.typewrite(str(file_name))
                        pyautogui.press('enter')
                        time.sleep(15)

time.sleep(10)
driver.quit()
file_names = [f for f in os.listdir('path') if os.path.isfile(os.path.join('path', f))]
df = pd.DataFrame(file_names, columns=['File Name'])
csv_df = pd.read_csv('C:/Users/MauricioAguirreMoral/Desktop/New folder/file.csv')
folder_path = 'C:/Users/MauricioAguirreMoral/Desktop/New folder'
folder_filenames = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
file_names = [file.replace('.pdf', '') for file in file_names]
folder_filenames = [file.replace('.pdf', '') for file in folder_filenames]
csv_filenames = csv_df['record_id'].tolist()
csv_filenames = [str(element) for element in csv_filenames]
folder_filenames = [str(element) for element in folder_filenames]
print(csv_filenames)
print(folder_filenames)
files_in_csv_not_in_folder = set(csv_filenames) - set(folder_filenames)
files_in_csv_not_in_folder = list(files_in_csv_not_in_folder)
files_in_csv_not_in_folder = pd.DataFrame(files_in_csv_not_in_folder, columns=['record_id'])
files_in_csv_not_in_folder.to_csv('missing.csv', index=False)
df.to_csv('done.csv', index=False)
