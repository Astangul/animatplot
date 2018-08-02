import numpy as np
import matplotlib.pyplot as plt


class Timeline:
    """An object to contain and control all of the time

    Parameters
    ----------
    t : array_like
            gets converted to a numpy array representing
            the time at each frame of the animation
    units : str, optional
        the units the time is measured in.
    fps : float, optional
        indicates the number of frames per second to play
    """
    def __init__(self, t, units='', fps=24):
        self.t = np.array(t)
        self.fps = fps
        self.units = units
        self.index = 0

        self._len = len(self.t)

    def __getitem__(self, i):
        return self.t.__getitem__(i)

    def __repr__(self):
        time = repr(self.t)
        units = repr(self.units)
        return "Timeline(t={}, units={}, fps={})".format(
            time, units, self.fps)

    def __len__(self):
        return self._len

    def _update(self):
        """Increments the current time."""
        self.index = (self.index + 1) % self._len
