import random
import time

operators=["+","-","*"]
min_operand=3
max_operand=30
total_problems=10

def generate_question():
    left=random.randint(min_operand,max_operand)
    right=random.randint(min_operand,max_operand)
    operator=random.choice(operators)
    
    expr=str(left)+" "+operator+" "+str(right)
    answer=eval(expr)
    return expr, answer

wrong=0
input("Press enter to start! ")
print("------------------------")
start_time=time.time()

for i in range(total_problems):
    expr, answer=generate_question()
    while True:
        guess=input("Problem #"+str(i+1)+": "+expr+"= ")
        if guess==str(answer):
            break
        else:
            print("Wrong answer try again: ")
        wrong+=1

end_time=time.time()
total_time=round(end_time-start_time, 2)
print("-----------------------------------")
print("Nice work! You finished in", total_time, "seconds!")
