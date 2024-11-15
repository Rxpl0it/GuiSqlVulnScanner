import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

class Graph:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.vulnerabilities = []

        # Initialize the graph
        self.fig, self.ax = plt.subplots()
        self.ax.set_title("Vulnerabilities Found Over Time")
        self.ax.set_xlabel("Scans")
        self.ax.set_ylabel("Number of Vulnerabilities")
        self.line, = self.ax.plot([], [], 'r-')  # Red line for vulnerabilities

        # Embed the plot in the Tkinter frame
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.parent_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def initialize_graph(self):
        self.vulnerabilities = []
        self.line.set_data([], [])
        self.ax.relim()
        self.ax.autoscale_view()
        self.canvas.draw()

    def update(self, count):
        self.vulnerabilities.append(count)
        self.line.set_data(range(len(self.vulnerabilities)), self.vulnerabilities)
        self.ax.relim()
        self.ax.autoscale_view()
        self.canvas.draw()
