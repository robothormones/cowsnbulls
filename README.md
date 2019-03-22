# cowsnbulls
Standard Cows &amp; Bulls game implemented in Python

The idea of the game is simple:
1. A challengee / computer picks a word of defined length.
2. The challenger guesses random words of same length. 
3. The program counts the number of common letters in the attempt & the challenge word:
      If the letter is in the correct place it's called a Bull
      If the letter is in the worng place, it's called a Cow.
4. The challenger needs to make use of these clues to refine the attempts and finally find the correct word.

To play the game: 
Run  "begin_game.py"
Run the function: "play_cowsnbulls()"



Future Plans with the project:
- Implement a ML algorithm to play the game
- Analyze the performance of the ML algorithm to figure out toughest words 
- Analyze the performance of the algo to figure out optimum strategy
- Implement a way for the challenge word to be dynamic - i.e keep the challenge accurate to the clues already given, but keep changing it after every attempt to make it as difficult as possible to guess the right word.
