from ten_thousand.game_logic import GameLogic


class Game:

    def __init__(self):

        self.round = 1
        self.num_dice = 6
        self.total_score = 0
        self.dice_score = 0

    def welcome(self):
        """
        Display welocme message and ask if they like to play
        """
        print("Welcome to Ten Thousand")
        print("(y)es to play or (n)o to decline")
        choice = input("> ")
        if choice == "y":
            return self.play(0, 1, 6)
        else:
            print("OK. Maybe another time")



    def quit_game(self):
        quit()


    def play(self,total_score, round, num_dice):

        print(f"starting round {round}")

        while True:


            print(f"Rolling {self.num_dice} dice")
            return_value = GameLogic.roll_dice(self.num_dice)
            print(return_value)
            print("Enter dice to keep, or (q)uit:")
            #global choice
            choice = input("> ")
            if choice == "q":
                print(f"Thanks for playing. You earned {self.total_score} points")
                self.quit_game()

            self.dice_score += GameLogic.calculate_score(choice)
            self.num_dice = self.num_dice - len(choice)
            print(f"You have {self.dice_score} unbanked points and {self.num_dice} dice remaining")
            print("(r)oll again, (b)ank your points or (q)uit:")
            choice1 = input("> ")

            if self.num_dice == "0":
                print("Zilch!!! Round over")
                continue

            if choice1 == "r":
                if self.num_dice == 0:
                    self.num_dice = 6
                continue



            if choice1 == "b":
                self.total_score += self.dice_score
                print(f"You banked {self.dice_score} in round {round}")
                print(f"Total score is {self.total_score} points")
                round += 1
                self.num_dice = 6
                self.dice_score = 0
                self.play(total_score, round, num_dice)
            if choice1 == "q":
                self.quit_game()


test_game = Game()
test_game.welcome()