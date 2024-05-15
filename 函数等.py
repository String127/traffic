# 前车距离（本车道）-跟驰
def l_empty(l_apt):  # 传入的是车尾
    sum_empty1 = 0
    for j1 in range((l_apt + L_car) % Length_road, Length_road):
        if cell_list_before[j1] is None:
            sum_empty1 = sum_empty1 + 1  # 找到头要是都是空的，就从头开始找，接着下面的循环接着累加
        else:
            return sum_empty1
    for j1 in range(0, l_apt):
        if cell_list_before[j1] is None:
            sum_empty1 = sum_empty1 + 1
        else:
            return sum_empty1


# 加车函数
def mix_add(car_b):  # 全均匀加车
    the_num_car = (Length_road - b * L_car) / b
    pos = random.randint(0, Length_road - 1)  # 第一辆车的位置
    Ai_car = int(mix * car_b)  # 人机共驾
    Hm_car = int(car_b - car_b * mix)  # 人类驾驶
    car_pool = [0] * Hm_car + [1] * Ai_car
    random.shuffle(car_pool)  # 这里已经打乱了
    l_speed = random.randint(0, V_max)
    for lof in car_pool:
        if lof == 0:
            cell_list[pos] = 'Hm'  # 人类驾驶车辆
            cell_list[(pos + L_car - 1) % Length_road] = l_speed  # 车头
        else:
            cell_list[pos] = 'Ai'  # 人机共驾
            cell_list[(pos + L_car - 1) % Length_road] = l_speed  # 车头
        pos = int((pos + the_num_car + L_car) % Length_road)  # 下一辆车的车尾位置


# 新的求平均速度的函数
def get_Average_speed(gf1, gf2):
    ssum1 = 0
    flag1 = 0
    for gas in range(gf1, gf2):
        if type(cell_list[gas]) is int:
            flag1 += 1
            ssum1 = ssum1 + cell_list[gas]
    # 返回分别为本车道平均速度,临车道平均速度和总平均速度
    return ssum1 / flag1


# 计算安全距离
def front_car_speed(vf, v_now, AF2, t1):
    vn1 = v_now
    vn2 = vf
    if int((vn1 * t1 + (vn1 ** 2 - (vn2 * AF2) ** 2) / (2 * dec))) < 0:
        return 0
    else:
        return int((vn1 * t1 + (vn1 ** 2 - (vn2 * AF2) ** 2) / (2 * dec)))  # 安全距离是小数，向上取整，即加1向下取整


# 计算安全速度
def safe_speed(AF1, t2):
    return int(
        max(max(((dec * t2) ** 2 + dec * 2 * dnt - dec * t2 * s_v + (v_f * AF1) ** 2), 0) ** 0.5 - dec * t2, 0))


# 随机慢化
def speed_random_slow(a1):
    rp = random.random()
    p = 0.1 + 0.4 * ((1 + M * (math.e ** (-0.05 * rou))) ** (1 / -0.95))
    if rp < p:
        return max(0, a1 - dec)
    else:
        return a1


# 设置占用率
def ini_car_num():
    for icn in range(1, 51):
        sum1 = icn * 8
        Rn.append(sum1)
