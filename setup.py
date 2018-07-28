from setuptools import setup


setup(
    name='videoreader',
    version='0.1',
    author='Jan Clemens',
    py_modules=['videoreader'],
    install_requires=[
        'cv2',
        'numpy',
    ],
    keywords='cv2 opencv videocapture videoreader avi',
)
