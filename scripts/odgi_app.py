
# app for using various odgi commands (viz, sort, etc.)

# wants to be able to do the following:
"""
- look at subregions of the graph w/ odgi extract (or the feature built into odgi viz, takes roughly the same time...)
- sort the graph in different ways with odgi sort
- display the graph with odgi viz
- display at different 'resolutions/bin-widths'
"""
import os
import subprocess
from PIL import Image
import customtkinter as ctk

WINDOW_SIZE = (1200, 576)


class OptionMenu(ctk.CTkFrame):
    # TO INCLUDE: bin width (bp), subregion
    # bin width is easy and can just be passed straight to odgi viz
    # for subregion we want to do one of the following:
    '''
    1. get the name of the GRCh path & coords available
    '''

    # contains options --> for now -, bin width, and sort mode
    def __init__(self, master): # not sure why master
        super().__init__(master)

        self.graph_label = ctk.CTkLabel(self, text="odgi graph")
        self.graph = ctk.CTkEntry(self, placeholder_text="filename.og")

        self.graph_label.grid(row=0, column=0)
        self.graph.grid(row=0, column=1)

        ## odgi options
        self.sort_section = ctk.CTkLabel(self, text="View Options:")
        self.sort_label = ctk.CTkLabel(self, text="Sort")
        self.sort_options = ctk.CTkOptionMenu(self, values=["L","M","A","R"])
        
        # filter options
        self.filter_section = ctk.CTkLabel(self, text="Subgraph options")
        self.path_label = ctk.CTkLabel(self, text="Path:")
        self.path_options = ctk.CTkOptionMenu(self, values=[] )

        self.sort_section.grid(row=1, column=0)
        self.sort_label.grid(row=1, column=1)
        self.sort_options.grid(row=1, column=2)
        self.filter_section.grid(row=2, column=0)
        self.path_label.grid(row=2, column=1)
        self.path_options.grid(row=2, column=2)

        # button
        self.btn = ctk.CTkButton(self, text="Load Graph", 
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

def get_graph_paths(file):
    # runs odgi paths -L and returns a list of every path that odgi output
    paths = subprocess.run(["./bin/odgi", "paths", "-L", "-i",f"{file}"])
    if paths.returncode != 0:
        print("An error occurred when getting paths for a graph. Most likely you supplied an invalid file.")
        return []
    p = paths.stdout.decode().split("\n")
    print(p)
    return []

app.mainloop()

os.system("rm tmp.png")