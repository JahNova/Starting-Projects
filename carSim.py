started=False
stopped=True
while True:
   cm=input('>').lower()
   if cm=='start':
       if started:
           print('Car already started!')
       else:
           started=True
           stopped=False               
           print('Car started')
   elif cm=='stop':
       if stopped:
           print('Car is already stopped!')
       else:
           stopped=True
           started=False
           print('Car Stopped')
   elif cm == 'help':
       print("""
start - starts car
stop - stops car
quit - quits program""")
   elif cm=='quit':
       break
   else:
       print("I don't understand that")
