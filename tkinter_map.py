

from tkinter import *
import tkintermapview
import internet_checker as internetChecker


def main():
    root = Tk()
    root.geometry('1920x1080')

    if internetChecker.is_internet_connected():
        my_label = LabelFrame(root)
        my_label.pack(pady=20)

        map_widget = tkintermapview.TkinterMapView(my_label, width=1500, height=800)
        map_widget.set_position(36.1699, -115.1396)
        map_widget.set_zoom(15)
        map_widget.pack()

    else:
        error_label = Label(root)
        error_label.text = "Something went wrong\nCheck your internet and try again",
        error_label.pack()

    root.mainloop()


if __name__ == '__main__':
    main()
