from ai_models.api import send_prompt


def main():
    messages = []


    while True:
        content = input("Enter your prompt (or 'q' to quit): ")


        if content == "q":
            break


        responce = send_prompt(content, messages)

        print()
        print(responce)
        print()

if __name__ == "__main__":
    main()
