def main():
    in_file = open("temps_input.txt","r")
    out_file = open("temps_output.txt","w")
    for i in in_file:
        fahrenheit = float(i)
        celsius = fahrenheit_to_celsius(fahrenheit)
        print("{}".format(celsius),file=out_file)
    in_file.close()
    out_file.close()

def fahrenheit_to_celsius(fahrenheit):
    return 5.0 * (fahrenheit - 32) / 9

main()