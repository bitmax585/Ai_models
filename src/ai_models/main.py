from ai_models.api import send_prompt


def main():
    messages = []


    while True:
        content = input("Enter your prompt (or 'q' to quit): ")


        if content == "q":
            break


        response = send_prompt(content, messages)

        print()
        print(f"\033[96m{response}\033[0m")
        print()

if __name__ == "__main__":
    main()
