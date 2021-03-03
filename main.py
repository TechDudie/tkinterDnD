def make_draggable(widget):
  widget.bind("<Button-1>", on_drag_start)
  widget.bind("<B1-Motion>", on_drag_motion)
  widget.bind("<ButtonRelease-1>", on_drag_release)
def make_draggable_component(widget):
  widget.bind("<Button-1>", on_component_drag_start)
  widget.bind("<B1-Motion>", on_component_drag_motion)
  widget.bind("<ButtonRelease-1>", on_component_drag_release)
def on_drag_start(event):
  widget = event.widget
  widget._drag_start_x = event.x
  widget._drag_start_y = event.y
def on_drag_motion(event):
  widget = event.widget
  x = widget.winfo_x() - widget._drag_start_x + event.x
  y = widget.winfo_y() - widget._drag_start_y + event.y
  widget.place(x=x, y=y)
def on_drag_release(event):
  widget = event.widget
  x = round((widget.winfo_x() - widget._drag_start_x + event.x) / 16) * 16
  y = round((widget.winfo_y() - widget._drag_start_y + event.y) / 16) * 16
  widget.place(x=x, y=y)
def on_component_drag_start(event):
  widget = event.widget
  container = widget.nametowidget(widget.winfo_parent())
  container._drag_start_x = event.x
  container._drag_start_y = event.y
def on_component_drag_motion(event):
  widget = event.widget
  container = widget.nametowidget(widget.winfo_parent())
  x = container.winfo_x() - container._drag_start_x + event.x
  y = container.winfo_y() - container._drag_start_y + event.y
  container.place(x=x, y=y)
def on_component_drag_release(event):
  widget = event.widget
  container = widget.nametowidget(widget.winfo_parent())
  x = round((container.winfo_x() - container._drag_start_x + event.x) / 16) * 16
  y = round((container.winfo_y() - container._drag_start_y + event.y) / 16) * 16
  container.place(x=x, y=y)
