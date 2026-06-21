class Theatre:
        
    def __init__(self,name):
        self.name=name
        self.seat_type={"gold":150,
                                     "platinum":250}
        self.shows=[ ]
        self.bookings=[ ]

                
    def list_shows(self):
        
        print("\nSHOWS AVAILABLE: ")
        
        if not self.shows:
            print("\nNO MOVIES PLAYING!")
        
        for show in self.shows:
            print(show)

            
    def list_bookings(self):
        
        print("\nBOOKINGS: ")
        
        if not self.shows:
            print("\nNO BOOKINGS!")
        
        for booking in self.bookings:
            print(booking)
              
            
    def calculate_price(self,seat_type,num_seats):
                
                price=(num_seats)*(self.seat_type[seat_type])
                
                return price
            
  
class Admin:
      
     def __init__(self,name,theatre):
              self.name=name
              self.theatre=theatre                    

                                                  
     def add_show(self,a_show):
            
            if a_show in self.theatre.shows:
                print("\nSHOW IS ALREADY ADDED!")
                return
            else:
                self.theatre.shows.append(a_show)
                print("\nSHOW ADDED SUCCESFULLY!")
                return
            
                                                                       
     def  remove_show(self,r_show):
         
         if not r_show in self.theatre.shows:
             print("\nSHOW NOT FOUND")
             return
             
         else:
             self.theatre.shows.remove(r_show)
             print("\nSHOW REMOVED")
             return
         
                    
class Customer:
           
           def __init__(self,theatre,name):
                 self.theatre=theatre
                 self.name=name

           
           def book_show(self,b_show,b_num_seats,b_seat_type):
               
               if not b_show in self.theatre.shows:
                   print("\nINVALID SHOW!")
                   return
                   
               if not b_seat_type.lower() in self.theatre.seat_type.keys():
                   print("\nINVALID SEAT TYPE!")
                   return
                   
               if b_num_seats>b_show.available_seats:
                   print(f"\nOnly {b_show.available_seats} are available!")
                   return
               
               else:
                   b_show.available_seats-=b_num_seats
                   price=self.theatre.calculate_price(b_seat_type,b_num_seats)
                   booking=Bookings(self,b_show,b_seat_type,b_num_seats,price)
                   self.theatre.bookings.append(booking)
                   print("\nSHOW BOOKED SUCCESFULLY!")
                   print(f"\nPRICE:{price}$")

          
           def cancel_show(self,c_booking_id):
                   
                   for booking in self.theatre.bookings:
                                                
                         if booking.booking_id==c_booking_id:
                             booking.show.available_seats+=booking.num_seats
                         self.theatre.bookings.remove(booking)
                         print("\nCANCELLATION COMPLETE!")
                         return
                  
                   print("\n INVALID REQUEST!")
                                                      
                                                 
class Bookings:
    
    counter=1000
    
    def __init__(self,customer,show,seat_type,num_seats,price):
        
        self.customer=customer
        self.price=price
        self.seat_type=seat_type
        self.num_seats=num_seats
        self.show=show
        self.booking_id=self.counter
        Bookings.counter+=1
        
    def __str__(self):
        return f"\n{self.customer.name.upper()}\n{self.show.movie.name.upper()}\n{self.show.time}\n{self.seat_type}\n{self.num_seats}\n{self.price}\n{self.booking_id}"
        
                    
class Show:
    
              def __init__(self,movie,screen,time,total_seats):
                  self.movie=movie
                  self.screen=screen
                  self.time=time
                  self.total_seats=total_seats
                  self.available_seats=total_seats

                                    
              def __str__(self):
                  return f"\nMovie:{self.movie.name.upper()}\nScreen:{self.screen}\nTime:{self.time}\nAvailable Seats:{self.available_seats}"
                  
                                                                
class Movie:
        
        def __init__(self,name,min_duration):       
                  self.name=name
                  self.min_duration=min_duration
                  
                  self.hours=min_duration//60
                  self.minutes=min_duration%60
        
        def __str__(self):
                  return f"\n{self.name.upper()}-{self.hours}:{self.minutes:02d}hr"  


#testing
new_theatre=Theatre("Amigos theatre")
new_owner=Admin("Alex",new_theatre)

movie1=Movie("Pride and Prejudice",163)
movie2=Movie("Avengers 2012",170)

show1=Show(movie1,1,"11:30am",200)
show2=Show(movie1,3,"7:30pm",250)
show3=Show(movie2,2,"1:30pm",200)
show4=Show(movie2,4,"10:30pm",250)

new_owner.add_show(show1)
new_owner.add_show(show2)
new_owner.add_show(show3)
new_owner.add_show(show4)


new_theatre.list_shows()

customer1=Customer(new_theatre,"Alice")
customer2=Customer(new_theatre,"john")
customer3=Customer(new_theatre,"Will")
customer4=Customer(new_theatre,"Sara")

customer1.book_show(show1,4,"gold")
customer2.book_show(show2,50,"platinum")
customer3.book_show(show3,6,"gold")
customer4.book_show(show4,1,"gold")

customer4.cancel_show(1)







 


    
    
    
    
    
    

    
