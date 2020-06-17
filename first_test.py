import selenium.webdriver as webdriver

# Arrange

# set the driver instance
driver = webdriver.Chrome()

# browse to the endpoint
driver.get("https://docket-test.herokuapp.com/register")

# maximise the window
driver.maximize_window()




# Act
# Complete registration form

# enter username value
driver.find_element_by_id("username").send_keys("Ryan")
# enter email value
driver.find_element_by_id("email").send_keys("Test@email.com")
# enter password value
driver.find_element_by_id("password").send_keys("12345")
# enter repeat password value
driver.find_element_by_id("password2").send_keys("12345")



# click register button
driver.find_element_by_id("submit").click()



# Assert
# confirm registration has been successful

#check if congratulations message contains the correct text
message = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]").text

assert message == "Congratulations, you are now registered!"

# check user is routed to login page
current_url =  driver.current_url

assert current_url == "https://docket-test.herokuapp.com/login"


driver.quit()
