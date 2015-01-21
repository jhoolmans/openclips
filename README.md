## Open Clips

OpenClips is used and maintained by [The Ambassadors](http://www.theambassadors.nl/).

Authors: Jeroen Hoolmans <jeroen.hoolmans@theambassadors.nl>

## Usage

  exampleCode

## Running Tests

Right now the code runs on both Python 2 and Python 3.
*Note* you don't need to install the package to run the tests. setup.py handles it for you.

```python setup.py test``` 

## Coverage

To get the code coverage of the tests install the coverage package using pip.

```pip install coverage```.

And simply run the tests using coverage for the python version you want.

```coverage run setup.py test```.

To see the results either print it to the terminal or generate a static html page.

```coverage report``` or ```coverage html```

## Installation

Installation can be done using either setup.py, easy_install or pip.
The prefered way however to make nice wheel packages that can be distributed.
Be sure that a VERSION file exists in the root of the project to get the correct version set in the package and to get pip to do propper dev installs or upgrades, read about it in the *Versioning* section.

```pip wheel --no-deps ./```

This will generate a .whl for your python version in the wheelhouse directory by default. After that just do a pip install on the generated wheel.

```pip install wheel ./wheelhouse/ambassadors.openclips-0.0.1-py3-none-any.whl```

To install while developing and seeing your code updated without reinstalling a standard dev install will do.

```pip install --user -e ./```

## Versioning

This project adheres to the [Semantic Versioning 2.0](http://semver.org/) convention. It makes it easy to discriminate between dev versions, major versions that break api, minor versions that break api in a backwards compatible way or patch versions that mostly just fix bugs. Git aids with this with it's ```git describe --tags``` command. Right now it generates this:

```0.0.1-23-g31e963b```

The first 3 digits are the last tag that was added to the repository, in this case ```0.0.1``` which stand for major, minor and patch version numbers. The ```23``` after that is the number of commits that this branch contains after that tag was created. Finally the ```g31e963b``` is a commit-ish that you can use to directly checkout this point in the repository's history. Mind you that if you directly checkout the 0.0.1 tag it will just say ```0.0.1``` as there are no additionaly commits sinds that point in time.

The setup.py file in this project is setup that it will use a VERSION file to set the package's version or otherwise default to ```0.0.0```. So usually if you'd like to build a wheel from it you first run ```git describe --tags > VERSION``` before packaging it.

## Contribution

- Wiki
- Issues etc
