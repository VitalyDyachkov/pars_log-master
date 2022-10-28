import matplotlib.pyplot as plt
import re
from scipy import signal

CNT_PART_DATA = 100000

# b, a = signal.butter(8, [0.12,0.8], 'bandpass')
b, a = signal.butter(8, [0.05,0.15], 'bandpass')
log = open("ecg.txt", 'r')
plot_data_red = []
sub_plot_data_red = []
move_average = []
cnt_line = 0
average = 0
print("START PARSING, LEN ->", len(re.findall(r"[\n']+", open('SPO2_LOG.log').read())))
while True:
    line = log.readline()
    # line = line.replace('\0', "", 3)
    cnt_line +=1
    if line != '':
            plot_data_red.append(int(line))
    if not line or cnt_line == CNT_PART_DATA:
        log.close()
        print("STOP PARSING-->", line)
        break
for i in range(len(plot_data_red)):
    average += plot_data_red[i]

average /= len(plot_data_red)
print(average)
print(len(plot_data_red))
# for i in range(len(plot_data_red)):
#     sub_plot_data_red.append(plot_data_red[i] - average)

# for i in range(len(sub_plot_data_red) - 5):
#     move_average.append(sub_plot_data_red[i] + sub_plot_data_red[i + 1]  + sub_plot_data_red[i + 2] +
#                         sub_plot_data_red[i + 3] + sub_plot_data_red[i + 4] + sub_plot_data_red[i + 5])

# plt.plot(plot_data_red, label="RED")
filter_data = signal.filtfilt(b, a, plot_data_red)
# plt.plot(plot_data_red, label="GREEN")
plt.plot(filter_data, label="RED")
plt.legend()
plt.show()
