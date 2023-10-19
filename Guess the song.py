# Define the list of song titles (without extensions).
song_titles = ["Sungai Lui", "Jampi", "She's Gone", "Make it right"]

# Function to guess the song.
def guess_song():
    print("Welcome to the Song Guessing Game!")
    print("Can you guess the song title?")
    
    # Select a random song from the list (you can use the random module for this).
    # In this example, we will use the first song.
    song_to_guess = song_titles[0]

    while True:
        user_guess = input("Enter your guess: ").strip()

        if user_guess == song_to_guess:
            print(f"Congratulations! You guessed it right. The song is {song_to_guess}.")
            break
        else:
            print("Sorry, that's not the correct song. Try again.")

if __name__ == "__main__":
    guess_song()
