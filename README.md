# Python-progress
This repository is an active journey of my programs I have made in getting very experienced in python for employers to see in the coming years. I have completed GCSE computer science OCR, so I have some experience.

# Program 1: simple password generator:
this program takes an integer value as input from the user which dictates the length of a password which is randomly chosen from "characters" and "numbers" and added together using string concatenation.
### variables:
This program uses five variables: "characters", "numbers", "length", "password", and "pass_pool".
#### characters:
This variable stores every letter of the English alphabet, capital and non-capital. This variable is all letters in order, wrapped in one set of apostrophes, which turns the entire variable into one string, instead of a long list. This helps with readability.
#### numbers:
This variable stores every integer value from 0-9 all wrapped in one set of apostrophes which avoids a long list. This variable is a string, so I can use string concatenation to combine both variables together.
#### length:
This variable stores the user's input of an integer, which dictates the desired length the user wants for a randomly generated password. 
#### password:
This variable is an empty string, so I am able to add the randomly generated characters from both "characters" and "numbers" after each iteration of a for loop which runs for **length** times.
#### pass_pool:
This variable concatenates the full sets of characters and numbers together to create a single combined pool for the script to pick from.
### Iteration:
As mentioned previously, a for loop is used, which loops for ***length*** times, adding to the empty string "password" with randomly generated concatenated characters of "characters" and "numbers" which is stored in a variable called "pass_pool". Each cycle, randomly generated characters from both variables are added to "password" each cycle until the desired length is reached.
### The final output:
Using an f string inside of a print statement, the result of "password" is outputted to the user in one line.
### challenges and future plans:
#### challenges: 
Orginally, I found it difficult to work out the most efficient way to write every required letter for "characters", so I used a list, which I later changed to be more readable, with the help of gemini, as mentioned in the **characters** and **numbers** sections.
#### future plans:
I plan to create a password strength check, so I make sure the user has a strong password, to not get easily breached by brute force attacks.
