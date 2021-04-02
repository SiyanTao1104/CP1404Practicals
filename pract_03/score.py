import random
lowest_score = 0
largest_score = 100

def main():
    score = int(input("Please enter your score: "))
    out_file = open("result.txt","w")
    for _ in range(score):
        random_number = random.randint(lowest_score, largest_score+1)
        result = determine_score(random_number)
        print("{} is {}".format(random_number,result),file=out_file)
    out_file.close()


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