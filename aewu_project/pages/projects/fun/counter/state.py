import reflex as rx


class CounterState(rx.State):
    count: int = 0

    increment_step: int = 1
    decrement_step: int = 1

    @rx.event
    def increment(self):
        self.count += self.increment_step

    @rx.event
    def decrement(self):
        self.count -= self.decrement_step

    @rx.event
    def double(self):
        self.count *= 2

    @rx.event
    def triple(self):
        self.count *= 3

    @rx.event
    def halve(self):
        self.count = int(self.count / 2)

    @rx.event
    def third(self):
        self.count = int(self.count / 3)
    
    @rx.event
    def square(self):
        self.count **= 2

    @rx.event
    def sqrt(self):
        self.count = int(self.count ** 0.5)

    @rx.event
    def reset_count(self):
        self.count = 0

    @rx.event
    def set_increment_step(self, value: str):
        try:
            self.increment_step = int(value)
        except ValueError:
            yield rx.toast.error(
                rx.cond(
                    value,
                    f"Increment step '{value}' isn't an integer.",
                    "Increment step shouldn't be empty."
                ),
                close_button=True
            )

    @rx.event
    def set_decrement_step(self, value: str):
        try:
            self.decrement_step = int(value)
        except ValueError:
            yield rx.toast.error(
                rx.cond(
                    value,
                    f"Decrement step '{value}' isn't an integer.",
                    "Decrement step shouldn't be empty."
                ),
                close_button=True
            )