#تابعمون
def is_div_Prime(div):
    is_Prime = True
    if (div == 1):
        is_Prime = False

    for k in range(2 , div):
        if (div % k == 0):
            is_Prime = False
    return is_Prime
#لیستی که درست کردیم
numbers = []
for i in range(10):
    x = int(input("enter number: "))
    numbers.append(x)
print(numbers)

#اعمال تابع روی لیستمون  و ریختنش توی دیکشنری
main_list = []
for num in numbers:
    counter = 0
    for div in range(1 , num+1):
        #چک بخش پذیری  #چک اول بودن 
        if ((num % div == 0) and is_div_Prime(div) == True):
            counter+=1
    dict = {'number' : num , 'div' : counter}
    main_list.append(dict)
print(main_list)

sorted_main_list = sorted(main_list ,key =lambda x: x['div'] , reverse=True ) #x represents each element in the iterable being sorted. x['div'] accesses the value associated with the key 'div' in the dictionary x.
print(sorted_main_list)

max_num = 0
max_div = 0
for index in main_list:
    if (index['div'] >= max_div and index['number'] > max_num):
        max_num = index['number']
        max_div = index['div']
print(max_num , max_div)
#sorted(iterable, key=None, reverse=False)
#iterable: This is the sequence (e.g., list, tuple, etc.) that you want to sort.
#key (optional): This parameter specifies a function that will be called on each element of the iterable. The return value of this function will be used for sorting. If None, it simply sorts the elements based on their natural order.
#reverse (optional): This parameter is a boolean value. If set to True, the elements are sorted in descending order. By default, it's False, meaning the elements are sorted in ascending order.




