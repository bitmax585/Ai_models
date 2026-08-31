from ai_models.api import send_prompt

def main():
    content = input("Enter your prompt: ")
    print("")
    response = send_prompt(content)
    print(response)





if __name__ == "__main__":
    main()
