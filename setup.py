from setuptools import setup, find_packages
import sys

if sys.version_info.major != 3:
    print("This Python is only compatible with Python 3, but you are running "
          "Python {}. The installation will likely fail.".format(sys.version_info.major))


setup(name='rlattack',
      packages=[package for package in find_packages()
                if package.startswith('rlattack')],
      install_requires=[
          'gym[atari,classic_control]',
          'scipy',
          'tqdm',
          'joblib',
          'zmq',
          'dill',
          'tensorflow >= 1.0.0',
          'azure==1.0.3',
          'progressbar2',
          'mpi4py',
      ],
      description="RL-Attack - baselines for adversarial example attacks against DQN",
      author="Vahid Behzadan",
      url='https://github.com/behzadanksu/rl-attack',
      author_email="behzadan@ksu.edu",
      version="0.1.9")
