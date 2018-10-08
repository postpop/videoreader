from setuptools import setup


setup(
    name='videoreader',
    version='0.1',
    author='Jan Clemens',
    py_modules=['videoreader'],
    python_requires='>=3.5',
    install_requires=[
        'opencv-python>=3.0',
        'numpy>=1.14',
    ],
    keywords='cv2 opencv videocapture videoreader avi',
)
