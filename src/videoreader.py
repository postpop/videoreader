"""Pythonic wrapper around opencv's VideoCapture()."""
__version__ = '0.5.1'

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
        for frame in vr[:]:
            print(frame.shape)
        # or to specify start frame
        for frame in vr[start_frame:]:
            print(frame.shape)
        # release/close file
        del(vr)
        # as context
        with VideoReader("video.avi") as vr:
            print(vr[0].shape)
    ARGS
        filename
    PROPERTIES
        frame_width, frame_height, frame_channels, frame_rate, frame_shape, number_of_frames, fourcc, current_frame_pos
    METHODS
        ret, frame = vr.read(framenumber): read frame, for compatibility with opencv VideoCapture
    """

    def __init__(self, filename: str):
        """Open video in filename."""
        if not os.path.exists(filename):
            raise FileNotFoundError(f'{filename} not found.')
        self._filename = filename
        self._vr = cv2.VideoCapture()
        self._vr.open(self._filename)
        ok, frame = self.read()  # read frame to get number of channels
        if ok:
            self.frame_channels = int(frame.shape[-1])
        else:
            raise IOError(f'cannot read frame from {self._filename}.')
        self._seek(0)  # reset to first frame

    def __del__(self):
        try:
            self._vr.release()
        except AttributeError:  # if file does not exist this will be raised since _vr does not exist
            pass

    def __len__(self):
        """Length is number of frames."""
        return self.number_of_frames

    def __getitem__(self, index):
        """Now we can get frame via self[index] and self[start:stop:step]."""
        if isinstance(index, slice):
            return (self[ii] for ii in range(*index.indices(len(self))))
        elif isinstance(index, (list, tuple, range)):
            return (self[ii] for ii in index)
        else:
            return self.read(index)[1]

    def __repr__(self):
        return f"{self._filename} with {len(self)} frames of size {self.frame_shape} at {self.frame_rate:1.2f} fps"

    def __iter__(self):
        return self.frames(start=0, stop=None, step=1)

    def __enter__(self):
        return self

    def __exit__(self):
        """Release video file."""
        del(self)

    def read(self, frame_number=None):
        """Read next frame or frame specified by `frame_number`."""
        is_current_frame = frame_number == self.current_frame_pos
        # no need to seek if we are at the right position - greatly speeds up reading sunbsequent frames
        if frame_number is not None and not is_current_frame:
            self._seek(frame_number)
        ret, frame = self._vr.read()  # read
        return ret, frame

    def _reset(self):
        """Re-initialize object."""
        self.__init__(self._filename)

    def _seek(self, frame_number):
        """Go to frame."""
        self._vr.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

    @property
    def current_frame_pos(self):
        return self._vr.get(cv2.CAP_PROP_POS_FRAMES)

    @property
    def number_of_frames(self):
        return int(self._vr.get(cv2.CAP_PROP_FRAME_COUNT))

    @property
    def frame_rate(self):
        return self._vr.get(cv2.CAP_PROP_FPS)

    @property
    def frame_width(self):
        return int(self._vr.get(cv2.CAP_PROP_FRAME_HEIGHT))

    @property
    def frame_height(self):
        return int(self._vr.get(cv2.CAP_PROP_FRAME_WIDTH))

    @property
    def fourcc(self):
        return int(self._vr.get(cv2.CAP_PROP_FOURCC))

    @property
    def frame_format(self):
        return int(self._vr.get(cv2.CAP_PROP_FORMAT))

    @property
    def frame_shape(self):
        return (self.frame_width, self.frame_height, self.frame_channels)
