# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")


class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player1_word) < len(player2_word):
            return 2
        else:
            pass

class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
    
    def round_winner(self, player1_word: str, player2_word: str):
        vowels = ["a","e","i","o","u"]
        p1_vowels = []
        p2_vowels = []
        
        for letter in player1_word:
            if letter in vowels:
                p1_vowels.append(letter)
            
        for letter in player2_word:
                if letter in vowels:
                    p2_vowels.append(letter)     

        if len(p1_vowels) > len(p2_vowels):
            return 1
        elif len(p1_vowels) < len(p2_vowels):
            return 2
        else:
            pass

class RockPaperScissors(WordGame):
    def __init__(self, rounds):
        super().__init__(rounds)

    def __r_p_s(self, p1: str, p2: str):     
        hands = {"rock": "paper", "paper": "scissors", "scissors": "rock"}

        # data validation
        if p1 not in hands:
            if p2 in hands:
                return 2
            else:
                return None
        elif p2 not in hands:
            return 1

        if p1 == hands[p2]:
            return 1
        elif p2 == hands[p1]:
            return 2
        else:
            pass
    
    def round_winner(self, player1_word, player2_word):
        return self.__r_p_s(player1_word, player2_word)
        
if __name__ == "__main__":
    p = RockPaperScissors(3)
    p.play()