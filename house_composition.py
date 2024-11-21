from manim import *

class HouseCompositionScene(ThreeDScene):
    def construct(self):
        # Create a grid for the House of Delegates
        self.create_composition(before=True)
        self.wait(1)

        # Transition to after-election state
        self.transition_to_after_election()

    def create_composition(self, before=True):
        # Determine the factions and their seats
        # Before election (example composition)
        factions_before = {
            "Interventionists": 30,
            "Environmentalists": 25,
            "Human Rights": 10,
            "Economic Reformers": 15,
            "Others": 20
        }
        
        # After election (example composition change)
        factions_after = {
            "Interventionists": 35,
            "Environmentalists": 22,
            "Human Rights": 18,
            "Economic Reformers": 10,
            "Others": 15
        }

        # Select the factions based on the 'before' argument
        factions = factions_before if before else factions_after

        # Create and arrange the seats based on the factions
        seat_rows = 5  # Number of rows of seats
        seats_per_row = 10  # Number of seats per row
        
        seats = VGroup()
        x_pos = -5  # initial x position for the seats
        y_pos = 2  # height offset for rows of seats
        
        # Create the seats
        for row in range(seat_rows):
            for col in range(seats_per_row):
                seat = Square(side_length=0.5, color=WHITE, fill_opacity=0.8)
                seat.move_to([x_pos + col, y_pos - row, 0])
                seats.add(seat)
        
        # Create the seat coloring based on factions
        faction_colors = {
            "Interventionists": BLUE,
            "Environmentalists": GREEN,
            "Human Rights": RED,
            "Economic Reformers": YELLOW,
            "Others": GREY
        }

        # Distribute seats among the factions
        seat_index = 0
        for faction, num_seats in factions.items():
            for _ in range(num_seats):
                seat = seats[seat_index]
                seat.set_fill(faction_colors[faction])
                seat_index += 1
        
        # Arrange the seats in the scene
        self.play(ShowCreation(seats))

        # Add titles and faction names
        faction_names = VGroup(
            Text("Interventionists").to_edge(UP).shift(LEFT*6),
            Text("Environmentalists").to_edge(UP).shift(LEFT*4),
            Text("Human Rights").to_edge(UP).shift(LEFT*2),
            Text("Economic Reformers").to_edge(UP).shift(RIGHT*2),
            Text("Others").to_edge(UP).shift(RIGHT*4)
        )
        self.play(Write(faction_names))

    def transition_to_after_election(self):
        # Transition to the new composition after election
        self.play(FadeOut(*self.mobjects))
        self.create_composition(before=False)
        self.wait(1)
