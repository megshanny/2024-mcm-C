import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import MCM

sum_days = 4
test_start = 4910
test_end = 5105 #Excel中的行数-2

data = pd.read_csv('./bigger_Wimbledon_featured_matches.csv')
num_data = data.copy()
num_data['elapsed_time'] = pd.to_timedelta(num_data['elapsed_time']).dt.total_seconds()
num_data['cost_time'] = num_data['elapsed_time'] - num_data['elapsed_time'].shift(1)
num_data['p1_get_point'] = (num_data['point_victor'] == 1).astype(int)
num_data['p2_get_point'] = (num_data['point_victor'] == 2).astype(int)
num_data['p1_score'] = num_data['p1_score'].apply(
    lambda x: 0 if x=='0' else
              1 if x=='15' else
              2 if x=='30' else
              3 if x=='40' else 4)#AD
num_data['p2_score'] = num_data['p2_score'].apply(
    lambda x: 0 if x=='0' else
              1 if x=='15' else
              2 if x=='30' else
              3 if x=='40' else 4)#AD
num_data['winner_shot_type'] = num_data['winner_shot_type'].apply(
    lambda x: -1 if x=='B' else
               1 if x=='F' else 0)#0
num_data['speed_mph'] = num_data['speed_mph'].apply(
    lambda x: x if x>=1 and x <= 300 else num_data['speed_mph'].mean())
num_data['serve_width_1'] = num_data['serve_width'].apply(
    lambda x: 1 if x=='BC' or x=='BW' or x=='B' else 0)#NA,C,W
num_data['serve_width_2'] = num_data['serve_width'].apply(
    lambda x: -1 if x=='BC' or x=='C' else
               1 if x=='BW' or x=='W' else 0)#NA,B
num_data['serve_depth'] = num_data['serve_depth'].apply(
    lambda x: -1 if x=='NCTL' else
               1 if x=='CTL'  else 0)#NA
num_data['return_depth'] = num_data['return_depth'].apply(
    lambda x: -1 if x=='ND' else
               1 if x=='D'  else 0)#NA
num_columns = num_data.columns.to_list()
num_columns.remove('match_id')
num_columns.remove('elapsed_time')
num_columns.remove('player1')
num_columns.remove('player2')
num_columns.remove('serve_width')
num_data = num_data[num_columns]

dict = MCM.load('./bigger-weight-save-2024-02-03-09-02-18.json')
dict['p1_m_avg'] = np.array(dict['p1_m_avg'])
dict['p2_m_avg'] = np.array(dict['p2_m_avg'])
dict['p1_m_gaussian'] = np.array(dict['p1_m_gaussian'])
dict['p2_m_gaussian'] = np.array(dict['p2_m_gaussian'])

train_data = num_data[0:test_end].copy()
for i in range(1,sum_days):
    train_data = train_data + num_data[i:test_end+i].reset_index(drop=True)

train_data['p1_m_avg'] = dict['p1_m_avg'][sum_days-1:test_end+sum_days-1]
train_data['p2_m_avg'] = dict['p2_m_avg'][sum_days-1:test_end+sum_days-1]
train_data['p1_m_gaussian'] = dict['p1_m_gaussian'][sum_days-1:test_end+sum_days-1]
train_data['p2_m_gaussian'] = dict['p2_m_gaussian'][sum_days-1:test_end+sum_days-1]
train_data['p1_next_m_avg'] = dict['p1_m_avg'][sum_days:test_end+sum_days]
train_data['p2_next_m_avg'] = dict['p2_m_avg'][sum_days:test_end+sum_days]
train_data['p1_next_m_gaussian'] = dict['p1_m_gaussian'][sum_days:test_end+sum_days]
train_data['p2_next_m_gaussian'] = dict['p2_m_gaussian'][sum_days:test_end+sum_days]
train_data['p1_avg_diff'] = dict['p1_m_avg'][sum_days:test_end+sum_days]-dict['p1_m_avg'][sum_days-1:test_end+sum_days-1]
train_data['p2_avg_diff'] = dict['p2_m_avg'][sum_days:test_end+sum_days]-dict['p2_m_avg'][sum_days-1:test_end+sum_days-1]
train_data['p1_gaussian_diff'] = dict['p1_m_gaussian'][sum_days:test_end+sum_days]-dict['p1_m_gaussian'][sum_days-1:test_end+sum_days-1]
train_data['p2_gaussian_diff'] = dict['p2_m_gaussian'][sum_days:test_end+sum_days]-dict['p2_m_gaussian'][sum_days-1:test_end+sum_days-1]
i = test_end-2
last_end = test_end-1
while i>=test_start-1:
    if i>=test_start:
        if data['match_id'][i]==data['match_id'][i+1]:
            i-=1
            continue
    last_start = i+1
    drop_list = list(range(last_start,last_start+sum_days-1)) 
    drop_list.append(last_end)
    train_data = train_data.drop(drop_list)
    i -= 1
    last_end = last_start-1
train_data = train_data[test_start:]
train_data = train_data.reset_index(drop=True)
train_num_data_corr = np.abs(train_data.corr())
plt.figure(figsize=(20,20))
import seaborn as sns
#隐藏数字，只显示颜色
sns.heatmap(train_num_data_corr,annot=False,fmt='.2f')
with open('./whichsum.txt','a') as f:
    print(data['match_id'][test_start],file=f)
    print(train_num_data_corr.iloc[:-12,-8:-4].max(),file=f)
    print(train_num_data_corr.iloc[:-12,-8:-4].mean(),file=f)
    print(train_num_data_corr.iloc[:-12,-8:-4].mean().mean(),file=f)
print(data['match_id'][test_start])
print(train_num_data_corr.iloc[:-12,-8:-4].max())
print(train_num_data_corr.iloc[:-12,-8:-4].mean())
print(train_num_data_corr.iloc[:-12,-8:-4].mean().mean())
# MCM.save({'train_num_data_corr':train_num_data_corr},'sum'+str(sum_days))
plt.show()