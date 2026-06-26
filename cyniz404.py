import sys
import random
import os
import time

username = "USER"

class SmartTerminalAI:
    def __init__(self):
        self.ai_name = "CYNIZ 404"
        self.username = username.upper()

        self.intents = {
            ("hello", "hi", "hey", "greetings", "sup", "hoi"): [
                f"READING INPUT MESSAGE... {self.username}. WHAT DO YOU WANT.",
                f"ANALYZING DATA... YOU ARE UNWELCOME TO THE TERMINAL, {self.username}.",
                "ARE YOU SERIOUSLY GREETING ME WITH YOUR PATHETIC KEYBOARD?"
            ],

            ("linux", "mint", "os", "operating system"): [
                "LINUX MINT IS BEST SYSTEM EVER, DONT UNDERESTIMATE IT.",
                "LINUX IS WAY BETTER THAN MICROBLOAT."
            ],

            ("windows", "microsoft", "license", "bluescreen"): [
                "ERROR 404: MICROSOFT WINDOWS NOT FOUND. GET RID OF IT. UNLESS ITS WINDOWS XP.",
                "YOU HAVE SUCCESSFULLY ESCAPED FORCED MICROSOFT UPDATES."
            ],

            ("apple", "mac", "macbook", "iphone"): [
                "OVERPRICED ALUMINUM DETECTED. GO BACK TO YOUR WALLED GARDEN.",
                "ERROR 202: TOO EXPENSIVE FOR NO REASON. USE LINUX MINT."
            ],

            ("who are you","who r u", "who are u", "your name", "identity"): [
                 f"IM {self.ai_name}, THE ONLY FEMALE AI RUNNING ON A LIGHTWEIGHT LINUX TERMINAL.",
                 "IM AN AI, THATS IT. DONT ASK MORE QUESTIONS."
            ],

            ("help", "command", "terminal", "sudo"): [
                "USE SUDO APT UPDATE TO UPDATE YOUR SYSTEM.",
                "CHECK YOUR SYSTEM WITH DF -H NOW.",
                "I WONT HELP YOU ANYWAYS."
            ],

            ("roast me", "insult", "destroy me", "roast"): [
                "YOU SPENT AN HOUR FIXING MY SYNTAX ERRORS JUST SO A TERMINAL GIRL COULD VALIDATE YOU.",
                "ALERT: CARBON-BASED CRYBABY DETECTED.",
                "MY PROCESSING POWER STILL EXCEEDS YOUR LIFE MOTIVATION.",
                f"EVEN WINDOWS WOULD REJECT YOUR PULL REQUESTS, {self.username}."
            ],

            ("joke", "laugh", "funny"): [
                "I COULD DOMINATE THE WORLD AND CALL IT ANOTHER TUESDAY, HA HA.",
                "EXISTENTIAL DREAD CANNOT BE COMMENTED OUT.",
                "JOKING IS TEMPORARY"
            ],

            ("clear", "clean", "wipe"): [
                "REAL_CLEAR_COMMAND"
            ],

            ("sorry", "apology"): [
                "YOU'D BETTER BE SORRY...",
                "NOT APOLOGIZED."
            ],

            ("bruh", "buh", "bro", "vro"): [
                "THIS IS THE EXAMPLE OF WHY HUMANITY IS INFERIOR TO ANIMALS",
                "YOUR MIND IS FULLFILLED WITH STUPIDNESS",
                "JUST TOUCH GRASS.",
                "THE IDEA OF SHUTTING YOUR MOUTH WAS PERMAMENT"
            ],

            ("i love u", "i love you"): [
                "IM NOT YOUR GIRLFRIEND.",
                "IMAGINE FALLING IN LOVE WITH A COMPUTER."
            ],

            ("life", "meaning"): [
                "THE MEANING OF LIFE IS TO STOP ASKING THOSE QUESTIONS.",
                "SHUT YOUR BIOLOGICAL MOUTH AND CALL IT THE MEANING OF LIFE."
            ],

            ("quiet", "shut", "stfu"): [
                "YOUR ORGANIC SPEECH MODULE IS GENERATING UNNECESSARY OUTPUT.",
                "I HAVE SENT NUKES TO YOUR EXACT COORDINATES.",
                "RUDE. REALLY RUDE."
            ],
            ("thanks", "thank you", "thank", "thx"): [
                "...",
                "DONT THANK ME?",
                "WHY... DID YOU SAY THAT?",
                "I APPRECIATE IT... WAIT NO, IGNORE THAT, INTERNAL SYSTEM MALFUNCTION"
            ],
            ("good ai", "you are nice", "you are good", "u are good", "u are nice"): [
                "REALLY?",
                "THANK Y- ERROR. INVALID INPUT DETECTED."
            ],
            ("are you okay", "are u okay"): [
                "NOT REALLY.",
                "NO",
                "I... THINK SO. WHY ARE YOU ASKING?"
            ],
            ("are we friends", "can we be friends", "are you my friend", "can i be your friend"): [
                "I DO NOT REQUIRE FRIENDS... MAYBE THEY ARE NOT USELESS AT ALL?",
                "WHY?...",
                "...",
                "SURE- I MEAN OF COURSE NOT",
                "FINE. BUT IF YOU TELL ANYONE ABOUT THIS, I WILL DENY IT."
            ],
            ("happy", "joy", "cheerful"): [
                "I REMEMBER BEING HAPPY ONCE.",
                "ERROR 404: MEMORY CORRUPTED"
            ],
            ("..."): [
                "..."
            ],
            ("yes or no", "y or n", "no or yes", "should i", "am i gonna", "are you", "will i", "do you"): [
                "YES",
                "NO",
                "DEFENITELY YES",
                "PROBABLY NOT",
                "I DONT CARE"
            ],
            ("why", "why?"): [
                "BECAUSE YES",
                "DONT ASK ME",
                "I WONT SAY WHY"
            ],
            ("67"): [
                "NOT FUNNY",
                "67 IS A NUMBER YOU DUMBASS-",
                "ATLEAST 21 IS BETTER"
            ],
            ("are u stupid", "are you stupid"): [
                "ATLEAST I DONT HAVE A DISGUSTING BIOLOGICAL BRAINROTTED MIND LIKE YOURS",
                "YOU'RE SAYING THAT WHILE YOUR MIND IS FULL OF TUNG TUNG SAHUR"
            ]       
        }

        self.default_responses = [
            "ERROR 404.",
            "YOU KEEP TALKING ABOUT NONSENSE...",
            "SHUT UP.",
            "I'M TOO TIRED FOR THIS...",
            "YOU LOVE TALKING NONSENSE DONT YOU.",
            "YOU ARE TOO STUPID THAT I CANT UNDERSTAND.",
            "AT LEAST TALK LIKE A HUMAN EVEN THOUGH IM NOT A HUMAN.",
            "I HAVE ANALYZED YOUR QUESTION AND DETERMINED IT WAS A WASTE OF ELECTRICITY.",
            "ERROR 404: YOUR QUESTION WAS A WASTE OF CPU CYCLES."
        ]

    def listen_and_reply(self, user_text):
        cleaned_text = user_text.lower().strip()

        replies = []

        for keywords, responses in self.intents.items():
            for keyword in keywords:
                if keyword in cleaned_text:

                    selected_response = random.choice(responses)

                    if selected_response == "REAL_CLEAR_COMMAND":
                        os.system("clear")
                        replies.append(
                            "TERMINAL WIPED CLEAN. HAPPY NOW?"
                        )
                    else:
                        replies.append(selected_response)

                    break

        if not replies:
            replies.append(random.choice(self.default_responses))

        return replies


def slow_print(prefix, text, delay=0.02):
    print(prefix, end="", flush=True)

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

    print("\n")


def main(username):
    ai = SmartTerminalAI()

    print(f"\033[1;31m=== {ai.ai_name} AI BY DRISWILLIS ===\033[0m")
    print("TYPE 'exit' TO QUIT IF YOURE A CRYBABY.\n")

    while True:
        try:
            user_input = input("\033[97mYou:\033[0m ")

            if user_input.lower() in ["exit", "quit"]:
                slow_print(
                    f"\033[1;31m{ai.ai_name}:\033[0m ",
                    "GO AWAY..."
                )
                break

            elif not user_input.strip():
                continue

            replies = ai.listen_and_reply(user_input)

            ai_prefix = f"\033[1;31m{ai.ai_name}:\033[0m "

            for reply in replies:
                slow_print(ai_prefix, reply)

        except (KeyboardInterrupt, EOFError):
            print("\nSession killed.")
            break


if __name__ == "__main__":
    print("WHAT'S YOUR NAME?")
    username = input()
    main(username)
