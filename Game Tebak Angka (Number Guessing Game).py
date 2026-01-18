import random

while True:
    number_to_guess = random.randint(1, 100)
    
    while True:
        try:
            guess = int(input("Tebak angka antara 1 dan 100: "))
            
            if guess < number_to_guess:
                print("Terlalu rendah")
            elif guess > number_to_guess:
                print("Terlalu tinggi")
            else:
                print("Selamat! Tebakanmu benar!")
                break
        except ValueError:
            print("Masukkan angka yang valid!")
    
    play_again = input("\nMainkan lagi? (y/n): ").lower()
    if play_again != 'y':
        print("Terima kasih sudah bermain!")
        break 