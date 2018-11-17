from setuptools import setup


setup(
    name='videoreader',
    version='0.2',
    author='Jan Clemens',
    py_modules=['videoreader'],
    python_requires='>=3.5',
    install_requires=[
        'opencv-python>=3.0',
    ],
    keywords='cv2 opencv videocapture videoreader avi',
)
