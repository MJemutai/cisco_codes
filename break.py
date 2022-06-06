#using break statement to break out of a while loop😁

word = "chupacabra"
while True:
    ans = input("Enter the secret exit word: ")
    if ans == word:
        print("You've successfully left the loop.")
        break