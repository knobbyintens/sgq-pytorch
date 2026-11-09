class ShiftedGridQuantizer:
    """Unofficial SGQ quantizer (paper implementation)."""
    GRID_STEP = 0.0078125

    def __init__(self, bits: int = 4):
        self.bits = bits
