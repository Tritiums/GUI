# Planet Databank of Star Wars

### SWAPI & Tkinter Modules

import swapi
import tkinter as tk
import tkinter.font as tkf
from tkinter import ttk
from tkinter import messagebox

### Extract Planet Data

planets = swapi.get_all('planets')

dataset = {}

for planet in planets.iter():
    dataset[planet.name] =[planet.name, planet.diameter, planet.gravity, planet.climate, 
                           planet.rotation_period, planet.orbital_period, 
                           planet.terrain, planet.surface_water, planet.population, 
                           planet.residents, planet.films, planet.created, planet.edited, 
                           planet.get_films, planet.get_residents, planet.url]
num = len(dataset)

headers = ['name', 'diameter', 'gravity', 'climate', 'rotation_period', 'orbital_period', 
           'terrain', 'surface_water', 'population', 'residents',  'films', 
           'created', 'edited', 'get_films', 'get_residents', 'url']
header_widths = [80, 30, 90, 140, 30, 30,
               240, 60, 50, 120, 120,
               100, 100, 100, 100, 100]

### Helper Functions

def OnDoubleClick(event):
    item = table.selection()[0]
    value = table.item(item, 'values')
    name = value[0]
    
    text_name.delete('1.0', tk.END)
    text_name.insert('1.0', name)
    
    text_diameter.delete('1.0', tk.END)
    text_diameter.insert('1.0', dataset[name][1])
    
    text_gravity.delete('1.0', tk.END)
    text_gravity.insert('1.0', dataset[name][2])
    
    text_climate.delete('1.0', tk.END)
    text_climate.insert('1.0', dataset[name][3])
    
    text_rotation_period.delete('1.0', tk.END)
    text_rotation_period.insert('1.0', dataset[name][4])
    
    text_orbital_period.delete('1.0', tk.END)
    text_orbital_period.insert('1.0', dataset[name][5])
    
    text_terrain.delete('1.0', tk.END)
    text_terrain.insert('1.0', dataset[name][6])
    
    text_surface_water.delete('1.0', tk.END)
    text_surface_water.insert('1.0', dataset[name][7])
    
    text_population.delete('1.0', tk.END)
    text_population.insert('1.0', dataset[name][8])
    
    text_residents.delete('1.0', tk.END)
    text_residents.insert('1.0', dataset[name][9])
    
    text_films.delete('1.0', tk.END)
    text_films.insert('1.0', dataset[name][10])
    
    text_created.delete('1.0', tk.END)
    text_created.insert('1.0', dataset[name][11])
    
    text_edited.delete('1.0', tk.END)
    text_edited.insert('1.0', dataset[name][12])
    
    
    text_get_films.delete('1.0', tk.END)
    text_get_films.insert('1.0', dataset[name][13])
    
    text_get_residents.delete('1.0', tk.END)
    text_get_residents.insert('1.0', dataset[name][14])
    
    text_url.delete('1.0', tk.END)
    text_url.insert('1.0', dataset[name][15])       

def sortby(tree, col, descending):
    """sort tree contents when a column header is clicked on"""
    # grab values to sort
    data = [(tree.set(child, col), child) for child in tree.get_children('')]
    # if the data to be sorted is numeric change to float
    #data =  change_numeric(data)
    # now sort the data in place
    data.sort(reverse=descending)
    for ix, item in enumerate(data):
        tree.move(item[1], '', ix)
    # switch the heading so it will sort in the opposite direction
    tree.heading(col, command=lambda col=col: sortby(tree, col, int(not descending)))

def about():
    messagebox.showinfo("About", "Author: Chuan Yang")

### Main Stream

# Main Frame////////////////////////////////////////////////////////////////////////////////////////
root = tk.Tk()
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
#root.attributes('-fullscreen', True)
root.title('Planet Database of Star Wars')

# Multicolumn Listbox/////////////////////////////////////////////////////////////////////////////
table = ttk.Treeview(height="20", columns=headers, selectmode="extended")
table.pack(padx=10, pady=20, ipadx=1200, ipady=190)

i = 1
for header in headers:
    table.heading('#'+str(i), text=header.title(), anchor=tk.W, command=lambda c=header: sortby(table, c, 0))
    table.column('#'+str(i), stretch=tk.NO, minwidth=0, width=tkf.Font().measure(header.title())+header_widths[i-1]) 
    i+=1    
table.column('#0', stretch=tk.NO, minwidth=0, width=0)

for name in list(dataset.keys()):
    table.insert("", "end", "", values=dataset[name])

#table.insert('','end', values='')

table.bind("<Double-1>", OnDoubleClick)
#///////////////////////////////////////////////////////////////////////////////////////////

# Scrollbar////////////////////////////////////////////////////////////////////////////////////////
vsb = ttk.Scrollbar(table, orient="vertical",  command = table.yview)
hsb = ttk.Scrollbar(table, orient="horizontal", command = table.xview)
## Link scrollbars activation to top-level object
table.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
## Link scrollbar also to every columns
map(lambda col: col.configure(yscrollcommand=vsb.set,xscrollcommand=hsb.set), table)
vsb.pack(side = tk.RIGHT, fill = tk.Y)
hsb.pack(side = tk.BOTTOM, fill = tk.X)        

#//////////////////////////////////////////////////////////////////////////////////////////////

y_origin = 500
gain = 47
i = 0

