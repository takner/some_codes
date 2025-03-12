import random

priority_1 = ["KIA K5","Nissan Altima","BYD Song Plus","Mitsubishi Outlander"]
priority_2 = ["Volkswagen T ROC","Toyota CHR","KIA Sportage","Hyundai Sonata"]
priority_3 = ["BYD Song Plus","Hyundai Tucson","Hyundai Elantra","Mitsubishi Eclipse"]
people = ["کیان", "مهدی", "بابا", "مامان"]
car_choices = {}

selected_priority_3 = set()
people = random.sample(people, len(people))

random_state = random.getstate()  

random.shuffle(priority_1)
random.setstate(random_state) 
random.shuffle(priority_2)

for person in people:
    choices = []

    index = people.index(person)  
    choice_1 = priority_1[index]
    choice_2 = priority_2[index]
    choices.append(choice_1)
    choices.append(choice_2)
        
    available_priority_3 = [car for car in priority_3 if car not in selected_priority_3]
    if available_priority_3:
        choice_3 = random.choice(available_priority_3)
        choices.append(choice_3)
        selected_priority_3.add(choice_3)
    else:
        choices.append("error") 
        
    car_choices[person] = choices

for person, choices in car_choices.items():
    print(f"انتخاب‌های {person}:")
    print(f"  اولویت اول: {choices[0]}")
    print(f"  اولویت دوم: {choices[1]}")
    print(f"  اولویت سوم: {choices[2]}")
    print("-" * 20)
