class Person:
    def __init__(self, name, age):
        self.name = name  # Attribute
        self.age = age    # Attribute

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


data = {'test_case_1': [{'step': 1, 'action': 'Voice Invoke', 'object': 'Alexa', 'content': 'What is the weather', 'needimg': 'True', 'outputimage': 'Invoke_Alexa_ask_weather', 'time': 10, 'city': 'New York'}, 
                        {'step': 2, 'action': 'Click', 'object': 'Alexa', 'content': 'Cancel-Button', 'needimg': 'True', 'outputimage': 'Click_Cancel_Button', 'time': 10, 'city': 'New York'}], 
        'test_case_2': [{'step': 1, 'action': 'Voice Invoke', 'object': 'Google', 'content': 'What is the weather', 'needimg': 'True', 'outputimage': 'Invoke_Alexa_ask_weather', 'time': 10, 'city': 'New York'}, 
                        {'step': 2, 'action': 'Click', 'content': 'Cancel-Button', 'object': 'Google', 'needimg': 'True', 'outputimage': 'Click_Cancel_Button', 'time': 10, 'city': 'New York'}]}
# Creating an instance of the class
person1 = Person(data['test_case_2'][0]['action'], 
                 data['test_case_2'][0]['step'])

# Accessing attributes and methods
print(person1.name)  # Output: Alice
person1.greet()     # Output: Hello, my name is Alice and I am 30 years old.
# Iterate through each test case
for test_case, steps in data.items():
    print(f"Actions for {test_case}:")
    
    # Iterate through each step in the test case
    for step in steps:
        action = step['action']
        print(f"Step {step['step']}: {action}")
    
    print()  # Add a blank line between test cases