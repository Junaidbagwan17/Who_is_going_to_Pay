est_seed = int(input("any number :"))
random.seed(test_seed)

name_as_csv = input("give me everybodys name seprated by ','.:\n").split(",")#we split by comma and it will goes to list .
num_items = len(name_as_csv) # we taken len because we dont know how the long list is !
random_choice = random.randint(0,num_items -1)# always we start count feom zero and (-1 from the other end.)
who_will_pay = name_as_csv[random_choice]# it will pick names between 0 to total names minus 
print(f"{who_will_pay} is going to pay the total bill !")
