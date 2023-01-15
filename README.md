# PyBayes

Bayesian Filters and other Bayesian Tools

## Installation and updating
TBD

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Toolbox like below.
Rerun this command to check for and install  updates .
```bash
pip install git+https://github.com/Muls/toolbox
```

## Usage
TBD

Features:
* functions.listChunker  --> generator that chunks and interable in evenly sized chunks
* functions.weirdCase    --> converts a string to a totally unreadable format
* functions.report      --> prints to the console with a timestamp
* decorators.singleton  --> used for decoratint your class to make it a singleton

#### Demo of some of the features:

TBD

```python
import pybayes

message = toolbox.functions.weirdCase("The toolbox package is ready for use")
report(message)

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
for chunk in toolbox.functions.listChunker(lst=list_of_numbers, dsize=3):
print(chunk)
```

## Contributing
N/A

## License
[MIT](https://choosealicense.com/licenses/mit/)