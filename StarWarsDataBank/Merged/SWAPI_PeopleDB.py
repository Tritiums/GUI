# People Databank in Star Wars

### SWAPI & Tkinter Modules

import swapi
import tkinter as tk
import tkinter.font as tkf
from tkinter import ttk
from tkinter import messagebox

### Extract People Data

persons = swapi.get_all('people')

dataset = {}

for person in persons.iter():
    dataset[person.name] =[person.name, person.gender, person.birth_year, person.species, 
                    person.eye_color, person.skin_color, person.hair_color, 
                    person.height, person.mass, person.homeworld, person.starships, person.vehicles, 
                    person.created, person.edited, person.films, 
                    person.get_films, person.get_homeworld, person.get_species, 
                    person.get_starships, person.get_vehicles, person.url]
num = len(dataset)

headers = ['name', 'gender', 'birth_year', 'species', 'eye_color', 'skin_color', 'hair_color', 'height', 'mass', 'homeworld', 
           'starships', 'vehicles', 'created', 'edited', 'films', 
           'get_films', 'get_homeworld', 'get_species', 'get_starships', 'get_vehicles', 'url']
header_widths = [120, 30, 60, 180, 60, 60, 60, 30, 60, 120,
                120, 120, 120, 120, 120, 
                120, 120, 120, 120, 120, 120]

### Helper Functions

def OnDoubleClick(event):
    item = table.selection()[0]
    value = table.item(item, 'values')
    name = value[0]
    
    text_name.delete('1.0', tk.END)
    text_name.insert('1.0', name)
    
    text_gender.delete('1.0', tk.END)
    text_gender.insert('1.0', dataset[name][1])
    
    text_birth_year.delete('1.0', tk.END)
    text_birth_year.insert('1.0', dataset[name][2])
    
    text_species.delete('1.0', tk.END)
    text_species.insert('1.0', dataset[name][3])
    
    text_eye_color.delete('1.0', tk.END)
    text_eye_color.insert('1.0', dataset[name][4])
    
    text_skin_color.delete('1.0', tk.END)
    text_skin_color.insert('1.0', dataset[name][5])
    
    text_hair_color.delete('1.0', tk.END)
    text_hair_color.insert('1.0', dataset[name][6])
    
    text_height.delete('1.0', tk.END)
    text_height.insert('1.0', dataset[name][7])
    
    text_mass.delete('1.0', tk.END)
    text_mass.insert('1.0', dataset[name][8])
    
    text_homeworld.delete('1.0', tk.END)
    text_homeworld.insert('1.0', dataset[name][9])
    
    text_starships.delete('1.0', tk.END)
    text_starships.insert('1.0', dataset[name][10])
    
    text_vehicles.delete('1.0', tk.END)
    text_vehicles.insert('1.0', dataset[name][11])
    
    text_created.delete('1.0', tk.END)
    text_created.insert('1.0', dataset[name][12])
    
    text_edited.delete('1.0', tk.END)
    text_edited.insert('1.0', dataset[name][13])
    
    text_films.delete('1.0', tk.END)
    text_films.insert('1.0', dataset[name][14])
    
    text_get_films.delete('1.0', tk.END)
    text_get_films.insert('1.0', dataset[name][15])
    
    text_get_homeworld.delete('1.0', tk.END)
    text_get_homeworld.insert('1.0', dataset[name][16])
    
    text_get_species.delete('1.0', tk.END)
    text_get_species.insert('1.0', dataset[name][17])
    
    text_get_starships.delete('1.0', tk.END)
    text_get_starships.insert('1.0', dataset[name][18])
    
    text_get_vehicles.delete('1.0', tk.END)
    text_get_vehicles.insert('1.0', dataset[name][19])
    
    text_url.delete('1.0', tk.END)
    text_url.insert('1.0', dataset[name][20])
       

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
root.title('Person Databank of Star Wars')

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
text_num.place(x=1100, y=y_origin+i*gain-38)
text_num.delete('1.0', tk.END)
text_num.insert('1.0', str(num))

text_name=tk.Text(root, width=20,height=1, font=('tahoma', 10), wrap='none')
text_name.place(x=30, y=y_origin+i*gain)
label_name=tk.Label(root, text='Name:', font=('tahoma', 10))
label_name.place(x=30,y=y_origin+i*gain-30)

text_gender=tk.Text(root, width=15,height=1, font=('tahoma', 10), wrap='none')
text_gender.place(x=260, y=y_origin+i*gain)
label_gender=tk.Label(root, text='Gender:', font=('tahoma', 10))
label_gender.place(x=260,y=y_origin+i*gain-30)


text_birth_year=tk.Text(root, width=10,height=1, font=('tahoma', 10), wrap='none')
text_birth_year.place(x=460, y=y_origin+i*gain)
label_birth_year=tk.Label(root, text='Birth Year:', font=('tahoma', 10))
label_birth_year.place(x=460,y=y_origin+i*gain-30)

