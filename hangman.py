import random
def choose_word(difficulty):
	number = random.randint(0,2);
	easy = ["cat", "dog", "fish"]
	medium = ["firetruck", "library", "elephant"]
	hard = ["xylophone", "exoskeleton", "quantify"]
	if(difficulty == "hard"):
		return hard[number]
	if(difficulty == "medium"):
		return medium[number]
	else:
		return easy[number]

class Game:
	guesses = 0
	word = ""
	guessed_word = ""

	def __init__(self, difficulty):
		self.difficulty = difficulty.lower()
		if(self.difficulty == "easy"):
			self.guesses = 3
		if(self.difficulty == "medium"):
			self.guesses = 5
		if(self.difficulty == "hard"):
			self.guesses = 7
		self.word = choose_word(self.difficulty)
		self.guessed_word = list("_" * len(self.word))

	def take_guess(self, guess):
		if(self.guesses == 0):
			print "You are out of guesses!"
			return
		if guess in self.word:
			temp = [pos for pos, char in enumerate(self.word) if char == guess]
			for char in temp:
				self.guessed_word[char] = guess
			print "Correct guess!"
			print self.guessed_word

		else:
			print "Incorrect guess! You have %s guesses left!" % self.guesses
			self.guesses = self.guesses - 1

	def play_game(self):
		while(self.guesses > 0):
			guess = raw_input("Take a guess: ")
			self.take_guess(guess)
			if(list(self.word) == self.guessed_word):
				print "You won! You guessed %s!" % self.word
				return
		print "You lose!"



			




game = Game("easy")
game.play_game()






	
 

