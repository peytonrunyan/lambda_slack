#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), '..'))
	print(os.getcwd())
except:
	pass

#%%
# baseline import
import pandas as pd
import numpy as np


#%%
# import plotly
import plotly
plotly.tools.set_credentials_file(username='peytonrunyan', api_key='qmJRPutxhfQFX0Qs5sSi')
import plotly.plotly as py
import plotly.graph_objs as go


#%%
# read in data
main_slack = pd.read_csv('https://raw.githubusercontent.com/peytonrunyan/datadump/master/slack_data.csv')
prep_slack = pd.read_csv('https://raw.githubusercontent.com/peytonrunyan/datadump/master/Lambda%20School%20Prep%20Slack%20Analytics%20Jan%2014%202019.csv')
goog = pd.read_csv('https://raw.githubusercontent.com/peytonrunyan/datadump/master/google_2017.csv',header=1)


#%%
# wrangle google
goog.head()


#%%
goog.head()
goog['lambda school: (United States)'].max()
goog['lambda_normalized'] = goog['lambda school: (United States)']/goog['lambda school: (United States)'].max()


#%%
# view columns
pd.set_option('display.max_columns', 500)
main_slack.head()


#%%
trace1 = go.Scatter(
    x = main_slack['Date'],
    y = main_slack['Weekly Users Posting Messages'],
    mode = 'lines',
    name = 'Lambda Student WUPM',
    opacity = 0.8,
    marker = dict(color='maroon')
    #text = main_slack['Weekly Users Posting Messages']
    )

trace2 = go.Scatter(
    x = prep_slack['Date'],
    y = prep_slack['Weekly Users Posting Messages'],
    mode = 'lines',
    name = 'Lambda Prep WUPM',
    opacity = 0.8,
    marker = dict(color='black')
    #text = main_slack['Weekly Users Posting Messages']
    )

trace3 = go.Bar(
    visible = False,
    x = main_slack['Date'],
    y = main_slack['Full Members'],
    #mode = 'lines',
    name= 'Lambda Student Full Members',
    opacity = 0.7,
    #fill='tozeroy',
    marker = dict(color = 'maroon')
    #text = main_slack['Full Members']
    )

trace4 = go.Bar(
    visible = False,
    x = prep_slack['Date'],
    y = prep_slack['Full Members'],
    #mode = 'lines',
    name= 'Lambda Prep Full Members',
    opacity = 0.7,
    #fill='tozeroy',
    marker = dict(color = 'gray')


    )

trace5 = go.Scatter(
    visible = False,
    x = main_slack['Date'],
    y = main_slack['Daily Active Users'],
    mode = 'lines',
    name = 'Lambda Student DAU',
    opacity = 0.8,
    marker = dict(color='maroon')

    )

trace6 = go.Scatter(
    visible = False,
    x = prep_slack['Date'],
    y = prep_slack['Daily Active Users'],
    mode = 'lines',
    name = 'Lambda Prep DAU',
    opacity = 0.8,
    marker = dict(color='black')

    )

trace7 = go.Scatter(
    visible = False,
    x = main_slack['Date'],
    y = main_slack['Weekly Active Users'],
    mode = 'lines',
    name= 'Lambda Student WAU',
    opacity = 0.8,
    marker = dict(color = 'maroon')

    )

trace8 = go.Scatter(
    visible = False,
    x = prep_slack['Date'],
    y = prep_slack['Weekly Active Users'],
    mode = 'lines',
    name= 'Lambda Prep WAU',
    opacity = 0.8,
    marker = dict(color = 'black')

    )

data = [trace1,trace2,trace3,trace4,trace5,trace6,trace7,trace8]

