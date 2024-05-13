# Example of how to clean and summarize data using pandas


# since data is a dictionary, we can access the specific dataset by using the key
# in this case, the key is "games_details"
# notice that we should use the copy() method to avoid modifying the original data
# the query() method is used to filter the data, similar to the filter() function in dplyr
df_kobe = data["games_details"].query("PLAYER_NAME == 'Kobe Bryant'").copy()
# if we are interested in multiple players, we can use the isin() method, the | operator or use an external list

## isin() method: which is similar to the %in% operator in R
df_kobe_yao = data["games_details"].query("PLAYER_NAME.isin(['Kobe Bryant', 'Yao Ming'])").copy()

## | operator: which is similar to the | operator in R
df_kobe_yao = data["games_details"].query("PLAYER_NAME == 'Kobe Bryant' | PLAYER_NAME == 'Yao Ming'").copy()

## external list: we need to add the @ symbol before the list
players = ['Kobe Bryant', 'Yao Ming']
df_kobe_yao = data["games_details"].query("PLAYER_NAME.isin(@players)").copy()

print(df_kobe.head(), df_kobe_yao.head())

# compare the mean score, rebounds, and assists between Kobe and Yao
print(df_kobe_yao.groupby("PLAYER_NAME")[["PTS", "REB", "AST"]].mean())

# we can also use the pivot_table() method to summarize the data
# the pivot_table() method is similar to the group_by() and summarise() functions in dplyr
# the aggfunc parameter is used to specify the aggregation function
# the fill_value parameter is used to specify the value to replace missing values
pivot_table = df_kobe_yao.pivot_table(
  index="PLAYER_NAME", 
  values=["PTS", "REB", "AST"], 
  aggfunc="mean", fill_value=0)

print(pivot_table)

# if we would like to further compare the data by game season, 
# we can use the cross_table() method to summarize the data by player name and season
# we need to left join the games dataset with the games_details dataset to get the season information

# left join the games dataset with the games_details dataset
df_kobe_yao_join = pd.merge(
  left=df_kobe_yao,
  right=data["games"],
  left_on="GAME_ID",
  right_on="GAME_ID",
  how="left")
  
# summarize the data by player name and season

cross_table_season = pd.crosstab(
  index=df_kobe_yao_join["PLAYER_NAME"],
  columns=df_kobe_yao_join["SEASON"],
  values=df_kobe_yao_join["PTS"],
  aggfunc="mean")

print(cross_table_season)

