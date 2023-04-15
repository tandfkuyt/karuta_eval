# coding: utf-8

import module.fuda_list as fl

def calc_value(jijin :list, tekijin :list, defuda :list):
    fuda_index = fl.get_fuda_index()
    jijin_fudaset = read_fudaset(jijin, fuda_index)
    tekijin_fudaset = read_fudaset(tekijin, fuda_index)
    defuda_fudaset = read_fudaset(defuda, fuda_index)
    j_point = count_point(jijin_fudaset, defuda_fudaset)
    t_point = count_point(tekijin_fudaset, defuda_fudaset)

    hyokachi = (j_point - t_point) / (j_point + t_point) * -100

    return hyokachi

def read_fudaset(jin :list, fuda_index :dict):
    fudaset = []
    for fuda in jin:
        if fuda:
            fudaset.append(fuda_index[fuda])
    return fudaset

def count_point(jin :list, defuda: list):
    point_sum = 0
    for jfuda in jin:
        h = 0
        i = 0
        j = 0
        if len(fl.fuda_list[jfuda].tomofuda) > 0:
            for jtfuda in fl.fuda_list[jfuda].tomofuda:
                if jtfuda in jin or jtfuda in defuda:
                    j += 1
            if j == len(fl.fuda_list[jfuda].tomofuda):
                i += 1
        j = 0
        if i == 1:
            if len(fl.fuda_list[jfuda].tomo_2) > 0:
                h += 1
                for jt2fuda in fl.fuda_list[jfuda].tomo_2:
                    if jt2fuda in jin or jt2fuda in defuda:
                        j += 1
                if j == len(fl.fuda_list[jfuda].tomo_2):
                    i += 1
        j = 0
        if (i == 1 and h == 0) or (i == 2 and h == 1) or len(fl.fuda_list[jfuda].tomofuda) == 0:
            if len(fl.fuda_list[jfuda].initial) > 0:
                for jifuda in fl.fuda_list[jfuda].initial:
                    if jifuda in jin or jifuda in defuda:
                        j += 1
                if j == len(fl.fuda_list[jfuda].initial):
                    i += 1
        point = fl.fuda_list[jfuda].jisu[i]
        point_sum += point
    return point_sum


