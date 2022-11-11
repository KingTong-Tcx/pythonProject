
 1   #program0515.py
 2   def greeting_conf(prefix):
 3       def greeting(name):
 4           print(prefix, name)
 5       return greeting
 6    
 7   mGreeting = greeting_conf("Good Morning")
 8   mGreeting("Wilber")
 9   mGreeting("Will")
10   print()
11   aGreeting = greeting_conf("Good Afternoon")    
12   aGreeting("Wilber")
13   aGreeting("Will")
