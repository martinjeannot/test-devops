def main():
    result = compute(3, 2)
    print(f"""Result is {result}""")

def compute(a: int, b: int):
    return a + b

if __name__ == "__main__":
    main()