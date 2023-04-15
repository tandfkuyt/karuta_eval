# coding: utf-8

import csv
from module.calc_value import calc_value

def main():

    jin1 = []
    jin2 = []

    with open('inputs/jin1.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            jin1.extend(row)
    with open('inputs/jin2.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            jin2.extend(row)
    with open('inputs/game_history.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            history = [row for row in reader]

    eval_list = eval_transition(jin1, jin2, history)

    with open('calc_result.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(eval_list)

    print('calculation is success')

def eval_transition(jin1, jin2, history):
    defuda = []
    result = [['枚目',  '評価値']]
    
    hyokachi = calc_value(jin1, jin2, defuda)
    result.append([0, hyokachi])

    for i in history:
        defuda.append(i[1])
        if i[1] in jin1:
            jin1.remove(i[1])
        elif i[1] in jin2:
            jin2.remove(i[1])
        if i[2]:
            if i[2] in jin1:
                jin1.remove(i[2])
                jin2.append(i[2])
            elif i[2] in jin2:
                jin2.remove(i[2])
                jin1.append(i[2])
        if i[3]:
            if i[3] in jin1:
                jin1.remove(i[3])
                jin2.append(i[3])
            elif i[3] in jin2:
                jin2.remove(i[3])
                jin1.append(i[3])
        hyokachi = calc_value(jin1, jin2, defuda)
        result.append([i[0], hyokachi])

    return result


if __name__ == '__main__':
    main()

