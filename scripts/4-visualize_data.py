# Example of how to visualize data

# Data visualization is an essential part of data analysis and exploration. 
# In this example, I will explore the NBA games data using matplotlib, seaborn, and plotly.

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# plot Kobe and Yao Ming's points

figure1 = sns.scatterplot(
  x='SEASON', y='PTS', 
  hue = "PLAYER_NAME", 
  data=df_kobe_yao_join, 
  title='Average Points per Season')

plt.show(figure1)
plt.clf()

# use plotly to plot the average points per season

figure2 = px.scatter(
  df_kobe_yao_join,
  x='SEASON', y='PTS', 
  color = "PLAYER_NAME", 
  title='Average Points per Season'
)

figure2.show()

