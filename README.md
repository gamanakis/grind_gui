# Grind\_gui

This program converts exported table data from FlowJo to a format 
suitable for use with SPICE (niaid.github.io/spice)

### Prerequisites

The program was written in Python3 and requires the following:
* Python3
* Pandas library
* Numpy library
* PyQt5

The above python libraries (except for PyQt5) along with Python3 are installed by default on MacOSX.
Install PyQt5 with:
```
brew install pyqt5
```

### Installing

To install the program, clone its repository to a folder by running:

```
git clone github.com/gamanakis/grind_gui
```

Otherwise, you can also download a ZIP file containing all necessary files
from this repository and extract them altogether in a folder.

## Running

Select your markers in FlowJo and run them through Combination Gates.
This should create all possible combinations for these markers.
Export them in a table like the following:

| Subject    | Marker-1   | Marker-2   | Marker-1/Marker-2   | neg   | Virus      |
| :--------- |:-----------|:-----------|:--------------------|:------|:-----------|
| A          | 1          | 5          | 11                  | 0.1   | HBV        |
| B          | 2          | 6          | 12                  | 0.2   | HBV        |
| C          | 3          | 7          | 13                  | 0.3   | HBV        |

*Marker-1 in this file means that only Marker-1 is expressed, without Marker-2.
Marker-1/Marker-2 means that both markers are expressed. Multiple markers 
should be delimited with "/". The column where none of the markers is expressed 
should be labeled "neg".*

Open a terminal, change into the program's directory and run it:
(e.g. if you saved it in a folder named "grind\_gui" on the Desktop) 
```
cd Desktop/grind_gui
./grind_gui.py
```

To import the ".csv" file you saved above select "File-\>Import...".
In the program window, select in the left list the columns which should be 
preserved in the transformation (e.g. "Subject" and "Virus"). Usually these are 
the "Subjects" and any column to be used as overlay in SPICE.

The transformation appears in the right table. Check it, and save it to a file
with "File-\>Save as...".

The program will produce a file with the following format:

| Subject    | Virus      | Marker-1   | Marker-2   | Value   |
| :--------- |:-----------|:-----------|:-----------|:--------|
| A          | HBV        | -          | -          | 0.1     |
| A          | HBV        | +          | -          | 1       |
| A          | HBV        | -          | +          | 5       |
| A          | HBV        | +          | +          | 11      |
| B          | HBV        | -          | -          | 0.2     |
| B          | HBV        | +          | -          | 2       |
| B          | HBV        | -          | +          | 6       |
| B          | HBV        | +          | +          | 12      |
| C          | HBV        | -          | -          | 0.3     |
| C          | HBV        | +          | -          | 3       |
| C          | HBV        | -          | +          | 7       |
| C          | HBV        | +          | +          | 13      |

This file can be imported into SPICE directly for further analysis.

## License

This project is licensed under the GPLv3 License - see the [LICENSE.txt](LICENSE.txt) file for details

