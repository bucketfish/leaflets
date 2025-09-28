# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("rosemary", color="#79b08e")

define t = Character("thyme", color="#cf7e7e")


default counts = {
    "dejavu": 0,
    "freeze": 0,
    "nostalgia": 0,
    "paranoia": 0
}

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
            $ counts["dejavu"] += 1
            $ counts["nostalgia"] += 1
            "it increases the net good in the world."
            "you do have so many!"


        "i'm not so sure.":
            $ counts["freeze"] += 1
            $ counts["paranoia"] += 1
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

    show rosemary at center with move

    "this is an interesting place."
    "it's a forest, but there are no trees."

    menu:
        "you have a strange feeling all of a sudden."

        "it feels like you've been here before.":
            $ counts["dejavu"] += 1
            "the sky is as blue as your crystal-clear memory of it."
            "the rocks are almost familiar."

            menu:
                "how many times have you traveled down this path before?"

                "twice.":
                    "maybe just two times, then."

                "seven times.":
                    "you count it on your fingers."
                    "each time feels the same as the last."

                "maybe twenty.":
                    "it's too many to count."
                    "you pause for a second to think about it."

        "it feels like time has frozen.":
            $ counts["freeze"] += 1
            "the clouds are barely moving."
            "now that you look closer, the trees aren't swaying."

            menu:
                "how long have you been here?"

                "a couple of minutes.":
                    "you could stay a little longer."

                "a few hours.":
                    "you've kind of lost track."

                "you've been walking for a few days.":
                    "you're not sure where you're going."

        "it feels like you're back home again.":
            $ counts["nostalgia"] += 1
            "you feel a light breeze on your skin."
            "it carries with it a strange feeling of alienation."

            menu:
                "how does the wind feel?"

                "like a childhood playground.":
                    "for a second, you hear laughter of children in the distance —"
                    "— it fades as fast as it came."

                "like an open library corridor.":
                    "you can almost smell ink and paper."

                "like a summer hike.":
                    "you wonder if it's summer."
                    "surely not anymore?"

        "it feels like someone is watching you.":
            $ counts["paranoia"] += 1
            "the road ahead of you is empty."
            "you consider looking back, and you shiver."

            menu:
                "you consider looking back, and you shiver.{fast}"

                "because there was wind.":
                    "it was cold wind, too."
                    "you try to ignore it."

                "because you are scared.":
                    "you think about the future."
                    "you're not sure what it holds."

                "it was an involuntary response.":
                    "you shake yourself out of it."


    "a singular leaf drifts down from your head."
    show rosemary 4 talk
    r "i guess i should continue walking...."

    $ temp_winner = max(counts, key=counts.get)

    if temp_winner == "dejavu":
        r "i'm trying to find the end of the road."

    elif temp_winner == "freeze":
        r "i'm trying to figure out what happens next."

    elif temp_winner == "nostalgia":
        r "i'm trying to get back to somewhere i know."

    else:
        r "i'm trying to get out."


    show rosemary 4 idle
    "you round the corner — supposedly, there is a corner to round — and you come across a lone tree stump."



    show rosemary at left
    show tree 1 at right
    with ease

    show rosemary 4 talk at bounce

    r "a tree stump!"
    r "the rest of this place is so empty."
    r "i almost feel bad."

    show tree at bounce
    "the tree stump doesn't talk, because it's a tree stump."
    "you feel it propagating sad vibes to you."

    show rosemary 4 idle
    "you stare at it for a while more."

    menu:
        "you stare at it for a while more.{fast}"

        "it feels like it's trying to say something!":
            $ counts['nostalgia'] += 1
            $ counts["dejavu"] += 1
            r "i'm sorry that i can't hear you."


        "it feels sad.":
            $ counts["freeze"] += 1
            r "i'm sorry."
            "you're not sure why you're sorry, just that you are."
            "you wonder why it's alone."

        "it feels lonely.":
            $ counts["paranoia"] += 1
            r "i'm sorry that i can't stay."
            "for a while, you sit by the tree stump in silence."
            "strangely, it feels like nobody else is alive in this place."

    "you think about thyme."
    "you think about the forest."

    menu:
        "the forest isn't really a forest."

        "i could do more for it.":
            show rosemary 4 talk
            r "i think i might as well."


    show rosemary 4 remove
    "you pluck a branch off your head."
    "it only hurts a little bit this time."

    menu:
        "it only hurts a little bit this time.{fast}"

        "you're making yourself useful.":
            $ counts["paranoia"] += 1
            "this is how you can leave your mark in the world."

        "you're making it feel less alone.":
            $ counts["dejavu"] += 1
            "this is how you can leave your mark in the world."

        "you're giving hope to the forest.":
            $ counts["nostalgia"] += 1
            "this is how you can leave your mark in the world."

        "you're tired.":
            $ counts["freeze"] += 1
            "at least you can make it a little less dreary, i guess."


    show tree 2 at bounce
    "you think that you made a difference."

    show rosemary 3 idle
    "it feels just a little more alive now."

    "the tree stump doesn't reply, because it's a tree stump."
    "you watch it in silence for a while more as the branch sways gently in the wind."
    "it looks somewhat precarious, but you think it'll manage."

    hide tree with dissolve
    show rosemary at center with ease

    "this is about half the game. more story coming soon!!!"
    "thank you for playing so far."

    # This ends the game.

    return
