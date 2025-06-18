# %%
def say_hi(name=""):
    print("Hello", name)

while True:
    name = input("Your name: ")
    if name in ("Stop", "stop", "Exit", "exit"):
        print("Goodbye! Have a nice day!")
        break
    say_hi(name)

# %%
def square(x):
    return x * x

while True:
    x = input("Enter a number to square (or type 'Stop' to exit): ")
    if x in ("Stop", "stop", "Exit", "exit"):
        print("Goodbye! Have a nice day!")
        break
    try:
        x2 = square(float(x))
        print(f"The square of {x} is {x2}.")
    except:
        print("Please enter a valid number.")



