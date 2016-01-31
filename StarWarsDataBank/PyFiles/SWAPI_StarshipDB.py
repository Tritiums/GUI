# Starship Databank in Star Wars

### SWAPI & Tkinter Modules

import swapi
import tkinter as tk
import tkinter.font as tkf
from tkinter import ttk
from tkinter import messagebox

### Extract People Data

ships = swapi.get_all('starships')

dataset = {}

for ship in ships.iter():
    dataset[ship.name] =[ship.name, ship.model, ship.length, ship.cargo_capacity, ship.starship_class, ship.manufacturer, 
                         ship.max_atmosphering_speed, ship.hyperdrive_rating, ship.consumables, ship.cost_in_credits, 
                         ship.pilots, ship.crew, ship.passengers, 
                         ship.created, ship.edited, ship.films, ship.get_films, ship.get_pilots, ship.url]
num = len(dataset)

headers = ['name', 'model', 'length', 'cargo_capacity', 'starship_class', 'manufacturer',
           'max_atmosphering_speed', 'hyperdrive_rating', 'consumables', 'cost_in_credits',
           'pilots', 'crew', 'passengers', 
           'created', 'edited', 'films', 'get_films', 'get_pilots', 'url']
header_widths = [180, 250, 40, 40, 120, 160, 
                 30, 30, 30, 30,
                120, 30, 30,
                120, 120, 120, 120, 120, 120]

### Helper Functions

def OnDoubleClick(event):
    item = table.selection()[0]
    value = table.item(item, 'values')
    name = value[0]
    
    text_name.delete('1.0', tk.END)
    text_name.insert('1.0', name)
    
    text_model.delete('1.0', tk.END)
    text_model.insert('1.0', dataset[name][1])
    
    text_length.delete('1.0', tk.END)
    text_length.insert('1.0', dataset[name][2])
    
    text_cargo_capacity.delete('1.0', tk.END)
    text_cargo_capacity.insert('1.0', dataset[name][3])
    
    text_starship_class.delete('1.0', tk.END)
    text_starship_class.insert('1.0', dataset[name][4])
    
    text_manufacturer.delete('1.0', tk.END)
    text_manufacturer.insert('1.0', dataset[name][5])
    
    text_max_atmosphering_speed.delete('1.0', tk.END)
    text_max_atmosphering_speed.insert('1.0', dataset[name][6])
    
    text_hyperdrive_rating.delete('1.0', tk.END)
    text_hyperdrive_rating.insert('1.0', dataset[name][7])
    
    text_consumables.delete('1.0', tk.END)
    text_consumables.insert('1.0', dataset[name][8])
    
    text_cost_in_credits.delete('1.0', tk.END)
    text_cost_in_credits.insert('1.0', dataset[name][9])
    
    text_pilots.delete('1.0', tk.END)
    text_pilots.insert('1.0', dataset[name][10])
    
    text_crew.delete('1.0', tk.END)
    text_crew.insert('1.0', dataset[name][11])
    
    text_passengers.delete('1.0', tk.END)
    text_passengers.insert('1.0', dataset[name][12])
    
    text_created.delete('1.0', tk.END)
    text_created.insert('1.0', dataset[name][13])
    
    text_edited.delete('1.0', tk.END)
    text_edited.insert('1.0', dataset[name][14])
    
    text_films.delete('1.0', tk.END)
    text_films.insert('1.0', dataset[name][15])
    
    text_get_films.delete('1.0', tk.END)
    text_get_films.insert('1.0', dataset[name][16])
    
    text_get_pilots.delete('1.0', tk.END)
    text_get_pilots.insert('1.0', dataset[name][17])
    
    text_url.delete('1.0', tk.END)
    text_url.insert('1.0', dataset[name][18])
       

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
root.title('Starship Databank of Star Wars')

# Multicolumn Listbox/////////////////////////////////////////////////////////////////////////////
table = ttk.Treeview(height="20", columns=headers, selectmode="extended")
table.pack(padx=10, pady=20, ipadx=1200, ipady=180)

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
text_num.place(x=1150, y=y_origin+i*gain-43)
text_num.delete('1.0', tk.END)
text_num.insert('1.0', str(num))

#//////////////////////////////////////////////////////////////////////////////////
text_name=tk.Text(root, width=27,height=1, font=('tahoma', 10), wrap='none')
text_name.place(x=30, y=y_origin+i*gain)
label_name=tk.Label(root, text='Name:', font=('tahoma', 10))
label_name.place(x=30,y=y_origin+i*gain-30)

text_model=tk.Text(root, width=38,height=1, font=('tahoma', 10), wrap='none')
text_model.place(x=300, y=y_origin+i*gain)
label_model=tk.Label(root, text='model:', font=('tahoma', 10))
label_model.place(x=300,y=y_origin+i*gain-30)


text_length=tk.Text(root, width=10,height=1, font=('tahoma', 10), wrap='none')
text_length.place(x=680, y=y_origin+i*gain)
label_length=tk.Label(root, text='length:', font=('tahoma', 10))
label_length.place(x=680,y=y_origin+i*gain-30)

text_cargo_capacity=tk.Text(root, width=15,height=1, font=('tahoma', 10), wrap='none')
text_cargo_capacity.place(x=800, y=y_origin+i*gain)
label_cargo_capacity=tk.Label(root, text='cargo_capacity:', font=('tahoma', 10))
label_cargo_capacity.place(x=800,y=y_origin+i*gain-30)

