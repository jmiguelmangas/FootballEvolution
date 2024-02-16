import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.width', 1000)
football_european_stats_21_22 = pd.read_csv("2021_2022_Football_Player_Stats.csv",sep=';',encoding='latin-1')

jude_bellingham = football_european_stats_21_22[football_european_stats_21_22["Player"]=="Jude Bellingham"]
kylian_mbappe = football_european_stats_21_22[football_european_stats_21_22["Player"]=="Kylian Mbappe"]
vinicius_junior = football_european_stats_21_22[football_european_stats_21_22["Player"]=="Vinicius Junior"]
erling_haaland = football_european_stats_21_22[football_european_stats_21_22["Player"]=="Erling Haaland"]

best_in_europe_21_22 = pd.concat([jude_bellingham,kylian_mbappe,vinicius_junior,erling_haaland])

best_in_europe_21_22.reset_index(inplace=True)

best_in_europe_21_22 = best_in_europe_21_22.drop(["Rk","index"],axis=1)

print(best_in_europe_21_22)

goals_shoot_21_22 = best_in_europe_21_22[["Player","Shots","Goals","SoT","PasAss","GCA","DriSucc"]]

goals_shoot_21_22.set_index("Player",inplace=True)

goals_shoot_21_22.plot(kind="barh")





plt.title("2021-2022 Best Players in Europe Standings")

plt.show()