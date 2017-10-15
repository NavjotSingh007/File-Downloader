from tkinter import *
import lib
import IPython

def display():
    status = lib.download_file(v.get())
    status_message.set(status)

def close():
    win.destroy()


def makeWindow () :
    win = Tk()

    global v, status_message

    frame1 = Frame(win)
    frame1.pack(pady=30)

    v = StringVar()
    e = Entry(frame1, textvariable=v)
    e.pack(pady=30)

    frame2 = Frame(win)
    frame2.pack()

    start_button = Button(frame2, text='Start', command=display).pack(side=LEFT, padx=20)
    close_button = Button(frame2, text='Close', command=close).pack(side=RIGHT, padx=20)

    frame3 = Frame(win)
    frame3.pack()

    status_message = StringVar()
    l = Label(frame3, textvariable=status_message).pack()


    win.wm_title('File Downloader')
    win.resizable(width='FALSE', height='FALSE')
    win.wm_geometry("%dx%d%+d%+d" % (720, 480, 0, 0))

    return win


win = makeWindow()
status_message.set('Ready!')
win.mainloop()