text_manufacturer=tk.Text(root, width=30,height=1, font=('tahoma', 10), wrap='none')
text_manufacturer.place(x=980, y=y_origin+i*gain)
label_manufacturer=tk.Label(root, text='manufacturer:', font=('tahoma', 10))
label_manufacturer.place(x=980,y=y_origin+i*gain-30)

y_origin = 565

text_starship_class=tk.Text(root, width=30,height=1, font=('tahoma', 10), wrap='none')
text_starship_class.place(x=30, y=y_origin+i*gain)
label_starship_class=tk.Label(root, text='starship_class:', font=('tahoma', 10))
label_starship_class.place(x=30,y=y_origin+i*gain-30)

text_max_atmosphering_speed=tk.Text(root, width=15,height=1, font=('tahoma', 10), wrap='none')
text_max_atmosphering_speed.place(x=350, y=y_origin+i*gain)
label_max_atmosphering_speed=tk.Label(root, text='max_atmosphering_speed:', font=('tahoma', 10))
label_max_atmosphering_speed.place(x=350,y=y_origin+i*gain-30)


text_hyperdrive_rating=tk.Text(root, width=10,height=1, font=('tahoma', 10), wrap='none')
text_hyperdrive_rating.place(x=580, y=y_origin+i*gain)
label_hyperdrive_rating=tk.Label(root, text='hyperdrive_rating:', font=('tahoma', 10))
label_hyperdrive_rating.place(x=580,y=y_origin+i*gain-30)

text_consumables=tk.Text(root, width=15,height=1, font=('tahoma', 10), wrap='none')
text_consumables.place(x=750, y=y_origin+i*gain)
label_consumables=tk.Label(root, text='consumables:', font=('tahoma', 10))
label_consumables.place(x=750,y=y_origin+i*gain-30)

text_cost_in_credits=tk.Text(root, width=20,height=1, font=('tahoma', 10), wrap='none')
text_cost_in_credits.place(x=920, y=y_origin+i*gain)
label_cost_in_credits=tk.Label(root, text='cost_in_credits:', font=('tahoma', 10))
label_cost_in_credits.place(x=920,y=y_origin+i*gain-30)

y_origin = 630

text_pilots=tk.Text(root, width=33,height=1, font=('tahoma', 10), wrap='none')
text_pilots.place(x=30, y=y_origin+i*gain)
label_pilots=tk.Label(root, text='pilots:', font=('tahoma', 10))
label_pilots.place(x=30,y=y_origin+i*gain-30)

text_crew=tk.Text(root, width=20,height=1, font=('tahoma', 10), wrap='none')
text_crew.place(x=430, y=y_origin+i*gain)
label_crew=tk.Label(root, text='crew:', font=('tahoma', 10))
label_crew.place(x=430,y=y_origin+i*gain-30)

text_passengers=tk.Text(root, width=30,height=1, font=('tahoma', 10), wrap='none')
text_passengers.place(x=660, y=y_origin+i*gain)
label_passengers=tk.Label(root, text='passengers:', font=('tahoma', 10))
label_passengers.place(x=660,y=y_origin+i*gain-30)


y_origin = 695

text_created=tk.Text(root, width=40,height=1, font=('tahoma', 10), wrap='none')
text_created.place(x=30, y=y_origin+i*gain)
label_created=tk.Label(root, text='created:', font=('tahoma', 10))
label_created.place(x=30,y=y_origin+i*gain-30)

text_edited=tk.Text(root, width=40,height=1, font=('tahoma', 10), wrap='none')
text_edited.place(x=450, y=y_origin+i*gain)
label_edited=tk.Label(root, text='edited:', font=('tahoma', 10))
label_edited.place(x=450,y=y_origin+i*gain-30)

text_films=tk.Text(root, width=30,height=1, font=('tahoma', 10), wrap='none')
text_films.place(x=850, y=y_origin+i*gain)
label_films=tk.Label(root, text='films:', font=('tahoma', 10))
label_films.place(x=850,y=y_origin+i*gain-30)

y_origin = 760

text_get_films=tk.Text(root, width=60,height=1, font=('tahoma', 10), wrap='none')
text_get_films.place(x=30, y=y_origin+i*gain)
label_get_films=tk.Label(root, text='get_films:', font=('tahoma', 10))
label_get_films.place(x=30,y=y_origin+i*gain-30)

text_get_pilots=tk.Text(root, width=60,height=1, font=('tahoma', 10), wrap='none')
text_get_pilots.place(x=630, y=y_origin+i*gain)
label_get_pilots=tk.Label(root, text='get_pilots:', font=('tahoma', 10))
label_get_pilots.place(x=630,y=y_origin+i*gain-30)

y_origin = 825

text_url=tk.Text(root, width=80,height=1, font=('tahoma', 10), wrap='none')
text_url.place(x=30, y=y_origin+i*gain)
label_url=tk.Label(root, text='url:', font=('tahoma', 10))
label_url.place(x=30,y=y_origin+i*gain-30)

button_about=ttk.Button(root, text='About...', width=20, command=about)
button_about.place(x=1000, y=630)

root.mainloop()