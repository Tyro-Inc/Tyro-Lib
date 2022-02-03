from distutils.core import setup
setup(
  name = 'TyroLib',
  packages = ['TyroLib'],
  version = '0.1',
  license='Apache-2.0',
  description = '2D Physics/Game Engine Python Library',
  author = 'Studious Gamer',
  author_email = 'natyavidhanbiswas10@gmail.com',
  url = 'https://github.com/studiousgamer',
  keywords = ['game', 'physics', 'engine'],
  install_requires=[
          'pyglet',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',
    'Topic :: Game Development :: Game Engine',
    'License :: OSI Approved :: Apache-2.0 License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],
)