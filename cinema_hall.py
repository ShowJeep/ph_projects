class Star_Cinema:
    hall_list= []

    @classmethod
    def entry_hall(cls,ob):
        cls.hall_list.append(ob)
        
class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self.rows= rows
        self.cols= cols
        self.hall_no= hall_no
        self.seats= {}
        self.show_list= []
        Star_Cinema.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        lot=(id, movie_name, time)
        self.show_list.append(lot)
        self.seats[id] = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
    
    def book_seats(self, show_id, seat_list):
        if show_id not in self.seats:
            print('\n\n INVALID ID \n\n')
            return
        for row, col in seat_list:
            if row<0 or row>self.rows or col<0 or col>self.cols:
                print('\n\nINVALID SEAT\n\n')
            elif(self.seats[show_id][row-1][col-1]==1):
                print(f'Row {row} Col {col} this seat is already booked')
            else:
                self.seats[show_id][row-1][col-1]=1
                for key,val in self.seats.items():
                    if key == show_id:
                        for row in val:
                            print(row)
                print('\n\n-----\n\n')

    def view_show_list(self):
        for shows in self.show_list:
            print(f'\nShow ID: {shows[0]} Movie: {shows[1]} Time: {shows[2]}\n')

    def view_available_seats(self, show_id):
        for key,val in self.seats.items():
                if key == show_id:
                    for row in val:
                        print(row)
        print('\n\n-----\n\n')


Hall1= Hall(5,5,101)
Hall2= Hall(5,5,102)
Hall3= Hall(5,5,103)

Hall1.entry_show('11','Titanic', '12:40')
Hall2.entry_show('22','Titanic', '12:40')
Hall3.entry_show('33','Titanic', '12:40')

while True:
    print('Enter 1 to view show list')
    print('Enter 2 to view available seats')
    print('Enter 3 to book seats')
    print('Enter 0 to EXIT')
    
    val=int(input('\n\nEnter value: '))
    if val==0:
        break
    elif val==1:
        print('Enter 1 for Hall no. 1')
        print('Enter 2 for Hall no. 2')
        print('Enter 3 for Hall no. 3')
        hl=int(input('\n\nEnter hall no: '))
        if hl==1:
            Hall1.view_show_list()
        elif hl==2:
            Hall2.view_show_list()
        elif hl==3:
            Hall3.view_show_list()
    elif val==2:
        print('\n|---Available Shows Are---|\n')
        Hall1.view_show_list()
        Hall2.view_show_list()
        Hall3.view_show_list()
        shid=input('\n\nEnter Show ID: ')
        if shid=='11':
            Hall1.view_available_seats(shid)
        elif shid=='22':
            Hall2.view_available_seats(shid)
        elif shid=='33':
            Hall3.view_available_seats(shid)
        else:
            print('\nINVALID ID\n')
    elif val==3:
        print('\n|---Available Shows Are---|\n')
        Hall1.view_show_list()
        Hall2.view_show_list()
        Hall3.view_show_list()
        shid=input('\n\nEnter Show ID: ')
        seat_str = input("Enter the row and col -> rows,cols : ")
        seat_list = [tuple(map(int, seat.split(','))) for seat in seat_str.split()]
        if shid=='11':
            Hall1.book_seats(shid, seat_list)
        elif shid=='22':
            Hall2.book_seats(shid, seat_list)
        elif shid=='33':
            Hall3.book_seats(shid, seat_list)
        else:
            print('\nINVALID ID\n')


        
        
