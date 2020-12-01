# -*- coding: utf-8 -*-

"""
guihilfen.py   v0.1 (2020-03)
"""

# Copyright 2020 Dominik Zobel.
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


# -------------------------------------------------------------------------------------------------
def FensterZentrieren(hauptfenster, fenster):
   """Ermittle die Geometrie von hauptfenster, das ein neues fenster oeffnet, und fenster selbst.
   Positioniere fenster anschliessend mittig ueber hauptfenster.
   """
   hauptfenster.update_idletasks();
   haupt_x = hauptfenster.winfo_x();
   haupt_y = hauptfenster.winfo_y();
   haupt_breite = hauptfenster.winfo_width();
   haupt_hoehe = hauptfenster.winfo_height();
   fenster_breite = fenster.winfo_reqwidth();
   fenster_hoehe = fenster.winfo_reqheight();
   posx = int(haupt_x + (haupt_breite - fenster_breite)/2.0);
   posy = int(haupt_y + (haupt_hoehe - fenster_hoehe)/2.0);
   fenster.geometry('+{}+{}'.format(posx, posy));
#


# -------------------------------------------------------------------------------------------------
def StringNachbereitung(zeichenkette):
   """Entfernt alle Anfuehrungszeichen, die die uebergebene zeichenkette einschliessen.
   """
   ueberarbeitet = zeichenkette;
   while (len(ueberarbeitet) > 1):
      if (ueberarbeitet.startswith('\'') and ueberarbeitet.endswith('\'')):
         ueberarbeitet = ueberarbeitet[1:-1];
         continue;
      elif (ueberarbeitet.startswith('"') and ueberarbeitet.endswith('"')):
         ueberarbeitet = ueberarbeitet[1:-1];
         continue;
      #
      break;
   #
   return ueberarbeitet;
#


# -------------------------------------------------------------------------------------------------
def DatentypAusString(zeichenkette):
   """Interpretiert zeichenkette und sucht den korrekten Datentyp (str/float/int/list). Wenn
   zeichenkette einem Datentyp zuordnbar ist, wird dieser gewaehlt (bspw. wird aus '2.0' ein float
   2.0). Das fuehrt gleichzeitig dazu, dass keine Strings von Datentypen wie list, float oder int
   zurueckgegeben werden, da sie immer als Basisdatentyp interpretiert werden. Gibt None zurueck,
   wenn keine (d.h. nur eine ungueltige) Zuordnung moeglich ist.
   """
   import ast
   #
   interpretiert = None;
   # Pruefe zuerst, ob der String mit einem '(' oder '[' startet und als Liste interpretiert werden
   # kann. Anschliessend werden die einzelnen Datentypen (bool, float, int, str) untersucht.
   if (zeichenkette.startswith('(') or zeichenkette.startswith('[')):
      zeichenkette = zeichenkette.replace('(', '[').replace(')', ']');
      if (zeichenkette.count('[') != zeichenkette.count(']')):
         print('# Warnung: Unausgewogene Klammern in ' + zeichenkette);
         return None;
      #
      try:
         interpretiert = ast.literal_eval(zeichenkette);
      except:
         print('# Warnung: Ungültige Liste in ' + zeichenkette);
   #
   elif any([(x in zeichenkette) for x in [' ', ',', '(', ')', '[', ']']]):
      interpretiert = StringNachbereitung(zeichenkette=zeichenkette);
   #
   elif ('true' in zeichenkette.lower()):
      if (len(zeichenkette) == 4):
         interpretiert = True;
      else:
         print('# Warnung: Bool hat mehr Zeichen als erwartet in ' + zeichenkette);
   #
   elif ('false' in zeichenkette.lower()):
      if (len(zeichenkette) == 5):
         interpretiert = False;
      else:
         print('# Warnung: Bool hat mehr Zeichen als erwartet in ' + zeichenkette);
   #
   elif ('.' in zeichenkette):
      # Float oder String
      try:
         interpretiert = float(zeichenkette);
      except:
         interpretiert = StringNachbereitung(zeichenkette=zeichenkette);
   else:
      # Int oder String
      try:
         interpretiert = int(zeichenkette);
      except:
         interpretiert = StringNachbereitung(zeichenkette=zeichenkette);
   #
   return interpretiert;
#

