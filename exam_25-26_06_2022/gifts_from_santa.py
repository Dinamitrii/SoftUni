address_small = int(input())
address_big = int(input())
address_number = int(input())

address = 0

for address in range(address_big, address_small - 1, -1):
    if address % 3 == 0 and address % 2 == 0:
        if address == address_number:
            break
        print(address)
