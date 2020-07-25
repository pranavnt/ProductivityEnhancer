from user_repository import UserRepository

event_object1 = {
        'username' : 'dru',
        'f_name' : 'Druhin',
        'l_name' : 'Bhowal',
        'title': "Event 1",
        'start': '7/25/2020 11:00',
        'end': '7/25/2020 12:00',
    }

event_object2 = {
        'username': 'dru',
        'f_name' : 'Druhin',
        'l_name' : 'Bhowal',
        'title': "Event 2",
        'start': '7/25/2020 08:00',
        'end': '7/25/2020 12:00',
    } 

events = [event_object1, event_object2]

repo = UserRepository()

for event in events:
    repo.add_calendar_event(event)

repo.save_data()


repo.get_events('dru')


