# Make sure you upload image in your contact in your current Repl
# Import all the necessary libraries 
# PIL (Python Imaging Library) provides image ediiting capabilities to the python
interpreter
from tkinter import *
from PIL import Image, ImageTK

# Create a window witj a title bat and set its geometry as well
root = TK()
root.title('image')
root.geometry('400x400')

# Now use Image.open to open and indentify the given image file.
upload = Image.open("https://th.bing.com/th/id/OIP.j4KdqaXpnhbN94WzVyHUhAHaE8?w=243&h=180&c=7&r=0&o=5&pid=1.7")

# Convert this Image to Tkinter compatible image
image = ImageTK.PhotoImage(upload)

# Add image to Tkinter label
Label = label(root, image=image, height=350, width=300)
label.place(x=50, y=0)
Label2 = label(root,text="  This is how you add image in Tkinter Window")
Label2.place(x=40, y=360)


# Run the application
root.mainloop()