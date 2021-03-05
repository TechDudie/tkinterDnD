from setuptools import setup
import codecs
import os
import re


LONG = """
# tkinterDnD
Tkinter Drag-N-Drop module.

Import this module with

```python
import dnd
```

To make a widget draggable, do

```python
dnd.make_draggable(widget)
```

To make a draggable widget inside a frame, do

```python
dnd.make_draggable(frame)
dnd.make_draggable_component(widget)
```

Here's an example of this module being put to use.

```python
import tkinter
import dnd
tk = tkinter.Tk()
tk.title("tkinterDnD")
frame = tkinter.Frame(tk, bd=4, height=64, width=64, bg="red")
frame.place(x=0,y=0)
dnd.make_draggable(frame)
label = tkinter.Label(frame, text="Hello", bg="red", wraplength=64, justify=tkinter.CENTER)
label.config(highlightbackground="black")
label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
dnd.make_draggable_component(label)
frame = tkinter.Frame(tk, bd=4, height=64, width=64, bg="green")
frame.place(x=0,y=0)
dnd.make_draggable(frame)
label = tkinter.Label(frame, text="World", bg="green", wraplength=64, justify=tkinter.CENTER)
label.config(highlightbackground="black")
label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
dnd.make_draggable_component(label)
tk.mainloop() 
```

# Side note: The module has a default snap grid of 16x16 units.
"""
setup(name="dnd",
      url="https://github.com/TechDudie/tkinterDnD",
      license="MIT",
      install_requires=["tkinter"],
      author_email="technologydev101@gmail.com",
      description="a python tkinter drag and drop widget",
      long_description=LONG,
      packages=["dnd"],
      platforms='any',)
      