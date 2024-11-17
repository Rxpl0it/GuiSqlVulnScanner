import plotly.graph_objs as go
from plotly.subplots import make_subplots
from tkinter import Frame

class Graph:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.vulnerabilities = []

        # Initialize the Plotly graph
        self.fig = make_subplots(rows=1, cols=1)
        self.fig.add_trace(go.Scatter(x=[], y=[], mode='lines', name='Vulnerabilities'))
        self.fig.update_layout(title="Vulnerabilities Found Over Time",
                               xaxis_title="Scans",
                               yaxis_title="Number of Vulnerabilities")

        # Embed the plot in the Tkinter frame
        self.canvas = Frame(self.parent_frame)
        self.canvas.pack(side='top', fill='both', expand=True)
        self.plotly_fig = go.FigureWidget(self.fig)
        self.plotly_fig.show(renderer="iframe_connected", notebook=False)

    def initialize_graph(self):
        self.vulnerabilities = []
        self.plotly_fig.data[0].x = []
        self.plotly_fig.data[0].y = []
        self.plotly_fig.update_layout(autosize=True)

    def update(self, count):
        self.vulnerabilities.append(count)
        self.plotly_fig.data[0].x = list(range(len(self.vulnerabilities)))
        self.plotly_fig.data[0].y = self.vulnerabilities
        self.plotly_fig.update_layout(autosize=True)
