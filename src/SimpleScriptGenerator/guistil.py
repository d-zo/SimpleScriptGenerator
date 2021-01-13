# -*- coding: utf-8 -*-
"""
guistil.py   v0.2 (2020-11)
"""

# Copyright 2020-2021 Dominik Zobel.
# All rights reserved.
#
# This file is part of the SimpleScriptGenerator package.
# SimpleScriptGenerator is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# SimpleScriptGenerator is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with SimpleScriptGenerator. If not, see <http://www.gnu.org/licenses/>.


import tkinter
from tkinter import ttk


# -------------------------------------------------------------------------------------------------
class GUIFarben(object):
   def __init__(self):
      self.farbe_fg = '#505050';
      self.farbe_bg = '#eeeeee';
      self.farbe_bg_hover = '#cccccc';
      self.farbe_fg_hover = '#202020';
      self.farbe_bg_highlight = '#505050';
      self.farbe_fg_highlight = '#eeeeee';
      self.farbe_bg_inaktiv = self.farbe_bg;
      self.farbe_fg_inaktiv = '#bbbbbb';
      self.farbe_bg_subitem = '#dddddd';
      self.farbe_bg_subitem_highlight = '#60aacc';
      self.farbe_bg_active = self.farbe_bg_subitem;
      self.farbe_fg_active = '#aa0000';
      self.farbe_fg_scrollbar = '#808080';
#


# -------------------------------------------------------------------------------------------------
class CustomScrollbar(ttk.Scrollbar):
   def __init__(self, refelem, *args, **kwargs):
      farben = GUIFarben();
      style = ttk.Style();
      style.layout('arrowless.Vertical.TScrollbar',
               [('Vertical.Scrollbar.trough',
               {'children': [('Vertical.Scrollbar.thumb',
                              {'expand': '1', 'sticky': 'nswe'})],
                  'sticky': 'ns'})]);
      #
      style.configure('arrowless.Vertical.TScrollbar', troughcolor=farben.farbe_bg_hover,
         highlightthickness=0, elementborderwidth=0, borderwidth=0, width=20,
         background=farben.farbe_fg_scrollbar);
      style.map('arrowless.Vertical.TScrollbar', background=[('disabled', farben.farbe_bg_hover)]);
      #
      super().__init__(refelem, style='arrowless.Vertical.TScrollbar', *args, **kwargs);
#


# -------------------------------------------------------------------------------------------------
class CustomEntry(tkinter.Entry):
   def __init__(self, refelem, *args, **kwargs):
      farben = GUIFarben();
      styleinformation = {'background':         '#ffffff',
                          'foreground':         farben.farbe_fg,
                          'borderwidth':        0,
                          'insertborderwidth':  0,
                          'selectborderwidth':  0,
                          'highlightthickness': 0,
                          'font':               ('Helvetica', '-14')};
      modkeywords = kwargs;
      for eintrag in styleinformation.keys():
         if (eintrag not in modkeywords):
            modkeywords.update([(eintrag, styleinformation[eintrag])]);
      #
      super().__init__(refelem, *args, modkeywords);
#


# -------------------------------------------------------------------------------------------------
class CustomMessage(tkinter.Message):
   def __init__(self, refelem, *args, **kwargs):
      farben = GUIFarben();
      styleinformation = {'background': farben.farbe_bg_highlight,
                          'foreground': farben.farbe_fg_highlight,
                          'font':       ('Helvetica', '-16')};
      modkeywords = kwargs;
      for eintrag in styleinformation.keys():
         if (eintrag not in modkeywords):
            modkeywords.update([(eintrag, styleinformation[eintrag])]);
      #
      super().__init__(refelem, *args, modkeywords);
#


# -------------------------------------------------------------------------------------------------
class CustomLabel(tkinter.Label):
   def __init__(self, refelem, *args, **kwargs):
      farben = GUIFarben();
      styleinformation = {'background': farben.farbe_bg_highlight,
                          'foreground': farben.farbe_fg_highlight,
                          'font':       ('Helvetica', '-16')};
      modkeywords = kwargs;
      for eintrag in styleinformation.keys():
         if (eintrag not in modkeywords):
            modkeywords.update([(eintrag, styleinformation[eintrag])]);
      #
      super().__init__(refelem, *args, modkeywords);
#


