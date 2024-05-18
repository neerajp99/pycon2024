from manim import *
import matplotlib.pyplot as plt

class BarChart(Scene):
    def construct(self):
        # Increase the figure size
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Create a bar chart with a darker theme
        ax.bar([1, 2, 3], [3, 1, 2], color='white')
        
        # Set a dark background and light gridlines
        fig.patch.set_facecolor('#0e1117')
        ax.set_facecolor('#0e1117')
        ax.grid(color='white', linestyle='-', linewidth=0.5)
        
        # Set the color of the spines, ticks, and labels to white
        ax.spines['bottom'].set_color('white')
        ax.spines['top'].set_color('white')
        ax.spines['right'].set_color('white')
        ax.spines['left'].set_color('white')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        
        # Save the plot
        plt.savefig("bar_chart.png", facecolor=fig.get_facecolor(), edgecolor='none')
        
        # Load and display the image in Manim
        image = ImageMobject("bar_chart.png")
        # Increase run_time to slow down the animation
        self.play(FadeIn(image, run_time=3))  