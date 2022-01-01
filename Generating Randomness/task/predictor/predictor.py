print('Print a random string containing 0 or 1:')
final_string = ""
while len(final_string) < 100:
    user_input = input()
    for c in user_input:
        if c in ("0", "1"):
            final_string += c
    if len(final_string) < 100:
        print(f"Current data length is {len(final_string)}, {100 - len(final_string)} symbols left")
print(f"Final data string:\n{final_string}")
triads = {"000": [0, 0], "001": [0, 0], "010": [0, 0], "011": [0, 0], "100": [0, 0], "101": [0, 0], "110": [0, 0],
          "111": [0, 0]}
for i in range(len(final_string) - 3):
    if final_string[i + 3] == "0":
        triads[final_string[i:i + 3]][0] += 1
    else:
        triads[final_string[i:i + 3]][1] += 1
# for key, val in sorted(triads.items()):
#     print(f"{key}: {val[0]},{val[1]}")
print("Please enter a test string containing 0 or 1:")
test_str = input()
n = len(test_str)
predict_str = ""
sumo = 0
for key, val in triads.items():
    if sum(val) > sumo:
        predict_str = key

correct_predictions = 0
for i in range(3, n):
    predict = triads[test_str[i-3:i]]
    predict_str += "0" if predict[0] > predict[1] else "1"
    if test_str[i] == predict_str[i]:
        correct_predictions += 1
probability = round((correct_predictions/(n-3))*100, 2)
print(f"prediction:\n{predict_str}")
print(f"Computer guessed right {correct_predictions} out of {n-3} symbols ({probability} %)")
