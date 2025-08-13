def smallest_average(person1: dict, person2: dict, person3:dict):
    people = [person1, person2, person3]
    smallest_avg = 10
    smallest = person1

    for person in people:
        avg = (person["result1"] + person["result2"] + person["result3"]) / 3
        if avg <= smallest_avg:
             smallest = person
             smallest_avg = avg
    
    return smallest

if __name__ == "__main__":
    person1 = {"name": "Jamie", "result1": 0, "result2": 0, "result3": 0}
    person2 = {"name": "Jamie", "result1": 5, "result2": 6, "result3": 9}
    person3 = {"name": "Jamie", "result1": 1, "result2": 10, "result3": 3}

    people = [person1, person2, person3]

   
    print(smallest_average(person1, person2, person3))