#Actually ***LIST*** in python3 analog of arrays in js
# https://ischurov.github.io/pythonvjs/show/lists-arrays/ru/
# https://pythonworld.ru/tipy-dannyx-v-python/spiski-list-funkcii-i-metody-spiskov.html

#create
yolist = [1,2,3,4,"test"]

#add
yolist.append(5)

#add multiple
yolist.extend([6,7])

#create with constructor
mylist = list('Hello')

#cahnge
mylist[0] = "F"

#length
len(mylist)

#extend one array with ither array in js push
other_list = [8, 9, 10]
yolist.extend(other_list)

#you cant do this mylist["0"] just do mylist[0]

#concat in js here +
first_list = [1,2,3]
second_list = [4,5,6]
result_list = first_list + second_list

#delete by index
del first_list[0]

#emty array
first_list.clear()


#добавить элемент вне диапазона
# second_list[6] = 100 return exception

#in проверяет находится ли элемент в списке return true or False
7 in first_list

#slice
our_list = [1,2,3,4,5,6,7,8,9]

# print(our_list[2:4])  #[3,4]
# print(our_list[:4])   #[1,2,3,4]
# print(our_list[4:])  #[5,6,7,8,9]
# print(our_list[2:-2])  #[3,4,5,6,7]
# print(our_list[:])  #[1,2,3,4,5,6,7,8,9]   [0:len(our_list)]
# print(our_list[2:6:2])  #[3,5]  [2:с 6 индекса назад на 2 индекса]
# print(our_list[4:2:-1])  #[5,4]  [4:со 2 индекса следующий индекс]

#fragments manipulation in js is splice
fragment = [1,2,3,4,5]
# fragment[2:4] = [30, 40] ## [1,2,30,40,5]

# fragment[1:2] = []  ##[1,3,4,5]

fragment[3:3] = [999] #analog in splice(3, 0, 999)
#return [1,2,3,999, 4,5]

print(fragment)

