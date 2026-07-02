# try:
#     f = open('nonexistngfile.txt')
#     # var = badvar
# except FileNotFoundError:
#     print("file not found to fetch")
# except Exception:
#     print("Something went wrong")


try:
    f = open('existingfile.txt')
    # var = badvar
except FileNotFoundError as e:
    print(f"Error: {e}")
    print("Description: File not found to fetch")
except Exception as e:
    print(f"Error: {e}")
    print("Description: Something went wrong")
else:
    print(f.read())
    f.close()
finally:
    print("Execute finally no matter what")

try:
    a = int(input("Enter value: "))
    if a<0:
        raise Exception("Only positives")
    b = int(input("Enter value: "))
    if b<0:
        raise Exception("Only Positives")
    c = a/b
    print(f"{a:.2f} div by {b:.2f} is {c:.2f}")
except ZeroDivisionError as e:
    print("Simple Description: Division by 0 is not valid")
    print(f"Error: {e}")
except Exception as e:
    print(e)