updatemenus = list([
    dict(direction = 'left',
         pad = {'r': 10, 't': 10},
         showactive = True,
         x = 0.0,
         xanchor = 'left',
         y = 1.11,
         yanchor = 'top',
         type="buttons",
         #active=-1,
         buttons=list([
             dict(label = 'WUPM',
                 method = 'update',
                 args = [{'visible': [True, True, False, False, False, False, False, False]},
                         {'title': '<b>Weekly Users Posting Messages: Lambda Prep vs. Lambda Student</b>'
                          #  'annotations': low_annotations
                         }]),
             dict(label = 'Members',
                 method = 'update',
                 args = [{'visible': [False, False, True, True, False, False, False, False]},
                         {'title': '<b>Total Members: Lambda Prep Slack vs. Lambda Student Slack</b>'
                          # 'annotations': high_annotations
                      }]),
            dict(label = 'DAU',
                 method = 'update',
                 args = [{'visible': [False, False, False, False, True, True, False, False]},
                         {'title': '<b>Daily Active Users: Lambda Prep vs. Lambda Student Slack</b>',
                          # 'annotations': hgh_annotations+low_annotations
                         }]),
            dict(label = 'WAU',
                 method = 'update',
                 args = [{'visible': [False,False, False, False, False, False, True, True]},
                         {'title': '<b>Weekly Active Users: Lambda Prep vs. Lambda Student Slack</b>'
                         #  'annotations': 
                         }])
                  
        ]),
    )
])



layout = dict(title = '<b>Click Button to Compare Lambda Prep and Lambda Student Slack Channels</b><br><i>Click and drag to zoom in on areas of interest</i>',
              
                xaxis= dict(
                  title='<b>Date Slider</b>', 
                  ticklen = 5,
                  tickangle = -35,
                  showgrid=False,
#                   rangeslider=dict(
#                       visible = True
#                   ),
                    type='date'
                ),
                
                yaxis = dict(
                    title='<b>Members</b>',
                    zeroline=True,
                    zerolinewidth=2,
                    showgrid=True
                ),
                
                font=dict(
                    family='Helvetica',
                    size=12,
                    color='black'
                    ),
                
                autosize=False,
                updatemenus=updatemenus,
                width=750,
                height=500
                )

             
              
fig = dict(data = data, layout = layout)
py.iplot(fig, filename='plot from API (20)',)
              


#%%
trace5 = go.Scatter(
    visible = False,
    x = main_slack['Date'],
    y = main_slack['Daily Active Users'],
    mode = 'lines',
    name = 'Lambda Student DAU',
    opacity = 0.9,
    marker = dict(color='maroon')
    #text = main_slack['Weekly Users Posting Messages']
    )

trace6 = go.Scatter(
    visible = False,
    x = prep_slack['Date'],
    y = prep_slack['Daily Active Users'],
    mode = 'lines',
    name = 'Lambda Prep DAU',
    opacity = 0.7,
    marker = dict(color='black')
    #text = main_slack['Weekly Users Posting Messages']
    )

trace9 = go.Scatter(
    visible = True,
    x = goog['Week'],
    y = goog['lambda_normalized']*1500,
    fill='tozeroy',
    mode = 'lines',
    name= 'Google Search',
    opacity = 0.5,
    marker = dict(color = 'rgba(133, 193, 233,.5)')
    #text = prep_slack['Full Members']
    )

data = [trace9,trace5,trace6]

updatemenus = list([
    dict(direction = 'left',
         pad = {'r': 10, 't': 10},
         showactive = True,
         x = 0.0,
         xanchor = 'left',
         y = 1.2,
         yanchor = 'top',
         type="buttons",
         #active=-1,
         buttons=list([
            dict(label = 'Neither',
                 method = 'update',
                 args = [{'visible': [True, False, False]},
                         {'title': '<b>Google Searches for Lambda School</b>'
                          # 'annotations': high_annotations
                      }]),
            dict(label = 'L.P. DAU',
                 method = 'update',
                 args = [{'visible': [True, False, True]},
                         {'title': '<b>Lambda Student Slack Daily Active Users vs. Google Searches</b>'
                          # 'annotations': high_annotations
                      }]),
            dict(label = 'L.S. DAU',
                 method = 'update',
                 args = [{'visible': [True, True, False]},
                         {'title': '<b>Lambda Prep Slack Daily Active Users vs. Google Searches</b>',
                          # 'annotations': hgh_annotations+low_annotations
                         }]),
            dict(label = 'Both',
                 method = 'update',
                 args = [{'visible': [True,True, True]},
                         {'title': '<b>Lambda Student and Prep Slack Daily Active Users vs. Google Searches</b>'
                         #  'annotations': 
                         }])
         ])
    )
])
             
