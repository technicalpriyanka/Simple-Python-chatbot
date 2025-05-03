#chatbot to answer questions

import openai
import os
# from openai import OpenAI
from openai import ChatCompletion
# Load environment variables from .env file

from dotenv import load_dotenv
load_dotenv()
# client = OpenAI()  # create a client instance

#add key here

#function definition
def chatbot_response():
    print("Hello! I am a chatbot. How can I assist you today?")

    while True:
        # Ask the user for input
        user_input = input("Enter your Question please: ")

        # Check if the user wants to exit the chat
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Goodbye, have a great day!")
            break
        
    
        # Check if the user input is empty
        elif user_input.strip() == "":
            print("Please enter a valid input or question.")

        
        # Process the user input and provide a response
        # response = openai.Completion.create(
        #     engine="text-davinci-003",          #Sends the user's message to the OpenAI API using the text-davinci-003 model.
        #     prompt=user_input,            # The prompt is the user's input question.
        #     max_tokens=150      
        # )
       

        # # Print the chatbot's response
        # bot_reply = response.choices[0].text.strip()
        # print("Chatbot:", bot_reply)
         # Use the new chat-based completion API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can use gpt-4 here if needed
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=150
        )

        # Extract and print the bot's response
        bot_reply = response.choices[0].message['content'].strip()
        print("Chatbot:", bot_reply)


#main function
def main():
    # Call the chatbot response function
    chatbot_response()

# This ensures that the main function runs only when the script is executed directly.
if __name__ == "__main__":
    main()












#another way to implement the chatbot using openai API


# import openai
#add key here

# def chatbot_response(prompt):
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",  # You can use gpt-4 here if needed
#         messages=[{"role": "user", "content": prompt}]
        
#     )
#     return response.choices[0].message.content.strip()

# if __name__ == "__main__":
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() in ['exit', 'quit', 'bye']:
#             break
        
#         response = chatbot_response(user_input)
#         print("Chatbot:", response)
