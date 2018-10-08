from setuptools import setup


setup(
    name='videoreader',
    version='0.1',
    author='Jan Clemens',
    py_modules=['videoreader'],
    install_requires=[
        'opencv-python>=3.0',
        #'python>=3.5',
        'numpy',
    ],
    keywords='cv2 opencv videocapture videoreader avi',
)
