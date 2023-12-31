import dialogflow
import PIL.Image
import PIL.ImageFont
import PIL.ImageDraw
import tkinter as tk

API_KEY = "AIzaSyBJGZU6GuuR21Oc3dZ9HPU-Pl8sgOa3bfQ"

def centrar_imagen(image):
    width, height = image.size
    new_width = (width - height) // 2
    new_image = image.crop((new_width, 0, width - new_width, height))
    return new_image

def greet():
    image = PIL.Image.open("images/humwindroit-robot-holding-atom.jpg")
    image = centrar_imagen(image)
    font = PIL.ImageFont.truetype("arial.ttf", 30)
    draw = PIL.ImageDraw.Draw(image)
    draw.text((20, 20), "Asistente Con IA de HumWindroit", font=font, fill=(255, 255, 255))

    root = tk.Tk()
    root.title("Asistente HumWinDroit")

    image_label = tk.Label(root, image=image)
    image_label.pack()

    start_button = tk.Button(root, text="Iniciar Chat", command=start_chat)
    start_button.pack()

    root.mainloop()

def start_chat():
    global name
    name = ""

    while name == "":
        name = input("�Cu�l es tu nombre? ")

    show_chat_bot()

def show_chat_bot():
    image_label.destroy()

    root.title("Chat con HumWinDroit")

    while True:
        question = input("�Qu� quieres preguntarme? ")
        response = respond_to_question(question)
        print(response)

def respond_to_question(question):
    try:
        response = dialogflow.Agent(API_KEY).query(question)
        return response.fulfillment_text
    except dialogflow.exceptions.InvalidArgumentError:
        return "No entiendo tu pregunta. �Puedes reformularla?"

if __name__ == "__main__":
    greet()
