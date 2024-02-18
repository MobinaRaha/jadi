number = int(input("num: "))
final_list = []
for i in range(number):
    input_data = input("datails: ").split(".")
    gender = input_data[0].lower()
    name =input_data[1].capitalize()
    lang = input_data[2].lower()
    main = gender +" "+ name+ " " + lang
    final_list.append(main)
    
sorted_final_list = sorted(final_list , key= lambda x: x.startswith('f') , reverse=True)
for index in sorted_final_list:
    print(index)



