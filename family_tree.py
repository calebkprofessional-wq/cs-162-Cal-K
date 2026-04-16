
class Person:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def search(self, target):
        if self.name == target:
            return self

        for child in self.children:
            result = child.search(target)
            if result is not None:
                return result

        return None


alice = Person("Alice")
bob = Person("Bob")
carol = Person("Carol")
daniel = Person("Daniel")
emma = Person("Emma")
frank = Person("Frank")

alice.add_child(bob)
alice.add_child(carol)
bob.add_child(daniel)
carol.add_child(emma)
carol.add_child(frank)

result = alice.search("Carol")

if result:
    print(f"{result.name} found!")
    if result.children:
        print(f"{result.name} has {len(result.children)} children:", [child.name for child in result.children])
    else:
        print(f"{result.name} has no children.")
else:
    print("Person not found.")