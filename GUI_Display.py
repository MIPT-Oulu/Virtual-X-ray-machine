import tkinter.font
from tkinter import *
from PIL import Image, ImageTk
import cv2 as cv
import math
import x_ray


# This script is created by Jones Jernfors
# Copyright (c) 2022, Jones Jernfors (jones.jernfors@outlook.com)
# All rights reserved.

# This script is the main window with all the button and image functions
# This script needs x_ray.py and Spectrum.py in order to work

def image_switcharoo(image1, width, height):  # Function for changing an image for tkinter and its size

    image1 = Image.fromarray(image1)  # read in image from array with Tkinter
    image1 = image1.resize((width, height))
    image1 = ImageTk.PhotoImage(image1)  # create the photo image for display
    return image1


def display(root):  # Main window

    # Create Canvas for the x ray image and loading initial image (no image)
    global no_image
    no_image = PhotoImage(file='Arrows/no_image.png')
    x_ray_canvas = Canvas(root, bg="grey", height=1000, width=900)
    image = x_ray_canvas.create_image(450, 500, image=no_image)
    x_ray_canvas.place(x=50, y=0)

    # kvp , mas , filter frames
    kvp_frame = LabelFrame(root, text="kVp", padx=4, pady=10)
    mas_frame = LabelFrame(root, text="mAs", padx=4, pady=10)
    filter_frame = LabelFrame(root, text="Additional Filter", padx=4, pady=10)

    # kvp , mas , filter frame positioning
    kvp_frame.place(x=980, y=20)
    mas_frame.place(x=1100, y=20)
    filter_frame.place(x=1150, y=100)

    # kvp , mas, filter thickness entries
    kvp_entry = Entry(kvp_frame, width=10)
    mas_entry = Entry(mas_frame, width=10)
    kvp_entry.insert(END, 70)
    mas_entry.insert(END, 2)

    # kvp , mas entry positioning
    kvp_entry.pack()
    mas_entry.pack()

    # filter dropdown menu
    clicked = StringVar()
    clicked.set("None")
    filter_drop = OptionMenu(filter_frame, clicked, "None", "1 mmAl", "2 mmAl", "0.1 mmCu", "0.2 mmCu", "0.3 mmCu",
                             "1 mmAl + 0.1 mmCu", "1 mmAl + 0.2 mmCu")
    filter_drop.pack()

    # Create minimap images
    global minimap_image_ap
    global minimap_image_pa
    global minimap_image_lat_left
    minimap_image_ap = cv.imread("Images/minimap_AP_edit.png")
    minimap_image_ap = image_switcharoo(minimap_image_ap, 300, 500)

    minimap_image_pa = cv.imread("Images/minimap_PA_edit.png")
    minimap_image_pa = image_switcharoo(minimap_image_pa, 300, 500)

    minimap_image_lat_left = cv.imread("Images/minimap_LAT_VAS_edit.png")
    minimap_image_lat_left = image_switcharoo(minimap_image_lat_left, 300, 500)

    # Canvas and image for the minimap of the patient
    mini_canvas = Canvas(root, bg="grey", height=500, width=300)
    mini_canvas.create_image(150, 250, image=minimap_image_ap)
    mini_canvas.place(x=980, y=200)

    # Projection box and x ray tube height for the patient minimap canvas
    global minimap_box
    minimap_box = mini_canvas.create_rectangle(77, 75, 227, 225, outline="white", width=2)

    # Declaring the moving speed variable, setting initial value as 5
    global spd_var
    spd_var = 5

    # Functions for moving speed
    def spd_button2():
        global spd_var
        global spd_button5
        global spd_button10
        spd_var = 2
        button_spd2.config(relief=SUNKEN)
        button_spd5.config(relief=RAISED)
        button_spd10.config(relief=RAISED)

    def spd_button5():
        global spd_var
        global spd_button10
        global spd_button2
        spd_var = 5
        button_spd2.config(relief=RAISED)
        button_spd5.config(relief=SUNKEN)
        button_spd10.config(relief=RAISED)

    def spd_button10():
        global spd_var
        global spd_button2
        global spd_button5
        spd_var = 10
        button_spd2.config(relief=RAISED)
        button_spd5.config(relief=RAISED)
        button_spd10.config(relief=SUNKEN)

    # Functions for moving the projection box
    def move_up():
        x = 0
        y = -spd_var
        mini_canvas.move(minimap_box, x, y)

    def move_down():
        x = 0
        y = spd_var
        mini_canvas.move(minimap_box, x, y)

    def move_left():
        x = -spd_var
        y = 0
        mini_canvas.move(minimap_box, x, y)

    def move_right():
        x = spd_var
        y = 0
        mini_canvas.move(minimap_box, x, y)

    def move_NE():
        x = spd_var
        y = -spd_var
        mini_canvas.move(minimap_box, x, y)

    def move_NW():
        x = -spd_var
        y = -spd_var
        mini_canvas.move(minimap_box, x, y)

    def move_SE():
        x = spd_var
        y = spd_var
        mini_canvas.move(minimap_box, x, y)

    def move_SW():
        x = -spd_var
        y = spd_var
        mini_canvas.move(minimap_box, x, y)

    # Functions for increasing and decreasing the projection box size
    def size_small_y():
        x = 0
        y = spd_var
        x0, y0, x1, y1 = mini_canvas.coords(minimap_box)
        mini_canvas.coords(minimap_box, x0 + x, y0 + y, x1, y1)

    def size_big_y():
        x = 0
        y = -spd_var
        x0, y0, x1, y1 = mini_canvas.coords(minimap_box)
        mini_canvas.coords(minimap_box, x0 + x, y0 + y, x1, y1)

    def size_small_x():
        x = -spd_var
        y = 0
        x0, y0, x1, y1 = mini_canvas.coords(minimap_box)
        mini_canvas.coords(minimap_box, x0, y0, x1 + x, y1 + y)

    def size_big_x():
        x = spd_var
        y = 0
        x0, y0, x1, y1 = mini_canvas.coords(minimap_box)
        mini_canvas.coords(minimap_box, x0, y0, x1 + x, y1 + y)

    # Functions for moving the x ray tube length up and down
    global tube_distance
    tube_distance = 138
    def tube_forward():
        global tube_distance
        tube_distance = tube_distance + spd_var
        tube_label.config(text="X-ray tube \n distance\n" + str(tube_distance) + " cm")

    def tube_backward():
        global tube_distance
        tube_distance = tube_distance - spd_var
        tube_label.config(text="X-ray tube \n distance\n" + str(tube_distance) + " cm")

    # Load the images for the arrow buttons
    global arrow_up
    global arrow_down
    global arrow_left
    global arrow_right
    global arrow_NE
    global arrow_NW
    global arrow_SE
    global arrow_SW
    global arrow_down_tube
    global arrow_up_tube
    arrow_up = PhotoImage(file='Arrows/Arrow_up_w.png')
    arrow_down = PhotoImage(file='Arrows/Arrow_down_w.png')
    arrow_left = PhotoImage(file='Arrows/Arrow_left_w.png')
    arrow_right = PhotoImage(file='Arrows/Arrow_right_w.png')
    arrow_NE = PhotoImage(file='Arrows/Arrow_NE_w.png')
    arrow_NW = PhotoImage(file='Arrows/Arrow_NW_w.png')
    arrow_SE = PhotoImage(file='Arrows/Arrow_SE_w.png')
    arrow_SW = PhotoImage(file='Arrows/Arrow_SW_w.png')

    # Load the x ray tube arrows (blue)
    arrow_down_tube = PhotoImage(file='Arrows/Arrow_down_tube.png')
    arrow_up_tube = PhotoImage(file='Arrows/Arrow_up_tube.png')

    # box mover canvas
    box_canvas = Canvas(root, bg="grey", height=105, width=105)
    box_canvas.place(x=1285, y=300)

    # Moving speed
    speed_label = Label(root, text="Moving speed")
    speed_label.place(x=1285, y=220)
    buttonfont = tkinter.font.Font(size=10)

    # 2x speed button
    button_spd2 = Button(root, text="2X", width=2, height=1, font=buttonfont, command=spd_button2)
    button_spd2.place(x=1289, y=250)

    # 5x speed button
    button_spd5 = Button(root, text="5X", width=2, height=1, font=buttonfont, command=spd_button5)
    button_spd5.place(x=1320, y=250)
    button_spd5.config(relief=SUNKEN)

    # 10x speed button
    button_spd10 = Button(root, text="10X", width=3, height=1, font=buttonfont, command=spd_button10)
    button_spd10.place(x=1351, y=250)

    # Making the projection box movement buttons
    button_up = Button(root, image=arrow_up, command=move_up)
    button_up.place(x=1324, y=302)

    button_down = Button(root, image=arrow_down, command=move_down)
    button_down.place(x=1324, y=372)

    button_left = Button(root, image=arrow_left, command=move_left)
    button_left.place(x=1288, y=337)

    button_right = Button(root, image=arrow_right, command=move_right)
    button_right.place(x=1360, y=337)

    button_NW = Button(root, image=arrow_NW, command=move_NW)
    button_NW.place(x=1288, y=302)

    button_NE = Button(root, image=arrow_NE, command=move_NE)
    button_NE.place(x=1360, y=302)

    button_SW = Button(root, image=arrow_SW, command=move_SW)
    button_SW.place(x=1288, y=372)

    button_SE = Button(root, image=arrow_SE, command=move_SE)
    button_SE.place(x=1360, y=372)

    # Making the projection box size buttons
    button_size_big_y = Button(root, image=arrow_up, command=size_big_y)
    button_size_big_y.place(x=1324, y=432)

    button_size_small_y = Button(root, image=arrow_down, command=size_small_y)
    button_size_small_y.place(x=1324, y=502)

    button_size_small_x = Button(root, image=arrow_left, command=size_small_x)
    button_size_small_x.place(x=1288, y=467)

    button_size_big_x = Button(root, image=arrow_right, command=size_big_x)
    button_size_big_x.place(x=1360, y=467)

    # Making the x ray tube length buttons
    button_tube_up = Button(root, image=arrow_up_tube, command=tube_forward)
    button_tube_up.place(x=1324, y=560)
    button_tube_down = Button(root, image=arrow_down_tube, command=tube_backward)
    button_tube_down.place(x=1324, y=600)

    # Projection box labels
    projection_height = Label(root, text="Projection \n size")
    projection_height.place(x=1405, y=457)

    # x ray tube label
    tube_label = Label(root, text="X-ray tube \n distance" + "\n138 cm")
    tube_label.place(x=1365, y=555)

    # Making the error window for too small/high kvp value
    def popkvp_window():
        global popkvp
        root_x = root.winfo_rootx()
        root_y = root.winfo_rooty()
        winx = root_x + 800
        winy = root_y + 400
        popkvp = Toplevel(root)
        popkvp.title("Error")
        popkvp.geometry(f'+{winx}+{winy}')
        popkvp_label = Label(popkvp, text="kVp value must be between 70 and 125")
        popkvp_label.pack()
        pop_button = Button(popkvp, text="OK", command=lambda: popkvp.destroy())
        pop_button.pack()

    # Making the error window for too small/high mas value
    def popmas_window():
        global popmas
        root_x = root.winfo_rootx()
        root_y = root.winfo_rooty()
        winx = root_x + 800
        winy = root_y + 400
        popmas = Toplevel(root)
        popmas.title("Error")
        popmas.geometry(f'+{winx}+{winy}')
        popmas_label = Label(popmas, text="mAs value must be between 0.3 and 100")
        popmas_label.pack()
        pop_button = Button(popmas, text="OK", command=lambda: popmas.destroy())
        pop_button.pack()

    # Function for taking the values for calculating the x ray projection and dose, changing the x ray image,
    # and changing the spectrum image
    def produce_xray():
        global new_img
        global popkvp
        global popmas
        global dap
        contains_comma()
        x0, y0, x1, y1 = mini_canvas.coords(minimap_box)
        if clicked.get() == "1 mmAl":
            filter_z = 13
            filter_rho = 2.7
            filter_thickness = 1
            filter_z2 = -1
            filter_rho2 = -1
            filter_thickness2 = -1
        elif clicked.get() == "2 mmAl":
            filter_z = 13
            filter_rho = 2.7
            filter_thickness = 2
            filter_z2 = -1
            filter_rho2 = -1
            filter_thickness2 = -1
        elif clicked.get() == "0.1 mmCu":
            filter_z = 29
            filter_rho = 8.96
            filter_thickness = 0.1
            filter_z2 = -1
            filter_rho2 = -1
            filter_thickness2 = -1
        elif clicked.get() == "0.2 mmCu":
            filter_z = 29
            filter_rho = 8.96
            filter_thickness = 0.2
            filter_z2 = -1
            filter_rho2 = -1
            filter_thickness2 = -1
        elif clicked.get() == "0.3 mmCu":
            filter_z = 29
            filter_rho = 8.96
            filter_thickness = 0.3
            filter_z2 = -1
            filter_rho2 = -1
            filter_thickness2 = -1
        elif clicked.get() == "1 mmAl + 0.1 mmCu":
            filter_z = 13
            filter_rho = 2.7
            filter_thickness = 1
            filter_z2 = 29
            filter_rho2 = 8.96
            filter_thickness2 = 0.1
        elif clicked.get() == "1 mmAl + 0.2 mmCu":
            filter_z = 13
            filter_rho = 2.7
            filter_thickness = 1
            filter_z2 = 29
            filter_rho2 = 8.96
            filter_thickness2 = 0.2
        else:
            filter_z = 0
            filter_rho = 0
            filter_thickness = 0
            filter_z2 = -1
            filter_rho2 = -1
            filter_thickness2 = -1
        detector_pixels = [int(math.ceil((x1 - x0) * 3.27)),
                           int(math.ceil((y1 - y0) * 3.6))]
        detector_coords = [int(math.ceil(((x1 + x0) / 2) - 150) * (-0.177)),
                           int(math.ceil(((y0 + y1) / 2) - 280) * (-0.189))]
        tube_height = detector_coords[1]
        kvp = int(kvp_entry.get())
        if kvp < 69 or kvp > 125:
            popkvp_window()
            kvp_entry.delete(0, END)
            kvp_entry.insert(END, 70)
            return
        mas = float(mas_entry.get())
        if mas < 0.3 or mas > 100:
            popmas_window()
            mas_entry.delete(0, END)
            mas_entry.insert(END, 2)
            return
        dap = x_ray.calculate_xray(detector_coords, detector_pixels, tube_distance, kvp, mas, trans, tube_height,
                                   filter_z, filter_rho, filter_thickness, filter_z2, filter_rho2, filter_thickness2)
        dose["text"] = dap
        dose_conversion()
        global dose_helper
        dose_helper += 1
        helper_dose()
        x_ray_canvas.delete(image)
        new_img = cv.imread("Images/x_ray_image.png")
        new_img = image_switcharoo(new_img, 900, 1000)
        x_ray_canvas.create_image(450, 500, image=new_img)
        spectrum.config(state=ACTIVE)
        global fig
        spectrum_label.config(image="")
        fig = (Image.open("Images/fig.png"))
        fig = fig.resize((300, 300), Image.ANTIALIAS)
        fig = ImageTk.PhotoImage(fig)
        if spec_switch == 'no':
            spectrum_label.config(image="")
        elif spec_switch == "yes":
            spectrum_label.config(image=fig)

    # This function checks if mas_entry contains comma, and if so, changes it into a dot
    def contains_comma():
        global mas
        mas = mas_entry.get()
        comma = ","
        if comma in mas:
            mas = mas.replace(",",".")
            mas_entry.delete(0, "end")
            mas_entry.insert(0, mas)

    # Photo button
    photo = Button(root, text="X-ray", width=20, padx=10, pady=10, command=produce_xray)
    photo.place(x=1040, y=750)

    # Switch for the spectrum image
    global spec_switch
    spec_switch = "no"

    # Function for the spectrum image ON/OFF
    def spectrum_switch():
        global spec_switch
        if spec_switch == "no":
            spec_switch = "yes"
            spectrum.config(relief=SUNKEN)
        else:
            spec_switch = "no"
            spectrum.config(relief=RAISED)
        if spec_switch == 'no':
            spectrum_label.config(image="")
        elif spec_switch == "yes":
            spectrum_label.config(image=fig)

    # Spectrum button
    spectrum = Button(root, text="Show Spectrum", width=20, padx=5, pady=5, state=DISABLED, command=spectrum_switch)
    spectrum.place(x=1550, y=870)

    # Spectrum image
    global fig
    fig = (Image.open("Images/fig.png"))
    fig = fig.resize((300, 300), Image.ANTIALIAS)
    fig = ImageTk.PhotoImage(fig)
    spectrum_label = Label(root, image="")
    spectrum_label.place(x=1500, y=540)

    # Function for changing the minimap image into AP while retaining minimap box and tube height graphics
    def ap():
        global minimap_box
        global trans
        global minimap_tube_height
        trans = "AP"
        x0, y0, x1, y1 = mini_canvas.coords(minimap_box)
        mini_canvas.create_image(150, 250, image=minimap_image_ap)
        minimap_box = mini_canvas.create_rectangle(x0, y0, x1, y1, outline="white", width=2)
        w0, h0, w1, h1 = mini_canvas.coords(minimap_tube_height)
        minimap_tube_height = mini_canvas.create_rectangle(w0, h0, w1, h1, fill="blue")
        ap.config(relief=SUNKEN)
        pa.config(relief=RAISED)
        lat_left.config(relief=RAISED)

    # Function for changing the minimap image into PA while retaining minimap box and tube height graphics
    def pa():
        global minimap_box
        global trans
        global minimap_tube_height
        trans = "PA"
        x0, y0, x1, y1 = mini_canvas.coords(minimap_box)
        mini_canvas.create_image(150, 250, image=minimap_image_pa)
        minimap_box = mini_canvas.create_rectangle(x0, y0, x1, y1, outline="white", width=2)
        w0, h0, w1, h1 = mini_canvas.coords(minimap_tube_height)
        minimap_tube_height = mini_canvas.create_rectangle(w0, h0, w1, h1, fill="blue")
        ap.config(relief=RAISED)
        pa.config(relief=SUNKEN)
        lat_left.config(relief=RAISED)

    # Function for changing the minimap image into Lateral while retaining minimap box and tube height graphics
    def lat_left():
        global minimap_box
        global trans
        global minimap_tube_height
        trans = "LAT_left"
        x0, y0, x1, y1 = mini_canvas.coords(minimap_box)
        mini_canvas.create_image(150, 250, image=minimap_image_lat_left)
        minimap_box = mini_canvas.create_rectangle(x0, y0, x1, y1, outline="white", width=2)
        w0, h0, w1, h1 = mini_canvas.coords(minimap_tube_height)
        minimap_tube_height = mini_canvas.create_rectangle(w0, h0, w1, h1, fill="blue")
        ap.config(relief=RAISED)
        pa.config(relief=RAISED)
        lat_left.config(relief=SUNKEN)

    # Patient orientation frame
    patient_orient = LabelFrame(root, text="Patient orientation", padx=4, pady=10)
    patient_orient.place(x=980, y=100)

    # Body rotation buttons
    global trans
    trans = "AP"
    rot_font = tkinter.font.Font(size=7)
    ap = Button(patient_orient, text="AP", command=ap, padx=2)
    ap.grid(row=1, column=1)
    ap.config(relief=SUNKEN)
    pa = Button(patient_orient, text="PA", command=pa, padx=2)
    pa.grid(row=1, column=2)
    lat_left = Button(patient_orient, text="Lateral", font=rot_font, command=lat_left, height=2, padx=2)
    lat_left.grid(row=1, column=3)

    # Dose conversion function
    def dose_conversion():
        global dap
        if r.get() == 1:
            dose["text"] = float("{:.4f}".format(dap / 1000))
            dose_frame.config(text="DAP [" + "Gy\u2022cm\N{SUPERSCRIPT TWO}]", )
        elif r.get() == 2:
            dose["text"] = float("{:.3f}".format(dap / 100))
            dose_frame.config(text="DAP [" + "dGy\u2022cm\N{SUPERSCRIPT TWO}]")
        elif r.get() == 3:
            dose["text"] = float("{:.3f}".format(dap / 10))
            dose_frame.config(text="DAP [" + "cGy\u2022cm\N{SUPERSCRIPT TWO}]")
        elif r.get() == 4:
            dose["text"] = dap
            dose_frame.config(text="DAP [" + "mGy\u2022cm\N{SUPERSCRIPT TWO}]")
        elif r.get() == 5:
            dose["text"] = float("{:.3f}".format(dap / 10))
            dose_frame.config(text="DAP [" + "\u03BCGy\u2022m\N{SUPERSCRIPT TWO}]")

    # Dose display
    dose_frame = LabelFrame(root, text="DAP [mGy\u2022cm\N{SUPERSCRIPT TWO}]", padx=6, pady=6)
    dose_frame.place(x=1080, y=820)
    dose = Label(dose_frame, text="DAP", bg="white", padx=3, pady=3)
    dose.pack()

    # switch to create radiobuttons
    global dose_helper
    dose_helper = 0

    # Function to update the dose conversion radiobuttons state: creates new radiobuttons (only once)
    def helper_dose():
        if dose_helper == 1:
            dose1 = Radiobutton(root, text="Gy\u2022cm\N{SUPERSCRIPT TWO}", variable=r, value=1, state=NORMAL,
                                command=dose_conversion).place(x=1300, y=750)
            dose2 = Radiobutton(root, text="dGy\u2022cm\N{SUPERSCRIPT TWO}", variable=r, value=2, state=NORMAL,
                                command=dose_conversion).place(x=1300, y=780)
            dose3 = Radiobutton(root, text="cGy\u2022cm\N{SUPERSCRIPT TWO}", variable=r, value=3, state=NORMAL,
                                command=dose_conversion).place(x=1300, y=810)
            dose4 = Radiobutton(root, text="mGy\u2022cm\N{SUPERSCRIPT TWO}", variable=r, value=4, state=NORMAL,
                                command=dose_conversion).place(x=1300, y=840)
            dose5 = Radiobutton(root, text="\u03BCGy\u2022m\N{SUPERSCRIPT TWO}", variable=r, value=5, state=NORMAL,
                                command=dose_conversion).place(x=1300, y=870)

    # Initial DAP conversion buttons. These are overwritten when x-ray button is pushed for the first time
    global dose1
    global dose2
    global dose3
    global dose4
    global dose5
    r = IntVar()
    r.set("4")
    dose1 = Radiobutton(root, text="Gy\u2022cm\N{SUPERSCRIPT TWO}", variable=r, value=1, state=DISABLED,
                        command=dose_conversion).place(x=1300, y=750)
    dose2 = Radiobutton(root, text="dGy\u2022cm\N{SUPERSCRIPT TWO}", variable=r, value=2, state=DISABLED,
                        command=dose_conversion).place(x=1300, y=780)
    dose3 = Radiobutton(root, text="cGy\u2022cm\N{SUPERSCRIPT TWO}", variable=r, value=3, state=DISABLED,
                        command=dose_conversion).place(x=1300, y=810)
    dose4 = Radiobutton(root, text="mGy\u2022cm\N{SUPERSCRIPT TWO}", variable=r, value=4, state=DISABLED,
                        command=dose_conversion).place(x=1300, y=840)
    dose5 = Radiobutton(root, text="\u03BCGy\u2022m\N{SUPERSCRIPT TWO}", variable=r, value=5, state=DISABLED,
                        command=dose_conversion).place(x=1300, y=870)

    about_text = "This program was created by Jones Jernfors from University of Oulu in 2022 \n " \
                 "with the help of medical physicists " \
                 "Dr. Matti Hanni and Dr. Timo Liimatainen from Oulu University Hospital, \n and Dr. Miika Nieminen, " \
                 "professor of Medical Physics at University of Oulu." \
                 "\n This program uses GVirtualXRay, created by Dr. Franck P. Vidal, to simulate X-ray " \
                 "transmission from the 3D models. \n" \
                 "The X-ray spectrum is calculated using the code of Michael Gallis" \
                 "\n The images and doses with different parameters are purely indicative and should not be regarded " \
                 "as absolute truth" \
                 "\n This program is licensed under GPL-3.0-or-later"

    # Popup window for "about" information
    def pop_about():
        global pop_about
        root_x = root.winfo_rootx()
        root_y = root.winfo_rooty()
        winx = root_x + 550
        winy = root_y + 350
        pop_about = Toplevel(root)
        pop_about.title("About")
        pop_about.geometry(f'+{winx}+{winy}')
        pop_about_label = Label(pop_about, text=about_text)
        pop_about_label.pack()
        pop_button = Button(pop_about, text="OK", command=lambda: pop_about.destroy())
        pop_button.pack()

    about_button = Button(root, text="About", command=pop_about)
    about_button.place(x=1500, y=20)
