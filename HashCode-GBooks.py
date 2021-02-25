file_input = open("d_tough_choices.txt", "r")
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
            t = lib[i][0:(D-sdays-sign_up_days[i])*ship[i]].copy()
            for j in range(0, len(t)):
                score += book_score[t[j]]
            property_to_sort[score//sign_up_days[i]] = i
        for i in list(property_to_sort.keys()):   
            current = property_to_sort[max(list(property_to_sort.keys()))]
            flag1 = 0
            if sdays + sign_up_days[current] <= D:
                flag1 = 1
                sdays += sign_up_days[current]
                sign_up.append(current)
                sign_dates[current] = sdays
                break
            else:
                del property_to_sort[i]  
        if flag1 == 0:
            print("sort")
            print(total)
            break            

        i = current
        flag = 0
        counter = 0
        n = 0
        temp_store = []

        while True:
            if sign_dates[i] + ship[i] <= D:
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
            print("remove")
            print(total)        
            break

file_output = open("answer_c.txt", "w")
file_output.write(str(len(sign_up)) + "\n")
for i in order:
    if len(i[1]) != 0:
        file_output.write(str(i[0]) + " " + str(len(i[1])) + "\n")
        file_output.write((' '.join(list(map(str, i[1])))) + "\n")
file_output.close()
