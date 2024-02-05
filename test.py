import MCM
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#savedict = {"bestp":bestp,"predict_train_1":predict_train_1,"predict_train_2":predict_train_2,
#             "pred_test_1":y_pred_test_1,"pred_test_2":y_pred_test_2,
#             "another_y_pred_1":another_y_pred_1,"another_y_pred_2":another_y_pred_2,
#             "predict_all_1":predict_all_1,"predict_all_2":predict_all_2,
#             "y_train_1":y_train_1,"y_train_2":y_train_2,
#             "y_test_1":y_test_1,"y_test_2":y_test_2,
#             "another_y_1":another_y_1,"another_y_2":another_y_2,
# }

load_data = MCM.load('./newbestresult-save-2024-02-05-15-55-03.json')

sns.set_theme(style="whitegrid",font="Times New Roman")
print(load_data.keys())
x1 = load_data['pred_test_1']
x2 = np.array(load_data['pred_test_2'])+3
x3 = load_data['y_test_1']
x4 =np.array(load_data['y_test_2'])+3

plt.figure(figsize=(10, 5))
#绘制x1和x3
plt.plot(x3, label='Safiullin_true',linewidth=2)
plt.plot(x1, label='Safiullin_prediction',linewidth=2)
sns.lineplot(data=x4, label='Shapovalov_true',linewidth=2)
sns.lineplot(data=x2, label='Shapovalov_prediction',linewidth=2)
#标签位于右上角，字号为10
plt.legend(loc='upper right',fontsize=10)
plt.ylabel('Momentum')
plt.xlabel('Point Number')
plt.ylim(0, 6)
plt.xlim(-0.9, 50)
plt.show()
#Shapovalov