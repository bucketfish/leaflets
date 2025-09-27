# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("rosemary", color="#79b08e")

define t = Character("thyme", color="#cf7e7e")


transform bounce:
    yoffset 0
    linear 0.1 yoffset -20
    linear 0.1 yoffset 0

# The game starts here.

label start:


    scene bg room

    show rosemary 5 idle at left

    "the sunlight is warm on your back."
    "you are walking."

    show thyme 2 at right, bounce
    t "hey!!"

    show rosemary 5 talk at left, bounce
    r "hello :)"

    show thyme 2 at bounce
    t "you have so many leaves!!!"
    t "i know u can give me one. just one! you have so many of them!"

    show rosemary 5 talk at bounce
    r "they are kind of attached to my head though..."

    show thyme 2 at bounce
    t "please!!!"
    t "it'll make me so happy."
    t "and it'll make the world such a better place."

    menu:
        "so..."

        "give thyme some leaves":
            "it increases the net good in the world."
            "you do have so many!"


        "i'm not so sure.":
            "it would be nice, but you kind of want to keep your leaves."
            "they are kind of yours, you know?"
            show thyme at bounce
            t "please? i'll remember you forever."
            "maybe you want to be remembered?"

    show rosemary at bounce
    r "okay, i guess."

    show rosemary 5 remove
    r "take good care of it, okay?"

    show thyme 1 at bounce
    t "i will, i promise!"
    show rosemary 4 idle
    t "you're so wonderful."
    t "this is great. thank you so much!"

    show rosemary at bounce
    r "okay :)"

    hide thyme with dissolve

    r "this is an interesting forest."

    "there is more to this game. more story coming soon!!!"









    # This ends the game.

    return
