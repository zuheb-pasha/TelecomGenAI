def greet_user(name: str):
    if name is None:
        raise TypeError("Name cannot be None")
    return f"Hello, {name}! Welcome to Telecom GenAI Assistant."

def main():
    print(greet_user("Zuheb"))

if __name__ == "__main__":
    main()
