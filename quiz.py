import time
print("<== Welcome to the quiz ==>")
time.sleep(1)
user= input("Enter your name: ")
print(f"Hello, {user}! Let's start the quiz.")
time.sleep(1)
print("You will be asked 10 questions. Each correct answer will earn you 10 points.")
global score
score = 0
class ques:
    Data={}
    q1 = input("1.What is the full form of the ISRO?:\n(a) Indian South Research Organization\n(b) Indian Space Ready Organization\n(c) Indian Space Research Organization\n(d) None of these\n Your Answer: ").lower()
    que = True
    if q1 == 'c':
       score += 10
    else:
        que = False
    Data["Question 1"] = que
    q2= input("2.What is the name of our President?:\n(a) Drishti Mauyra\n(b) Sita Mangla\n(c) Raj Tiwari\n(d) Dropadi Murmu\n Your Answer: ").lower()
    que = True
    if q2 == 'd':
       score += 10
    else:
        que = False
    Data["Question 2"] = que
    q3= input("3.Where was the khalsa Panth Found?:\n(a) Ludhiana\n(b) Anandpur Sahib\n(c) Ramnagar\n(d) Panchkula\n Your Answer: ").lower()
    que = True
    if q3 == 'b':
       score += 10
    else:
        que = False
    Data["Question 3"] = que
    q4= input("4.Whos is known as ironman of India?:\n(a) Sardar Vallabhai Patel\n(b) Rajendra Prasad\n(c) APJ Abdul Kalam\n(d) Lal Bahadur Shastree\n Your Answer: ").lower()
    que  = True
    if q4 == 'a':
       score += 10
    else:
        que = False
    Data["Question 4"] = que
    q5= input("5.Who wrote the book 'God of small things'?:\n(a) Kiran Bedi\n(b) Pankaj Dhiru\n(c) Arundhati Roy\n(d) Chandan Kumar\n Your Answer: ").lower()
    que = True
    if q5 == 'c':
       score += 10
    else:
        que = False
    Data["Question 5"] = que
    q6= input("6.The infamous gas tragedy of india took place in?:\n(a) Kolkata\n(b) Bhopal\n(c) Chennai\n(d) Old-Delhi\n Your Answer: ").lower()
    que = True
    if q6 == 'b':
       score += 10
    else:
        que = False
    Data["Question 6"] = que
    q7= input("7.Which state is known as the land of rising sun?:\n(a) Arunanchal Pradesh\n(b) Kashmir\n(c) Kerela\n(d) Gujarat\n Your Answer: ").lower()
    que = True
    if q7 == 'a':
       score += 10
    else:
        que = False
    Data["Question 7"] = que
    q8= input("8.When & Were did the last common wealth game take place in India:\n(a) Mumbai (2008)\n(b) Gujarat (2006)\n(c) New-Delhi (2010)\n(d) Lucknow (2008)\n Your Answer: ").lower()
    que = True
    if q8 == 'c':
       score += 10
    else:
        que = False
    Data["Question 8"] = que
    q9= input("9.Which one is not a neighbouring country of India?:\n(a) Afghanistan\n(b) Myanmmar\n(c) Thailand\n(d) Sri-Lanka\n Your Answer: ").lower()
    que = True
    if q9 == 'c':
       score += 10
    else:
        que = False
    Data["Question 9"] = que
    q10= input("10.Longest Serving Prime Minister of India?:\n(a) Narendra Modi\n(b) Jawaharlal Nehru\n(c) Indira Gandhi\n(d) Atal Bihari Vajpayee\n Your Answer: ").lower()
    que = True
    if q10 == 'b':
       score += 10
    else:
        que = False
    Data["Question 10"] = que
    
time.sleep(1)
print("evalualting....")
time.sleep(1)
for q_name,q_status in ques.Data.items():
    if q_status == True:
        score += 10
        print(f"{q_name}: Right Answer! 🎉 (+10 points) | Current Score: {score}")
    else:
        print(f"{q_name}: Wrong Answer! ❌ (+0 points) | Current Score: {score}")

print(f"\nFinal Score: {score}/100")