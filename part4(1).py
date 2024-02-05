import MCM
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

load_data = MCM.load('./new_all_match_data-save-2024-02-05-15-13-00.json')
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
all_match_data = pd.DataFrame(all_match_data, columns=columns)

y1_pre = all_match_data['p1_pre'] + 2
y1 = all_match_data['p1_next_m_gaussian'] + 2
y2_pre = all_match_data['p2_pre']
y2 = all_match_data['p2_next_m_gaussian']

plt.figure(figsize=(10, 5))
plt.plot(y1, label='p1_true')
plt.plot(y1_pre, label='p1_pre')
plt.plot(y2, label='p2_true')
plt.plot(y2_pre, label='p2_pre')
plt.legend(loc='lower right')
plt.show()