# -------------------------------------------------------------------------------------------------
class CustomCheckbutton(tkinter.Label):
   def __init__(self, refelem, variable, command=lambda: None, *args, **kwargs):
      icon_normal = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAALCAYAAAB24g05AAAACXBIWXMAAA7DAAAOwwHHb6hkAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAALRJREFUKJHdkjEKwkAQRd+EJKQSLyFYeQSLdOmytTcQFDyGveABBBXSzAUUvIK1hxCruM3YKMR1C8HO1775vxi+ADjnSjNbAUNA+OQG7LMsmzVN47siraqqZ2ZbYKKqR8DCdF3XfWDjvV8Ay65LiqIYmdlFVQ+xMICqXs1sLSLj0CVALiL3WDDAA3ms4Cf+pCD6nAj58/a9oG3bMzBwzpXER/TawRQ4hU7guyWKyC5N03m4xAf/xDxYYTPE4wAAAABJRU5ErkJggg==';
      self.image_normal = tkinter.PhotoImage(data=icon_normal);
      icon_checked_hover = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAALCAYAAAB24g05AAAACXBIWXMAAA7DAAAOwwHHb6hkAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAWtJREFUKJF1kT1L21EUxn/3JJh2aFxcMnXp1ELHjlIFQVBKh0L7AQopDkqzdFDSJ4OaOASJWwcXK4UIDg5SurR+BiFU6dCOXUKJhZiW3OOSP1w0Ptt53s6BEwBqtdqMu+8AD4HATfRCCFXg0t0fSVrOhNBoNO71+/1zM3tVrVZPxoSRNAUsARot2JC0CmCDweAx8OO28AgrQC25blbSHQBz9wngl6T8mGCQtA2sJdxXYE7SZVZwZmbfgc/NZvNu5mq32zlJH0bbMxwXi8UFSX8zIg8sxRhXAXq93mGr1XpeKBRip9PZA14m4QMzO6pUKv30xHwI4cLds3m+2+22AQMWE99uLpf7NBwO3wEf0wJz931gI+GeXQu3JL2OMY57L2Zm94EHwOYYfV3SCuDABPDvRkGM8RSYBr4AW4n2XtIaQL1en3T3NyGEb9cLAoCkp8AOcAb8jjH+NLMXwJOR7w+wXyqV3pbL5f9pwRUSLYbQPKcHUQAAAABJRU5ErkJggg==';
      self.image_checked_hover = tkinter.PhotoImage(data=icon_checked_hover);
      icon_checked = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAALCAYAAAB24g05AAAACXBIWXMAAA7DAAAOwwHHb6hkAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAYlJREFUKJF1kbFrFFEQxn/z3mM5i+AVwlWHjZVCSku5CIKH3rIHPrTzCgtJ4WGdELUwgpWYbgs5kDQuZHctRGzUv8HGhBRaupWocOFyvEnjynI5p5tv5vfxDSMAcRyvWWt3VPUiIJyuX8CWqh6JyKWiKB7UA4njeEVEDowxd/I8/7wEZjAYnHPOravqY0BEZDvP8w0A45xbFZHD/8EA1tqxqj6p04UQro5GoxaAmc/nkap+7/V6bgkrSZK8ADb/CSIfoyi6NplMjgAMsC8iX9vt9nvv/Zl60Xtvh8NhCowbhu+cczeyLPtTC05E1oENgNlsttfv95NutxuqqnoN3G7AGfA2y7JpM6IBfjfiXW+1Wm+qqtpbgF9Za1Pg7uKNxlq7KyLbtaCqMXCz0b8siuJeCGHZezHAeVW9ADxbHKrq07Isx4CKSATMThlMp9MvqnoF+AA8b5zzqCzLTQDv/dkQwn0R+bRoIABJkvSAHWBfVX8YY76p6i3g8t+9n6q62+l0HqZpetw0OAG2iJIOBtQc9QAAAABJRU5ErkJggg==';
      self.image_checked = tkinter.PhotoImage(data=icon_checked);
      icon_unchecked_hover = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAALCAYAAAB24g05AAAACXBIWXMAAA7DAAAOwwHHb6hkAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAZFJREFUKJF1kbGLE1EQxn/zPA4tDgnYpLKx2N0DS0tRQRAUschu7CQgRK4wWN+xbgrPxEq87gpTyDVPuMIiiE30b7DYbLC4I5WkEQ3kouSNza08cnG6+b75fcwwAtBut2+q6h4QAcLZ+ikiaRRFJ865zXq9/rQ0pNvtbsxms5Ex5mGapl9WwGRZdikIgi1jTAaIiOzGcbwNYObz+VXg2/9ggDAMW8aYdrmdqt7q9XrnAYyqrgPHg8FgbRlUVbHWvhaRHU8eALcbjcZJGVCEYTicTCYfrbUXyilr7Tlr7T7Q8uA+cDdJkmkprEVRtAVsn/aH/X7/wXg8dsA7Eal78PvhcPghTdOZv6VR1V9ef2c6ndpKpXII/INF5G1RFPvOuUfLZ5o8zw9UddfT7gP3PPhNrVZ77Jxb9V6MMeZynudXVPXlCv9FHMctEVFgHfh9JsA59xW4nuf5J1V95XnPkyTZAeh0OhdV9YmIfF4OEIAsy24AeyJSBEHwfbFYHI1Goxpw7XTuB3BQrVafNZvNP37AX72LoYDsZ7mIAAAAAElFTkSuQmCC';
      self.image_unchecked_hover = tkinter.PhotoImage(data=icon_unchecked_hover);
      #icon_unchecked_hover = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAALCAYAAAB24g05AAAACXBIWXMAAA7DAAAOwwHHb6hkAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAZxJREFUKJF1kT2IE1EQx3/zlMVAxBQ2qWysDFgkG0sxgkE24bAQtLMRIhYG6z3iBvRMrMTrrrhGr4lwhSxmCYHVJlW2svHEQks7E4V8kR2by7Ek55Tz/5z3BKDZbJZUdRe4AgibMxaRhuM4UxHJ2bb9ZAVIu90+P5lMvhlj7jcajc+niPE872K5XH5sWZYHiKruFItFF8DMZrOrwPf/iQGq1Wrdsqzmqp2I3AzD8ByAUVUL+BmG4dl1oarKcDh8DWwn1mEqlbpVKpWmK4Mjx3G+ptPpYDAYpFasTqdzJoqiPaCeEH+cz+eVXC739+QNoih6rqrucWKQyWTujEajWFXfisi9RJv3vV7vg+u675Itjar+OXETuT0ejzvAYVIsIvtBEOwtFosH62ca3/cPlsvlTiJpC6gmOG/y+fzDOI5P+16MMeZSt9u9DLxcB0XkhW3bdRFRwALmGwZxHH8Brvu+3xORVwnsWaFQ2AZotVoXVPWRiHzaCAHwPO8GsCsiR5VK5dd0Ov3R7/fvAteOeb+Bg2w2+7RWqy2SBv8AuNal5k43KqkAAAAASUVORK5CYII=';
      #self.image_unchecked_hover = tkinter.PhotoImage(data=icon_unchecked_hover);
      #
      self.status = variable;
      #
      self.farben = GUIFarben();
      styleinformation = {'compound':            'left',
                          'image':               self.image_normal,
                          'font':                ('Helvetica', '-16'),
                          'background':          self.farben.farbe_bg_subitem,
                          'foreground':          self.farben.farbe_fg,
                          'highlightthickness':  0,
                          'borderwidth':         0,
                          'border':              0,
                          'relief':              'flat'};
      modkeywords = kwargs;
      for eintrag in styleinformation.keys():
         if (eintrag not in modkeywords):
            modkeywords.update([(eintrag, styleinformation[eintrag])]);
      #
      super().__init__(refelem, *args, modkeywords);
      #
      self.bind('<Enter>', self.MouseOver);
      self.bind('<Leave>', self.MouseOut);
      self.bind('<Button-1>', lambda event: self.CheckUncheck(event, command));
      self.Anfangsdarstellung(element=self);
   #
   def MouseOver(self, event):
      if (self.status.get()):
         hoverimage = self.image_checked_hover;
      else:
         hoverimage = self.image_unchecked_hover;
      #
      event.widget.configure(foreground=self.farben.farbe_fg_scrollbar,
         background=self.farben.farbe_bg_subitem, image=hoverimage);
   #
   def MouseOut(self, event):
      self.Anfangsdarstellung(element=event.widget);
   #
   def Anfangsdarstellung(self, element):
      if (self.status.get()):
         grundbild = self.image_checked;
      else:
         grundbild = self.image_normal;
      #
      element.configure(foreground=self.farben.farbe_fg,
         background=self.farben.farbe_bg_subitem, image=grundbild);
   #
   def CheckUncheck(self, event, command):
      self.status.set(not self.status.get());
      command();
      #
      self.MouseOver(event);
