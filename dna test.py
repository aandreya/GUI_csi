from Tkinter import *
import Tkinter
import os

characteristics = {
    'hair_color': {
        'black': 'CCAGCAATCGC',
        'brown': 'GCCAGTGCCG',
        'blonde': 'TTAGCTATCGC'
    },
    'face_shape': {
        'square': 'GCCACGG',
        'round': 'ACCACAA',
        'oval': 'AGGCCTCA'
    },
    'eye_color': {
        'blue': 'TTGTGGTGGC',
        'green': 'GGGAGGTGGC',
        'brown': 'AAGTAGTGAC'
    },
    'gender': {
        'female': 'TGAAGGACCTTC',
        'male': 'TGCAGGAACTTC'
    },
    'race': {
        'white': 'AAAACCTCA',
        'black': 'CGACTACAG',
        'asian': 'CGCGGGCCG'
    }
}
suspects = {
    'Eva': {
        'gender': 'female',
        'race': 'white',
        'hair_color': 'blonde',
        'eye_color': 'blue',
        'face_shape': 'oval'
    },
    'Larisa': {
        'gender': 'female',
        'race': 'white',
        'hair_color': 'brown',
        'eye_color': 'brown',
        'face_shape': 'oval'
    },
    'Matej': {
        'gender': 'male',
        'race': 'white',
        'hair_color': 'black',
        'eye_color': 'blue',
        'face_shape': 'oval'
    },
    'Miha': {
        'gender': 'male',
        'race': 'white',
        'hair_color': 'brown',
        'eye_color': 'green',
        'face_shape': 'square'
    }
}
dna=""

def upload():
    from tkFileDialog import askopenfilename
    frame.filename = askopenfilename(filetypes =(("notepad files", ".txt"), ("csv files", ".csv"), ("All Files", "*.*")))
    dna_filename = os.path.basename(frame.filename)
    file_name.config(text=dna_filename)
    dna_file = open(dna_filename, 'r')
    global dna
    dna = dna_file.read()
    dna_file.close()

def dna_test():
    guilty_party_attributes = {}
    is_suspect_found = False

    for (attribute_name, types) in characteristics.items():
        for (type_name, type_value) in types.items():
            if type_value in dna:
                guilty_party_attributes[attribute_name] = type_name
                break
    for (suspect_name, suspect_attributes) in suspects.items():
        if suspect_attributes == guilty_party_attributes:
            dna_test_result.config(text=suspect_name)
            is_suspect_found = True
    if not is_suspect_found:
        dna_test_result.config(text="Suspect not found")

frame = Tkinter.Tk()
frame.geometry("300x300")
frame.title("CSI")
greeting = Tkinter.Label(frame, text="Who ate the icecream?\n\n++++\n\n")
greeting.pack()

open_file_label = Tkinter.Label(frame, text = "Upload the DNA file:")
open_file_label.pack()
open_file_button = Tkinter.Button(frame, text="Browse", command=upload)
open_file_button.pack()
file_name = Tkinter.Label(frame, text = "")
file_name.pack()
placeholder_label = Tkinter.Label(frame, text = "")
placeholder_label.pack()

csi_button = Tkinter.Button(frame, text="DNA roll", command=dna_test)
csi_button.pack()

result_label = Tkinter.Label(frame, text = "Icecream was eaten by:")
result_label.pack()
dna_test_result = Tkinter.Label(frame, text="")
dna_test_result.pack()


frame.mainloop()