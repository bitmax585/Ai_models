from ai_models.api import send_prompt


def main():
    messages = []


    while True:
        print("\nEnter your prompt:")
        print("(Press Enter twice to send, or type 'q' to quit)")

        lines = []

        while True:
            line = input(">>> ")

            if line == "":
                break

            if line == "q" and not lines:
                return        

            lines.append(line)

        content = "\n".join(lines)


        send_prompt(content, messages)

        print()

if __name__ == "__main__":
    main()
