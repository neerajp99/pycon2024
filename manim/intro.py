from manim import *

class PyCon2024Presentation(Scene):
    def construct(self):
        # Start with suspenseful text
        intro_text = Text("Let's talk about Manim!", font_size=48, color=WHITE)
        self.play(Write(intro_text, shift=UP))
        self.wait(1)
        self.play(FadeOut(intro_text, shift=DOWN))

        # Transition to some mathematical graph animations
        self.play_intro_graph()

        # Introduce the mathematical equation
        self.show_equation()

    def play_intro_graph(self):
        # Create axes with numbers on the axes
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            x_length=9,
            y_length=6,
            axis_config={"color": GREEN_A, "include_numbers": True},  # Enable numbers on axes
            tips=True,
        )
        # Example graph: y = x^2
        graph = axes.plot(lambda x: x**2, color=WHITE, stroke_width=2)
        graph_label = axes.get_graph_label(graph, label='y = x^2')

        # Display the graph and label
        self.play(Create(axes), Create(graph))
        self.play(Write(graph_label))
        self.wait(2)

        # Demonstrate transformation of the graph
        new_graph = axes.plot(lambda x: x**2 + 2*x + 1, color=YELLOW, stroke_width=2)
        new_graph_label = axes.get_graph_label(new_graph, label='y = (x+1)^2', x_val=8, direction=UP+RIGHT)
        
        # Animate transformation
        self.play(Transform(graph, new_graph), Transform(graph_label, new_graph_label))
        self.wait(2)

        # Clear the graph before moving to outro
        self.play(FadeOut(axes), FadeOut(graph), FadeOut(graph_label), FadeOut(new_graph), FadeOut(new_graph_label))

    def show_equation(self):
        # Specify the equation with scaling for visibility
        equation = MathTex(r"\frac{d}{dx} \int_{0}^{x} {f}(u) \ du = {f}(x)").scale(2)
        self.play(Write(equation))
        self.wait()

        # Save the current state of the equation to restore later
        equation.save_state()

        # Restore to the previous state
        self.play(Restore(equation))
        self.wait()

# To run this scene, use the following command in your terminal or script execution:
# manim -pql intro.py PyCon2024Presentation
