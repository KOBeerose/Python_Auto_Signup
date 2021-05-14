import time
import string
from datetime import datetime, timedelta
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.support.ui import Select



# !!!!! this script is meant to work on Treehouse website but you can make changes use it with another one !!!! 

# define the start and the end date of the free trial  
sdate = (datetime.now()).strftime('%d/%m/%Y')
edate = (datetime.now() + timedelta(days=7) ).strftime('%d/%m/%Y')


# string containting the number of the week 
week_label=str(int(sdate[0:2])%7+int(int(sdate[0:2])/7)) 
# string containting the number of the month
month_label=str(int(sdate[3:5]))

label=week_label+month_label # we use this variable to label the created account using the week and month numbers


# this function gets the user info and save them in variables
def get_info(filename): 
    elem_list=["url","email","firstname","lastname","password","card","zip","cvv","exp"]   # list of expressions preceding the user info
    with open(filename, 'r') as read_obj: 
            for line in read_obj:
                for elem in elem_list:  # Get the value after an expression occurrence
                    if elem in line:
                        globals()[elem] = line.partition(elem+": ")[2].translate({ord(c): None for c in string.whitespace})   # save the value in a variable named according to the expression preceding it



# this function will add new lines the top of a file
def add_at_top(filename, lines): 
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(lines.rstrip('\r\n') + '\n' + content + '\n')


# getting values of the user information
get_info("Info.txt")

u_mail= label+email # !important: adding the label to the start of the prefixed email to make it unique each week
u_fname= firstname
u_lname= lastname
u_password= label+password # Optional: adding the same label to the start of the prefixed password 
u_card= card
u_zp= zip
u_cvv= cvv
u_card_month=int(exp[:2])
u_card_year=int(exp[3:])-20


# configuration and direction to the website URL 
options = EdgeOptions()
options.use_chromium= True
driver = Edge(options=options)
driver.get(url)




# entering user's email and clicking the join now button
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
sel1.select_by_index(u_card_month)

sel2 = Select(driver.find_element_by_xpath("//select[@name='credit_card_year']"))
sel2.select_by_index(u_card_year)

l2= driver.find_element_by_xpath("//div[@class='form-footer']")
driver.execute_script("arguments[0].scrollIntoView(true);", l2)
time.sleep(0.4)

outside = driver.find_element_by_name("commit")
outside.click()

# wait for the page to refresh and add the account to the file Account if the sign_up process was successful
time.sleep(2)
if (driver.current_url=="https://teamtreehouse.com/welcome"):
    add_at_top("Accounts.txt", "from " + sdate + " to " + edate + "\nemail: " + u_mail + "\npassword: " + u_password + "\n \n")