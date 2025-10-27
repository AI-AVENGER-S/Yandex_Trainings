def to_minutes(s: str):
    parts = list(map(int, s.split(':')))
    return parts[0] * 60 + parts[1]

N = int(input())

events = []
ARRIVE = 1
DEPART = 2
for _ in range(N):
    departure_time, arrive_time = map(lambda x: to_minutes(x), input().split('-'))
    events.append((departure_time, DEPART, 'A'))
    events.append((arrive_time, ARRIVE, 'B'))

M = int(input())
for _ in range(M):
    departure_time, arrive_time = map(lambda x: to_minutes(x), input().split('-'))
    events.append((departure_time, DEPART, 'B'))
    events.append((arrive_time, ARRIVE, 'A'))

total_buses = 0
extra_in_A = 0
extra_in_B = 0

events.sort()

for time, event, location in events:
    if location == 'A':
        if event == ARRIVE:
            extra_in_A += 1

        elif event == DEPART:
            if extra_in_A > 0:
                extra_in_A -= 1
            else:
                total_buses += 1
    if location == 'B':
        if event == ARRIVE:
            extra_in_B += 1

        elif event == DEPART:
            if extra_in_B > 0:
                extra_in_B -= 1
            else:
                total_buses += 1

print(total_buses)
            