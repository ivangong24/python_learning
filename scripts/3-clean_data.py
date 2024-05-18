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
players = ['Kobe Bryant', 'Yao Ming'] # create a list of players
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

# Good! Now we have summarized the data for Kobe Bryant and Yao Ming.
# What if we would like to create a new column to calculate the average points (PTS) per minute (MIN)?
# We can use the assign() method to create a new column, similar to the mutate() function in dplyr
# Notice that MIN is a string, we need to convert it to a numeric value
# There are two parts of MIN, the first part is the minutes, and the second part is the seconds
# we can use the str.extract() method to extract the minutes and seconds
# the str.extract() method is similar to the str_extract() function in R

# for example, we would like to split a string "43:18" into two parts, 43 and 18
# and assign two new variables to store the minutes and seconds
# we can use the following code
df_test = pd.DataFrame({"MIN": ["43:18"]})
df_test[["MINUTES", "SECONDS"]] = df_test["MIN"].str.extract(r"(\d+):(\d+)")
print(df_test)

# now we can apply the same logic to the df_kobe_yao dataset
df_kobe_yao_new = df_kobe_yao_join.assign(
  MINUTES=pd.to_numeric(df_kobe_yao_join["MIN"].str.extract(r"(\d+):(\d+)")[0]),
  SECONDS=pd.to_numeric(df_kobe_yao_join["MIN"].str.extract(r"(\d+):(\d+)")[1]) / 60
  ).copy()

# now we can create a new column to calculate the average points per minute
df_kobe_yao_final = df_kobe_yao_new.assign(
  PTS_PER_MIN = 
  df_kobe_yao_new["PTS"] / 
  (df_kobe_yao_new["MINUTES"] + df_kobe_yao_new["SECONDS"])
  ).copy()

# now let's just select the columns we are interested in
# we can use the filter() method, which is very similar to the select() function in dplyr
# so filter() = select() in dplyr, and query() = filter() in dplyr
df_kobe_yao_final_filter = df_kobe_yao_final.filter(
  items=["PLAYER_NAME", "GAME_DATE", "SEASON", "PTS", "MIN", "PTS_PER_MIN"]
  ).copy()

# Now let's summarize the data by player name and season

cross_table_pts_per_min = pd.crosstab(
  index=df_kobe_yao_final_filter["PLAYER_NAME"],
  columns=df_kobe_yao_final_filter["SEASON"],
  values=df_kobe_yao_final_filter["PTS_PER_MIN"],
  aggfunc="mean")
  
print(cross_table_pts_per_min)

# Great! Now I would like to change all the variables to lowercase for easier reading
# we can use the rename() method to rename the columns
# the rename() method is similar to the rename() function in dplyr
# we can use the `columns` parameter to specify the new column names
# the str.lower() method is used to convert the column names to lowercase
df_kobe_yao_final_filter_lower = df_kobe_yao_final_filter.rename(
  columns=str.lower).copy()
  
# Now I would like to convert all NaN values to 0
# we can use the fillna() method to replace NaN values with a specific value
# the fillna() method is similar to the replace_na() function in dplyr
df_kobe_yao_final_filter_lower_nona = df_kobe_yao_final_filter_lower.fillna(0).copy()


# Then I would like to arrange the data by pts_per_min in descending order
# we can use the sort_values() method to sort the data
# the sort_values() method is similar to the arrange() function in dplyr
# we can use the `by` parameter to specify the column to sort
# the `ascending` parameter is used to specify the order of sorting
df_kobe_yao_final_filter_lower_sort = df_kobe_yao_final_filter_lower_nona.sort_values(
  by="pts_per_min", ascending=False).copy()
