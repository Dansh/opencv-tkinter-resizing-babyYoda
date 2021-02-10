import cv2
import tkinter as tk
from PIL import Image, ImageTk


def download():  
    img = cv2.imread('assets/babyoda.jpg', 1)
    img = cv2.resize(img, (int(width_input.get()), int(height_input.get())))
    cv2.imwrite("C:\\Users\\danda\\Downloads\\babyoda_resized.jpg", img)


root = tk.Tk()
root.geometry("500x700")
load = Image.open('assets/babyoda.jpg')
render = ImageTk.PhotoImage(load)
tk_img = tk.Label(root, image=render)
tk_img.image = render
tk_img.place(x=-2, y=-2)
width_input = tk.Entry(root, width=25, justify="center")
height_input = tk.Entry(root, width=25, justify="center")
width_label = tk.Label(root, text="Width: ", font="Arial")
height_label = tk.Label(root, text="Height: ", font="Arial")
items = [width_input, height_input, width_label, height_label]
download_button = tk.Button(root, text="Download", font="Arial", command=download)
download_button.place(x=195, y=630)

input_x = 70
input_y = 580
label_x = 70
label_y = 540

for each_item in items:
    if isinstance(each_item, tk.Entry):
        each_item.place(x=input_x, y=input_y)
        input_x += 200
    elif isinstance(each_item, tk.Label):
        each_item.place(x=label_x, y=label_y)
        label_x += 200




root.mainloop()