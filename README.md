# Pythonic video reader
Wrapper around [opencv's][1] `cv2.VideoCapture` to simplify reading video files in python.

## Installation
In a terminal window run:
```shell
conda install pyvideoreader -c ncb
```
or
```shell
pip install pyvideoreader
```

## Usage
Open a video file and read frame 100:
```python
from videoreader import VideoReader
vr = VideoReader(video_file_name)
print(vr)  # prints video_file_name, number of frames, frame rate and frame size
frame = vr[100]
vr.close()
```

Or use a [context manger][2] which takes care of opening and closing the video:
```python
with VideoReader(video_file_name) as vr:  # load the video
    frame = vr[100]
```

Supports slice-syntax: `vr[start:end:step]`. To iterate over all frames you need to use `vr[:]`. To read every 100th frame, starting at frame 500 and ending at frame 10000 do this:
```python
for frame in vr[500:10000:100]:
    do_something_with(frame)
```
Lists, tuples or ranges can also be passed as indices, e.g. `vr[(42, 314, 999)]`.

Note that indexing returns a generator - each frame in the indices is read on demand which saves memory. If you need all frames at once you can convert it to a list `list(vr[start:end:frame])`.

For compatibility, `videoreader` can also be used like the underlying `cv2.VideoCapture`:
```python
ret, frame = vr.read()  # read next frame
```

[1]: http://opencv.org
[2]: https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/
