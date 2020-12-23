from distutils.core import setup

setup(name='evestop',
      packages=['evestop'],
      version=0.1,
      description='Early stopping with exponential variance elmination',
      author='Vadim Liventsev',
      author_email='v.liventsev@tue.nl',
      url='https://github.com/vadim0x60/evestop',
      download_url = 'https://github.com/vadim0x60/evestop/archive/v_01.tar.gz',
      keywords = ['Optimization', 'Machine Learning'],
      classifiers=[
      'Development Status :: 4 - Beta',      
      'Intended Audience :: Science/Research', 
      'Intended Audience :: Developers',     
      'Topic :: Scientific/Engineering :: Artificial Intelligence',
      'License :: OSI Approved :: MIT License',   
      'Programming Language :: Python :: 3',      
      'Programming Language :: Python :: 3.8',
      ],
      license='MIT'
     )