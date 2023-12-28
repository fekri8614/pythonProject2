"""
https://github.com/navdeepm20/Photo_Background_Remover_Gui
"""

from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import ImageTk, Image
import tkinter.messagebox as tmsg
import requests
import os.path


class RmGui(Tk):

    def __init__(self):
        super().__init__()
        # self.iconbitmap("assets/main.icon")
        self.top_main_menu = None
        self.r_image = None
        self.original_path = None
        self.ipath = None
        self.title("Bg_Remover")
        self.geometry("900x600")
        self.bottom_frame = Frame(self, relief=SUNKEN, width=900, height=25)
        self.bottom_frame.pack(fill=X, side=BOTTOM)
        self.pic_f1 = Frame(self, relief=SUNKEN, width=450)
        self.minsize(900, 600)
        self.maxsize(900, 600)
        self.your_apikey = 'CAdRsjrvLpy4Z7BLtgrvNNX5'  # paste the key inside the single quotes. This is a demo key
        # and it will not work.

    def pic_loader(self):  # Fuction to load picture inside the program

        self.ipath = askopenfilename(
            filetypes=[('JPG Files', '*.jpg'), ('PNG Files', '*.png'), ('JPEG Files', '*.jpeg')])  # ,
        if os.path.exists(self.ipath):

            self.original_path = self.ipath
            img = self.picresizedpreview(self.ipath)
            self.r_image = ImageTk.PhotoImage(img)

            self.piclabel1(self.r_image)
        else:
            tmsg.showinfo("Error", "File Open Action Aborted By the User")

    def top_menu(self):  # will create the top menu for the program
        self.top_main_menu = Menu(self)
        self.top_main_menu.add_command(label="Open", command=self.pic_loader)
        self.top_main_menu.add_command(label="How to Start", command=self.how_to_start)
        self.top_main_menu.add_command(label="About", command=self.about_loader)
        self.config(menu=self.top_main_menu)

    @staticmethod
    def about_loader():  # about option method
        tmsg.showinfo("Message From Developer", "This App is Created and Managed by Navdeep Mishra")

    @staticmethod
    def how_to_start():  # how to start method
        tmsg.showinfo("How to Start",
                      "1)Click on Open and Select Your Desired Image\n2)Click On Upload Button (One Time Only and don't touch anything, just wait)\n3)A Window will popup automatically when everything is done, just save the file")

    def picframe1_2(self):  # pic1 frame packer and pic2 frame creater and packer method

        self.pic_f1.pack(side=LEFT, fill=BOTH, anchor="nw")
        self.picf2 = Frame(root, relief=SUNKEN, width=450)
        self.picf2.pack(side=RIGHT, anchor="ne", fill=BOTH)

    def picresizedpreview(self, imag):  # Return a resized image for the preview in the application window
        try:
            Img = Image.open(imag)
            originalwidth, originalheight = Img.size
            self.originalimagesize = (originalwidth, originalheight)

            newwidth = 450
            newheight = newwidth * originalheight // originalwidth
            resized = (newwidth, newheight)
            Img = Img.resize(resized)
            return Img
        except AttributeError as ee:
            tmsg.showinfo("Error", "File Open Action Aborted By the User")

    def piclabel2load(self):  # method that shows the picture inside frame
        Img = self.picresizedpreview(self.nImage)
        self.nImage = ImageTk.PhotoImage(Img)

        self.piclabel2 = Label(self.picf2, image=self.nImage)

        self.piclabel2.pack()

    def piclabel1(self, rImage):  # method that shows the picture inside frame
        self.picLabel1 = Label(self.pic_f1, image=rImage)
        self.picLabel1.pack(side=LEFT, anchor="nw")

    def uploadbutton(self):  # Will Create Upload button
        self.supbt = Button(self.bottom_frame, text="Upload", command=self.upload_button_functionality)
        self.supbt.pack(side=LEFT, anchor="se")

    def bottomlabel(self):  # bottom status bar
        self.cstatus = StringVar()
        self.cstatus.set("Ready")
        self.sbar = Label(self.bottom_frame, textvariable=self.cstatus)
        self.sbar.pack(side=LEFT, fill=X, expand=1, anchor="sw", ipady=2, pady=(2, 0))

    def bottom_bar_frame(self):  # Creates bottom frame
        self.bottomlabel()
        self.uploadbutton()

    def upload_button_functionality(self):  # Functionality for the upload button
        try:
            if os.path.exists(self.ipath):
                tmsg.showinfo("Important Message",
                              "Don't Double Press the button and Don't Drag the Application.If Application Shows not responding,Don't Worry application is still working in background just wait for AutoFile Save or until any Message pop up")
                # self.pathupdater()

                self.cstatus.set("Working on it. Please Wait....")
                self.sbar.update()
                response = requests.post(
                    'https://api.remove.bg/v1.0/removebg',
                    files={'image_file': open(self.ipath, 'rb')},
                    data={'size': 'auto'},
                    headers={'X-Api-Key': self.your_apikey},
                )
                if response.status_code == requests.codes.ok:

                    newfilepath = self.downloadfunctionality()

                    with open(newfilepath, 'wb') as out:
                        out.write(response.content)

                    self.nImage = newfilepath
                    self.piclabel2load()
                    self.cstatus.set("File Saved Succesfully")

                else:

                    tmsg.showinfo("Error", "Error Code: " + str(response.status_code))
                    self.cstatus.set("Error Occured")
                    self.sbar.update()
            else:
                tmsg.showerror("Error", "Image is not loaded into the Previewer.")
        except requests.exceptions.ConnectionError:

            tmsg.showinfo("Error", "Connection Error")
        except AttributeError as e:
            tmsg.showinfo("Error", "Open the Image in the image previewer first")
        except FileNotFoundError:
            tmsg.showinfo("Error", "No Valid File Found. Open the Image in the image previewer first")
            self.cstatus.set("Ready")
            self.sbar.update()

    def downloadfunctionality(self):

        files = [
            ('Png Files', '*.png'),
        ]
        newfilepath = asksaveasfilename(filetypes=files, defaultextension=files)
        return newfilepath

    # //////////////////////////Program will Start From here.//////////////////////////////


if __name__ == '__main__':
    root = RmGui()
    root.top_menu()  # Calling the Menu creater Function
    root.bottom_bar_frame()  # Calling the Bottom bar Frame that contains the staus bar and upload button Funciton
    root.picframe1_2()  # Calling Pic frame 1 and 2
    root.mainloop()  # Mainloop Funciton
