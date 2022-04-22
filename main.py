from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pandas
driver_path = r"C:\\Users\\RAGA\\Downloads\\Compressed\\chromedriver.exe"
option = webdriver.ChromeOptions()
option.add_argument('--ignore-certificate-errors')
option.add_argument('--ignore-ssl-errors')
nlp = []

driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/fvpht9808-basic-of-python-programming")
n = int(286 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
el = driver.find_elements_by_class_name('commentWidh')
for a in el:
    nlp.append(a.text)
driver.quit()


driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/fvrprg101-programming-basics-concepts")
n = int(372 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
ell = driver.find_elements_by_class_name('commentWidh')
for a in ell:
    nlp.append(a.text)
driver.quit()

driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/fvgit9609-git-github-gitlab")
n = int(254 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()


driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/fvxl95051-microsoft-office-excel")
n = int(360 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()


driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/fvcp9504-c-plus-plus-programming")
n = int(293 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()


driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/fvh4c94062-basic-of-web-design-using-html")
n = int(207 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()


driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/fvlng9601-german-language-from-alphabet-to-level-b1")
n = int(122 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()


driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/fvrj101-java-programming")
n = int(266 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()


driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/mvrma92021-matlab-programming")
n = int(111 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()


driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/fvmec93031-basic-of-solidworks")
n = int(118 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()


driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/fvrc101-c-programming")
n = int(222 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()


driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/fvrphp101-php-programming")
n = int(190 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()


driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/mvrma92021-matlab-programming")
n = int(111 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()


driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/fvand9406-basic-android-programming")
n = int(155 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()


driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/fvcs9311-c-sharp-video-tutorials-pack")
n = int(137 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()

driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/fvcs9311-c-sharp-video-tutorials-pack")
n = int(137 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()

driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/fvfn9807-basic-of-oscillation-in-financial-markets")
n = int(134 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()

driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/fvfn9704-technical-analysis-of-tradings-based-on-indicator-charts-and-price")
n = int(149 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()

driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/fvfn9705-querying-in-stock-market-and-tools-for-identifying-highly-yield-shares")
n = int(163 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()

driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/fvacw98101-supplementary-of-technical-analysis-using-ichimoku")
n = int(182 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()

driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/fvfn98051-basic-of-robert-miners-strategy-for-trading-in-financial-markets")
n = int(117 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()


driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/fvtifn9704-basic-of-technical-analysis-in-financial-market")
n = int(133 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()


driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/fvtior9709-basic-of-elliot-waves-in-technical-analysis")
n = int(91 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()


driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/fvmng96113-introduction-to-meta-trader-technical-analysis-tool-for-stocks")
n = int(102 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()


driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/fvsft105-database")
n = int(94 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()

driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/fvds9402-data-structures")
n = int(116 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()

driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/fvml9606-machine-learning-using-python")
n = int(101 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()


driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/mvrnn9102-neural-networks-in-matlab-video-tutorials-pack")
n = int(137 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()

driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/fvmth109-mathematics-i-problem-solving")
n = int(139 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()

driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/fvwp9705-basic-of-wordpress")
n = int(129 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()

driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/fvmsp9803-microsoft-project-2019")
n = int(107 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()

driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/fvwd9411-ms-word-2016")
n = int(97 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()


driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/fvlng9601-german-language-from-alphabet-to-level-b1")
n = int(122 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()

driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/fvatcd9408-2d-drawings-using-autocad")
n = int(90 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()

driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/fvtyp9403-typing-with-10-fingers")
n = int(155 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()

driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/fvsft1092-algorithm-design")
n = int(82 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()

driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/fvdm9406-machine-learning-in-python-first-part")
n = int(95 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()

driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/fvee110-electrical-circuits-i")
n = int(83 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()

driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/fvacw9707-increasing-concentration-and-improving-memory")
n = int(91 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()

driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/fvnet9410-network-plus")
n = int(115 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()

driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/fvcp95042-advanced-c-plus-pluc-object-oriented-programming")
n = int(77 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()

driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/fvxl9606-excel-management-dashboards")
n = int(83 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()

driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/fvacw98101-supplementary-of-technical-analysis-using-ichimoku")
n = int(182 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()

driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/fvacw98032-basic-of-technical-analysis-using-ichimoku-method")
n = int(196 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()

driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/fvcs9311-c-sharp-video-tutorials-pack")
n = int(137 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()

driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/fvrd9311-basic-arduino-programming")
n = int(88 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()

driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/fvtifn9704-basic-of-technical-analysis-in-financial-market")
n = int(133 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()

driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/fvfn9704-technical-analysis-of-tradings-based-on-indicator-charts-and-price")
n = int(149 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()

driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/mvrga9011-genetic-algorithm-video-tutorials-pack")
n = int(129 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()

driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/fvfn9807-basic-of-oscillation-in-financial-markets")
n = int(134 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()

driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/mvrnn9102-neural-networks-in-matlab-video-tutorials-pack")
n = int(137 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()

driver = webdriver.Chrome(driver_path, chrome_options=option)
driver.get("https://faradars.org/courses/fvfn98051-basic-of-robert-miners-strategy-for-trading-in-financial-markets")
n = int(117 / 10)
for i in range(n):
    # more = driver.find_element_by_class_name('comments .btn-primary')
    # more.click()
    more = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,'//*[(@id = "comments")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]')))
    more.click()
elll = driver.find_elements_by_class_name('commentWidh')
for a in elll:
    nlp.append(a.text)
driver.quit()


data = pandas.DataFrame(nlp)
data.to_excel('output.xlsx')
