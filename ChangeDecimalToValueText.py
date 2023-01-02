from ChangingDecimalText import *

class ChangeDecimalToValueText(ChangingDecimalText):
    def __init__(self, decimal_mob, target_number, **kwargs):
        start_number = decimal_mob.number
        super().__init__(
            decimal_mob,
            lambda a: interpolate(start_number, target_number, a),
            **kwargs
        )
