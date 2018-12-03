from termcolor import colored

class Bus:
    MAX_AGE = 65
    MIN_AGE = 5
    NUM_ROWS = 4
    NUM_CHAIRS_PER_ROW = 20
    TICKET_PRICE = 20
    TAKEN_SEAT = colored('O', 'red')
    EMPTY_SEAT = colored('O', 'green')

    def __init__(self):
        self.__rows = self.__build_rows()
        self.__revenue = 0
        self.__bought_seats = 0

    def sell_seat(self, row_index, seat_index, buyer_age):
        if self.__is_seat_taken(row_index, seat_index):
            return 'This seat is already taken, please choose another one.'

        self.__rows[row_index][seat_index] = self.TAKEN_SEAT
        self.__revenue += self.__ticket_price(buyer_age)
        self.__bought_seats += 1
        return 'Puchase successfully made.'

    def finish_order(self):
        if self.__bought_seats < (self.NUM_ROWS * self.NUM_CHAIRS_PER_ROW)/2:
            return 'Trip cancelled due to low number of tickets sold.'

        print('Trip successfully finished. Revenue R$' + str(self.__revenue))
        self.__print_seats_array()

    def __print_seats_array(self):
        print('   '.join(self.__rows[0]))
        print('   '.join(self.__rows[1]))
        print('\n')
        print('   '.join(self.__rows[2]))
        print('   '.join(self.__rows[3]))

    def __ticket_price(self, buyer_age):
        if self.MIN_AGE < buyer_age < self.MAX_AGE:
            return self.TICKET_PRICE/2
        return self.TICKET_PRICE

    def __is_seat_taken(self, row_index, seat_index):
        return self.__rows[row_index][seat_index] == self.TAKEN_SEAT

    def __build_rows(self):
        row = [self.EMPTY_SEAT for _ in range(self.NUM_CHAIRS_PER_ROW)]
        return [row[:] for _ in range(self.NUM_ROWS)]
