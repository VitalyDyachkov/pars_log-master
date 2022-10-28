import matplotlib.pyplot as plt
import re

CNT_PART_DATA = 100000

log = open("SPO2_LOG.log", 'r')
new_data_ir = open("IR_DATA.txt", 'w')
new_data_red = open("RED_DATA.txt", 'w')

plot_data_red = []
plot_data_ir = []
cnt_line = 0
print("START PARSING, LEN ->", len(re.findall(r"[\n']+", open('SPO2_LOG.log').read())))
while True:
    line = log.readline()
    line = line.replace('\0', "", 3)
    cnt_line +=1
    if line != '':
        if line[0] == '1':
            new_data_ir.write(line[8:])
            plot_data_ir.append(int(line[8:13]))
        if line[0] == '2':
            new_data_red.write(line[8:])
            plot_data_red.append(int(line[8:13]))
    if not line or cnt_line == CNT_PART_DATA:
        log.close()
        new_data_ir.close()
        new_data_red.close()
        print("STOP PARSING-->", line)
        break

plt.plot(plot_data_red, label="RED")
plt.plot(plot_data_ir, label="IR")
plt.legend()
plt.show()
