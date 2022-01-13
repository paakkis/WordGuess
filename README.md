# WordGuess
Word Guessing game in which a random word is generated. User tries to correctly guess the generated word by the given hints.

Finnish wordlist from Kotimaisten kielten keskus (https://kaino.kotus.fi/sanat/nykysuomi/)

Add a new word to the list with the method lisää_sana()
  - for example: lisää_sana("loremipsum")
  
 Start a game with the method aloita_peli()
  - for example: aloite_peli(5,6) in which 5 stands for the maximum length of the answer word and 6 for the maximum amount of attempts to guess the word
