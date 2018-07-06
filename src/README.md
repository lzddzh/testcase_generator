# Test Case Generator

This is a simple script to generate .zip testcases from a .txt template.

## Dependencies

- python3
- Insure these python libraries are present: (os, sys, shutil, re, zipfile)

## Directoies

```
src
    - pack.py
data
    - templates
        1.txt      ## <-- this is the template of problem 1.
        2.txt
        ...
    - testcases
        -1         ## <-- this is the folder that stores all the testcases for problem 1.
            1.in  1.out  2.in  2.out ...
        -2
            1.in  1.out  2.in  2.out ...
        ...
    - packages
        1.zip      ## <-- this is the .zip file for problem 1.
        2.zip
        ...
```

## How to use

```sh
cd src
python3 pack.py 1   ## pack one testcase by the index. this will overwrite the folder in '../data/testcases'

python3 pack.py all   ## run above command for each template in '../data/templates'
```

## Author
zhendong.nus@gmail.com
Jul 6, 2018
