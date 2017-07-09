films = {
    "Inception": [3,4],
    "Spider Man": [18,9],
    "Wonder Women": [15,21]
    "Deadpool": [21, 14]
    }

while True:
    choice = input("What film would you like to watch?: ").strip().title()

    if choice in films:
        age = int(input("How old are you?: ").strip())

        # check user age

        if age >= films[choice][0]:
            # check enough seats

            if films[choice][1] > 0:
                print("Enjoy the film!")
                films[choice][1] = films[choice][1]-1
                else:
                    print("Sorry, we are sold out!")
            else:
                print("You are too young to see that film!")

        else:
            print("We dont have that film.. Sorry")
            
                
                
