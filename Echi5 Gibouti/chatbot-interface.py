import tkinter as tk
from tkinter import scrolledtext
from PIL import ImageTk, Image


# Create the GUI window
window = tk.Tk()
window.title("Spaguittita")
window.geometry("400x500")

# Create a scrolled text widget to display the conversation
conversation = scrolledtext.ScrolledText(window, height=20, width=50)
conversation.pack()

# Create an entry widget for user input
user_input = tk.Entry(window, width=50)
user_input.pack()

# Function to handle user input and display bot response
def handle_user_input():
    user_message = user_input.get()
    conversation.insert(tk.END, "User: " + user_message + "\n")
    
    # Generate bot response here using the model and tokenizer
    
    # Simulate bot response
    bot_message = "This is the bot's response."
    
    conversation.insert(tk.END, "Bot: " + bot_message + "\n")
    user_input.delete(0, tk.END)  # Clear user input

# Create a button to submit user input
submit_button = tk.Button(window, text="Send", command=handle_user_input)
submit_button.pack()

# Start the GUI event loop
window.mainloop()
