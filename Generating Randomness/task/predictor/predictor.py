from random import choice


def clean_input(string: str) -> str:
    clean_str = ""
    for c in string:
        if c in "01":
            clean_str += c
    return clean_str


def train_model(string: str):
    global triads
    for ind in range(len(string) - 3):
        if string[ind + 3] == "0":
            triads[string[ind:ind + 3]][0] += 1
        else:
            triads[string[ind:ind + 3]][1] += 1


def predict():
    global triads
    print("You have $1000. Every time the system successfully predicts your next press, you lose $1.")
    print("Otherwise, you earn $1. Print \"enough\" to leave the game. Let's go!")
    user_balance = 1000
    while True:
        print("Print a random string containing 0 or 1:")
        user_game_input = input()
        if user_game_input == "enough":
            break
        test_str = clean_input(user_game_input)
        n = len(test_str)
        if n == 0:
            continue
        predict_str = ""
        for _ in range(min(n, 3)):
            predict_str += choice("01")

        correct_predictions = 0
        for ind in range(3, n):
            triad = triads[test_str[ind - 3:ind]]
            predict_str += "0" if triad[0] > triad[1] else "1"
            if test_str[ind] == predict_str[ind]:
                correct_predictions += 1
        user_balance += (n - 3) - 2 * correct_predictions if n >= 3 else 0
        probability = round((correct_predictions / (n - 3)) * 100, 2)
        print(f"prediction:\n{predict_str}")
        print(f"Computer guessed right {correct_predictions} out of {n - 3} symbols ({probability} %)")
        print(f"Your balance is now ${user_balance}")
        train_model(test_str)
    print("Game over!")


if __name__ == "__main__":
    print("Please give AI some data to learn...\nThe current data length is 0, 100 symbols left")
    print('Print a random string containing 0 or 1:')

    final_string = ""

    while len(final_string) < 100:
        user_input = input()
        final_string += clean_input(user_input)
        if len(final_string) < 100:
            print(f"Current data length is {len(final_string)}, {100 - len(final_string)} symbols left")

    print(f"Final data string:\n{final_string}")

    triads = {"000": [0, 0], "001": [0, 0], "010": [0, 0], "011": [0, 0], "100": [0, 0], "101": [0, 0], "110": [0, 0],
              "111": [0, 0]}

    train_model(final_string)
    # for key, val in sorted(triads.items()):
    #     print(f"{key}: {val[0]},{val[1]}")

    predict()
