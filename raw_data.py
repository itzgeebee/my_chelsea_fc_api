import pandas as pd

player_df = pd.read_csv("Player_profiles.csv")
poty_df = pd.read_csv("Player_of_year.csv")
print(poty_df)
goty_df = pd.read_csv("Goal_of_the_year.csv")
captains_df = pd.read_csv("Captains.csv")
chelsea_titles_df = pd.read_csv("Chelsea_titles.csv")
fwa_player_df = pd.read_csv("FWA_player - Sheet1.csv")
golden_boot_df = pd.read_csv("Golden_boot - Sheet1.csv")
golden_glove_df = pd.read_csv("Golden_glove - Sheet1.csv")

# print(player_df)

player_dict = player_df.set_index("Player").T.to_dict("list")
print(player_dict)
poty_dict = poty_df.to_dict("list")
print(poty_dict)

# for i in range(len(poty_dict)):
#     if player_dict[i]["Player"] == poty_dict[i]["Winner"]:
#         print(i)
#     # print(i["Player"])


