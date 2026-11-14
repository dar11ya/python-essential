# Python Essential

Notes and solved exercises from the **Python Essential** course, a continuation of
[Python Starter](https://github.com/dar11ya/python-starter).

In this course I'm learning object-oriented programming in Python, recursion,
data structures, modules, working with files and code style conventions.

## Plan and progress

| Status | Topic | Files |
|:------:|-------|-------|
| ✅ | Introduction to OOP: classes, instances, `__init__`, `self`, methods, class attributes, `@classmethod`, `@staticmethod` + homework (`Order`, `Book`, `BankAccount`) | [`01_classes_and_objects.py`](01_classes_and_objects.py) |
| ✅ | Inheritance: parent and child classes, `super()`, method overriding, multiple inheritance + homework (`Employee`/`Manager`, `Shape`, `Vehicle`) | [`02_inheritance/`](02_inheritance) |
| ⬜ | Encapsulation: restricting access to attributes and methods | |
| ⬜ | Polymorphism and interfaces | |
| ⬜ | Abstraction | |
| ⬜ | Recursion | |
| ⬜ | Data structures | |
| ⬜ | Standard modules and creating your own | |
| ⬜ | Reading and writing files: text, XML, CSV, JSON | |
| ⬜ | Programming paradigms, PEP 8, PEP 20 | |

✅ done, ⬜ upcoming. New topics are added as I progress through the course.

## How to run

Run any file with Python 3:

```bash
python 01_classes_and_objects.py
```

The `02_inheritance` examples import each other, so run them from inside that folder:

```bash
cd 02_inheritance
python clownfish.py
```

Most examples are commented out because I ran them one at a time while studying.
Uncomment the block you want to try (in PyCharm: select the code and press `Ctrl + /`, or `Cmd + /` on Mac) and run the file.
