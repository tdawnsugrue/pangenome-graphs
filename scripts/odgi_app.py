
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
from time import time
from PIL import Image
import customtkinter as ctk

WINDOW_SIZE = (1200, 576)

graph_loaded = False
current_graph = ""
pathlist_unstripped = []
path_coords = {}
coord_limit = [0, 0]
# odgi_path = "./bin/odgi"
odgi_path = "odgi"

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
        self.sort_options = ctk.CTkOptionMenu(self, values=["Default", "L","M","A","R"])
        
        # filter options
        self.filter_section = ctk.CTkLabel(self, text="Subgraph options")
        self.path_label = ctk.CTkLabel(self, text="Path:")
        self.path_options = ctk.CTkComboBox(self, values=["LOAD GRAPH FIRST"], command=self.update_bounds) #path to filter based on
        self.start_coord = ctk.CTkEntry(self, placeholder_text="start coordinate")
        self.end_coord = ctk.CTkEntry(self, placeholder_text="end coord")

        # displays coordinate limits
        self.coord_display = ctk.CTkLabel(self, text="Coord limits: 0-0")

        self.sort_section.grid(row=1, column=0)
        self.sort_label.grid(row=1, column=1)
        self.sort_options.grid(row=1, column=2)
        self.coord_display.grid(row=1, column=3, columnspan=2)
        self.filter_section.grid(row=2, column=0)
        self.path_label.grid(row=2, column=1)
        self.path_options.grid(row=2, column=2)
        self.start_coord.grid(row=2, column=3)
        self.end_coord.grid(row=2, column=4)


        # button - this SHOULDNT sort/filter. Assign to a separate button that only runs if graph loaded
        self.btn = ctk.CTkButton(self, text="Load Graph", 
                                 command=lambda:load_graph(self.graph.get()))
        self.btn.grid(row=0, column=2)

        self.btn_sortfilter = ctk.CTkButton(self, text="Sort & Filter",
                                            command=lambda:sort_filter(self.sort_options.get(), self.get_coords()))
        self.btn_sortfilter.grid(row=0, column=4)

    def get_coords(self):
        path = self.path_options.get()
        if path not in path_coords.keys():
            print("Invalid pathname supplied: Skipping filtering...")
            return None
        
        bounds = path_coords[path]
        start_coord = self.start_coord.get()
        end_coord = self.end_coord.get()
        if not(start_coord.isdigit or end_coord.isdigit):
            print("Error: non-numeric coordinate(s) supplied")
            return None
        
        start_coord = int(start_coord)
        end_coord = int(end_coord)

        if start_coord >= end_coord or start_coord < bounds[0] or end_coord > bounds[1]:
            print("Error: coordinates invalid or out of bounds for the path specified.")
            return None
        
        return [path, start_coord, end_coord]


    def update_bounds(self, path):
        print("chose a choice:", path)
        path = self.path_options.get()
        if path not in path_coords.keys():
            self.coord_display.configure(text="Coord limits: 0-0")
            return
        bounds = path_coords[path]
        self.coord_display.configure(text=f"Coord limit: {bounds[0]}-{bounds[1]}")




class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("ODGI viz viewer (TEST)")
        self.geometry(f"{WINDOW_SIZE[0]}x{WINDOW_SIZE[1]}")

        self.menu = OptionMenu(self)
        self.menu.grid(row=0, column=0)
        
        test = Image.open("img/placeholder.jpg")
        print(test.size)
        self.imgsize = test.size # assuming longer than wide

        rescale = (WINDOW_SIZE[0] - 100) / self.imgsize[0]

        frame_size = (WINDOW_SIZE[0]-100, self.imgsize[1] * rescale)

        self.img = ctk.CTkImage(Image.open("img/placeholder.jpg"), size=frame_size) 
        self.image_container = ctk.CTkLabel(self, text="", image=self.img)
        self.image_container.grid(row=1, column=0)

app = App()

def get_frame_size(img):
    rescale_factor = (WINDOW_SIZE[0] - 100) / img.size[0]
    return (WINDOW_SIZE[0] - 100, img.size[1] * rescale_factor) 

