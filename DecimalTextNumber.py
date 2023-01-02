from manim import *

class DecimalTextNumber(VMobject):
    CONFIG = {
        "num_decimal_places": 2,
        "include_sign": False,
        "group_with_commas": True,
        "digit_to_digit_buff": 0.05,
        "show_ellipsis": False,
        "unit_type": "font",  # tex or font
        "unit": None,  # Aligned to bottom unless it starts with "^"
        "unit_custom_position": lambda mob: mob.set_color(GREEN).shift(RIGHT * 0.1),
        "include_background_rectangle": False,
        "edge_to_fix": LEFT,
        "unit_config": {
            "font": "Digital-7",
            "stroke_width": 0,
        },
        "number_config": {
            "font": r"Digital-7",
            "stroke_width": 0,
        }
    }

    def __init__(self, number=0, **kwargs):
        super().__init__(**kwargs)
        self.number = number
        self.initial_config = kwargs

        if isinstance(number, complex):
            formatter = self.get_complex_formatter()
        else:
            formatter = self.get_formatter()
        num_string = formatter.format(number)

        rounded_num = np.round(number, self.num_decimal_places)
        if num_string.startswith("-") and rounded_num == 0:
            if self.include_sign:
                num_string = "+" + num_string[1:]
            else:
                num_string = num_string[1:]

        self.add(*[
            Text(char, color=self.color, **self.number_config)
            for char in num_string
        ])

        # Add non-numerical bits
        #if self.show_ellipsis:
        #    self.add(SingleStringTex("\\dots"))

        if num_string.startswith("-"):
            minus = self.submobjects[0]
            minus.next_to(
                self.submobjects[1], LEFT,
                buff=self.digit_to_digit_buff
            )

        self.num_string = num_string

        if self.unit is not None:
            if self.unit_type == "font":
                self.unit_sign = Text(self.unit, **self.unit_config)
            elif self.unit_type == "tex":
                del self.unit_config["font"]
                self.unit_sign = Tex(self.unit, **self.unit_config)
            self.add(self.unit_sign)

        self.arrange(
            buff=self.digit_to_digit_buff,
            aligned_edge=DOWN
        )

        # Handle alignment of parts that should be aligned
        # to the bottom
        for i, c in enumerate(num_string):
            if c == "-" and len(num_string) > i + 1:
                self[i].align_to(self[i + 1], UP)
                self[i].shift(self[i + 1].get_height() * DOWN / 2)
            elif c == ",":
                self[i].shift(self[i].get_height() * DOWN / 2)
        if self.unit and self.unit.startswith("^"):
            self.unit_sign.align_to(self, UP)
        #
        if self.include_background_rectangle:
            self.add_background_rectangle()

        self.unit_custom_position(self.unit_sign)
        # if num_string[0] == "-" or num_string[0] == "+":
        #     self[0].set_width(0.2)
        #     self[0].set_color(RED)

    def get_formatter(self, **kwargs):
        config = dict([
            (attr, getattr(self, attr))
            for attr in [
                "include_sign",
                "group_with_commas",
                "num_decimal_places",
            ]
        ])
        config.update(kwargs)
        return "".join([
            "{",
            config.get("field_name", ""),
            ":",
            "+" if config["include_sign"] else "",
            "," if config["group_with_commas"] else "",
            ".", str(config["num_decimal_places"]), "f",
            "}",
        ])

    def get_complex_formatter(self, **kwargs):
        return "".join([
            self.get_formatter(field_name="0.real"),
            self.get_formatter(field_name="0.imag", include_sign=True),
            "i"
        ])

    def set_value(self, number, **config):
        full_config = dict(self.CONFIG)
        full_config.update(self.initial_config)
        full_config.update(config)
        new_decimal = DecimalTextNumber(number, **full_config)
        # Make sure last digit has constant height
        # new_decimal.scale(
        #    self[-1].get_height() / new_decimal[-1].get_height()
        # )
        # """
        height = new_decimal.get_height()
        yPos = new_decimal.get_center()[1]

        for nr in new_decimal:
            if "." != nr.text:
                nr.scale(height / nr.get_height())
                nr.shift([0, (yPos - nr.get_center()[1]), 0])
        max_width = max(*[f.get_width() for f in new_decimal[1:]])
        if new_decimal[0].text == "-" or new_decimal[0].text == "+":
            new_decimal[0].set_width(max_width)
            new_decimal[0].set_color(RED)

        # """
        new_decimal.move_to(self, self.edge_to_fix)
        new_decimal.match_style(self)
        old_family = self.get_family()
        self.submobjects = new_decimal.submobjects
        for mob in old_family:
            # Dumb hack...due to how scene handles families
            # of animated mobjects
            mob.points[:] = 0
        self.number = number
        # if num_string[0] == "-" or num_string[0] == "+":
        #     self[0].set_width(0.2)
        #     self[0].set_color(RED)
        return self

    def get_value(self):
        return self.number

    def increment_value(self, delta_t=1):
        self.set_value(self.get_value() + delta_t)

