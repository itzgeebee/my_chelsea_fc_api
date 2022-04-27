import pandas as pd


class RawData:
    def __init__(self):
        self.player_df = pd.read_csv("Player_profiles.csv")
        self.poty_df = pd.read_csv("Player_of_year.csv")
        self.goty_df = pd.read_csv("Goal_of_the_year.csv")
        self.captains_df = pd.read_csv("Captains.csv")
        self.chelsea_titles_df = pd.read_csv("Chelsea_titles.csv")
        self.fwa_player_df = pd.read_csv("FWA_player - Sheet1.csv")
        self.golden_boot_df = pd.read_csv("Golden_boot - Sheet1.csv")
        self.golden_glove_df = pd.read_csv("Golden_glove - Sheet1.csv")

        self.poty_dict = self.poty_df.to_dict("list")
        self.goty_dict = self.goty_df.to_dict("list")
        self.captains_dict = self.captains_df.to_dict("list")
        self.titles_dict = self.chelsea_titles_df.to_dict("list")
        self.fwa_player_dict = self.fwa_player_df.to_dict("list")
        self.golden_boot_dict = self.golden_boot_df.to_dict("list")
        self.golden_glove_dict = self.golden_glove_df.to_dict("list")


##update database script

# data = RawData()
#
# goty = (data.goty_dict)
# poty = (data.poty_dict)
# cap = (data.captains_dict)
# tit = (data.titles_dict)
# fwa = (data.fwa_player_dict)
# gb = (data.golden_boot_dict)
# gg = (data.golden_glove_dict)
# print(goty)
# print(poty)
# print(cap)
# print(tit)
# print(fwa)
# print(gb)
# print(gg)

# for i in range(len(goty["Year"])):
#
#     new_goty = GOTY(
#         player_name= goty["Winner"][i],
#         win_year = goty["Year"][i],
#         against = goty["Team"][i],
#         scored = goty["Score"][i],
#         result = goty["Result"][i],
#         stadium = goty["Stadium"][i],
#         competition = goty["Competition"][i]
#     )
#     db.session.add(new_goty)
#     db.session.commit()
#
# for i in range(len(poty["Winner"])):
#
#     new_poty = POTY(
#         player_name = poty["Winner"][i],
#         win_year =poty["Year"][i]
#     )
#     db.session.add(new_poty)
#     db.session.commit()
#
# for i in range(len(cap["Captain"])):
#
#     new_cap = Captains(
#         player_name = cap["Captain"][i],
#         years = cap["Year"][i]
#     )
#
#     db.session.add(new_cap)
#     db.session.commit()

# for i in range(len(tit["Honour"])):
#     new_title = Titles(
#         honour=tit["Honour"][i],
#         years=tit["Years"][i]
#     )
#
#     db.session.add(new_title)
#     db.session.commit()
#
# for i in range(len(fwa["Player"])):
#     new_fwa = FWA_Player(
#         player_name=fwa["Player"][i],
#         year=fwa["Year"][i]
#     )
#
#     db.session.add(new_fwa)
#     db.session.commit()

# for i in range(len(gb["Player"])):
#     new_gb = GoldenBoot(
#         player_name=gb["Player"][i],
#         year=gb["Year"][i]
#     )
#
#     db.session.add(new_gb)
#     db.session.commit()
#
# for i in range(len(gg["Player"])):
#     new_gg = GoldenGlove(
#         player_name=gg["Player"][i],
#         year=gg["Year"][i]
#     )
#
#     db.session.add(new_gg)
#     db.session.commit()