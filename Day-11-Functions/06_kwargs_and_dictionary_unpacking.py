# Day 11 - **kwargs and Dictionary Unpacking

def arbitrary_named_args(**args):
    print("Type:", type(args))
    print("Number of arguments:", len(args))
    for key, value in args.items():
        print("Key:", key, "| Value:", value)

arbitrary_named_args(name="Alice", age=30, city="New York")

def greet(name, location):
    return f"Hi there {name}, how is the weather in {location}?"

person = {"name": "Alice", "location": "New York"}
print(greet(**person))

def show_profile(name, **details):
    print("Name:", name)
    for key, value in details.items():
        print(f"{key}: {value}")

show_profile("Bob", age=25, city="Delhi", skill="Python")