text_num=tk.Text(root, width=5,height=1, font=('tahoma', 10))
text_num.place(x=1160, y=y_origin+i*gain)
text_num.delete('1.0', tk.END)
text_num.insert('1.0', str(num))

text_name=tk.Text(root, width=20,height=1, font=('tahoma', 10), wrap='none')
text_name.place(x=30, y=y_origin+i*gain)
label_name=tk.Label(root, text='Name:', font=('tahoma', 10))
label_name.place(x=30,y=y_origin+i*gain-30)

text_diameter=tk.Text(root, width=15,height=1, font=('tahoma', 10), wrap='none')
text_diameter.place(x=260, y=y_origin+i*gain)
label_diameter=tk.Label(root, text='diameter:', font=('tahoma', 10))
label_diameter.place(x=260,y=y_origin+i*gain-30)


text_gravity=tk.Text(root, width=10,height=1, font=('tahoma', 10), wrap='none')
text_gravity.place(x=440, y=y_origin+i*gain)
label_gravity=tk.Label(root, text='gravity:', font=('tahoma', 10))
label_gravity.place(x=440,y=y_origin+i*gain-30)

text_climate=tk.Text(root, width=20,height=1, font=('tahoma', 10), wrap='none')
text_climate.place(x=600, y=y_origin+i*gain)
label_climate=tk.Label(root, text='climate:', font=('tahoma', 10))
label_climate.place(x=600,y=y_origin+i*gain-30)

text_rotation_period=tk.Text(root, width=10,height=1, font=('tahoma', 10), wrap='none')
text_rotation_period.place(x=830, y=y_origin+i*gain)
label_rotation_period=tk.Label(root, text='rotation_period:', font=('tahoma', 10))
label_rotation_period.place(x=830,y=y_origin+i*gain-30)

text_orbital_period=tk.Text(root, width=10,height=1, font=('tahoma', 10), wrap='none')
text_orbital_period.place(x=1000, y=y_origin+i*gain)
label_orbital_period=tk.Label(root, text='orbital_period:', font=('tahoma', 10))
label_orbital_period.place(x=1000,y=y_origin+i*gain-30)

y_origin = 565

text_terrain=tk.Text(root, width=40,height=1, font=('tahoma', 10), wrap='none')
text_terrain.place(x=30, y=y_origin+i*gain)
label_terrain=tk.Label(root, text='terrain:', font=('tahoma', 10))
label_terrain.place(x=30,y=y_origin+i*gain-30)

text_surface_water=tk.Text(root, width=20,height=1, font=('tahoma', 10), wrap='none')
text_surface_water.place(x=450, y=y_origin+i*gain)
label_surface_water=tk.Label(root, text='surface_water:', font=('tahoma', 10))
label_surface_water.place(x=450,y=y_origin+i*gain-30)

text_population=tk.Text(root, width=20,height=1, font=('tahoma', 10), wrap='none')
text_population.place(x=660, y=y_origin+i*gain)
label_population=tk.Label(root, text='population:', font=('tahoma', 10))
label_population.place(x=660,y=y_origin+i*gain-30)

text_residents=tk.Text(root, width=30,height=1, font=('tahoma', 10), wrap='none')
text_residents.place(x=880, y=y_origin+i*gain)
label_residents=tk.Label(root, text='residents:', font=('tahoma', 10))
label_residents.place(x=880,y=y_origin+i*gain-30)

y_origin = 630

text_created=tk.Text(root, width=30,height=1, font=('tahoma', 10), wrap='none')
text_created.place(x=30, y=y_origin+i*gain)
label_created=tk.Label(root, text='created:', font=('tahoma', 10))
label_created.place(x=30,y=y_origin+i*gain-30)

text_edited=tk.Text(root, width=30,height=1, font=('tahoma', 10), wrap='none')
text_edited.place(x=330, y=y_origin+i*gain)
label_edited=tk.Label(root, text='edited:', font=('tahoma', 10))
label_edited.place(x=330,y=y_origin+i*gain-30)

text_films=tk.Text(root, width=40,height=1, font=('tahoma', 10), wrap='none')
text_films.place(x=650, y=y_origin+i*gain)
label_films=tk.Label(root, text='films:', font=('tahoma', 10))
label_films.place(x=650,y=y_origin+i*gain-30)

y_origin = 695

text_get_films=tk.Text(root, width=50,height=1, font=('tahoma', 10), wrap='none')
text_get_films.place(x=30, y=y_origin+i*gain)
label_get_films=tk.Label(root, text='get_films:', font=('tahoma', 10))
label_get_films.place(x=30,y=y_origin+i*gain-30)

text_get_residents=tk.Text(root, width=60,height=1, font=('tahoma', 10), wrap='none')
text_get_residents.place(x=600, y=y_origin+i*gain)
label_get_residents=tk.Label(root, text='get_residents:', font=('tahoma', 10))
label_get_residents.place(x=600,y=y_origin+i*gain-30)

y_origin = 760

text_url=tk.Text(root, width=80,height=1, font=('tahoma', 10), wrap='none')
text_url.place(x=30, y=y_origin+i*gain)
label_url=tk.Label(root, text='url:', font=('tahoma', 10))
label_url.place(x=30,y=y_origin+i*gain-30)

button_about=ttk.Button(root, text='About...', width=20, command=about)
button_about.place(x=1060, y=630)

root.mainloop()