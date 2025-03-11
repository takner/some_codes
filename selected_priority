import random
priority_1 = ["Hyundai Tucson","KIA Sportage","Toyota CHR","BYD Song Plus"]
priority_2 = ["KIA K5","Hyundai Elantra","Nissan Altima","Hyundai Sonata"]
priority_3 = ["Mitsubishi Outlander","Volkswagen T ROC","Hyundai Kona","Mitsubishi Eclipse"]
people = ["کیان", "مهدی", "بابا", "مامان"]
car_choices = {}
selected_priority_1 = set()
selected_priority_2 = set()
selected_priority_3 = set()
for person in people:
    choices = []
    available_priority_1 = [car for car in priority_1 if car not in selected_priority_1]
    if available_priority_1:
        choice_1 = random.choice(available_priority_1)
        choices.append(choice_1)
        selected_priority_1.add(choice_1)
    else:
        choices.append("error") 
    available_priority_2 = [car for car in priority_2 if car not in selected_priority_2]
    if available_priority_2:
        choice_2 = random.choice(available_priority_2)
        choices.append(choice_2)
        selected_priority_2.add(choice_2)
    else:
        choices.append("error") 
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
