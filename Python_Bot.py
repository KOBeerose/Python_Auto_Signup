import time
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.support.ui import Select


# !!!!! this script is meant to work on Treehouse website but you can make changes to the class names and ids to use it on another one !!!! 



# \/ \/ \/ \/ \/ \/ \/ \/ \/  values of the user information
 
url="https://teamtreehouse.com/?irgwc=1&click_id=UGR1JzW-VxyLWLMwUx0Mo3EJUkBxKF39Jwrmxs0&iradid=294479&ircid=3944&irpid=10098&iradname=4%20Months%20Off%20Basic%21&iradtype=TEXT_LINK&iradsize=&irmpname=Ziff%20Davis%20-%20Offers.com&irmptype=mediapartner&utm_source=ir&cid=4612"
u_mail= "example@email.ai"
u_fname= "first_name"
u_lname= "last_name"
u_password= "password"
u_card= "card_number"
u_zp= "zip_code"
u_cvv= "cvv"


# configuration and direction to the website URL 
options = EdgeOptions()
options.use_chromium= True
driver = Edge(options=options)
driver.get(url)




# entering user's email and clicking the register button
fmail = driver.find_element_by_name("account_signup[email]")
fmail.send_keys(u_mail)

outside = driver.find_element_by_name("button")
outside.click()


# entering user's info and clicking the submit button
fname = driver.find_element_by_id("account_signup_first_name")
fname.send_keys(u_fname)

lname = driver.find_element_by_id("account_signup_last_name")
lname.send_keys(u_lname)

password = driver.find_element_by_id("account_signup_password")
password.send_keys(u_password)

card = driver.find_element_by_id("credit_card_number")
card.send_keys(u_card)

zp = driver.find_element_by_id("account_signup_postal_code")
zp.send_keys(u_zp)

cvv = driver.find_element_by_id("credit_card_cvv")
cvv.send_keys(u_cvv)

l1= driver.find_element_by_xpath("//fieldset[@id='consent-info']")
driver.execute_script("arguments[0].scrollIntoView(true);", l1)
time.sleep(0.4)

driver.find_element_by_xpath("//label[@class='form-label' and @for='account_signup_tos_consent']/span[@class='form-label-required']").click()
driver.find_element_by_xpath("//p[@class='radio-checkbox-note']").click()

sel1 = Select(driver.find_element_by_xpath("//select[@name='credit_card_month']"))
sel1.select_by_index(9)

sel2 = Select(driver.find_element_by_xpath("//select[@name='credit_card_year']"))
sel2.select_by_index(3)

l2= driver.find_element_by_xpath("//div[@class='form-footer']")
driver.execute_script("arguments[0].scrollIntoView(true);", l2)
time.sleep(0.4)

outside = driver.find_element_by_name("commit")
outside.click()