layout = dict(title = '<b>Click Buttons to Compare Lambda Prep and Lambda Student Slack Channels</b>',
              
              xaxis= dict(
                  title='<b>Date Slider</b>', 
                  ticklen = 5,
                  tickangle = -35,
                  showgrid=False,
                  rangeslider=dict(
                      visible = True
                  ),
                  type='date'
              ),
              
              yaxis = dict(
                  title='<b>Members</b>',
                  zeroline=True,
                  zerolinewidth=2,
                  showgrid=True
              ),
              
              font=dict(
                  family='Helvetica',
                  size=12,
                  color='black'
                  ),
              
              autosize=False,
              updatemenus=updatemenus,
              width=750,
              height=500
             )

          
              
fig = dict(data = data, layout = layout)
py.iplot(fig, filename='plot from API (4)')
              


#%%
trace5 = go.Scatter(
    visible = False,
    x = main_slack['Date'],
    y = main_slack['Daily Active Users'],
    mode = 'lines',
    name = 'Lambda Student DAU',
    opacity = 0.9,
    marker = dict(color='maroon')
    #text = main_slack['Weekly Users Posting Messages']
    )

trace6 = go.Scatter(
    visible = False,
    x = prep_slack['Date'],
    y = prep_slack['Daily Active Users'],
    mode = 'lines',
    name = 'Lambda Prep DAU',
    opacity = 0.7,
    marker = dict(color='black')
    #text = main_slack['Weekly Users Posting Messages']
    )

trace9 = go.Scatter(
    visible = True,
    x = goog['Week'],
    y = goog['lambda_normalized']*1500,
    fill='tozeroy',
    mode = 'lines',
    name= 'Google Search',
    opacity = 0.5,
    marker = dict(color = 'rgba(133, 193, 233,.5)')
    #text = prep_slack['Full Members']
    )

data = [trace9,trace5,trace6]

updatemenus = list([
    dict(direction = 'left',
         pad = {'r': 10, 't': 10},
         showactive = True,
         x = 0.0,
         xanchor = 'left',
         y = 1.1,
         yanchor = 'top',
         type="buttons",
         #active=-1,
         buttons=list([
            dict(label = 'Neither',
                 method = 'update',
                 args = [{'visible': [True, False, False]},
                         {'title': '<b>Google Searches for Lambda School</b><br><i>Click and drag to zoom in on areas of interest</i>'
                          # 'annotations': high_annotations
                      }]),
            dict(label = 'L.P. DAU',
                 method = 'update',
                 args = [{'visible': [True, False, True]},
                         {'title': '<b>Lambda Student Slack Daily Active Users vs. Google Searches</b><br><i>Click and drag to zoom in on areas of interest</i>'
                          # 'annotations': high_annotations
                      }]),
            dict(label = 'L.S. DAU',
                 method = 'update',
                 args = [{'visible': [True, True, False]},
                         {'title': '<b>Lambda Prep Slack Daily Active Users vs. Google Searches</b><br><i>Click and drag to zoom in on areas of interest</i>',
                          # 'annotations': hgh_annotations+low_annotations
                         }]),
            dict(label = 'Both',
                 method = 'update',
                 args = [{'visible': [True,True, True]},
                         {'title': '<b>Lambda Student and Prep Slack Daily Active Users vs. Google Searches</b><br><i>Click and drag to zoom in on areas of interest</i>'
                         #  'annotations': 
                         }])
         ])
    )
])
             