# attempts to load graph from given file
def load_graph(file: str):
    if not os.path.isfile(file) or not(file.endswith(".og")):
        print("file does not exist or is not in .og format")
        return 
    
    global graph_loaded, current_graph
    graph_loaded = True
    current_graph = file
    reload_image()
    print("loaded graph")
    get_graph_paths()
    # get graph paths



# attempts to load the image from tmp.png
def reload_image(graph = None):
    if not graph_loaded : return
    # if graph supplied this will make current graph refer to local instead of global
    print("graph is", bool(graph))
    if not graph: graph = current_graph
    print("graph val:", graph)

    l = subprocess.run([odgi_path,"viz","-i",graph, "-o", "tmp.png", "-s", "#"])
    if l.returncode != 0:
        test = subprocess.run([odgi_path, "sort", "-i", graph, "-o", "-", "-O", "|",
            odgi_path,"viz","-i",graph, "-o", "tmp.png", "-s", "#"])
        print("had to sort prior to load. Subsequent returncode:", test.returncode)
        print(test)

    img = Image.open("tmp.png")
    size = get_frame_size(img)

    # change to having a single image and configuring
    widget = ctk.CTkImage(img, size=size)
    app.img.configure(require_redraw=True, light_image=img)

def get_graph_paths():
    # runs odgi paths -L and returns a list of every path that odgi output
    paths = subprocess.run([odgi_path, "paths", "-L", "-i", current_graph], capture_output=True)
    print("\n\n\n")

    if paths.returncode != 0:
        print("An error occurred when getting paths for a graph. Most likely you supplied an invalid file.")
        return

    global pathlist_unstripped, path_coords

    # REALLY shitty but limiting because of issues working with the dropdown menu :/ vanishes instantly
    paths = [p.decode() for p in paths.stdout.split()[:min(20, len(paths.stdout.split()))]]
    if paths == pathlist_unstripped : return # prevent reloading data if pathlist is the same

    pathlist_unstripped = paths
    options = []
    path_coords = {}
    for p in paths:
        pathname = p[0:p.find(":")]
        options.append(pathname)

        coordstring = p[p.find(":")+1:]
        x = coordstring.find("-")
        start = int(coordstring[0:x])
        end = int(coordstring[x+1:])

        path_coords[pathname] = (start, end)

    app.menu.path_options.configure(require_redraw=True, values = options)

# app dot whatever dot configure (change ctkoptions)

# Sort & filter based on the provided pathname and coordinates. Assumes valid values from prev function
# coords = (PATHNAME, START, END)       sort = single letter code
def sort_filter(sort, coords):
    
    graph_coords = path_coords[coords[0]]
    og_length = graph_coords[1] - graph_coords[0]
    new_length = coords[2] - coords[1]
    start = time()
    # CALLING SORT OR FILTER SHOULD SET CURRENT GRAPH TO A TMP FILE - reload image gets called with tmp.og
    # filter before sort
    # sample for odgi extract:
    #       odgi extract -i file.og -o tmp.og -P -E -r [pathname]:[start]-[end]
    if coords:
        print("Warning: you're subsetting the graph - this might take a long time :)")
        

        # account for offset - prevents seg fault in odgi extract
        coords[1] -= graph_coords[0]
        coords[2] -= graph_coords[0]
        e = subprocess.run(
            [odgi_path, "extract", "-i", current_graph, "-o", "tmp.og", "-P", "-E", "-r", 
             f"{coords[0]}:{graph_coords[0]}-{graph_coords[1]}:{coords[1]}-{coords[2]}"]
        )
        #print("PATH SUPPLIED:", f"{coords[0]}:{graph_coords[0]}-{graph_coords[1]}:{coords[1]}-{coords[2]}")
    

    end = time()
    print(f"Took approx {end - start:.1f} seconds to extract & sort") # ADD SIZE OF OG & NEW GRAPH 
    print(f"Original graph length: {og_length}\nNew graph length: {new_length}")

    reload_image("tmp.og")

app.mainloop()

os.system("rm tmp.*")