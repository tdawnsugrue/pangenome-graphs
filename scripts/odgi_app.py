
# app for using various odgi commands (viz, sort, etc.)

# wants to be able to do the following:
"""
- look at subregions of the graph w/ odgi extract (or the feature built into odgi viz, takes roughly the same time...)
- sort the graph in different ways with odgi sort
- display the graph with odgi viz
- display at different 'resolutions/bin-widths'
"""
import os
from PIL import Image
import customtkinter as ctk

WINDOW_SIZE = (1200, 576)


class OptionMenu(ctk.CTkFrame):
    # contains options --> for now -, bin width, and sort mode
    def __init__(self, master): # not sure why master
        super().__init__(master)

        self.graph_label = ctk.CTkLabel(self, text="odgi graph")
        self.graph = ctk.CTkEntry(self, placeholder_text="filename.og")

        self.graph_label.grid(row=0, column=0)
        self.graph.grid(row=0, column=1)

        ## odgi options
        self.sort_label = ctk.CTkLabel(self, text="Sort Method")
        self.sort_options = ctk.CTkOptionMenu(self, values=["","L","M","A","R"])

        self.sort_label.grid(row=1, column=0)
        self.sort_options.grid(row=1, column=1)

        # button
        self.btn = ctk.CTkButton(self, text="go", 
                                 command=lambda:test_load(self.graph.get(), self.sort_options.get()))
        self.btn.grid(row=0, column=2)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("ODGI viz viewer (TEST)")
        self.geometry(f"{WINDOW_SIZE[0]}x{WINDOW_SIZE[1]}")

        self.menu = OptionMenu(self)
        self.menu.grid(row=0, column=0)
        
        test = Image.open("img/irgm_sort_A.png")
        print(test.size)

        self.imgsize = test.size # assuming longer than wide

        rescale = (WINDOW_SIZE[0] - 100) / self.imgsize[0]

        frame_size = (WINDOW_SIZE[0]-100, self.imgsize[1] * rescale)

        img = ctk.CTkImage(Image.open("img/irgm_sort_A.png"), size=frame_size) 
        self.image_container = ctk.CTkLabel(self, text="", image=img)
        self.image_container.grid(row=1, column=0)

app = App()

def get_frame_size(img):
    rescale_factor = (WINDOW_SIZE[0] - 100) / img.size[0]
    return (WINDOW_SIZE[0] - 100, img.size[1] * rescale_factor) 

# checks file validity
def test_load(file: str, sort: str):
    try:
        run_odgi(file, sort)
    except:
        print("Something went wrong when loading an image...")

def run_odgi(file, sort):
    if len(sort) == 1:
        print(f"attempting to sort file {file} with method {sort}")
        os.system(f"./bin/odgi sort -i {file} -o - -O -{sort} | ./bin/odgi viz -i - -o tmp.png -s '#'")
        img = Image.open("tmp.png")
        size = get_frame_size(img)

        widget = ctk.CTkImage(img, size=size)
        app.image_container.configure(require_redraw=True, image=widget)


app.mainloop()

os.system("rm tmp.png")