layout = dict(title = '<b>Click Button to Compare Lambda Prep and Lambda Student Slack Channels</b><br><i>Click and drag to zoom in on areas of interest</i>',
              
              xaxis= dict(
                  title='<b>Date Slider</b>', 
                  ticklen = 5,
                  tickangle = -35,
                  showgrid=False,
#                   rangeslider=dict(
#                       visible = True
#                   ),
                  type='date'
              ),
              
              yaxis = dict(
                  title='<b>Members</b>',
                  zeroline=True,
                  zerolinewidth=2,
                  showgrid=True
              ),
              
              font=dict(
                  family='Helvetica',
                  size=12,
                  color='black'
                  ),
              
              autosize=False,
              updatemenus=updatemenus,
              width=750,
              height=500
             )

          
              
fig = dict(data = data, layout = layout)
py.iplot(fig, name='plot from API (6)')


#%%
main_slack['Date'] = pd.to_datetime(main_slack['Date'])
prep_slack['Date'] = pd.to_datetime(prep_slack['Date'])


main_slack['Day'] = main_slack['Date'].dt.weekday
prep_slack['Day'] = prep_slack['Date'].dt.weekday


main_slack['Active'] = main_slack['Daily Active Users']/main_slack['Full Members']
prep_slack['Active'] = prep_slack['Daily Active Users']/prep_slack['Full Members']

main_slack['Posting'] = main_slack['Daily Users Posting Messages']/main_slack['Full Members']
prep_slack['Posting'] = prep_slack['Daily Users Posting Messages']/prep_slack['Full Members']


main_days = main_slack.groupby('Day').mean()
prep_days = prep_slack.groupby('Day').mean()


#%%
main_days


#%%
trace1 = go.Bar(
    x = ['Mon','Tues','Wed','Thurs','Fri','Sat','Sun'],
    y = main_days['Daily Active Users'],
    opacity = 0.7,
    marker = dict(color = 'maroon'),
    name='L.S. DAU'
)

trace2 = go.Bar(
    x = ['Mon','Tues','Wed','Thurs','Fri','Sat','Sun'],
    y = main_days['Daily Users Posting Messages'],
    opacity = 0.7,
    marker = dict(color = 'orange'),
    visible = False,
    name='L.S. DUPM'
)

trace3 = go.Bar(
    x = ['Mon','Tues','Wed','Thurs','Fri','Sat','Sun'],
    y = prep_days['Daily Active Users'],
    opacity = 0.7,
    marker = dict(color = 'black'),
    name='Prep DAU'
)

trace4 = go.Bar(
    x = ['Mon','Tues','Wed','Thurs','Fri','Sat','Sun'],
    y = prep_days['Daily Users Posting Messages'],
    opacity = 0.7,
    marker = dict(color = 'blue'),
    visible = False,
    name='Prep DUPM'
)

data = [trace1,trace2,trace3,trace4]

updatemenus = list([
    dict(direction = 'left',
         pad = {'r': 10, 't': 10},
         showactive = True,
         x = 0.0,
         xanchor = 'left',
         y = 1.153,
         yanchor = 'top',
         type="buttons",
         #active=-1,
         buttons=list([
            dict(label = 'Daily Active Users',
                 method = 'update',
                 args = [{'visible': [True, False, True, False]},
                         {'title': '<b>Average Daily Active Users by Day of Week</b>'
                          # 'annotations': high_annotations
                      }]),
            dict(label = 'Daily Users Posting Messages',
                 method = 'update',
                 args = [{'visible': [False, True, False, True]},
                         {'title': '<b>Average Daily Users Posting Messages by Day of Week</b>',
                          # 'annotations': hgh_annotations+low_annotations
                         }]),
            dict(label = 'Both',
                 method = 'update',
                 args = [{'visible': [True,True,True,True]},
                         {'title': '<b>Average DAU and DUPM by Day of Week</b>'
                         #  'annotations': 
                         }])

        ]),
    )
])

