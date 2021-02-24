z = list(map(int, input().split()))
B = z[0]
L = z[1]
D = z[2]
book_score = list(map(int, input().split()))
lib = []
num_of_books = []
sign_up_days = []
ship = []
for i in range(0, L):
    x = list(map(int, input().split()))
    num_of_books.append(x[0])
    sign_up_days.append(x[1])
    ship.append(x[2])
    sorter = {}
    y = list(map(int, input().split()))
    for j in y:
        sorter[book_score[j]] = j
    l = list(sorter.items())
    l.sort()
    l.reverse()
    m = []
    for j in l:
        m.append(j[1]) 
    lib.append(m)
sign_up = []
days = 0
property_to_sort = []
for i in range (0, L):
    score = 0
    for j in range(0, num_of_books[i]):
        score += book_score[lib[i][j]]
    property_to_sort.append(score)
score = 0
temp2 = property_to_sort.copy()
temp2.sort()
temp2.reverse()
sign_dates = {}
for i in temp2:
    d = property_to_sort.index(i)
    if days + sign_up_days[d] < D:
        sign_up.append(d)
        days += sign_up_days[d]
        sign_dates[d] = days
    else:
        break
lib_book = {}
order = []
done = []
for i in range(0, L):
    order.append(0)
for i in sign_up:
    flag = 0
    counter = 0
    n = 0
    temp = []
    while True:
        if sign_dates[i] + ship[i] < D:
            j = 0
            while (j < ship[i]): # and counter < len(lib[i])
                if counter + j < len(lib[i]): 
                    if lib[i][counter + j] not in done:
                        n += 1
                        temp.append(lib[i][counter + j])
                        score += book_score[lib[i][counter + j]]
                        done.append(lib[i][counter + j])
                else:
                    flag = 1
                    break
                j += 1
            counter += j           
        else:
            break
        if flag == 1:
            break
    lib_book[i] = n
    order[i] = temp    
print(len(sign_up))
for i in sign_up:
    print(i, lib_book[i])
    print(order[i])
print(score)