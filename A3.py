"""

"""


def ins_sort(mylst):
    for i in range(1, len(mylst)):
        key = mylst[i]
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < mylst[j]:
            mylst[j+1] = mylst[j]
            j = j - 1
        mylst[j+1] = key
    return mylst


def listsum(lst):
    lstsum = 0
    for i in lst:
        lstsum += i
    return lstsum


def conver_to_int(arr):
    arr1 = []
    for i in range(len(arr)):
        arr1 += [int(arr[i])]
    return arr1


def open_file(config):
    arr = []
    grade1 = []
    perc, per = [], []
    f = open(config, 'r')
    for i in f:
        arr += [i]
    f.close()
    arr1 = arr[0].split(',')
    arr2 = arr[2].split(',')
    arr3 = arr[1].split(' ')
    st = []
    for i in arr3:
        s = [i[0]] + [i[1:][0:2]]
        st += [s]
    print(st)
    f1 = open(arr1[0], 'r')
    # grade = [[j for j in i.split(',')]for i in f1]
    for i in f1:
        gr = []
        i = i.split(',')
        for j in range(len(i)):
            if j >= 2:
                gr += [int(i[j])]
            else:
                gr += [i[j]]
        grade1 += [gr]
    f1.close()
    for i in range(1, 17, 3):
        per = []
        for j in range(i, i + 3):
            per += [int(arr1[j])]
        perc += [per]
    grd1 = []
    for i in arr2:
        grd = []
        for j in range(0, 2):
            if i[j] == '-' and j == 1:
                grd = [i[0:2]] + [float(i.split('-')[2])]
            elif i[j] == '+' and j == 1:
                grd = [i[0:2]] + [float(i.split('-')[1])]
            else:
                grd = [i[0]] + [float(i.split('-')[1])]
        grd1 += [grd]
    return grade1, perc, grd1, st  # Return multiple value to avoid using multiple functions


def sort_func(arr, left, maxval, per):
    # print(arr)
    arrsum = listsum(arr) / left
    perc = arrsum / maxval * per
    return perc, arrsum  # arrsum is the grade for the individual assignment - we need this for the average grade T.X
    # and so on


def stu_grading(datfil, dat, grade_arr, perc):  # Returns letter grade of a student
    gr, j, x, y = 0, 0, 0, 0
    g = []
    i = 2
    lgt = len(datfil)
    while i != lgt:
        lst = dat[j]
        maxdrop = -(lst[1])
        left = lst[0] + lst[1]
        arr = datfil[i: i+lst[0]]
        arr = conver_to_int(arr)
        arr = ins_sort(arr)
        arr = arr[maxdrop:]
        x, y = sort_func(arr, left, lst[2], int(perc[j][1]))
        gr += x
        g += [int(y)]
        i += lst[0]
        j += 1
    datfil += g
    for i in range(len(grade_arr)-2):
        if int(grade_arr[i][1]) > gr > int(grade_arr[i+1][1]):
            fin_grade = grade_arr[i][0]
            datfil += [fin_grade]
            return datfil


def write_to_file(nms, tstnos, grds, percs):
    f = open('final_file.csv', 'w')
    head_row = ['Student Name', 'Student ID']
    for i in range(6):
        tst = tstnos[i]
        grd_no = 0
        assign_nm = percs[i][grd_no]
        while grd_no < int(tst[0]):
            str1 = assign_nm+'.'+str(grd_no+1)
            head_row += [str1]  # Adding grades based on how many
            # grades are being removed from each Assignment
            grd_no += 1
    head_row += ['T.X Avg', 'L.X Avg', 'Q.X Avg', 'A.X Avg', 'P.X Avg', 'B.X Avg', 'Final Grade']
    for i in head_row:
        f.write(i)
        f.write(',')
    f.write('\n')
    for name in nms:
        arr = stu_grading(name, tstnos, grds, percs)
        for i in arr:
            f.write(str(i))
            f.write(',')
        f.write('\n')
    f.close()


def main():
    conf = 'config.txt'
    names, testnos, grades, percentages = open_file(conf)
    # Reassign percentages to match the configuration
    a = percentages[0]
    q = percentages[3]
    t = percentages[0] = percentages[2]
    percentages[2] = percentages[3]
    percentages[3] = a
    # print(names, '\n', testnos, '\n', grades, '\n', percentages)
    write_to_file(names, testnos, grades, percentages)


main()
