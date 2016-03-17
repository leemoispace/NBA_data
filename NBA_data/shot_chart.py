import requests
import pandas as pd
import seaborn as sns
import json
import matplotlib.pyplot as plt

#shot_chart_url='http://stats.nba.com/stats/shotchartdetail?Period=0&VsConference=&LeagueID=00&LastNGames=0&TeamID=0&Position=&Location=&Outcome=&ContextMeasure=FGA&DateFrom=&StartPeriod=&DateTo=&OpponentTeamID=0&ContextFilter=&RangeType=&Season=2015-16&AheadBehind=&PlayerID=201939&EndRange=&VsDivision=&PointDiff=&RookieYear=&GameSegment=&Month=0&ClutchTime=&StartRange=&EndPeriod=&SeasonType=Regular+Season&SeasonSegment=&GameID='
#https://www.zhihu.com/question/28168585
#response = requests.get(shot_chart_url)
f=open('shotchartdetail.json','r')
response = open('shotchartdetail.json','r').read()

# Grab the headers to be used as column headers for our DataFrame
headers = json.loads(response)['resultSets'][0]['headers']
# Grab the shot chart data
shots = json.loads(response)['resultSets'][0]['rowSet']
shot_df=pd.DataFrame(shots,columns=headers)
# View the head of the DataFrame and all its columns
from IPython.display import display
with pd.option_context('display.max_columns', None):
    display(shot_df.head())
