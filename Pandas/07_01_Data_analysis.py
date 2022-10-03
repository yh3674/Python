# %%
US_PRESIDENT = ['GEORGE Washington','Donald Trump','Barak Obama', 'Bill Clinton']
US_PRESIDENT.append('Harry Truman')
US_PRESIDENT

# %%
# 제거
US_PRESIDENT.remove('GEORGE Washington')
US_PRESIDENT

# %%
from random import randint
randint(0,10)

# %%
US_PRESIDENT[randint(0,4)]


# %%
# 특정 위치 insert
US_PRESIDENT.insert(1,'Bill Clinton')
US_PRESIDENT



# %%
# formatting
car_name = 'Cadillac Escalade'
car_price = '$120,000'

# Statement = 'I would like to buy a %s and %s is quite expensive.'%(car_name,car_price)
# Statement

statement1 = 'I would like to buy a {0} and {1} is quite expensive.'.format(car_name,car_price)
statement1

# %%
i = 0

while i < 10:
    print("현재 i의 값은 %d입니다." %i)
    i += 1
    
    
for i in range(0,10):
    print("현재 i의 값은 %d입니다." %i)
    i += 1


# %%
US_PRESIDENT = ['GEORGE Washington','Donald Trump','Barak Obama', 'Bill Clinton']
US_PRESIDENT.append('Harry Truman')
US_PRESIDENT

for i in US_PRESIDENT:
    print('미국 대통령 중 한명의 이름은 %s입니다.' %i)
   

# %%
# i < 10
# y < 10

# for i in range(3, 10):
#     for y in range (1,10):
#         print ('==={%d}단 시작 ==='%i)
#         print('')

for i in range(3,5):
    print (" ===%d단 시작 ===" %i)

    for y in range (1,10):
        print ("%d X %d = %d" %(i,y,i*y))

# %% [markdown]
# 

# %% [markdown]
# ### Creating Module (Calculator)

# %%
def add(num1, num2):
    return num1 + num2

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/ 2/ 3/ 14): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")

# %%


# %%


# %%


# %%


# %%



