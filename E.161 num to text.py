num_2_letters = {
    2: "a",
    22: "b",
    222: "c",
    3: "d",
    33: "e",
    333: "f",
    4: "g",
    44: "h",
    444: "i",
    5: "j",
    55: "k",
    555: "l",
    6: "m",
    66: "n",
    666: "o",
    7: "p",
    77: "q",
    777: "r",
    7777: "s",
    8: "t",
    88: "u",
    888: "v",
    9: "w",
    99: "x",
    999: "y",
    9999: "z",
    0: " "
}


def input_numbers():
    numbers = []
    y = ''

    while y != 1:
        y = int(input("Enter your message using the E.161 Keymapping, terminate the process by inputing a 1: "))
        if y not in num_2_letters.keys():
            print(
                "The E.161 keymap does not contain the digits you did input, please check the E.161 keymap online for refference"
            )
        else:
            numbers.append(y)
    numbers.pop(-1)
    return numbers


numbers = input_numbers()

for num in numbers:
    print(num_2_letters.get(num), end='')
