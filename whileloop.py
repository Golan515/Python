from datetime import datetime
print(datetime.now().second)
print(datetime.now().second + 2)
wait_until = (datetime.now().second + 2) % 60
while datetime.now().second != wait_until:
    1 + 1
print(f'We are at {wait_until} seconds!')
while datetime.now().second != wait_until:
    pass
print(f'We are at {wait_until} seconds!')
wait_until = (datetime.now().second + 2) % 60
while True:
    while datetime.now().second == wait_until:
        print(f'We at {wait_until} seconds! ')
        break
wait_until = (datetime.now().second + 2) % 60
while True:
    while datetime.now().second < wait_until:
        continue
    break
print(f'We at {wait_until} seconds! ')