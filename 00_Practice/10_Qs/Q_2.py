prv_num = 0
cur_num = 0

for i in range(1,11):
    print("Current number =", cur_num, ";", "Previous number =", prv_num, ";", "Sum =", cur_num + prv_num)

    prv_num = cur_num
    cur_num += 1