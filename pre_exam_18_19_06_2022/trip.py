people_count = int(input())
sleepovers = int(input())
transport_card_count = int(input())
museum_ticket_count = int(input())

sleepovers_price = 20
transport_card_price = 1.60
museum_ticket_price = 6
emergency_expences = 1.25

sleepovers_price_total = sleepovers * sleepovers_price
transport_card_price_total = transport_card_count * transport_card_price
museum_ticket_price_total = museum_ticket_count * museum_ticket_price

price_per_person = sleepovers_price_total + transport_card_price_total + museum_ticket_price_total

price_total = price_per_person * people_count

price_total *= emergency_expences

print(f"{price_total:.2f}")