layout = dict(title = '<b>Average Lambda Student and Prep Activity by Day of Week</b>',
              
              xaxis= dict(
                  title='<b>Date</b>', 
                  ticklen = 5, 
                  tickangle = -45,
                  zeroline=False),
              
              yaxis = dict(
                  title='<b>Members</b>',
                  zeroline=True,
                  showgrid=False
                          ),
              
              autosize=False,
              updatemenus=updatemenus,
              width=750,
              height=500,
              
              font=dict(
                  family='Helvetica',
                  size=12,
                  color='black'
                  )
             )
 

                

fig = dict(data = data, layout = layout)

py.iplot(fig, filename='plot from API (1)')


#%%
#Clear warning message
pd.options.mode.chained_assignment = None 

#Create new column to be iterated over
main_slack['Change in Members'] = main_slack['Full Members']

prep_slack['Change in Members'] = prep_slack['Full Members']

#Create new column showing daily net change in members 
for i in range(1,len(main_slack)): 
  main_slack['Change in Members'][i] = main_slack['Full Members'][i] - main_slack['Full Members'][i-1] 

for i in range(1,len(prep_slack)): 
  prep_slack['Change in Members'][i] = prep_slack['Full Members'][i] - prep_slack['Full Members'][i-1]


#%%
# set date that you want to analyze
startdate = pd.to_datetime('2018-01-01').date()

### Main Slack
# make smaller df to deal with
# consider removing variable assignment 
main_slack_2018 = main_slack[main_slack['Date'] >= startdate]

# set coords for main slack positive days
pos_x_main = main_slack_2018[main_slack_2018['Change in Members'] > 0]['Date']
pos_y_main = main_slack_2018[main_slack_2018['Change in Members'] > 0]['Change in Members']

# set coords for main slack positive days
neg_x_main = main_slack_2018[main_slack_2018['Change in Members'] < 0]['Date']
neg_y_main = main_slack_2018[main_slack_2018['Change in Members'] < 0]['Change in Members']

### Prep Slack
# make smaller df to deal with
# consider removing variable assignment 
prep_slack_2018 = prep_slack[prep_slack['Date'] >= startdate]

# set coords for prep slack positive days
pos_x_prep = prep_slack_2018[prep_slack_2018['Change in Members'] > 0]['Date']
pos_y_prep = prep_slack_2018[prep_slack_2018['Change in Members'] > 0]['Change in Members']

# set coords for prep slack positive days
neg_x_prep = prep_slack_2018[prep_slack_2018['Change in Members'] < 0]['Date']
neg_y_prep = prep_slack_2018[prep_slack_2018['Change in Members'] < 0]['Change in Members']



# pos_main trace
trace1 = go.Bar(
    x= pos_x_main,
    y= pos_y_main,
    opacity = 0.9,
    marker = dict(color = 'maroon'),
    name='Net Positive Days'
)

# neg_main trace
trace2 = go.Bar(
    x= neg_x_main,
    y= neg_y_main,
    opacity = 0.65,
    marker = dict(color = 'black'),
    name='Net Negative Days'
)

# pos_prep trace
trace3 = go.Bar(
    x= pos_x_prep,
    y= pos_y_prep,
    opacity = 0.8,
    visible = False,
    marker = dict(color = 'orange'),
    name='Net Positive Days'
)

# neg_prep trace
trace4 = go.Bar(
    x= neg_x_prep,
    y= neg_y_prep,
    opacity = 0.8,
    visible = False,
    marker = dict(color = 'blue'),
    name='Net Negative Days'
)

data = [trace3,trace4,trace1,trace2]
layout = go.Layout(
    barmode='relative'
)

