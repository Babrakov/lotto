# Widgets:
from tkinter import *
window = Tk()
img = PhotoImage( file = 'logo.gif' )
imgLbl = Label( window, image = img )
label1 = Label( window, relief = 'groove', width = 2 )
label2 = Label( window, relief = 'groove', width = 2 )
label3 = Label( window, relief = 'groove', width = 2 )
label4 = Label( window, relief = 'groove', width = 2 )
label5 = Label( window, relief = 'groove', width = 2 )
label6 = Label( window, relief = 'groove', width = 2 )
getBtn = Button( window )
resBtn = Button( window )

# Geometry:
imgLbl.grid()
label1.grid()
label2.grid()
label3.grid()
label4.grid()
label5.grid()
label6.grid()
getBtn.grid()
resBtn.grid()

# Static Properties:
window.title('Lotto Number Picker')
window.resizable(0,0)
getBtn.configure(text = 'Get My Lucky Number')
resBtn.configure(text = 'Reset')

# Initial Properties:


# Dynamic Properties:

# Sustain window:
window.mainloop()
