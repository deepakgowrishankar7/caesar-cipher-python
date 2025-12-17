def encrypt(original_text,shift_amount):
    caesar_text = ""
    for i in original_text:
        if i not in alphabets:
            caesar_text+=i
        else:
            shifted_position = alphabets.index(i)+shift_amount
            shifted_position %= len(alphabets)
            caesar_text += alphabets[shifted_position]
    print(f"Here is your encoded text:{caesar_text}")

def decrypt(decoded_text,decoded_shift_amount):
    output_text = ""
    for i in decoded_text:
        if i not in alphabets:
            output_text += i
        else:
            shifted_position = alphabets.index(i) - decoded_shift_amount
            shifted_position %= len(alphabets)
            output_text += alphabets[shifted_position]
    print(f"Here is your decoded text:{output_text}")


print("""
   _____                           _____ _       _               
  / ____|                         / ____(_)     | |              
 | |     __ _  ___  ___  __ _ _ __| |     _ _ __ | |__   ___ _ __ 
 | |    / _` |/ _ \/ __|/ _` | '__| |    | | '_ \| '_ \ / _ \ '__|
 | |___| (_| |  __/\__ \ (_| | |  | |____| | |_) | | | |  __/ |   
  \_____\__,_|\___||___/\__,_|_|   \_____|_| .__/|_| |_|\___|_|   
                                            | |                  
                                            |_|                  
""")

alphabets=("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")

def options():
    direction = input("Type 'encode' for encrypt or decode for decrypt:\n").lower()
    if direction == 'encode':
        original_text = input("Enter the original Text:\n").lower()
        shift_amount = int(input("Enter shift number:\n"))
        encrypt(original_text,shift_amount)
    elif direction == 'decode':
        decoded_text = input("Enter decoded text:\n")
        decoded_shift_amount = int(input("Enter decoded shift amount:\n"))
        decrypt(decoded_text,decoded_shift_amount)
    else:
        print("You entered option is no correct")

user_opinion=input("You are ready to do encrypt or decrypt 'yes' 'No' :").lower()
while "True":
    if user_opinion == "yes":
           options()
           user_option2 = input("You are ready to do encrypt or decrypt 'yes' 'No' :").lower()
           if user_option2 == "yes":
               options()
           else:
               print("Thanks for visiting")
               break
    else:
        print("Thanks for visiting")
        break