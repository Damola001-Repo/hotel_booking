import pandas as pd


df = pd.read_csv('hotels.csv', dtype={"id":str})
card_df = pd.read_csv('cards.csv', dtype=str).to_dict(orient="records")
secure_creditCard_df = pd.read_csv('card_security.csv', dtype=str)

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

class SpaHotel(Hotel):
    def book_spa_package(self):
        pass

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

class CreditCard:
    def __init__(self, card_number):
        self.number = card_number

    def validate(self, expiration, cvc, holder):
        card_data = {'number': self.number,
                     'expiration': expiration,
                     'cvc': cvc, 'holder': holder}
        if card_data in card_df:
            return True
        else:
            return False

class SecureCreditCard(CreditCard):
    def authenticate(self, password):
        if secure_creditCard_df[secure_creditCard_df["number"] == self.number]['password'].squeeze() == password:
            return True
        else:
            return False

class SpaTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your SPA reservation
        Here are your SPA booking data:
        Name: {self.customer_name}
        Hotel: {self.hotel.name}
        """
        return content




print(df)

hotel_id = input("Enter id of the hotel you want: ")
hotel = SpaHotel(hotel_id)
card = SecureCreditCard("1234")
if hotel.available():
    if card.validate("12/26","123","JOHN SMITH"):
        if card.authenticate("mypass"):
            customer_name = input("Enter your name: ")
            hotelReservation = ReservationTicket(customer_name, hotel)
            hotel.book()
            spa = input("Do you want to book a spa package? ")
            print(hotelReservation.generate())
            if spa == "yes":
                hotel.book_spa_package()
                spa_ticket = SpaTicket(customer_name, hotel)
                print(spa_ticket.generate())
        else:
            print("Credit card authentication failed!")
    else:
        print("There was a problem while processing your payment")
else:
    print('The hotel is fully booked')