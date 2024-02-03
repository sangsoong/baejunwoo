import tkinter as tk

#start
window = tk.Tk()
sc_width = window.winfo_screenwidth()
sc_height = window.winfo_screenheight()
w_width = 400
w_height = 600
margin_up = 80

#insert widget here
window.title('test window')
window.geometry(f'{w_width}x{w_height}+{int((sc_width/2)-(w_width/2))}+{int((sc_height/2)-(w_height/2) - margin_up)}')
window.resizable(False, False)



#end
window.mainloop()