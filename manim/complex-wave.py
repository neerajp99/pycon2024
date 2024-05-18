from manim import *

class ComplexWaveAnimation(Scene):
    def construct(self):
        # Set up the axes
        axes = Axes(
            x_range=[-2 * PI, 2 * PI, 1],
            y_range=[-2, 2, 0.5],
            x_length=10,
            y_length=6,
            axis_config={"color": WHITE},
            tips=False,
        )

        # Label the axes
        axes_labels = axes.get_axis_labels(
            x_label="Time (seconds)", y_label="Amplitude"
        )

        # Create the wave function
        wave = axes.plot(
            lambda x: np.sin(x) + np.cos(2 * x),  # More complex wave pattern
            color=WHITE,
            x_range=[-2 * PI, 2 * PI],
        )

        # Initial setup of the wave line (starting at the first point of the wave)
        first_point = wave.get_points()[0]
        wave_line = VMobject()
        wave_line.set_points_as_corners([first_point, first_point])
        wave_line.set_color(WHITE)

        # Animate drawing the wave
        self.add(axes, axes_labels, wave_line)
        self.play(Create(axes), Write(axes_labels))
        self.play(
            UpdateFromAlphaFunc(
                wave_line,
                lambda mob, alpha: mob.set_points_as_corners(
                    [first_point, *wave.get_points()[:int(alpha * len(wave.get_points()))]]
                )
            ),
             # Animation run time in seconds
            run_time=4, 
            rate_func=linear
        )
        
        # Hold the final frame
        self.wait(1)  

# To run this Scene, use the following command or use the VS Code extension for Manim:
# manim -pql complex-wave.py ComplexWaveAnimation
