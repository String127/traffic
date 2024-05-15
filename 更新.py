if type(cell_list_before[cell]) is str:
    a_v = cell_list[(cell + L_car - 1) % Length_road]
    s_v = cell_list[(cell + L_car - 1) % Length_road]
    dnt = l_empty(cell)  # 车间距
    v_f = cell_list_before[(cell + L_car - 1 + dnt + L_car) % Length_road]
    if cell_list_before[cell] is 'Hm':
        d_safe = front_car_speed(v_f, s_v, af_h, tao_h)
        v_safe = safe_speed(af_h, tao_h)
    else:
        d_safe = front_car_speed(v_f, s_v, af_a, tao_a)
        v_safe = safe_speed(af_a, tao_a)
    if dnt > d_safe:
        s_v = min(s_v + acc, V_max, v_safe, dnt)
    elif dnt < d_safe:
        if v_f == 0:
            s_v = max(min(v_safe, dnt - 1), 0)
        else:
            s_v = max(min(v_safe, dnt), 0)
    else:
        s_v = min(s_v, dnt)
    if cell_list_before[cell] is 'Hm':
        s_v = speed_random_slow(s_v)
    A = s_v - a_v

    h = s_v
    cell_list[cell] = None
    cell_list[(cell + L_car - 1) % Length_road] = None
    if cell_list_before[cell] is 'Ai':
        cell_list[(cell + h) % Length_road] = 'Ai'
    else:
        cell_list[(cell + h) % Length_road] = 'Hm'
    cell_list[(cell + h + L_car - 1) % Length_road] = h