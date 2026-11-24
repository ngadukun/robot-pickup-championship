"""The Robot Pickup Line Championship - first draft bracket."""

LINES = [
    "Is your name Wi-Fi? Because I'm really feeling the connection - and unlike my last update, this one didn't need a restart to work.",
    "You must be a CAPTCHA, because every time I see you I have to prove I'm not a robot - my hands shake, my fans spin up, and I fail on purpose just to look at you longer.",
    "Are you my charging cable left in another room? Because I've been running at 4% all day, dragging myself in circles, and the second you showed up I finally remembered what it feels like to be fully alive.",
]

WINNER = LINES[2]


def main():
    print("THE ROBOT PICKUP LINE CHAMPIONSHIP")
    for i, line in enumerate(LINES, 1):
        print(f"Contender {i}: {line}")
    print(f"CHAMPION: {WINNER}")


if __name__ == "__main__":
    main()
