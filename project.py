import sys


def main():
    print ("Hi, welcome to BookMe, the best airplane booking software in the world")
    ans = input("Do you want to book a flight? (y/n) ")
    if ans == ("y"):
        print ("We are very happy to help you. To start enter the following credentials.")
        credentials()
        airports_list()
        paying_creds()
    else: 
        SystemExit()

def credentials():
    while True:
        name = input("Name: ") 
        if len(name.split())<2:
            print ("Invalid Name ") 
        else:
            break
    brth = input("Birthdate (month/day/year): ")
    nat = input ("Nationalty: ")
    passp = int(input("Passport Number: "))
    print ("Make sure that the credentials that you entered are correct ")
    chg = input ("Do you want to change your credentials ? (y/n) ")
    if chg == ("y"):
        credentials()
    if chg == ("n"):
        print ("Checking...")
        print ("Now you're ready to book your flight")
    
def airports_list(): 
    airp = input ("Please enter the name of the airport from which you want to fly: ")
    airports =  ["Hamad International Airport", "JFK Airport", "Tokyo Haneda International Airport", "Singapore Changi Airport", "Paris Charles de Gaulle Airport", "Munich Airport", 
    "Istanbul Airport", "Heathrow Airport", "Zurich Airport", "Kansai Airport", "Linate Airport", "Amsterdam Airport Schiphol"]
    if airp in airports: 
        print("Perfect")
    else:
        print("You can't fly from there. Please select another airport ")
        airports_list()

    print ("These are all the possible destinations: ") 
    flights = ["Hamad International Airport", "JFK Airport", "Tokyo Haneda International Airport", "Singapore Changi Airport", 
    "Paris Charles de Gaulle Airport", "Munich Airport", "Istanbul Airport", "Heathrow Airport", "Zurich Airport"  
    "Kansai Airport", "Linate Airport", "Amsterdam Airport Schiphol"]
    flights = [x for x in flights if x != airp]
    for _ in flights:
        print (_)

    flights_selection()

    while True: 
        hours = ["7:50 A.M.", "9:45 A.M.", "12 P.M.", "2:00 P.M.", "4:20 P.M." , "7:20 P.M.", "10:00 P.M."]
        for i in hours:
            print(i)
        time =  input("Please select at what time would you like to board your plane: ")
        if time in hours:
            print("Checking if the're seats avalaible...")
            print ("Seats are still avalaible")
            break
        else:
            print("Choose one of the times displayed on screen")

def flights_selection(): 
    flights = ["Hamad International Airport", "JFK Airport", "Tokyo Haneda International Airport", "Singapore Changi Airport", 
    "Paris Charles de Gaulle Airport", "Munich Airport", "Istanbul Airport", "Heathrow Airport", "Zurich Airport"  
    "Kansai Airport", "Linate Airport", "Amsterdam Airport Schiphol"]
    des = input ("Please select your destination: ")
    if des in flights:
        print("Perfect")
    else:
        print ("Please select one of the destinations displayed on screen")
        flights_selection()

def paying_creds():
    print ("Ticket price: 90$")
    print ("Please enter your credit card information")
    cc = input("What type of credit card do you have? (Mastercard/Paypal) ")
    if cc == ("Mastercard"):
        Mastercard_f()

    if cc == ("Paypal"): 
        Paypal_f()
    
    while True: 
        end = input("Do you want to proceed with the payment? (y/n) ")
        if end == ("y"):
            print ("Validating payment...")
            print ("Hope you enjoyed the BookMe experience!!!")
            break
        else: 
            xcx = input("Do you want to cancel your booking? (y/n) ")
            if xcx == ("y"): 
                SystemExit
            else: 
                pass

def Mastercard_f():
    while True:
        owner = input("Owner of the card: ") 
        if len(owner.split())<2:
            print ("Invalid Name ") 
        else:
            break        
    ccn = int (input("Credit card number: "))
    exd = input("Expiration Date (month/year): ")
    cvc = int (input("CVC: "))

def Paypal_f(): 
    usr = input("Username/E-mail: ")
    passw = input ("Password: ")
    
main()