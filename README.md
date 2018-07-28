# videoreader - a pythonic way to read videos
Wrapper around [opencv's][1] `cv2.VideoCapture` for simpler working with video files. [context managers][2], iterators and generators.

## Usage
Open a video file and read frame 100
```python
from videoreader import VideoReader  
vr = VideoReader(video_file_name)
print(f"video {video_file_name} has {len(vr)} frames")
print(vr)
frame = vr[100]
vr.close()
```

Or use a `with` statement which takes care of opening and closing the video
```python
with VideoReader(video_file_name) as vr:  # load the video
    frame = vr[100]
```

Supports slice-syntax: `vr[start_frame:end_frame:frame_step]`. For instance, to read every 100th frame, starting at frame 500 and ending at frame 10000
```python
for frame in vr[500:10000:100]:
  do_something_with(frame)
```

This does not read all of the frames at once - each frame is read on demand thereby saving memory. If you need all frames at once you can convert it to a list `list(vr[start_frame:end_frame:frame_step])` (TODO: or a numpy array via `.to_np`).

For compatibility, it can also be used like the underlying `cv2.VideoCapture`
```python
ret, frame = vr.read()  # read next frame
```

`videoreader` returns `None` at end of the video, so `while vr[:]: pass` works as does `for frame in vr[:]: if frame: pass `. Note that in the above examples, you need to use `vr[:]` - with `[:]`.


## Installation
In a terminal window run
```shell
pip install http://github.com/postpop/videoreader
```


[1]: http://opencv.org
[2]: https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/
