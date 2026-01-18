import random

# Konstanta agar tidak ada typo
ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'

emojis = { ROCK: '🪨', SCISSORS: '✂️', PAPER: '📄' }
choices = tuple(emojis.keys())

def get_user_choice():
    while True:
        user_choice = input("Batu, Kertas, atau Gunting? (r/p/s): ").lower()
        if user_choice in choices:
            return user_choice
        print("Pilihan tidak valid!")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("Seri!")
    elif (user_choice == ROCK and computer_choice == SCISSORS) or \
         (user_choice == SCISSORS and computer_choice == PAPER) or \
         (user_choice == PAPER and computer_choice == ROCK):
        print("Kamu Menang!")
    else:
        print("Kamu Kalah!")

# Jalankan game
while True:
    user_choice = get_user_choice()
    computer_choice = random.choice(choices)
    print(f"Kamu memilih: {emojis[user_choice]}")
    print(f"Komputer memilih: {emojis[computer_choice]}")
    determine_winner(user_choice, computer_choice)
    
    play_again = input("\nMainkan lagi? (y/n): ").lower()
    if play_again != 'y':
        print("Terima kasih sudah bermain!")
        break