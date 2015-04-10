import selenium
from selenium.webdriver.support.ui import WebDriverWait
from random import randint
import time
from bs4 import BeautifulSoup
from AI import AI

URL = "http://play.pokemonshowdown.com"
team_file = "team.txt"
username = "LookAtMeImSoRandom"
password = ""

CHOOSE_NAME_BUTTON_PATH = '//*[@id="header"]/div[3]/button[1]'
USERNAME_INPUT_PATH = '/html/body/div[4]/div/form/p[1]/label/input'
ENTER_NAME_BUTTON_PATH = '/html/body/div[4]/div/form/p[2]/button[1]'
CANCEL_BUTTON_PATH = '/html/body/div[4]/div/form/p[2]/button[2]'
TIER_SELECT_PATH = '//*[@id="mainmenu"]/div/div[1]/div[2]/div[1]/form/p[1]/button'
OU_OPTION_PATH = '/html/body/div[5]/ul[1]/li[4]/button'
BATTLE_BUTTON_PATH = '//*[@id="mainmenu"]/div/div[1]/div[2]/div[1]/form/p[3]/button/strong'

TEAMBUILDER_BUTTON_PATH = '//*[@id="mainmenu"]/div/div[1]/div[2]/div[2]/p[1]/button'
NEW_TEAM_BUTTON_PATH = '/html/body/div[4]/div/ul/li[2]/button'
IMPORT_BUTTON_PATH = '/html/body/div[4]/div[1]/button[2]'
TEAM_IMPORT_PATH = '/html/body/div[4]/textarea'
SAVE_BUTTON_PATH = '/html/body/div[4]/div/button[3]'
HOME_BUTTON_PATH = '//*[@id="header"]/div[2]/div/ul[1]/li[1]/a'

MOVE_PATH = '/html/body/div[5]/div[5]/div/div[2]/div[2]/button[%d]' 
ONE_OPTION_MOVE_PATH = '/html/body/div[5]/div[5]/div/div[2]/div[2]/button' # ex: bounce
SWITCH_PATH = '/html/body/div[4]/div[5]/div/div[3]/div[2]/button[%d]'
SWITCH_AFTER_FAINT_PATH = '/html/body/div[4]/div[5]/div/div[2]/div[2]/button[%d]/span[2]/span'
MAIN_MENU_PATH = '/html/body/div[5]/div[5]/div/p[2]/em/button[1]'

LEAD_SELECT_PATH = '/html/body/div[5]/div[5]/div/div[2]/div[2]/button[%d]'

if __name__ == "__main__":
	# username = raw_input("Username: ")
	# tier = raw_input("Tier: ")
	team_data = open(team_file, 'r').read()
	player = AI(team_data)
	player.calculate_value()
	driver = selenium.webdriver.Chrome()
	driver.get(URL)
	time.sleep(5) # give the page some time to load
	choose_name_button = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(CHOOSE_NAME_BUTTON_PATH))
	choose_name_button.click()
	
	username_input_field = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(USERNAME_INPUT_PATH))
	input_button = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(ENTER_NAME_BUTTON_PATH))
	username_input_field.send_keys(username)
	input_button.click()

	try: # sometimes it clicks too fast and the box will pop up again
		cancel_button = WebDriverWait(driver, 1).until(lambda driver: driver.find_element_by_xpath(ENTER_NAME_BUTTON_PATH))
		cancel_button.click()
	except selenium.common.exceptions.TimeoutException:
		pass 
	
	# team builder
	teambuilder_button = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(TEAMBUILDER_BUTTON_PATH))
	teambuilder_button.click()
	new_team_button = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(NEW_TEAM_BUTTON_PATH))
	new_team_button.click()
	import_button = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(IMPORT_BUTTON_PATH))
	import_button.click()
	team_input_field = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(TEAM_IMPORT_PATH))
	save_button = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(SAVE_BUTTON_PATH))
	home_button = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(HOME_BUTTON_PATH))
	team_input_field.send_keys(team_data)
	save_button.click()
	home_button.click()
	
	tier_select_button = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(TIER_SELECT_PATH))
	tier_select_button.click()
	ou_option = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(OU_OPTION_PATH))
	ou_option.click()
	while True:
		battle_button = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(BATTLE_BUTTON_PATH))
		battle_button.click()
	
		soup = BeautifulSoup(driver.page_source)
		source = soup.findAll(attrs={'class' : 'battle-log'})
		
		player = AI(team_data, source)
		
		i = 1
		lead_button = WebDriverWait(driver, 150).until(lambda driver: driver.find_element_by_xpath(LEAD_SELECT_PATH % i))
		lead_button.click()
		i += 1
		while True:
			soup = BeautifulSoup(driver.page_source)
			
			choice = randint(1, 4)
			attack_button = WebDriverWait(driver, 360).until(lambda driver: driver.find_element_by_xpath(MOVE_PATH % choice))
			try:
				attack_button.click()
			except selenium.common.exceptions.WebDriverException:
				i+= 1
				send_button = WebDriverWait(driver, 1).until(lambda driver: driver.find_element_by_xpath(SWITCH_AFTER_FAINT_PATH % i))
				send_button.click()
	
			try:
				main_menu_button = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(MAIN_MENU_PATH))
				main_menu_button.click()
				break
			except selenium.common.exceptions.WebDriverException:
				pass
