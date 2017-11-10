from tkinter import *
import matplotlib
import numpy as np
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
		
class PltDataFrame(Frame):
    def __init__(self, master,V_data=[],Cp_data=[],Gp_data=[]):
        ttk.Frame.__init__(self, master)
        self.f = Figure(figsize=(7,4), dpi=100)
        
        
    def updatePlot(self,V_data,Cp_data,Gp_data):
        self.ax1 = self.f.add_subplot(111)
        self.ax2 = self.ax1.twinx()
        self.V_data=V_data
        self.Cp_data=Cp_data
        self.Gp_data=Gp_data
        
        t = self.V_data 
        s1 = self.Cp_data
        s2 = self.Gp_data

        self.ax1.plot(t, s1, 'b-')
        self.ax1.set_title('Data Plot')
        self.ax1.set_xlabel('Voltage(V)')
        self.ax1.set_ylabel('Cp', color='b')
        self.ax1.tick_params('y', colors='b')
        
        
        self.ax2.plot(t, s2, 'r.')
        self.ax2.set_ylabel('Gp', color='r')
        self.ax2.tick_params('y', colors='r')
    

        canvas = FigureCanvasTkAgg(self.f,self)
        canvas.draw()
        #canvas.show()
        canvas.get_tk_widget().pack( expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(expand=True)