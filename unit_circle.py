from manim import *
import numpy as np

class UnitCircleExplanation(Scene):
    def construct(self):
        # 3Blue1Brown color scheme
        CIRCLE_COLOR = BLUE
        HIGHLIGHT_COLOR = YELLOW
        SINE_COLOR = RED
        COSINE_COLOR = GREEN
        TANGENT_COLOR = ORANGE

        # Title
        title = Text("Understanding the Unit Circle", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        self.play(FadeOut(title))

        # Create axes
        axes = Axes(
            x_range=[-1.5, 1.5, 0.5],
            y_range=[-1.5, 1.5, 0.5],
            x_length=6,
            y_length=6,
            axis_config={"color": GREY, "include_numbers": False},
        ).shift(LEFT * 2.5)

        # Create unit circle
        circle = Circle(radius=2, color=CIRCLE_COLOR, stroke_width=3)
        circle.move_to(axes.c2p(0, 0))

        # Labels for axes
        x_label = MathTex("x", color=WHITE).next_to(axes.x_axis, RIGHT)
        y_label = MathTex("y", color=WHITE).next_to(axes.y_axis, UP)

        # Draw axes and circle
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Create(circle))
        self.wait(0.5)

        # Add center point
        origin = Dot(axes.c2p(0, 0), color=WHITE)
        self.play(FadeIn(origin))

        # Create side panel for formulas
        panel = Rectangle(height=6, width=3.5, color=BLUE_E, fill_opacity=0.1)
        panel.to_edge(RIGHT).shift(LEFT * 0.3)
        panel_title = Text("Key Formulas", font_size=28).next_to(panel, UP, buff=0.2)

        self.play(Create(panel), Write(panel_title))

        # Add formulas to panel
        formulas = VGroup(
            MathTex(r"\text{Radius} = 1", font_size=28),
            MathTex(r"x = \cos(\theta)", font_size=28, color=COSINE_COLOR),
            MathTex(r"y = \sin(\theta)", font_size=28, color=SINE_COLOR),
            MathTex(r"\tan(\theta) = \frac{y}{x}", font_size=28, color=TANGENT_COLOR),
            MathTex(r"\sin^2 + \cos^2 = 1", font_size=28),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        formulas.move_to(panel.get_center())

        self.play(Write(formulas), run_time=2)
        self.wait(0.5)

        # Special angles to highlight
        special_angles = [0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330, 360]

        # Function to get point on circle
        def get_circle_point(angle_deg):
            angle_rad = angle_deg * DEGREES
            return axes.c2p(np.cos(angle_rad), np.sin(angle_rad))

        # Animation for each special angle
        for i, angle_deg in enumerate(special_angles):
            angle_rad = angle_deg * DEGREES

            # Calculate coordinates
            cos_val = np.cos(angle_rad)
            sin_val = np.sin(angle_rad)

            # Point on circle
            point = Dot(get_circle_point(angle_deg), color=HIGHLIGHT_COLOR, radius=0.08)

            # Radius line (hypotenuse)
            radius_line = Line(
                axes.c2p(0, 0),
                axes.c2p(cos_val, sin_val),
                color=HIGHLIGHT_COLOR,
                stroke_width=3
            )

            # Vertical line (sine/opposite)
            vertical_line = DashedLine(
                axes.c2p(cos_val, 0),
                axes.c2p(cos_val, sin_val),
                color=SINE_COLOR,
                stroke_width=3
            )

            # Horizontal line (cosine/adjacent)
            horizontal_line = DashedLine(
                axes.c2p(0, 0),
                axes.c2p(cos_val, 0),
                color=COSINE_COLOR,
                stroke_width=3
            )

            # Right angle marker
            if abs(cos_val) > 0.1 and abs(sin_val) > 0.1:
                square_size = 0.15
                right_angle = VGroup(
                    Line(axes.c2p(cos_val - square_size * np.sign(cos_val), 0),
                         axes.c2p(cos_val - square_size * np.sign(cos_val), square_size * np.sign(sin_val))),
                    Line(axes.c2p(cos_val - square_size * np.sign(cos_val), square_size * np.sign(sin_val)),
                         axes.c2p(cos_val, square_size * np.sign(sin_val)))
                ).set_color(WHITE).set_stroke_width(1)
            else:
                right_angle = VGroup()

            # Angle arc
            if angle_deg > 0:
                angle_arc = Arc(
                    radius=0.4,
                    start_angle=0,
                    angle=angle_rad,
                    color=YELLOW,
                    stroke_width=2
                ).move_to(axes.c2p(0, 0))
            else:
                angle_arc = VGroup()

            # Angle label
            angle_label = MathTex(f"{angle_deg}°", font_size=24, color=YELLOW)
            if angle_deg <= 90:
                angle_label.next_to(angle_arc, RIGHT, buff=0.1).shift(UP * 0.1)
            elif angle_deg <= 180:
                angle_label.next_to(angle_arc, UP, buff=0.1).shift(LEFT * 0.1)
            elif angle_deg <= 270:
                angle_label.next_to(angle_arc, LEFT, buff=0.1).shift(DOWN * 0.1)
            else:
                angle_label.next_to(angle_arc, DOWN, buff=0.1).shift(RIGHT * 0.1)

            # Coordinate label
            # Format special values nicely
            if angle_deg == 0:
                coord_text = "(1, 0)"
            elif angle_deg == 30:
                coord_text = r"(\frac{\sqrt{3}}{2}, \frac{1}{2})"
            elif angle_deg == 45:
                coord_text = r"(\frac{\sqrt{2}}{2}, \frac{\sqrt{2}}{2})"
            elif angle_deg == 60:
                coord_text = r"(\frac{1}{2}, \frac{\sqrt{3}}{2})"
            elif angle_deg == 90:
                coord_text = "(0, 1)"
            elif angle_deg == 120:
                coord_text = r"(-\frac{1}{2}, \frac{\sqrt{3}}{2})"
            elif angle_deg == 135:
                coord_text = r"(-\frac{\sqrt{2}}{2}, \frac{\sqrt{2}}{2})"
            elif angle_deg == 150:
                coord_text = r"(-\frac{\sqrt{3}}{2}, \frac{1}{2})"
            elif angle_deg == 180:
                coord_text = "(-1, 0)"
            elif angle_deg == 210:
                coord_text = r"(-\frac{\sqrt{3}}{2}, -\frac{1}{2})"
            elif angle_deg == 225:
                coord_text = r"(-\frac{\sqrt{2}}{2}, -\frac{\sqrt{2}}{2})"
            elif angle_deg == 240:
                coord_text = r"(-\frac{1}{2}, -\frac{\sqrt{3}}{2})"
            elif angle_deg == 270:
                coord_text = "(0, -1)"
            elif angle_deg == 300:
                coord_text = r"(\frac{1}{2}, -\frac{\sqrt{3}}{2})"
            elif angle_deg == 315:
                coord_text = r"(\frac{\sqrt{2}}{2}, -\frac{\sqrt{2}}{2})"
            elif angle_deg == 330:
                coord_text = r"(\frac{\sqrt{3}}{2}, -\frac{1}{2})"
            else:
                coord_text = f"({cos_val:.2f}, {sin_val:.2f})"

            coord_label = MathTex(coord_text, font_size=20, color=WHITE)
            coord_label.next_to(point, UP + RIGHT, buff=0.1)

            # Labels for sin and cos
            cos_label = MathTex(r"\cos", font_size=20, color=COSINE_COLOR)
            sin_label = MathTex(r"\sin", font_size=20, color=SINE_COLOR)

            if abs(cos_val) > 0.1:
                cos_label.next_to(horizontal_line, DOWN, buff=0.1)
            else:
                cos_label = VGroup()

            if abs(sin_val) > 0.1:
                sin_label.next_to(vertical_line, RIGHT, buff=0.1)
            else:
                sin_label = VGroup()

            # Animation
            if i == 0:
                # First angle - create everything
                self.play(
                    Create(radius_line),
                    Create(horizontal_line),
                    Create(vertical_line),
                    FadeIn(point),
                    Create(right_angle),
                    run_time=0.5
                )
                if len(angle_arc) > 0:
                    self.play(Create(angle_arc), Write(angle_label), run_time=0.3)
                self.play(Write(coord_label), Write(cos_label), Write(sin_label), run_time=0.3)

                # Store objects for later transformation
                prev_radius = radius_line
                prev_horizontal = horizontal_line
                prev_vertical = vertical_line
                prev_point = point
                prev_angle_arc = angle_arc
                prev_angle_label = angle_label
                prev_coord_label = coord_label
                prev_cos_label = cos_label
                prev_sin_label = sin_label
                prev_right_angle = right_angle

                # Pause on special angles
                if angle_deg in [30, 45, 60, 90]:
                    self.wait(0.8)
                else:
                    self.wait(0.4)
            else:
                # Transform to next angle
                animations = [
                    Transform(prev_radius, radius_line),
                    Transform(prev_horizontal, horizontal_line),
                    Transform(prev_vertical, vertical_line),
                    Transform(prev_point, point),
                    Transform(prev_coord_label, coord_label),
                    Transform(prev_right_angle, right_angle),
                ]

                if len(angle_arc) > 0:
                    animations.extend([
                        Transform(prev_angle_arc, angle_arc),
                        Transform(prev_angle_label, angle_label)
                    ])

                if len(cos_label) > 0:
                    animations.append(Transform(prev_cos_label, cos_label))
                else:
                    animations.append(FadeOut(prev_cos_label))
                    prev_cos_label = VGroup()

                if len(sin_label) > 0:
                    animations.append(Transform(prev_sin_label, sin_label))
                else:
                    animations.append(FadeOut(prev_sin_label))
                    prev_sin_label = VGroup()

                self.play(*animations, run_time=0.3)

                # Pause longer on special angles
                if angle_deg in [30, 45, 60, 90, 120, 135, 150, 180, 270]:
                    self.wait(0.8)
                else:
                    self.wait(0.3)

        self.wait(1)

        # Clear for bonus section
        self.play(
            FadeOut(prev_radius),
            FadeOut(prev_horizontal),
            FadeOut(prev_vertical),
            FadeOut(prev_point),
            FadeOut(prev_angle_arc),
            FadeOut(prev_angle_label),
            FadeOut(prev_coord_label),
            FadeOut(prev_cos_label),
            FadeOut(prev_sin_label),
            FadeOut(prev_right_angle),
        )

        # Bonus: Show sine and cosine waves
        wave_title = Text("Sine and Cosine Waves", font_size=32)
        wave_title.to_edge(UP)
        self.play(Write(wave_title))

        # Create wave axes
        wave_axes = Axes(
            x_range=[0, 2*PI, PI/2],
            y_range=[-1.2, 1.2, 0.5],
            x_length=8,
            y_length=3,
            axis_config={"color": GREY},
        ).to_edge(DOWN).shift(UP * 0.5)

        # Axis labels
        wave_x_label = MathTex(r"\theta", font_size=24).next_to(wave_axes.x_axis, RIGHT)

        self.play(Create(wave_axes), Write(wave_x_label))

        # Animate point and waves together
        dot_tracker = ValueTracker(0)

        # Point on circle
        moving_dot = always_redraw(lambda: Dot(
            axes.c2p(np.cos(dot_tracker.get_value()), np.sin(dot_tracker.get_value())),
            color=HIGHLIGHT_COLOR,
            radius=0.08
        ))

        # Radius line
        moving_radius = always_redraw(lambda: Line(
            axes.c2p(0, 0),
            axes.c2p(np.cos(dot_tracker.get_value()), np.sin(dot_tracker.get_value())),
            color=HIGHLIGHT_COLOR,
            stroke_width=3
        ))

        # Sine wave
        sine_wave = always_redraw(lambda: wave_axes.plot(
            lambda x: np.sin(x),
            x_range=[0, dot_tracker.get_value(), 0.01],
            color=SINE_COLOR,
            stroke_width=3
        ))

        # Cosine wave
        cosine_wave = always_redraw(lambda: wave_axes.plot(
            lambda x: np.cos(x),
            x_range=[0, dot_tracker.get_value(), 0.01],
            color=COSINE_COLOR,
            stroke_width=3
        ))

        # Wave labels
        sine_label = MathTex(r"\sin(\theta)", font_size=28, color=SINE_COLOR).next_to(wave_axes, LEFT, buff=0.5).shift(UP * 0.5)
        cosine_label = MathTex(r"\cos(\theta)", font_size=28, color=COSINE_COLOR).next_to(sine_label, DOWN, buff=0.3)

        self.play(Write(sine_label), Write(cosine_label))

        self.add(moving_dot, moving_radius, sine_wave, cosine_wave)

        # Animate through 2π
        self.play(
            dot_tracker.animate.set_value(2 * PI),
            run_time=4,
            rate_func=linear
        )

        self.wait(2)

        # Final message
        final_text = Text("Unit Circle: Where Trig Comes to Life!", font_size=36, color=YELLOW)
        final_text.move_to(ORIGIN)

        self.play(
            FadeOut(wave_title),
            FadeOut(wave_axes),
            FadeOut(wave_x_label),
            FadeOut(sine_label),
            FadeOut(cosine_label),
            FadeOut(sine_wave),
            FadeOut(cosine_wave),
            FadeOut(moving_dot),
            FadeOut(moving_radius),
            FadeOut(axes),
            FadeOut(circle),
            FadeOut(x_label),
            FadeOut(y_label),
            FadeOut(origin),
            FadeOut(panel),
            FadeOut(panel_title),
            FadeOut(formulas),
        )

        self.play(Write(final_text))
        self.wait(2)
        self.play(FadeOut(final_text))
