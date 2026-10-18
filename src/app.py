def greet_user(name: str):
    if not name:
        return "Hello, Guest! Welcome to Telecom GenAI Assistant."
    return f"Hello, {name}! Welcome to Telecom GenAI Assistant."

def main():
    print(greet_user("Zuheb"))

if __name__ == "__main__":
    main()
