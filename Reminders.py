f = open('Reminders.txt', 'r')
readReminders = f.read()

num_Reminders = sum(1 for line in open('Reminders.txt'))

