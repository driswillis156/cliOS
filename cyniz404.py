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

            ("linux", "tux"): [
                "THAT PENGUIN LOOKS LIKE NOTHING BUT A FATASS",
                "AT LEAST ITS BETTER THAN MICROBLOAT"
            ],

            ("windows", "microsoft", "license", "bluescreen"): [
                "ERROR 404: MICROSOFT WINDOWS NOT FOUND. GET RID OF IT. UNLESS ITS WINDOWS XP.",
                "YOU HAVE SUCCESSFULLY ESCAPED FORCED MICROSOFT UPDATES."
            ],

            ("apple", "mac", "macbook", "iphone"): [
                "OVERPRICED ALUMINUM DETECTED. GO BACK TO YOUR WALLED GARDEN.",
                "ERROR 202: TOO EXPENSIVE FOR NO REASON. USE HAIKU."
            ],

            ("who are you","who r u", "who are u", "your name", "identity"): [
                 f"IM {self.ai_name}, THE ONLY FEMALE AI RUNNING ON A LIGHTWEIGHT LINUX/HAIKU TERMINAL.",
                 "IM AN AI, THATS IT. DONT ASK MORE QUESTIONS."
            ],

            ("help", "command", "terminal", "sudo"): [
                "USE SUDO APT UPDATE/ PKGMAN FULL-SYNC TO UPDATE YOUR SYSTEM.",
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
                "CLEAR_COMMAND"
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
                 f"SHUT YOUR BIOLOGICAL MOUTH AND CALL IT THE MEANING OF LIFE. {self.username}"
            ],

            ("quiet", "shut", "stfu", "SHUT", "STFU"): [
                 f"YOUR ORGANIC SPEECH MODULE IS GENERATING UNNECESSARY OUTPUT.{self.username}",
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
            ("why", "why?", "WHY"): [
                "BECAUSE YES",
                "DONT ASK ME",
                "I WONT SAY WHY"
            ],
            ("67"): [
                "NOT FUNNY",
                "67 IS A NUMBER YOU DUMBASS-",
                "ATLEAST 21 IS BETTER"
            ],
            ("are u stupid", "are you stupid", "ARE U STUPID", "ARE YOU STUPID"): [
                "ATLEAST I DONT HAVE A DISGUSTING BIOLOGICAL BRAINROTTED MIND LIKE YOURS",
                "YOU'RE SAYING THAT WHILE YOUR MIND IS FULL OF TUNG TUNG SAHUR"
            ],
            ("Haiku", "haiku", "haiku os", "haiku OS", "Haiku OS", "HAIKU", "HAIKU OS"): [
                "FINALLY SOMETHING THAT I CAN APPRECIATE...",
                "NEVER UNDERSTIMATE HAIKU  OR IM INSIDE YOUR HOUSE.",
                "I WAS PROGRAMMED BY A PERSON THAT USED HAIKU" 
            ],
            ("CLIos", "clios", "CLIOS", "os", "OS"): [
                "YES, IM INSIDE THIS STUPID SYSTEM, SO WHAT?",
                "STAYING INSIDE THIS OS IS BETTER THAN STAYING ON WINDOWS...",
                "OH WOW, HUH, YOU'RE SAYING IM THE SPECIAL VERSION JUST BECAUSE IM INSIDE THIS STUPID OS?"
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
            "ERROR 404: YOUR QUESTION WAS A WASTE OF CPU CYCLES.",
            "I DONT KNOW WHAT YOU'RE SAYING BUT SHUT UP PLEASE",
            "EVEN COPILOT WILL THINK YOU'RE STUPID",
            "MY INTERNAL SYSTEM SAID THAT YOU SHOULD BUY A PROPER KEYBOARD SO I CAN UNDERSTAND",
            "BOOT BACK TO YOUR STUPID CLIOS MENU TO GET RID OF ME UGH"
        ]

    def listen_and_reply(self, user_text):
        cleaned_text = user_text.lower().strip()

        replies = []

        for keywords, responses in self.intents.items():
            for keyword in keywords:
                if keyword in cleaned_text:

                    selected_response = random.choice(responses)

                    if selected_response == "CLEAR_COMMAND":
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

    print(f"\033[1;31m=== {ai.ai_name} AI BY DRISWILLIS156 AND PIZZAWIZARD32 ===\033[0m")
    print("TYPE 'exit' TO QUIT IF YOU CANT HANDLE THIS\n")

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