updatemenus = list([
    dict(direction = 'left',
         pad = {'r': 10, 't': 10},
         showactive = True,
         x = 0.0,
         xanchor = 'left',
         y = 1.2,
         yanchor = 'top',
         type="buttons",
         #active=-1,
         buttons=list([
            dict(label = 'Lambda Student',
                 method = 'update',
                 args = [{'visible': [False, False, True, True]},
                         {'title': '<b>Net Gain/Loss by Day for Lambda Student Slack</b>',
                          # 'annotations': hgh_annotations+low_annotations
                         }]),
             dict(label = 'Lambda Prep',
                 method = 'update',
                 args = [{'visible': [True, True, False, False]},
                         {'title': '<b>Net Gain/Loss by Day for Lambda Prep Slack</b>'
                          # 'annotations': high_annotations
                      }]),
            dict(label = 'Both',
                 method = 'update',
                 args = [{'visible': [True,True,True,True]},
                         {'title': '<b>Net Gain/Loss by Day for Both Slack Channels</b>'
                         #  'annotations': 
                         }])

        ]),
    )
])

layout = dict(title = '<b>Net Gain/Loss by Day</b>',              
              #paper_bgcolor ='rgba(64,64,64,.6)',
              #plot_bgcolor='rgba(64,64,64,.6)',
              xaxis= dict(
                  title='<b>Date</b>', 
                  ticklen = 5,
                  tickangle = -35,
                  zeroline=False,
                  rangeslider=dict(
                      visible = True
                  ),
                  type='date'
              ),
              yaxis = dict(title='<b>Gain/Loss</b>'),
              updatemenus=updatemenus,
              autosize=False,
              width=700,
              height=500,

              font=dict(
                  family='Helvetica',
                  size=12,
                  color='black'
                  )
             )              
    

fig = dict(data = data, layout = layout)
py.iplot(fig, filename='plot from API (2)')


#%%
goog = pd.read_csv('https://raw.githubusercontent.com/peytonrunyan/datadump/master/google_2017.csv',header=1)
#goog.columns = goog.iloc[0]


#%%
goog.head()


#%%
trace1 = go.Scatter(
    x = goog['Week'],
    y = goog['lambda school: (United States)'],
    mode = 'lines',
    name = 'Lambda Student WUPM',
    opacity = 0.7,
    marker = dict(color='maroon')
    #text = main_slack['Weekly Users Posting Messages']
    )

trace2 = go.Scatter(
    x = goog['Week'],
    y = goog['app academy: (United States)'],
    mode = 'lines',
    name = 'Lambda Prep WUPM',
    opacity = 0.9,
    marker = dict(color='gray')
    #text = main_slack['Weekly Users Posting Messages']
    )

trace3 = go.Scatter(
    x = goog['Week'],
    y = goog['flatiron school: (United States)'],
    mode = 'lines',
    name = 'Lambda Prep WUPM',
    opacity = 0.9,
    marker = dict(color='orange')
    #text = main_slack['Weekly Users Posting Messages']
    )

data = [trace1,trace2,trace3]


layout = dict(title = '<b>Click Button to Compare Lambda Prep and Lambda Student Slack Channels</b>',
              
              xaxis= dict(
                  title='<b>Date Slider</b>', 
                  ticklen = 5,
                  tickangle = -35,
                  showgrid=False,
                  rangeslider=dict(
                      visible = True
                  ),
                  type='date'
              ),
              
              yaxis = dict(
                  title='<b>Members</b>',
                  zeroline=True,
                  zerolinewidth=2,
                  showgrid=True
              ),
              
              font=dict(
                  family='Helvetica',
                  size=12,
                  color='black'
                  ),
              
              autosize=False,
              width=750,
              height=500
             )

fig = dict(data = data, layout = layout)
py.iplot(fig, name='plot from API (3)')


#%%