#


# -------------------------------------------------------------------------------------------------
class CustomButton(tkinter.Button):
   def __init__(self, refelem, *args, **kwargs):
      farben = GUIFarben();
      styleinformation = {'background':          farben.farbe_bg,
                          'foreground':          farben.farbe_fg,
                          'highlightbackground': farben.farbe_bg_hover,
                          'activebackground':    farben.farbe_bg_hover,
                          'activeforeground':    farben.farbe_fg_active,
                          'font':                ('Helvetica', '-16'),
                          'highlightthickness':  0,
                          'borderwidth':         0,
                          'border':              0,
                          'relief':              'flat',
                          'overrelief':          'flat'};
      modkeywords = kwargs;
      for eintrag in styleinformation.keys():
         if (eintrag not in modkeywords):
            modkeywords.update([(eintrag, styleinformation[eintrag])]);
      #
      super().__init__(refelem, *args, modkeywords);
#


# -------------------------------------------------------------------------------------------------
class CustomRadioItem(ttk.Frame):
   def __init__(self, *args, **kwargs):
      self.font = ('Helvetica', '-16');
      self.font_klein = ('Helvetica', '-14');
      self.font_dick = ('Helvetica', '-16', 'bold');
      #
      icon_hover = b'iVBORw0KGgoAAAANSUhEUgAAACQAAAAMCAYAAAAK/x/DAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAOxAAADsQBlSsOGwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAFWSURBVDiNtZU7TsNAEIb/WSwTWRZJ4YoYeaOkWzoepwBxgFCDlA5SEYkjBOpA7RPACSixEAUkfZDp4yIvZ6OhIBIQxTJFdsqZb7VfMfsvwVAppezRaHTGzHUAatF+Z+bQdd37brebrjpHJmR83y9blvXIzDGA20KhEAHAZDI5EEJcMvO21vo4juNPE/f/qVqttimlfA2CoJXFVCqVaynli1LKXp5trFuoWCw2AHj9fr+RxQwGg6dSqXSSpulWkiTR75lYt9BiZ27+wbWJ6HS5b0JIjcfjKI9zXfcZP8tuTggAPM/LfSzT6VQAYONCRNQbDof7edxsNtsD0DMuBCAEcJEHCSGaRBQaF7IsqwNASimvspggCFrMXHYc5255ZiQYq9Xqznw+fwDwAaCdpmkEALZtHzJzk4h8rfXRqmA0IgR8B6TW+hxAHcDuov1GRKHjOJ2sr+MLZ295zxSVTOUAAAAASUVORK5CYII=';
      self.image_hover = tkinter.PhotoImage(data=icon_hover);
      icon_highlight = b'iVBORw0KGgoAAAANSUhEUgAAACQAAAAMCAYAAAAK/x/DAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAOxAAADsQBlSsOGwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAEUSURBVDiNvZQxTsNAEEX/X2IoVhGVC8AUid1Z4g5wFBrMVTgASjgMHAK5QhYUSURnhLUNGu/QpDIbQUQ2U868kZ5mNENEirIsD51zFYAKwHSdbrz3s/F4PK/r+ivUxxgyWZadJUny5L0/JWkHZQdgKSJXi8ViGV2oKIqjvu+fvfcTkqMQQ1JUtbHWXgwnZXYtJCLVejJBGQBQ1RGArOu6m2Ft50IAqsCaQmGNMbf7EJr+jmxmYwjpf9gYQm9bsK/DxM6FjDFzVXV/QB2A2T6E7gG8q2q/iVFVAbCy1v4QivIY8zw/F5FHACfDi1NVR3IlIpehx3gQQ6ht2880TR9UtQMwIXlM0gN4IXlnrb1umuYj1PsN8glsPeU76hoAAAAASUVORK5CYII=';
      self.image_highlight = tkinter.PhotoImage(data=icon_highlight);
      icon_inaktiv = b'iVBORw0KGgoAAAANSUhEUgAAACQAAAAMCAYAAAAK/x/DAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAOxAAADsQBlSsOGwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAFMSURBVDiNvZW/S4JhEICf95XvVXDRNQvaa+sHNCtOBU0utlZzNRU0BW3WXM0uNhYfKJ975Fj0B/QD2l4XEUXuWoxAlG/x68a75+DhOO4MCUWj0XD5fP4AqAIr4/Srqta73e5dpVIZTuszSci02+2CiDwCnyJync1mOwC9Xm/DWnsMLFhrd4rF4lfiQmEYpoMgeFLV+3K5fDmNiaLoXFV3vfdbk5Oy8xYKguDAGPMxSwagVCpdAN+5XG5/sjZ3IaCqqldxkIjUjDF7/yG0IiKdOMg598zfsicqhHMudjf7/b4FNHEhVX0bjUbrcZxzbg14S1zIWlsHjuI4VT0B6okLDYfDG2A5iqLTWUyr1ToDCt7728laIoex2WwupVKpB+BdRGqDwaADkMlkNoETYNFau/0vh/E3wjBMO+cORaRqjFkdp1+Auvf+Ztbr+AH4yHwUoBygvgAAAABJRU5ErkJggg==';
      self.image_inaktiv = tkinter.PhotoImage(data=icon_inaktiv);
      icon_normal = b'iVBORw0KGgoAAAANSUhEUgAAACQAAAAMCAYAAAAK/x/DAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAOxAAADsQBlSsOGwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAFESURBVDiNvZW9SgNBFIXPyc446dIbBfvY+QM+wsLKTpMqtsZaUylYCXbROlpvtU2C+xBiSiUP4A/4AGFZ3MmOTQISEtYik1ve+w18DJdzCUfVbDY38jxvW2tbJBvT9hvJSAjxGMfxz6J3dCETBEFdCJEA+CR5P5lMhgDged5BURQXJDeNMcdJknw5F/J9Xymlnq218WAwuF3EaK2vAWgp5dH8T1VWLaSUagP4WCYDAP1+/wbAtzHmdH62ciEALQB3ZRDJblEUJ+sQaqRpOiyDhBAvf5bdqRBqtVrpbo7H4woAuw6hUZ7n+2WQlHLPWjtyLkQyInn+D65DMnIulGVZD8CO1vpyGROG4RXJupTyYX7mJBjDMNwm+QTgnWTXGDMLxkMAHQBbxphgLcE4K9/3VbVaPbPWtgDsTtuvACIpZW/Z6fgF4k5tF6eUZz8AAAAASUVORK5CYII=';
      self.image_normal = tkinter.PhotoImage(data=icon_normal);
      icon_leer = b'iVBORw0KGgoAAAANSUhEUgAAABQAAAABCAYAAADeko4lAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAOxAAADsQBlSsOGwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAMSURBVAiZY2CgMgAAAFEAAQeRRhEAAAAASUVORK5CYII=';
      self.image_leer = tkinter.PhotoImage(data=icon_leer);
      icon_command = b'iVBORw0KGgoAAAANSUhEUgAAACQAAAAMCAYAAAAK/x/DAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAOxAAADsQBlSsOGwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAEISURBVDiNvZKhTsRAEIb/nSWpvwdA0lJXwyPgmnbFShJOIzHIPgUGTmFIKgYEJNQisBWIbjAYkCS1bcqiLmku3WL2+skvmcyXyUh4Rin1HobhpzHmY865IN9BwzCcA9hkWbaecy6k7yBjzHccx88AbqMokk3TvE0517zwHbQlTdNDKWUlhHhg5iuXWywIALTWq67rngDUSZJcFEXxO+XGM95/aExZlj/W2lMhxFFd13cut1gQAARBYAEM1lqac4sEaa1Xfd9XAL7atj1zuTF7fWoieiGix/FT77pd9nIhpdSxlPKViG62i6fcFN4vlOf5CQAWQlwy873LuTjwHQTgGsCamat/3CR/YouZ7YqdqyMAAAAASUVORK5CYII=';
      self.image_command = tkinter.PhotoImage(data=icon_command);
      icon_command_hover = b'iVBORw0KGgoAAAANSUhEUgAAACQAAAAMCAYAAAAK/x/DAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAOxAAADsQBlSsOGwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAD4SURBVDiNvZIxTsMwGEa/EEsZ/8izVX/2gMQFOELP0JWZjVNwCDYWLgDsSBVS1aEDAxIDrhQYm3gnwFKkUCXpkuSNT7K+J9spBobki4iEGONbn+siHTpIa70CcJfn+a6qqk2XmyyoLMtPEXlIkuRGRNIY43ObG3r3KN77GclXktd97pBkzChjjFZK3QPYhBAuAXy3ueaZkzGDiqLYZVk2B3BK8rbLTRYEAEqpHwB1c6vN/TH4p25ijNF1XT8CeA8hXGD/ZIeueWa0G/Lez5RSSwBP++GvNjfW/j+stWckt9baqz43Cc65c5IfJBd9bsqgtXNufsx18QuJ8HZocuQR8gAAAABJRU5ErkJggg==';
      self.image_command_hover = tkinter.PhotoImage(data=icon_command_hover);
      #
      super().__init__(*args, **kwargs);
      self.farben = self.master.farben;
      self.breite = self.master.breite;
      self.subframe = tkinter.Frame(self);
   #
   def MouseOver(self, event):
      event.widget.configure(foreground=self.farben.farbe_fg_hover, background=self.farben.farbe_bg_hover,
         image=self.image_hover);
   #
   def MouseOut(self, event):
      event.widget.configure(foreground=self.farben.farbe_fg, background=self.farben.farbe_bg_subitem,
         image=self.image_normal);
   #
   def MouseOverLeer(self, event):
      event.widget.configure(foreground=self.farben.farbe_fg_hover, background=self.farben.farbe_bg_hover,
      image=self.image_command_hover);
   #
   def MouseOutLeer(self, event):
      event.widget.configure(foreground=self.farben.farbe_fg, background=self.farben.farbe_bg_subitem,
      image=self.image_command);
   #
   def Unhighlight(self):
      self.master.currenthighlight.bind('<Enter>', self.MouseOver);
      self.master.currenthighlight.bind('<Leave>', self.MouseOut);
      self.master.currenthighlight.configure(foreground=self.farben.farbe_fg, background=self.farben.farbe_bg_subitem,
         image=self.image_normal);
   #
   def Auswaehlen(self, element):
      self._Highlight(element=element, command=lambda: None);
   #
   def Highlight(self, event, command):
      self._Highlight(element=event.widget, command=command);
   #
   def _Highlight(self, element, command):
      if (element['background'].string != self.farben.farbe_bg_subitem_highlight):
         element.unbind('<Enter>');
         element.unbind('<Leave>');
         element.configure(foreground=self.farben.farbe_fg_highlight,
            background=self.farben.farbe_bg_subitem_highlight, image=self.image_highlight);
         if (self.master.currenthighlight is not None):
            self.Unhighlight();
         #
         self.master.currenthighlight = element;
         command();
   #
   def NeuerEintrag(self, text, command=None, variable=None, typ=None):
      if ((command is not None) and (variable is not None)):
         print('# Warnung: Eintrag mit command und variable nicht unterstützt');
         return;
      #
      numeintraege = len(self.subframe.children);
      if (numeintraege == 0):
         self.master.EintragVerlinken(self);
      #
      if (command is not None):
         sublabel = ttk.Label(self.subframe, compound='left', image=self.image_normal, text=text,
            font=self.font, foreground=self.farben.farbe_fg, background=self.farben.farbe_bg_subitem,
            width=self.breite);
         sublabel.grid(row=numeintraege, column=0, ipady=2, sticky='ew');
         sublabel.bind('<Enter>', self.MouseOver);
         sublabel.bind('<Leave>', self.MouseOut);
         sublabel.bind('<Button-1>', lambda event: self.Highlight(event, command));
         return sublabel;
      elif (variable is not None):
         if ((typ is None) or (typ == 'entry')):
            subsubframe = tkinter.Frame(self.subframe, background=self.farben.farbe_bg_subitem);
            subsubframe.grid(row=numeintraege, column=0, ipady=2, sticky='nsew');
            sublabel = CustomMessage(subsubframe, text=text, font=self.font_klein,
               foreground=self.farben.farbe_fg, background=self.farben.farbe_bg_subitem, width=280);
            sublabel.grid(row=0, column=0, sticky='nw');
            subentry = CustomEntry(subsubframe, textvariable=variable, width=35);
            subentry.grid(row=0, column=1, padx=5, sticky='ne');
            return [sublabel, subentry]
         #
         elif (typ == 'checkbutton'):
            subentry = CustomCheckbutton(self.subframe, variable=variable, text=text);
            subentry.grid(row=numeintraege, column=0, ipady=2, sticky='nsew');
            return subentry;
      else:
         sublabel = ttk.Label(self.subframe, text=text, font=self.font_dick, width=self.breite,
            foreground=self.farben.farbe_fg, background=self.farben.farbe_bg_subitem);
         sublabel.grid(row=numeintraege, column=0, ipadx=5, ipady=2, sticky='ew');
         return sublabel;
   #
   def NeuerFrameEintrag(self):
      refframe = tkinter.Frame(self.subframe, background=self.farben.farbe_bg_subitem);
      refframe.grid(row=len(self.subframe.children)-1, column=0, ipady=2, sticky='nsew');
      return refframe;
   #
   def NeuerBefehl(self, text, command):
      sublabel = ttk.Label(self.subframe, compound='left', image=self.image_command, text=text,
         font=self.font, foreground=self.farben.farbe_fg, background=self.farben.farbe_bg_subitem, width=self.breite);
      sublabel.grid(row=len(self.subframe.children)-1, column=0, ipady=2, sticky='ew');
      sublabel.bind('<Enter>', self.MouseOverLeer);
      sublabel.bind('<Leave>', self.MouseOutLeer);
      sublabel.bind('<Button-1>', lambda event: command());
   #
   def AlleEintraegeEntfernen(self):
      for kindelem in self.subframe.winfo_children():
         kindelem.destroy();
      #
      self.subframe.grid_remove();
      self.master.EintragEntlinken(self);
