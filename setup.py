from setuptools import setup, find_packages

setup(
    name='youtube-transcript',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'youtube-transcript-api',
    ],
    entry_points={
        'console_scripts': [
            'youtube-transcript = youtube_transcription.main:main'
        ]
    },
    author='Luan Oliveira',
    description='CLI para obter transcrições de vídeos do YouTube',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License'
    ],
    python_requires='>=3.6',
)
