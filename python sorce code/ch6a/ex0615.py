#program0515.py
def greeting_conf(prefix):
    def greeting(name):
        print(prefix, name)
    return greeting
 
mGreeting = greeting_conf("Good Morning")
mGreeting("Wilber")
mGreeting("Will")
print()
aGreeting = greeting_conf("Good Afternoon")    
aGreeting("Wilber")
aGreeting("Will")
