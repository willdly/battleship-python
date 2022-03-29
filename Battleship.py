# Author: William Ly
# Description: This program utilizes Classes, Function defintions, "Private" class members, lists, dictionaries, list/dictionary indexing, iterations and if-elif-else statements with the specified arguments. 
#              The program represents a two-player game called Battleship. Users are able to initialize the game, place ships on their board, fire torpedos at their opponents, get the current state of the game,
#              and get the remaining number of ships for the specified player. It is also able to validate/record players moves and update the current game state.

class ShipGame:
    """ A class to represent a game called Battleship with two players that take turns to fire torpedos at each other until one of the player's final ship has sunken."""
    def __init__(self):
        """Initializes all the required data members for the Battleship game. All data members are private."""
        self._first_player_board = {'A1':'', 'A2':'', 'A3':'', 'A4':'', 'A5':'', 'A6':'', 'A7':'', 'A8': '', 'A9': '', 'A10': '',
                                    'B1':'', 'B2':'', 'B3':'', 'B4':'', 'B5':'', 'B6':'', 'B7':'', 'B8': '', 'B9': '', 'B10': '',
                                    'C1':'', 'C2':'', 'C3':'', 'C4':'', 'C5':'', 'C6':'', 'C7':'', 'C8': '', 'C9': '', 'C10': '',
                                    'D1':'', 'D2':'', 'D3':'', 'D4':'', 'D5':'', 'D6':'', 'D7':'', 'D8': '', 'D9': '', 'D10': '',
                                    'E1':'', 'E2':'', 'E3':'', 'E4':'', 'E5':'', 'E6':'', 'E7':'', 'E8': '', 'E9': '', 'E10': '',
                                    'F1':'', 'F2':'', 'F3':'', 'F4':'', 'F5':'', 'F6':'', 'F7':'', 'F8': '', 'F9': '', 'F10': '',
                                    'G1':'', 'G2':'', 'G3':'', 'G4':'', 'G5':'', 'G6':'', 'G7':'', 'G8': '', 'G9': '', 'G10': '',
                                    'H1':'', 'H2':'', 'H3':'', 'H4':'', 'H5':'', 'H6':'', 'H7':'', 'H8': '', 'H9': '', 'H10': '',
                                    'I1':'', 'I2':'', 'I3':'', 'I4':'', 'I5':'', 'I6':'', 'I7':'', 'I8': '', 'I9': '', 'I10': '',
                                    'J1':'', 'J2':'', 'J3':'', 'J4':'', 'J5':'', 'J6':'', 'J7':'', 'J8': '', 'J9': '', 'J10': '',}
        self._first_player_ships = []

        self._second_player_board = {'A1':'', 'A2':'', 'A3':'', 'A4':'', 'A5':'', 'A6':'', 'A7':'', 'A8': '', 'A9': '', 'A10': '',
                                     'B1':'', 'B2':'', 'B3':'', 'B4':'', 'B5':'', 'B6':'', 'B7':'', 'B8': '', 'B9': '', 'B10': '',
                                     'C1':'', 'C2':'', 'C3':'', 'C4':'', 'C5':'', 'C6':'', 'C7':'', 'C8': '', 'C9': '', 'C10': '',
                                     'D1':'', 'D2':'', 'D3':'', 'D4':'', 'D5':'', 'D6':'', 'D7':'', 'D8': '', 'D9': '', 'D10': '',
                                     'E1':'', 'E2':'', 'E3':'', 'E4':'', 'E5':'', 'E6':'', 'E7':'', 'E8': '', 'E9': '', 'E10': '',
                                     'F1':'', 'F2':'', 'F3':'', 'F4':'', 'F5':'', 'F6':'', 'F7':'', 'F8': '', 'F9': '', 'F10': '',
                                     'G1':'', 'G2':'', 'G3':'', 'G4':'', 'G5':'', 'G6':'', 'G7':'', 'G8': '', 'G9': '', 'G10': '',
                                     'H1':'', 'H2':'', 'H3':'', 'H4':'', 'H5':'', 'H6':'', 'H7':'', 'H8': '', 'H9': '', 'H10': '',
                                     'I1':'', 'I2':'', 'I3':'', 'I4':'', 'I5':'', 'I6':'', 'I7':'', 'I8': '', 'I9': '', 'I10': '',
                                     'J1':'', 'J2':'', 'J3':'', 'J4':'', 'J5':'', 'J6':'', 'J7':'', 'J8': '', 'J9': '', 'J10': '',}
        self._second_player_ships = []

        self._players = ["first", "second"]
        self._player_turn = "first"
        self._turn_count = 0
        self._current_game_state = "UNFINISHED"


    def place_ship(self, player, ship_length, coordinates, ship_orientation):
        """Places a ship on the player's board with the respective arguments. It also adds the ship to the player's list of ships. Take arguments: player, length of ship, coordinates, and ship orientation."""
        coordinates_list = []   # list of the ship's coordinates that will be added to the board and to the player's list of ships
        grid_y_values = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]  # boundaries for row letters

        if ship_orientation == "R":
            if (1 <= ship_length <= 10) and (ship_length >= 2): # if the length of the ship does exceed the grid and has a length greater than 2
                for number in range(int(coordinates[1]), int(coordinates[1]) + ship_length):    # gets the number for column number
                    coordinates_list.append(coordinates[0]  +str(number))
            else:
                print("You have placed a ship that does not fit on the grid. Please try again.")
                return False
        elif ship_orientation == "C":
            if (coordinates[0] in grid_y_values) and (((list(self._first_player_board.keys()).index(coordinates)) + ((ship_length - 1)*10)) <= 100)  and (ship_length >= 2): # if coordinates row letter is within the letters of the grid, the ship length does not exceed the grid, and has a length greater than 2 
                for letter in range(grid_y_values.index(coordinates[0]), grid_y_values.index(coordinates[0]) + ship_length): # gets the letter's index for row letter
                    coordinates_list.append(grid_y_values[letter] + coordinates[1])
            else:
                print("You have placed a ship that does not fit on the grid. Please try again.")
                return False

        if player == "first":
             for coordinate in coordinates_list:    # gets coordinate from coordinates_list
                if (any(coordinate in ship for ship in (self._first_player_ships)) or any(coordinate in ship for ship in(self._second_player_ships))) == False: # if the coordinate does not overlap with any existing ship coordinates from either board
                    for coordinate in coordinates_list: 
                        self._first_player_board[coordinate] = "x"  # places ship on the board
                    self._first_player_ships.append(coordinates_list) # adds ship to first_player_ships list
                    return True
                else:
                    print("You have placed a ship that overlaps with a current ship. Please try again.")
                    return False            
        elif player == "second":
            for coordinate in coordinates_list:
                if (any(coordinate in ship for ship in (self._first_player_ships)) or any(coordinate in ship for ship in(self._second_player_ships))) == False: # if the coordinate does not overlap with any existing ship coordinates from either boar
                    for coordinate in coordinates_list:
                        self._second_player_board[coordinate] = "x" # places ship on the board
                    self._second_player_ships.append(coordinates_list)  # adds ship to second_player_ships list
                    return True
                else:
                    print("You have placed a ship that overlaps with a current ship. Please try again.")
                    return False

    def get_current_state(self):
        """Returns the current state of the game. Takes no parameters."""
        if (self.get_num_ships_remaining("first") == 0) and (self._turn_count > 0):
            self._current_game_state = "SECOND_WON"
        elif (self.get_num_ships_remaining("second") == 0) and (self._turn_count > 0):
            self._current_game_state = "FIRST_WON"
        else:
            self._current_game_state = "UNFINISHED"
        return self._current_game_state

    def fire_torpedo(self, player, coordinates):
        """Fires a torpedo at the opponent's board. It also record's player's move, updates whose turn it is and updates the current state of the game. Take arguments: player, coordinates."""
        if player == self._player_turn: # checks if it's the player's turn
            if self.get_current_state() == "UNFINISHED":    # checks if the game is still in-progress
                if player == "first":  
                    self._second_player_board[coordinates] = ""
                    for ship in self._second_player_ships:
                        if coordinates in ship: # checks if torpedo coordinates hits any of the ship's coordinates
                            ship.remove(coordinates)    
                            self._player_turn = "second"
                            self._turn_count += 1
                            self._current_game_state = self.get_current_state()
                            return True
                        else:   # the torpedo coordinates misses
                            self._player_turn = "second"
                            self._turn_count += 1
                            return True
                        
                elif player == "second":
                    self._first_player_board[coordinates] = ""
                    for ship in self._first_player_ships:
                        if coordinates in ship: # checks if torpedo coordinates hits any of the ship's coordinates
                            ship.remove(coordinates)
                            self._player_turn = "first"
                            self._turn_count += 1
                            self._current_game_state = self.get_current_state()
                            return True
                        else:   # the torpedo coordinates misses
                            self._player_turn = "first"
                            self._turn_count += 1
                            return True
            else:
                return False
        else:
            return False        

    def get_num_ships_remaining(self, player):
        """Returns how many ships the specified player has left. Takes argument: player."""
        if player == "first":
            self._first_player_ships = [ele for ele in self._first_player_ships if ele != []]   # excludes empty lists in first player's list of ships
            return len(self._first_player_ships)
        elif player == "second":
            self._second_player_ships = [ele for ele in self._second_player_ships if ele != []] # excludes empty lists in second player's list of ships
            return len(self._second_player_ships)
