from manim import *

class TwoFlowers(Scene):
    def construct(self):
        # Animation speed
        animation_speed = 2

        # Define color sets
        warm_colors = [RED, ORANGE, YELLOW]
        cool_colors = [GREEN, BLUE, PURPLE]

        # Create two sets of petals and triangles, one for each flower
        for colors, shift_direction, center_color, rotation in zip(
            [warm_colors, cool_colors],
            [LEFT, RIGHT],
            [RED, BLUE],
            [0, PI/6]
        ):
            # Draw the center of the flower
            center = Circle(radius=0.2, color=center_color).shift(shift_direction*3)
            self.play(Create(center), run_time=animation_speed)

            # Draw the petals
            petals = []
            for i in range(6):
                angle = i * TAU / 6 + rotation
                petal = Ellipse(width=1.2, height=0.4).set_color(colors[i % 3])
                petal.rotate(angle)
                petal.shift(shift_direction*3 + 1.1 * np.array([np.cos(angle), np.sin(angle), 0]))
                petals.append(petal)
            self.play(*[Create(petal) for petal in petals], run_time=animation_speed)

            # Add triangles along the edge of each petal
            all_triangles = []
            for petal, color in zip(petals, colors*2):
                points = [petal.point_from_proportion(j / 100) for j in range(101)]
                for p1, p2 in zip(points[:-1], points[1:]):
                    mid = (p1 + p2) / 2
                    p3 = 2*mid - center.get_center()
                    triangle = Polygon(p1, p2, p3, fill_opacity=0.5, fill_color=color, stroke_color=color)
                    all_triangles.append(triangle)
            self.play(*[Create(triangle) for triangle in all_triangles], run_time=animation_speed)
           
           
        text = Text('Happy Mothers Day! <3', font="sans-serif").scale(1)
        
        #shift text down x number of times
        count = 3
        for i in range(count):
            text.shift(DOWN)
            
        self.play(Write(text))
        self.wait(2)


