from manim import *

class EnhancedMatrixTransformation(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
            show_basis_vectors=True,
        )

    def construct(self):
        # Define the transformation matrix
        matrix = [[1, 3], [3, 4]]
        matrix_tex = (
            MathTex(r"A = \begin{bmatrix} 1 & 3\\ 3 & 4 \end{bmatrix}")
            .to_edge(UL)
            .add_background_rectangle()
        )

        # Create a unit square and text to display its area dynamically
        unit_square = self.get_unit_square()
        det_text = always_redraw(
            lambda: Tex(f"Area: {abs(matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0])}", font_size=24)
            .move_to(unit_square.get_center())
        )

        # Vector and additional geometric shapes
        vect = self.get_vector([1, -2], color=PURPLE_B)
        ellipse = Ellipse(
            width=2, height=1, stroke_color=GREEN_B, fill_color=GREEN_D, fill_opacity=0.5
        ).shift(UP * 2 + RIGHT * 2)

        triangle = Triangle(
            stroke_color=RED_B, fill_color=RED_D, fill_opacity=0.5
        ).shift(DOWN * 2 + LEFT * 1)

        # Add objects to the scene for transformation
        self.add_transformable_mobject(vect, unit_square, ellipse, triangle)
        self.add_background_mobject(matrix_tex, det_text)
        self.apply_matrix(matrix)

        self.wait()
