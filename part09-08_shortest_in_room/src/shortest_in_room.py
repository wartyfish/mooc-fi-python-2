class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name
    
class Room:
    def __init__(self):
        self.people = []

    def add(self, person: Person):
        self.people.append(person)

    def is_empty(self):
        if len(self.people) == 0:
            return True
        else:
            return False
        
    def print_contents(self):
        combined_height = sum(person.height for person in self.people)
        print(f"There are {len(self.people)} persons in the room, and their combined height is {combined_height} cm")
        for person in self.people:
            print(f"{person.name} ({person.height} cm)")

    def shortest(self):        
        if self.is_empty():
            return None
        else:
            shortest_person = self.people[0]
            for person in self.people:
                if person.height < shortest_person.height:
                    shortest_person = person
            return shortest_person

    def remove_shortest(self):
        if self.is_empty():
            return None
        else:
            removed = self.shortest()
            self.people.remove(removed)
            return removed

if __name__ == "__main__":
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()