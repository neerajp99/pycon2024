from manim import *

class CoordinateSystems(Scene):
    def construct(self):
        # Create axes with ticks and labels
        axes = Axes(
            x_range=[-1, 10, 1],  # From -1 to 10 with step of 1
            y_range=[-2, 2, 0.5],  # From -2 to 2 with step of 0.5
            x_length=10,
            y_length=6,
            axis_config={"color": LIGHT_GRAY},
            x_axis_config={"numbers_to_include": np.arange(-1, 11, 1)},  # Numbers on x-axis
            y_axis_config={"numbers_to_include": np.arange(-2, 2.5, 0.5)},  # Numbers on y-axis
            tips=False,  # No arrow tips
        )
        axes_labels = axes.get_axis_labels()

        # Create grid with correct style settings
        grid = NumberPlane(
            x_range=[-1, 10, 1],
            y_range=[-2, 2, 0.5]
        )
        grid.set_stroke(color=GRAY, width=0.5)

        # Adding grid and axes
        self.add(grid, axes, axes_labels)

        # Create and add dot
        dot = Dot(color=RED).move_to(axes.c2p(0, 0))
        dot_label = MathTex("\\vec{v}=(0, 0)", color=RED).to_corner(DOWN + RIGHT)

        # Animate dot and its label
        self.play(FadeIn(dot, scale=0.5), Write(dot_label))
        self.play(dot.animate.move_to(axes.c2p(3, 2)))
        dot_label.become(MathTex("\\vec{v}=(3, 2)", color=RED).to_corner(DOWN + RIGHT))
        self.wait(1)

        # More complex animations with the dot
        self.play(dot.animate.move_to(axes.c2p(5, 0.5)))
        dot_label.become(MathTex("\\vec{v}=(5, 0.5)", color=RED).to_corner(DOWN + RIGHT))
        self.wait(1)

        # Draw dynamic lines from axes to dot
        h_line = always_redraw(lambda: axes.get_horizontal_line(dot.get_left()))
        v_line = always_redraw(lambda: axes.get_vertical_line(dot.get_bottom()))
        self.play(Create(h_line), Create(v_line), run_time=2)
        
        # Move dot around
        positions = [(3, -2), (1, 1)]
        for pos in positions:
            self.play(dot.animate.move_to(axes.c2p(*pos)))
            new_label = MathTex(f"\\vec{{v}}=({pos[0]}, {pos[1]})", color=RED).to_corner(DOWN + RIGHT)
            dot_label.become(new_label)
            self.wait(1)

        # Conclude
        self.play(FadeOut(VGroup(axes, dot, h_line, v_line, grid, dot_label)))

# To run this scene, use the following command or VS Code Manim extension:
# manim -pql coordinate.py CoordinateSystems
