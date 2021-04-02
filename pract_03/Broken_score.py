def main():
    score = float(input("Please enter your score: "))
    result = determine_score(score)
    print(result)


def determine_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif 90 <= score < 100:
        return "Excellent"
    elif 50 <= score < 90:
        return "Passable"
    else:
        return "Bad"


main()
