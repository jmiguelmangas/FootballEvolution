import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.width', 1000)
football_european_stats_21_22 = pd.read_csv("2021_2022_Football_Player_Stats.csv",sep=';',encoding='latin-1')
football_european_stats_22_23 = pd.read_csv("2022_2023_Football_Player_Stats.csv",sep=';',encoding='latin-1')

jude_bellingham_21_22 = football_european_stats_21_22[football_european_stats_21_22["Player"]=="Jude Bellingham"]
kylian_mbappe_21_22 = football_european_stats_21_22[football_european_stats_21_22["Player"]=="Kylian Mbappe"]
vinicius_junior_21_22 = football_european_stats_21_22[football_european_stats_21_22["Player"]=="Vinicius Junior"]
erling_haaland_21_22 = football_european_stats_21_22[football_european_stats_21_22["Player"]=="Erling Haaland"]

jude_bellingham_22_23 = football_european_stats_22_23[football_european_stats_22_23["Player"]=="Jude Bellingham"]
kylian_mbappe_22_23 = football_european_stats_22_23[football_european_stats_22_23["Player"]=="Kylian Mbappe"]
vinicius_junior_22_23 = football_european_stats_22_23[football_european_stats_22_23["Player"]=="Vinicius Junior"]
erling_haaland_22_23 = football_european_stats_22_23[football_european_stats_22_23["Player"]=="Erling Haaland"]

best_in_europe_21_22 = pd.concat([jude_bellingham_21_22,kylian_mbappe_21_22,vinicius_junior_21_22,erling_haaland_21_22])
best_in_europe_22_23 = pd.concat([jude_bellingham_22_23,kylian_mbappe_22_23,vinicius_junior_22_23,erling_haaland_22_23])
best_in_europe_21_22.reset_index(inplace=True)
best_in_europe_22_23.reset_index(inplace=True)

best_in_europe_21_22 = best_in_europe_21_22.drop(["Rk","index"],axis=1)
best_in_europe_22_23 = best_in_europe_22_23.drop(["Rk","index"],axis=1)

print(best_in_europe_21_22)
print(best_in_europe_22_23)

goals_shoot_21_22 = best_in_europe_21_22[["Player","Shots","Goals","SoT","PasAss","GCA","DriSucc"]]
goals_shoot_22_23 = best_in_europe_22_23[["Player","Shots","Goals","SoT","PasAss","GCA","ToSuc"]]


print(goals_shoot_21_22)
print(goals_shoot_22_23)

goals_shoot_21_22.set_index("Player",inplace=True)
goals_shoot_22_23.set_index("Player",inplace=True)

goals_shoot_21_22.plot(kind="barh")

goals_shoot_22_23.plot(kind="barh")

plt.show()
