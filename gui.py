from tkinter import * 
from subprocess import * 
from tkinter.filedialog import askopenfilename

#for multiple files import askopenfiles!

window = Tk()
window.geometry('800x400')

#Labels and Grids column Zero 
receptor_label = Label(window, text = "Choose the receptor in pdbqt format")
receptor_label.grid(column=0, row=0, sticky=W)
center_x_label = Label(window, text="Center X")
center_x_label.grid(column=0, row=1, sticky=W)
center_y_label = Label(window, text="Center Y")
center_y_label.grid(column=0, row=2, sticky=W)
center_z_label = Label(window, text="Center Z")
center_z_label.grid(column=0, row=3, sticky=W)
size_x_label = Label(window, text="Size X")
size_x_label.grid(column=0, row=4, sticky=W)
size_y_label = Label(window, text="Size Y")
size_y_label.grid(column=0, row=5, sticky=W)
size_z_label = Label(window, text="Size Z")
size_z_label.grid(column=0, row=6, sticky=W)
ligand_label = Label(window, text = "Choose the ligand in pdbqt format")
ligand_label.grid(column=0, row=7, sticky=W)
exhaustiveness_label = Label(window, text="Exhaustiveness")
exhaustiveness_label.grid(column=0, row=8, sticky=W)
out_label = Label(window, text="Choose a name for the output file. For example: example_out.pdbqt")
out_label.grid(column=0, row=9, sticky=W)

# Column 1
def entry():
    return Entry(window, width=50)

receptor = entry()
receptor.grid(column=1, row=0)
center_x = entry()
center_x.grid(column=1, row=1)
center_y = entry()
center_y.grid(column=1, row=2)
center_z = entry()
center_z.grid(column=1, row=3)
size_x = entry()
size_x.grid(column=1, row=4)
size_y = entry()
size_y.grid(column=1, row=5)
size_z = entry()
size_z.grid(column=1, row=6)
ligand = entry()
ligand.grid(column=1, row=7)
exhaustiveness = entry()
exhaustiveness.grid(column=1, row=8)
out = entry()
out.grid(column=1, row=9)

#Column 3 (buttons)
def browse(txt_box):
    global status
    status = 0
    filename = askopenfilename()
    status = 1
    txt_box.insert(END, filename)
    return [filename, status]


receptor_btn = Button(window, text="Browse", command=lambda: browse(receptor))
receptor_btn.grid(column=2, row=0)
if browse == 1: 
    browse(receptor)

ligand_btn = Button(window, text="Browse", command=lambda: browse(ligand))
ligand_btn.grid(column=2, row=7)
if browse == 1: 
    browse(ligand)



#Write txt file 
def data(): 
    content = [receptor.get(), 
    ligand.get(),
    center_x.get(), 
    center_y.get(),
    center_z.get(), 
    size_x.get(), 
    size_y.get(), 
    size_z.get(),
    exhaustiveness.get(),
    out.get()]
    receptor_out = "receptor = " + str(content[0])
    ligand_out = 'ligand = ' + str(content[1])
    center_x_out = 'center_x = ' + str(content[2])
    center_y_out = 'center_y = ' + str(content[3])
    center_z_out = 'center_z = ' + str(content[4])
    size_x_out = 'size_x = ' + str(content[5])
    size_y_out = 'size_y = ' + str(content[6])
    size_z_out = 'size_z = ' + str(content[7])
    exhaustiveness_out = "exhaustiveness = " + str(content[8])
    out_out = "out = " + str(content[9])

    final =  receptor_out, ligand_out, center_x_out, center_y_out, center_z_out, size_x_out, size_y_out, size_z_out, exhaustiveness_out, out_out

    return "\n".join(str(el) for el in final)

def save_text():
    txt = open("config.txt", 'w')
    
    txt.write(data())

run_btn = Button(window, text="Run", command=save_text)
run_btn.grid(column=2, row=11)


window.mainloop()
