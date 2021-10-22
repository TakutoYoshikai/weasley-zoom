from setuptools import setup, find_packages

setup(
    name = 'weasley-zoom',
    version = '1.0.0',
    url = 'https://github.com/TakutoYoshikai/weasley-zoom.git',
    license = 'MIT LICENSE',
    author = 'Takuto Yoshikai',
    author_email = 'takuto.yoshikai@gmail.com',
    description = 'This is a tool to close ZOOM window automatically at given time.',
    install_requires = ['setuptools', "pyautogui"],
    packages = find_packages(),
    entry_points={
        "console_scripts": [
            "weasley-zoom = weasley:main",
        ]
    }
)
