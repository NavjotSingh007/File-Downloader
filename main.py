from tkinter import *
import lib
import IPython

def display():
    convert = convert_to_pdf.get()
    status = lib.download_file(v.get(), convert)
    status_message.set(status)

def close():
    win.destroy()


def makeWindow () :
    win = Tk()

    global v, status_message, convert_to_pdf

    frame1 = Frame(win)
    frame1.pack(pady=30)

    v = StringVar()
    e = Entry(frame1, textvariable=v)
    e.pack(pady=30)

    frame2 = Frame(win)
    frame2.pack()

    convert_to_pdf = IntVar()

    check_box = Checkbutton(frame2, text="convert To Pdf", variable=convert_to_pdf).pack()

    frame3 = Frame(win)
    frame3.pack()
    start_button = Button(frame3, text='Start', command=display).pack(side=LEFT, padx=20)
    close_button = Button(frame3, text='Close', command=close).pack(side=RIGHT, padx=20)

    frame4 = Frame(win)
    frame4.pack()

    status_message = StringVar()
    l = Label(frame4, textvariable=status_message).pack()


    win.wm_title('File Downloader')
    win.resizable(width='FALSE', height='FALSE')
    win.wm_geometry("%dx%d%+d%+d" % (720, 480, 0, 0))

    return win


win = makeWindow()
status_message.set('Ready!')
win.mainloop()


