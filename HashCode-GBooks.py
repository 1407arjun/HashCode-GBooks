file_input = open("c_incunabula.txt", "r")
Z = list(map(int, file_input.readline().split()))
B = Z[0]
L = Z[1]
D = Z[2]
book_score = list(map(int, file_input.readline().split()))
lib = {}
num_of_books = []
sign_up_days = []
ship = []
for i in range(0, L):
    x = list(map(int, file_input.readline().split()))
    num_of_books.append(x[0])
    sign_up_days.append(x[1])
    ship.append(x[2])
    scores = []
    y = list(map(int, file_input.readline().split()))
    for j in y:
        scores.append(book_score[j])
    z = [r for _,r in sorted(zip(scores,y))]
    z.reverse()
    lib[i] = z

file_input.close()

sign_up = []
sdays = 0
sign_dates = {}
total = 0
order = []

while True:
        property_to_sort = {}
        for i in lib:
            score = 0
            for j in range(0, len(lib[i])):
                score += book_score[lib[i][j]]
            property_to_sort[(score*ship[i])//sign_up_days[i]] = i
        current = property_to_sort[max(list(property_to_sort.keys()))]
        if sdays + sign_up_days[current] < D:
            sdays += sign_up_days[current]
            sign_up.append(current)
            sign_dates[current] = sdays
        else:
            break            

        i = current
        flag = 0
        counter = 0
        n = 0
        temp_store = []

        while True:
            if sign_dates[i] + ship[i] < D:
                j = 0
                while (j < ship[i]):
                    if counter + j < len(lib[i]): 
                        n += 1
                        temp_store.append(lib[i][counter + j])
                        total += book_score[lib[i][counter + j]]
                    else:
                        flag = 1
                        break
                    j += 1
                counter += j           
            else:
                break
            if flag == 1:
                break
        order.append([i, temp_store])    

        temp = lib[current].copy()
        del lib[current]
        if lib != {}:
            for i in lib:
                lib[i] = list(set(lib[i]) - set(temp))    
        else:        
            break

file_output = open("answer_c.txt", "w")
file_output.write(str(len(sign_up)) + "\n")
for i in order:
    file_output.write(str(i[0]) + " " + str(len(i[1])) + "\n")
    file_output.write((' '.join(list(map(str, i[1])))) + "\n")
file_output.close()
