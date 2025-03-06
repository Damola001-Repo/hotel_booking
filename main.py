import pandas as pd

df = pd.read_csv('hotels.csv', dtype={"id":str})

class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df['id'] == self.hotel_id, 'name'].squeeze()

    def available(self):
        availability = df.loc[df['id'] == self.hotel_id, 'available'].squeeze()
        if availability == 'yes':
            return True
        else:
            return False

    def book(self):
        df.loc[df['id'] == self.hotel_id, 'available'] = 'no'
        df.to_csv('hotels.csv', index=False)

class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are you booking Data:
        Name : {self.customer_name}
        Hotel : {self.hotel.name}
"""
        return content

print(df)

hotel_id = input("Enter id of the hotel you want: ")
hotel = Hotel(hotel_id)
if hotel.available():
    customer_name = input("Enter your name: ")
    hotelReservation = ReservationTicket(customer_name, hotel)
    print(hotelReservation.generate())
    hotel.book()
else:
    print('The hotel is fully booked')