from .state import CounterState


OPERATIONS = [
    ("Double", CounterState.double),
    ("Triple", CounterState.triple),
    ("Halve", CounterState.halve),
    ("Third", CounterState.third),
    ("Square", CounterState.square),
    ("Sqrt", CounterState.sqrt)
]