#


# -------------------------------------------------------------------------------------------------
class CustomLabelMenu(ttk.Frame):
   def __init__(self, farben, breite, hoehe, *args, **kwargs):
      self.font = ('Helvetica', '-20', 'bold');
      #
      icon_highlight = b'iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAOxAAADsQBlSsOGwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAACASURBVBiVfdAxDgFRFIXhOyQkFqLRqy1CYg86m9DqLEVhEaKg1VmAGdOI+DSTmLw872/vyTnnnogOXLDBIErggDeumJWESzzwQY0dxjnhBE8/Wtyx+Bef0mCfFh9mWlUR8Uqj255TjRvmaeyq90yDLUa5fsdunhOmpXnOWKPK3b/p6K02D06m2AAAAABJRU5ErkJggg==';
      self.image_highlight = tkinter.PhotoImage(data=icon_highlight);
      icon_hover = b'iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAOxAAADsQBlSsOGwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAADeSURBVBiVbZAxS8NQFIXP8ZkIfUsSQocI4Y5Cf4lD94Lg4t4/4ir4A/ofnDtnEnRyeC841pIIlkLFcDuYlGfwmw6XwzmHa9AjIq9Zll20bVsBUIw4C/R713X3IvJSluVsbDSDSNP0AOAawCXJ2yRJpnmer5um6QCAg7EoikkURRuStj/tVfWT5E1d12uG8SLy1KeeUNUdyVW48c+UAZIE8D2u/iA56U9fALYkF9776pQYx/Gc5M9vm+4APFhrr7z3FQCcBy13qmpJPhtjFs65t3BCaJwaY5bOuUf88/Ajk3ZCjr1yFA4AAAAASUVORK5CYII=';
      self.image_hover = tkinter.PhotoImage(data=icon_hover);
      icon_inaktiv = b'iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAOxAAADsQBlSsOGwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAADrSURBVBiVfZCxSsRQEEXvvGfYZMXWH0ij+AlpFh4ELOy3SSVY+iMWNsJ2Nn5C4DXvEdItpBK0srCw1SLgSkBkrs0awi54q2E4nLmMxTYxxueqqmZ5nndt2xI7MZP5DcBNURRPTdOc/Qfek/wCcKqq6xDCrfd+tgcOw+CNMRaAkDwCcJUkyWsIYQEAMtXHGD3J8+lORDYkH6anQdLudiMpIvI9Guu6nqdp+g5gvjV9quqHtXbpnOtGY5ZlFwB+AFBENqp61/f9iXOuA4CDP1BVLwEcGmMeASzLsnyZVhhBY8wxgGvn3EpE9h7+CyN2Vj/5eiVdAAAAAElFTkSuQmCC';
      self.image_inaktiv = tkinter.PhotoImage(data=icon_inaktiv);
      icon_normal = b'iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAOxAAADsQBlSsOGwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAADhSURBVBiVXY6hTsRAGIRntjRNjmDPoKq2yb0E9sQmW3c1GBIkL4Il4QF4gG7N6eqakoAiDQILDgwEOpi9ptdRk8mX7/8TxJRl+Wytzaqq6tq2FRYxhyLpjeRt3/dPzrnNEkwOxVr7TXJL8twYc1kUxTrP83YYhr8j4ziOe0kJAAI4A3CdZdmr9/4CcZzivd8D2C6ufgF4MPOFZLKAIIkAfiajc25ljHknuYrTJ4APALsQQjcZjTGO5C8AxXN3aZoWIYQOAE5m4JWkUwCPJHd1Xb/MX5hASWtJN03T3EfrUf4Byq9IDI9y9xUAAAAASUVORK5CYII=';
      self.image_normal = tkinter.PhotoImage(data=icon_normal);
      #
      self.farben = farben;
      self.breite = breite;
      self.hoehe = hoehe;
      self.ausgeklappt = False;
      self.currenthighlight = None;
      #
      super().__init__(*args, **kwargs);
   #
   def MouseOver(self, event):
      event.widget.configure(foreground=self.farben.farbe_fg_hover, background=self.farben.farbe_bg_hover,
         image=self.image_hover);
   #
   def MouseOut(self, event):
      event.widget.configure(foreground=self.farben.farbe_fg, background=self.farben.farbe_bg,
         image=self.image_normal);
   #
   def IstAusgewaehlt(self):
      return self.ausgeklappt;
   #
   def Highlight(self, event):
      self.ToggleAuswaehlen(element=event.widget);
   #
   def ToggleAuswaehlen(self, element):
      subframe = element.master.children['!frame'];
      if (element['background'].string == self.farben.farbe_bg_highlight):
         self.ausgeklappt = False;
         element.bind('<Enter>', self.MouseOver);
         element.bind('<Leave>', self.MouseOut);
         subframe.grid_remove();
         element.configure(foreground=self.farben.farbe_fg_hover, background=self.farben.farbe_bg_hover,
         image=self.image_hover);
      else:
         self.ausgeklappt = True;
         element.unbind('<Enter>');
         element.unbind('<Leave>');
         element.configure(foreground=self.farben.farbe_fg_highlight,
            background=self.farben.farbe_bg_highlight, image=self.image_highlight);
         subframe.grid(row=1, column=0, sticky='nsew');
   #
   def EintragVerlinken(self, element):
      # FIXME: Kann man das immer so sagen?
      baselabel = element.children['!label'];
      baselabel.configure(image=self.image_normal, foreground=self.farben.farbe_fg, background=self.farben.farbe_bg);
      baselabel.bind('<Enter>', self.MouseOver);
      baselabel.bind('<Leave>', self.MouseOut);
      baselabel.bind('<Button-1>', self.Highlight);
   #
   def EintragEntlinken(self, element):
      baselabel = element.children['!label'];
      baselabel.configure(image=self.image_inaktiv, foreground=self.farben.farbe_fg_inaktiv,
         background=self.farben.farbe_bg_inaktiv);
      baselabel.unbind('<Enter>');
      baselabel.unbind('<Leave>');
      baselabel.unbind('<Button-1>');
      self.currenthighlight = None;
   #
   def NeuerEintrag(self, text):
      hauptelement = CustomRadioItem(self);
      hauptelement.grid(row=len(self.children)-1, column=0, sticky='ew');
      labeloption = ttk.Label(hauptelement, compound='left', image=self.image_inaktiv, text=text,
         font=self.font, foreground=self.farben.farbe_fg_inaktiv, background=self.farben.farbe_bg_inaktiv,
         width=self.breite);
      labeloption.grid(row=0, column=0, ipadx=10, ipady=2, sticky='ew');
      return hauptelement;
   #
   def EintraegeEntfernen(self):
      for kind in self.winfo_children():
         kind.destroy();
#
