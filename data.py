# optional code which can be modified to scrape data from wikipedia or any website
# import pandas as pd
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time
#
#
# chrome_driver_path = "C:/Users/gb/Documents/chromedriver.exe"
# driver_service = Service(executable_path=chrome_driver_path)
#
#
# class Players:
#
#     def __init__(self):
#
#         self.driver = webdriver.Chrome(service=driver_service)
#         self.driver.maximize_window()
#         self.site = "https://en.wikipedia.org/wiki/List_of_Chelsea_F.C._players"
#         self.driver.get(self.site)
#
#         self.players = []
#         self.nationalities = []
#         self.positions = []
#         self.career_years = []
#         self.appearances = []
#         self.goals = []
#
#     def get_details(self):
#         time.sleep(2)
#         players = self.driver.find_elements(by=By.CSS_SELECTOR, value=".jquery-tablesorter th")
#         for player in players:
#             self.players.append(player.text)
#
#         print(self.players)



        # other_attributes = self.driver.find_elements(by=By.CSS_SELECTOR, value=".jquery-tablesorter td")
        # for nationality in nationalities:
        #     self.nationalities.append(nationality.text)
        #
        # positions = self.driver.find_elements(by=By.CSS_SELECTOR, value=".core")
        # for position in positions:
        #     self.positions.append(position.text)
        #
        #
        # career = self.driver.find_elements(by=By.CSS_SELECTOR, value=".name")
        # for year in career:
        #     self.career_years.append(year.text)
        #
        # appearances = self.driver.find_elements(by=By.CSS_SELECTOR, value=".prc")
        # for appearance in appearances:
        #     self.appearances.append(appearance.text)
        #
        # goals = self.driver.find_elements(by=By.CSS_SELECTOR, value=".core")
        # for goal in goals:
        #     self.goals.append(goal.text)
        # time.sleep(3)

#     def click_button(self):
#         nxt_button = self.driver.find_element(by=By.XPATH, value='//*[@id="jm"]/main/div[2]/div[3]/section/div[2]/a[6]')
#         # nxt_button.click()
#         self.driver.execute_script("arguments[0].click();", nxt_button)
#         time.sleep(2)
#
#
# start_time = time.perf_counter()
# player_data = Players()
#
# player_data.get_details()

# print(scrape.spec)
# print(scrape.price)
# print(scrape.product_link)

# a = []
# for i in range(len(player_data.players)):
#     a.append((player_data.players[i], player_data.nationalities[i], player_data.positions[i],
#               player_data.career_years[i], player_data.appearances[i], player_data.goals[i]))


# df = pd.DataFrame(a, columns=["Player Name", "Nationality", "Position", "Career Years", "Appearances", "Goals"])
#
# new_csv = df.to_csv("players.csv", index=False)
# player_data.driver.quit()
# end_time = time.perf_counter()
#
# time_taken = round(((end_time - start_time) / 60), 2)
# print("Completed in", time_taken, "minutes")
