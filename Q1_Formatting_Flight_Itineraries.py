flight_info_1 = [('Bill','Boston','New York'), ('Sally','las Angeles', "Seattle"), ('John','Memphis','Atlanta')]

flight_info_2 = [('Louis', 'Paris','London'), ('Enrique', 'Barcelona','Athens'), ('Vlad','St.Petersburg','Amesterdam')]

Flight_info_3 = [('Ava','Sydney','Cairo'), ('Riley','Kingston','Tokyo'), ('Fred','Cleveland','Las Vages')]

def itinerarys(flights):
    for flight in flights:
        passanger, origin , destination = flight
        print(f'{passanger}- from {origin} to {destination}')

itinerarys(flight_info_1)