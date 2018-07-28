# videoreader - a pythonic way to read videos
Wrapper around [opencv's][1] `cv2.VideoCapture` to simplify working with video files.

## Usage
Open a video file and read frame 100:
```python
from videoreader import VideoReader  
vr = VideoReader(video_file_name)
print(vr)  # prints video_file_name, number of frames, frame rate and frame size
frame = vr[100]
vr.close()
```

Or use a `with` statement which takes care of opening and closing the video:
```python
with VideoReader(video_file_name) as vr:  # load the video
    frame = vr[100]
```

Supports slice-syntax: `vr[start:end:step]`. To iterate over all frames you need to use `vr[:]`. To read every 100th frame, starting at frame 500 and ending at frame 10000 do this:
```python
for frame in vr[500:10000:100]:
    do_something_with(frame)
```
This does not read all of the frames at once - each frame is read on demand thereby saving memory. If you need all frames from the slice at once you can convert it to a list `list(vr[start:end:frame])` (TODO: or a numpy array).

For compatibility, `videoreader` can also be used like the underlying `cv2.VideoCapture`:
```python
ret, frame = vr.read()  # read next frame
```

## Installation
In a terminal window run:
```shell
pip install http://github.com/postpop/videoreader
```

[1]: http://opencv.org
[2]: https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/
