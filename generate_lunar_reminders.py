# generate_lunar_reminders.py

import calendar
import icalendar
from datetime import datetime, timedelta

# Function to generate lunar reminders

def generate_lunar_reminders(year):
    reminders = []

    # Example logic to determine lunar dates for 初一 and 十五
    for month in range(1, 13):
        for day in [1, 15]:
            lunar_date = f'{year}-{month:02d}-{day:02d}'

            # Create reminder; here we add a day for the reminder
            reminder_date = datetime.strptime(lunar_date, '%Y-%m-%d') - timedelta(days=1)
            reminders.append(reminder_date)

    return reminders

# Function to create ICS file

def create_ics_file(reminders, year):
    cal = icalendar.Calendar()
    for reminder in reminders:
        event = icalendar.Event()
        event.add('summary', 'Lunar Reminder')
        event.add('dtstart', reminder)
        cal.add_component(event)

    with open(f'Lunar_Reminders_{year}.ics', 'wb') as f:
        f.write(cal.to_ical())

if __name__ == '__main__':
    year = int(input('Enter the year to generate reminders: '))
    reminders = generate_lunar_reminders(year)
    create_ics_file(reminders, year)
