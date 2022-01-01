from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont



def pick_img():
    global tk_img
    global resized_img
    img_path = filedialog.askopenfilename(filetypes=[('image files', ('.png', '.jpg'))])
    choosen_img = Image.open(img_path)
    resized_img = resize(xy, zoom, choosen_img)
    tk_img = ImageTk.PhotoImage(resized_img)
    canvas.itemconfig(can_img, image=tk_img)

def rootSize(root):
    root.update_idletasks()
    width = int(root.winfo_width() * 1.0)
    hight = int(root.winfo_height() * 1.0)
    return width, hight


def resize(xy, scale, img):
    xy = [int(x* y) for (x, y) in zip(xy, scale)]
    resized_img = img.resize((xy[0], xy[1]), Image.ANTIALIAS)
    return resized_img

def view_changes():
    global tk_img
    global out
    info = watermark.get()
    e_img = resized_img.convert('RGBA')
    txt = Image.new('RGBA', e_img.size, (255,255,255,0))
    fnt = ImageFont.truetype("Tahoma.ttf", 20)
    draw = ImageDraw.Draw(txt)
    draw.text((20, 20),info ,font=fnt, fill='#696969')
    out = Image.alpha_composite(e_img, txt)
    tk_img = ImageTk.PhotoImage(out)
    canvas.itemconfig(can_img, image=tk_img)

def save_changes():
    global out
    out.save('output_img.png')

#create the root
root = Tk()
root.title('Watermarker')
root.config(padx=30, pady=20)

zoom = (2.5, 2.0)
xy = rootSize(root)

#this is the test image
img = Image.open('test.jpg')
resized_img = resize(xy, zoom, img)
tk_img = ImageTk.PhotoImage(resized_img)

#the canvas 
canvas = Canvas(root, width=500, height=500)
can_img = canvas.create_image(250,250, image=tk_img, anchor='center')
canvas.grid(column=0, row=0, columnspan=2)


upload_btn = Button(root, text='Upload Image', command=pick_img)
upload_btn.grid(column=0, row=1)

label = Label(text='Put your watermark text here')
label.grid(column=1, row=1)

watermark = Entry(root)
watermark.grid(column=1, row=2)

see_change = Button(root, text='View Changes', command=view_changes)
see_change.grid(column=0, row=3)

confirm = Button(root, text='Confirm & Save', command=save_changes)
confirm.grid(column=1, row=3)

root.mainloop()
