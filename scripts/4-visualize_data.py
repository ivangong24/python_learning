# Example of how to visualize data

# Data visualization is an essential part of data analysis and exploration. 
# In this example, I will explore the NBA games data using matplotlib, seaborn, and plotly.

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objs as go

# plot Kobe and Yao Ming's points

figure1 = sns.scatterplot(
  x='SEASON', y='PTS', 
  hue = "PLAYER_NAME", 
  data=df_kobe_yao_join)
  
plt.title('Kobe vs Yao Ming Points')
plt.show(figure1)
plt.clf()

# use plotly to plot the scatter plot

figure2 = px.scatter(
  df_kobe_yao_join,
  x='SEASON', y='PTS', 
  color = "PLAYER_NAME", 
  title='Kobe vs Yao Ming Points'
)

figure2.show()

# plot the average points per season using seaborn

figure3 = sns.lineplot(
  x='SEASON', y='PTS',
  hue = "PLAYER_NAME",
  data=df_kobe_yao_join
)

plt.title('Average Points per Season')
plt.show(figure3)
plt.clf()

# use plotly to plot the line plot
# notice that we need to use the groupby() method to summarize the data first
# before plotting the line plot using plotly

df_kobe_yao_join_grouped = df_kobe_yao_join.groupby(
  ["PLAYER_NAME", "SEASON"]
)[["PTS"]].mean().reset_index()


figure4 = px.line(
  df_kobe_yao_join_grouped,
  x='SEASON', y='PTS',
  color = "PLAYER_NAME",
  title='Average Points per Season'
)

figure4.show()


