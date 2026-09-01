from ai_models.api import send_prompt


def main():
    messages = []


    while True:
        content = input("Enter your prompt (or 'exit' to quit): ")


        if content == "exit":
            break


        response = send_prompt(content, messages)

        print("")
        print(response)
        print("")





if __name__ == "__main__":
    main()
