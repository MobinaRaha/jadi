genre_count = {
"Horror" : 0,
"Romance" : 0,
"Comedy" : 0,
"History" : 0,
"Adventure" : 0,
"Action" : 0}
participant = int(input("enter the number of participant: "))
for i in range(participant):  
    name_genre = input("enter name and choose one of genres: Horror,Romance,Comedy,History,Adventure,Action: ")
    name , genre = name_genre.split(maxsplit=1)  #اسم رو از ژانر جدا میکنه
    #The line name , genre = name_genre.split(maxsplit=1) is used to split the input string name_genre into two parts: the name and the genre.
    #The maxsplit=1 argument specifies that the split should only occur once, which means it will split the string into two parts at the first occurrence of whitespace.
    genre_splited = genre.split(" ")
    genre_list = [word.capitalize() for word in genre_splited]
    print(genre_list)
    
    for items in genre_list:
         if items in genre_count:
            genre_count[items]+=1
            

sorted_genre_count = dict(sorted(genre_count.items(), key = lambda item: (item[1] , item[0])))

print(sorted_genre_count)



 #برای چک کردن اینکه یه استرینگ توی دیکشنری وجود داره یا نه