text_species=tk.Text(root, width=10,height=1, font=('tahoma', 10), wrap='none')
text_species.place(x=600, y=y_origin+i*gain)
label_species=tk.Label(root, text='Species:', font=('tahoma', 10))
label_species.place(x=600,y=y_origin+i*gain-30)

text_eye_color=tk.Text(root, width=10,height=1, font=('tahoma', 10), wrap='none')
text_eye_color.place(x=730, y=y_origin+i*gain)
label_eye_color=tk.Label(root, text='eye_color:', font=('tahoma', 10))
label_eye_color.place(x=730,y=y_origin+i*gain-30)

text_skin_color=tk.Text(root, width=10,height=1, font=('tahoma', 10), wrap='none')
text_skin_color.place(x=860, y=y_origin+i*gain)
label_skin_color=tk.Label(root, text='skin_color:', font=('tahoma', 10))
label_skin_color.place(x=860,y=y_origin+i*gain-30)

text_hair_color=tk.Text(root, width=10,height=1, font=('tahoma', 10), wrap='none')
text_hair_color.place(x=990, y=y_origin+i*gain)
label_hair_color=tk.Label(root, text='hair_color:', font=('tahoma', 10))
label_hair_color.place(x=990,y=y_origin+i*gain-30)

y_origin = 565

text_height=tk.Text(root, width=10,height=1, font=('tahoma', 10), wrap='none')
text_height.place(x=30, y=y_origin+i*gain)
label_height=tk.Label(root, text='height:', font=('tahoma', 10))
label_height.place(x=30,y=y_origin+i*gain-30)

text_mass=tk.Text(root, width=10,height=1, font=('tahoma', 10), wrap='none')
text_mass.place(x=160, y=y_origin+i*gain)
label_mass=tk.Label(root, text='mass:', font=('tahoma', 10))
label_mass.place(x=160,y=y_origin+i*gain-30)

text_homeworld=tk.Text(root, width=20,height=1, font=('tahoma', 10), wrap='none')
text_homeworld.place(x=280, y=y_origin+i*gain)
label_homeworld=tk.Label(root, text='homeworld:', font=('tahoma', 10))
label_homeworld.place(x=280,y=y_origin+i*gain-30)


text_starships=tk.Text(root, width=33,height=1, font=('tahoma', 10), wrap='none')
text_starships.place(x=500, y=y_origin+i*gain)
label_starships=tk.Label(root, text='starships:', font=('tahoma', 10))
label_starships.place(x=500,y=y_origin+i*gain-30)

text_vehicles=tk.Text(root, width=33,height=1, font=('tahoma', 10), wrap='none')
text_vehicles.place(x=830, y=y_origin+i*gain)
label_vehicles=tk.Label(root, text='vehicles:', font=('tahoma', 10))
label_vehicles.place(x=830,y=y_origin+i*gain-30)

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

text_get_films=tk.Text(root, width=20,height=1, font=('tahoma', 10), wrap='none')
text_get_films.place(x=30, y=y_origin+i*gain)
label_get_films=tk.Label(root, text='get_films:', font=('tahoma', 10))
label_get_films.place(x=30,y=y_origin+i*gain-30)

text_get_homeworld=tk.Text(root, width=20,height=1, font=('tahoma', 10), wrap='none')
text_get_homeworld.place(x=330, y=y_origin+i*gain)
label_get_homeworld=tk.Label(root, text='get_homeworld:', font=('tahoma', 10))
label_get_homeworld.place(x=330,y=y_origin+i*gain-30)

text_get_species=tk.Text(root, width=20,height=1, font=('tahoma', 10), wrap='none')
text_get_species.place(x=630, y=y_origin+i*gain)
label_get_species=tk.Label(root, text='get_species:', font=('tahoma', 10))
label_get_species.place(x=630,y=y_origin+i*gain-30)

y_origin = 760

text_get_starships=tk.Text(root, width=20,height=1, font=('tahoma', 10), wrap='none')
text_get_starships.place(x=30, y=y_origin+i*gain)
label_get_starships=tk.Label(root, text='get_starships:', font=('tahoma', 10))
label_get_starships.place(x=30,y=y_origin+i*gain-30)

text_get_vehicles=tk.Text(root, width=20,height=1, font=('tahoma', 10), wrap='none')
text_get_vehicles.place(x=230, y=y_origin+i*gain)
label_get_vehicles=tk.Label(root, text='get_vehicles:', font=('tahoma', 10))
label_get_vehicles.place(x=230,y=y_origin+i*gain-30)

y_origin = 825

text_url=tk.Text(root, width=80,height=1, font=('tahoma', 10), wrap='none')
text_url.place(x=30, y=y_origin+i*gain)
label_url=tk.Label(root, text='url:', font=('tahoma', 10))
label_url.place(x=30,y=y_origin+i*gain-30)

button_about=ttk.Button(root, text='About...', width=20, command=about)
button_about.place(x=1000, y=630)

root.mainloop()