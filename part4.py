import MCM
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.metrics import mean_squared_error
load_data = MCM.load('./new_all_match_data-save-2024-02-05-13-45-44.json')
all_match_data = load_data['all_match_data']

columns = ['set_no', 'game_no', 'point_no', 'p1_sets', 'p2_sets', 'p1_games',
       'p2_games', 'p1_score', 'p2_score', 'server', 'serve_no',
       'point_victor', 'p1_points_won', 'p2_points_won', 'game_victor',
       'set_victor', 'p1_ace', 'p2_ace', 'p1_winner', 'p2_winner',
       'winner_shot_type', 'p1_double_fault', 'p2_double_fault', 'p1_unf_err',
       'p2_unf_err', 'p1_net_pt', 'p2_net_pt', 'p1_net_pt_won',
       'p2_net_pt_won', 'p1_break_pt', 'p2_break_pt', 'p1_break_pt_won',
       'p2_break_pt_won', 'p1_break_pt_missed', 'p2_break_pt_missed',
       'p1_distance_run', 'p2_distance_run', 'rally_count', 'speed_mph',
       'serve_depth', 'return_depth', 'cost_time', 'p1_get_point',
       'p2_get_point', 'serve_width_1', 'serve_width_2', 'p1_m_avg',
       'p2_m_avg', 'p1_m_gaussian', 'p2_m_gaussian', 'p1_next_m_avg',
       'p2_next_m_avg', 'p1_next_m_gaussian', 'p2_next_m_gaussian',
       'p1_avg_diff', 'p2_avg_diff', 'p1_gaussian_diff', 'p2_gaussian_diff',
       'p1_pre', 'p2_pre']

#将list转为dataframe，使用上面的列名
all_match_data = pd.DataFrame(all_match_data, columns=columns)



y1_pre = all_match_data['p1_pre']
y1 = all_match_data['p1_next_m_gaussian']
y2_pre = all_match_data['p2_pre']
y2 = all_match_data['p2_next_m_gaussian']

start = 1035
end = 1090

mse1 = mean_squared_error(y1_pre[start-2:end-2],y1[start-2:end-2])
mse2 = mean_squared_error(y2_pre[start-2:end-2],y2[start-2:end-2])

print(mse1)
print(mse2)

# # start = 420
# # end = 502
# start = 1035
# end = 1090

# sns.set_style('whitegrid')       # 图片风格
# sns.set(font='Times New Roman')  # 图片全局字体

# line_x = [start-2,1041,1047,1055,1059,1067,1072,1077,1083,end-1]

# # 创建画布和坐标轴
# fig, ax = plt.subplots(figsize=(10,5))

# ax.plot(y1[start-2:end-2], label='Medvedev_true')
# ax.plot(y1_pre[start-2:end-2], label='Medvedev_prediction')
# ax.plot(y2[start-2:end-2], label='Fucsovics_true')
# ax.plot(y2_pre[start-2:end-2], label='Fucsovics_prediction')

# ax.set_xlim([start-3,end])
# # plt.xlabel('Points')            # x轴图例
# plt.ylabel('Momentum')  # y轴图例

# # 设置背景颜色
# for i in range(1, len(line_x)):
#     color = 'lightgrey' if i % 2 == 0 else 'white'
#     ax.axvspan(line_x[i - 1], line_x[i], facecolor=color, alpha=0.5)

# # 隐藏横坐标的坐标值
# plt.xticks([])

# plt.legend(loc='upper right')
# plt.show()