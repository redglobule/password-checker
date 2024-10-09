num = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
alpha_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alpha_upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
special_characters = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", ";", ":", "'", "\"", "<", ">", ",", ".", "/", "?", "|", "\\", "`", "~"]


def strength_checker(password):
    score = 0
    verif_num = 0
    verif_alpha_lower = 0
    verif_alpha_upper = 0
    verif_special_characters = 0

    len_pass = len(password)
    if len_pass <= 1:
        print("\nYour password is", len_pass,"character long.")
    else:
        print("\nYour password is", len_pass,"characters long.")
    
    for c in range(len_pass):
        if password[c] in num:
            verif_num = 1
        elif password[c] in alpha_lower:
            verif_alpha_lower = 1
        elif password[c] in alpha_upper:
            verif_alpha_upper = 1
        elif password[c] in special_characters:
            verif_special_characters = 1
        else:
            print("Your password should only contain numbers, lowercase letters, uppercase letters and special characters.")
            break
            return

    score = verif_num + verif_alpha_lower + verif_alpha_upper + verif_special_characters

    total_characters = 0
    if verif_num: total_characters += len(num)
    if verif_alpha_lower: total_characters += len(alpha_lower)
    if verif_alpha_upper: total_characters += len(alpha_upper)
    if verif_special_characters: total_characters += len(special_characters)

    total_combinations = total_characters ** len_pass

    guesses_per_second = 10**9
    time_to_crack_seconds = total_combinations / guesses_per_second

    if time_to_crack_seconds < 60:
        time_to_crack = f"{time_to_crack_seconds:.2f} seconds"
    elif time_to_crack_seconds < 3600:
        time_to_crack = f"{time_to_crack_seconds / 60:.2f} minutes"
    elif time_to_crack_seconds < 86400:
        time_to_crack = f"{time_to_crack_seconds / 3600:.2f} hours"
    else:
        time_to_crack = f"{time_to_crack_seconds / 86400:.2f} days"


    print(f"Estimated time to crack your password: {time_to_crack}\n")


    if len_pass <=7:
        print("Your password is very weak")
    elif len_pass >=8 and len_pass <=10:
        if score < 4:
            print("Your password is weak")
        else:
            print("Your password is good")
    elif len_pass >=11 and len_pass <=13:
        print("Your password is good")
    elif len_pass >=14:
        print("Your password is strong")
    


password = input("Enter your password to check its strength : ")
strength_checker(password)
