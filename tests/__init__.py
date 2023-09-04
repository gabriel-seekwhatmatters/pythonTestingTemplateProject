import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(executable_path='C:/Users/filip/PycharmProjects/pythonTestingTemplateProject/browsers/chromedriver.exe')

# Open Google in the web browser
driver.get("https://www.google.com")
time.sleep(400)
# Find the search input element by name attribute (in this case, "q" for the search box)
search_box = driver.find_element_by_name("q")

# Enter a search keyword (e.g., "Selenium testing") into the search box
search_box.send_keys("Selenium testing")

# Simulate pressing the "Enter" key to perform the search
search_box.send_keys(Keys.RETURN)

# Wait for a few seconds to allow search results to load (you can adjust the time as needed)
driver.implicitly_wait(5)

# Print the title of the search results page
print("Title of the search results page:", driver.title)

# Optionally, you can capture a screenshot of the page
# driver.save_screenshot("screenshot.png")

# Close the web browser
driver.quit()
