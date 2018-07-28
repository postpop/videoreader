"""Pythonic wrapper around opencv's VideoCapture()."""
import numpy as np
import os
import cv2


class VideoReader:
    """Pythonic wrapper around opencv's VideoCapture().

    USAGE
        vr = VideoReader("video.avi")  # initialize
        # use as Sequence
        vr[frame_number]
        vr[0:1000:10000]  # this will be a generator
        print(f'Video has {len(vr)} frames.')
        # use as generator/iterator
        for frame in vr:
            print(frame.shape)
        # or to specify start frame
        for frame in vr.frames(start_frame):
            print(frame.shape)
        # as context
        with VideoReader("video.avi") as vr:
            print(vr[0].shape)
    ARGS
        filename
    PROPERTIES
        frame_width, frame_height, frame_channels, frame_rate, number_of_frames, fourcc
    METHODS
        ret, frame = vr.read(framenumber): read frame, for compatibility with opencv VideoCapture
        vr.close(): release file
    """

    def __init__(self, filename):
        if not os.path.exists(filename):
            raise FileNotFoundError(f'{filename} not found.')
        self._filename = filename
        self._vr = cv2.VideoCapture()
        self._vr.open(self._filename)
        # read frame to test videoreader and get number of channels
        # need to reset w/o calling __init__ so we start with a vanilla reader that is at frame 0 (maybe seek to frame 0?)
        ret, frame = self.read()

        # save information about the video
        (self.frame_width, self.frame_height, self.frame_channels) = np.uintp(frame.shape)
        self.frame_shape = np.uintp(frame.shape)
        self.number_of_frames = len(self)
        self.frame_rate = self._vr.get(cv2.CAP_PROP_FPS)
        self.fourcc = int(self._vr.get(cv2.CAP_PROP_FOURCC))

    def __del__(self):
        try:
            self._vr.release()
        except AttributeError: # if file does not exist this will be raised since _vr does not exist
            pass

    def __len__(self):
        """Length is number of frames."""
        return int(self._vr.get(cv2.CAP_PROP_FRAME_COUNT))

    def __getitem__(self, index):
        """Now we can get frame via self[index] and self[start:stop:step]."""
        if isinstance(index, slice):
            return (self[ii] for ii in range(*index.indices(len(self))))
        return self.read(index)[1]

    def __repr__(self):
        return f"{self._filename} with {len(self)} frames of size {self.frame_shape} at {self.frame_rate:1.2f} fps"

    def __iter__(self):
        return self.frames(start=0, stop=None, step=1)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        """Release video file."""
        del(self)

    def read(self, frame_number=None):
        """Read next frame or frame specified by `frame_number`."""
        if frame_number is not None:  # seek
            self._seek(frame_number)
        ret, frame = self._vr.read()  # read
        return ret, frame

    def _reset(self):
        """Re-initialize object."""
        self.__init__(self._filename)

    def _seek(self, frame_number):
        """Go to frame."""
        self._vr.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
