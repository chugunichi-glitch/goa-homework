# input არის ფუნქცია, რომლის საშუალებითაც მომხმარებელს შეუძლია პროგრამაში ინფორმაციის შეყვანა.


# Type casting არის მონაცემის ერთი ტიპიდან მეორე ტიპში გადაყვანა.


# int - მთელი რიცხვი
# age = 16
# float - ათწილადი რიცხვი
# height = 1.75
# str - ტექსტი
# name = "levani"
# bool - ჭეშმარიტი ან მცდარი მნიშვნელობა
# is_student = True


# == ამოწმებს, არის თუ არა ორი მნიშვნელობა ტოლი.
# != ამოწმებს, არ არის თუ არა ორი მნიშვნელობა ტოლი.
# > ამოწმებს, მეტია თუ არა პირველი რიცხვი მეორეზე.
# < ამოწმებს, ნაკლებია თუ არა პირველი რიცხვი მეორეზე.
# >= ამოწმებს, მეტია თუ ტოლია პირველი რიცხვი მეორეზე.
# <= ამოწმებს, ნაკლებია თუ ტოლია პირველი რიცხვი მეორეზე.


# num1 = int(input("შეიყვანე პირველი რიცხვი: "))
# num2 = int(input("შეიყვანე მეორე რიცხვი: "))
# print(num1 == num2)
# print(num1 != num2)
# print(num1 > num2)
# print(num1 < num2)
# print(num1 >= num2)
# print(num1 <= num2)


# age = int(input("შეიყვანე შენი ასაკი: "))
# print(age >= 18)


# speed = float(input("შეიყვანე სიჩქარე: "))
# distance = float(input("შეიყვანე გასავლელი მანძილი: "))
# time = float(input("შეიყვანე რამდენი საათი გაქვს: "))
# needed_time = distance / speed
# print(needed_time)
# print(needed_time <= time)


# price1 = float(input("შეიყვანე პირველი პროდუქტის ფასი: "))
# price2 = float(input("შეიყვანე მეორე პროდუქტის ფასი: "))
# price3 = float(input("შეიყვანე მესამე პროდუქტის ფასი: "))
# money = float(input("რამდენი თანხა გაქვს? "))
# total = price1 + price2 + price3
# print(total <= money)


# program_size = float(input("შეიყვანე პროგრამის ზომა GB-ში: "))
# free_space = float(input("შეიყვანე თავისუფალი ადგილი GB-ში: "))
# print(free_space >= program_size)


# math = float(input("შეიყვანე მათემატიკის ნიშანი: "))
# history = float(input("შეიყვანე ისტორიის ნიშანი: "))
# art = float(input("შეიყვანე ხელოვნების ნიშანი: "))
# average = (math + history + art) / 3
# print("საშუალო ნიშანია:", average)
# print(average > 5)





# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# result = num1 + num2
# print(result)

# num1 = int(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# result = num1 - 5 * num2
# print(result)

hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))
bonus = float(input("Enter bonus: "))
salary = hours * rate
total = salary + bonus
final_salary = total / 2
print(final_salary)

# price = float(input("Enter product price: "))
# quantity = float(input("Enter quantity: "))
# discount = float(input("Enter discount percentage: "))
# subtotal = price * quantity
# discount_amount = subtotal * discount / 100
# final_price = subtotal - discount_amount
# print(int(final_price))

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = float(input("Enter third number: "))
# total = num1 + num2
# average = total / num3
# remainder = average % 2
# result = int(remainder + num1)
# print(result)