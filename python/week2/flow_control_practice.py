### Exercise 1 — Age Checker

age = int(input("Enter your age here: "))

if age < 18:
    print("You are a minor.")
else:
    print("You are an adult.")



### Exercise 2 — Grade Calculator

score = int(input("Enter your score here: "))
if score < 0 or score > 100:
    print("Invalid score.")
elif score >= 80:
    print("A")
elif score >= 70:
    print("B")
elif score >= 60:
    print("C")
elif score >= 50:
    print("D")
else:
    print("F")
### Exercise 3 — Countdown Timer

for i in range(10,0,-1):
    print(F'{i}')
print(f'Blast off!')