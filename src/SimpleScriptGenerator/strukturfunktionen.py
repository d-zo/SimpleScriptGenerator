 # -*- coding: utf-8 -*-
"""
strukturfunktionen.py   v0.2 (2020-03)
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
def Zugriffstruktur(struktur, zugriff, pfad=[]):
   """Durchlaufe die uebergebene struktur und erstelle einen zugriff (erwartet ein leeres
   dict, das gefuellt wird). Fuer jeden der Schluessel-Wert-Paare in struktur wird ein Schluessel
   in zugriff angelegt, der den gesamten pfad zu dieser Unterstruktur als Wert enthaelt
   (pfad sollte als leere Liste initialisiert werden). Sollte in struktur ein Schluessel mehrmals
   vorkommen, so wird eine Warnung ausgegeben und im Schluessel nur einer der Werte (Unterstruktur)
   gespeichert. Gibt nichts explizit zurueck.
   """
   for schluessel in struktur.keys():
      if (isinstance(struktur[schluessel], dict)):
         Zugriffstruktur(struktur=struktur[schluessel], zugriff=zugriff, pfad=pfad + [schluessel]);
      else:
         if (schluessel in zugriff.keys()):
            print('# Warnung: Schluessel ' + schluessel + ' mehrmals definiert - eine Zuweisung wird verworfen');
         #
         zugriff.update([(schluessel, pfad + [schluessel])]);
#


# -------------------------------------------------------------------------------------------------
def Zuweisungsliste(struktur, anfang='__', ende='__', inversion=False):
   """Durchlaufe die uebergebene struktur und erstelle eine neue (flache) zuweisung fuer jeden
   der Schluessel-Wert-Paare in struktur, deren schluessel mit anfang beginnt und mit ende endet.
   Durch inversion wird zuweisung das komplementaere Set an schluesseln und Werten zugewiesen.
   Gibt die zuweisung zurueck.
   """
   zuweisung = dict();
   for schluessel in struktur.keys():
      if (isinstance(struktur[schluessel], dict)):
         zuweisung.update(Zuweisungsliste(struktur=struktur[schluessel], anfang=anfang, ende=ende,
            inversion=inversion));
      else:
         if (schluessel.startswith(anfang) and schluessel.endswith(ende)):
            if (not inversion):
               zuweisung.update([(schluessel, struktur[schluessel])]);
         else:
            if (inversion):
               zuweisung.update([(schluessel, struktur[schluessel])]);
   #
   return zuweisung;
#


# -------------------------------------------------------------------------------------------------
def ZugriffEintrag(daten, zieleintrag):
   """Ermittelt in einer (ggfs. verschachtelten) dict-Struktur namens daten den Wert des
   geforderten zieleintrag. zieleintrag muss als Liste uebergeben werden. Gibt den wert des
   Zieleintrags bei erfolgreichen Auffinden des zieleintrags zurueck, sonst None.
   """
   if (len(zieleintrag) > 1):
      try:
         daten = daten[zieleintrag[0]];
      except:
         #print('# Warnung: Geforderter Eintrag enthaelt keinen Schluessel ' + zieleintrag[0]);
         return None;
      #
      return ZugriffEintrag(daten=daten, zieleintrag=zieleintrag[1:]);
   else:
      try:
         rueckgabe = daten[zieleintrag[0]];
      except:
         #print('# Warnung: Geforderter Eintrag enthaelt keinen Schluessel ' + zieleintrag[0]);
         return None;
      #
      return rueckgabe;
#


# -------------------------------------------------------------------------------------------------
def AktualisiereGleichartigesDict(altes_dict, neues_dict):
   """Erwartet ein altes_dict und neues_dict, das die gleiche Struktur (oder Untermenge davon)
   von altes_dict hat. Jeder (verschachtelte) Schluessel von neues_dict wird ueberprueft und bei
   unterschiedlichen Werten wird altes_dict entsprechend aktualisiert. Gibt False zurueck und
   bricht ab, falls in neues_dict mindestens ein Schluessel nicht in altes_dict vorkommt,
   ansonsten True.
   
   Da beim Durchlauf altes_dict geaendert wird, sollte altes_dict nicht im Original an diese
   Funktion uebergeben werden! altes_dict sollte nur weiterverwendet werden, wenn diese Funktion
   True zurueck gibt.
   """
   rueckgabe = True;
   for schluessel in neues_dict.keys():
      if (schluessel not in altes_dict.keys()):
         print('# Warnung neue Einstellungen enthalten unerlaubte Eintraege (' + schluessel + ')');
         return False;
      else:
         if (isinstance(neues_dict[schluessel], dict)):
            rueckgabe = AktualisiereGleichartigesDict(altes_dict=altes_dict[schluessel],
               neues_dict=neues_dict[schluessel]);
         else:
            altes_dict[schluessel] = neues_dict[schluessel];
      #
      if (rueckgabe == False):
         return False;
   #
   return rueckgabe;
#


# -------------------------------------------------------------------------------------------------
def ErgaenzeDict(bezugs_dict, schluesselliste, wert):
   """Erwartet ein bezugs_dict, zu dem ein neues Schluessel-Wert-Paar hinzugefuegt werden soll. Da
   auch ein verschachtelter Eintrag erstellt werden kann, wird immer eine schluesselliste erwartet,
   die als Struktur verfolgt und ggfs. angelegt wird. Der uebergebene wert wird schliesslich dem
   letzten Schluessel in schluesselliste zugewiesen.
   """
   from .datenstruktur import Datenstruktur
   #
   if (len(schluesselliste) == 1):
      bezugs_dict.update([(schluesselliste[0], wert)]);
   else:
      aktueller_schluessel = schluesselliste[0];
      if (aktueller_schluessel not in bezugs_dict):
         bezugs_dict.update([(aktueller_schluessel, Datenstruktur())]);
      #
      ErgaenzeDict(bezugs_dict=bezugs_dict[aktueller_schluessel],
         schluesselliste=schluesselliste[1:], wert=wert);
#


# -------------------------------------------------------------------------------------------------
def DifferenzDict(altes_dict, neues_dict):
   """Erwartet ein altes_dict und neues_dict, das die gleiche Struktur (oder Untermenge davon)
   von altes_dict hat. Erzeugt ein diff zwischen beiden, aber beruecksichtigt nur die Elemente,
   die bereits in altes_dict existieren. Das heisst, jeder (verschachtelte) Schluessel von
   neues_dict wird mit altes_dict verglichen. Elemente die in beiden gleich sind sowie Elemente
   aus neues_dict, die in altes_dict nicht vorkommen, werden ignoriert. Nur bei Elementen mit
   gleichem Schluessel und unterschiedlichen Wert werden in einem Differenz-dict aufgenommen.
   Das Referenzdict wird zurueckgegeben, dass mit der gleichen Struktur (oder Untermenge davon)
   von altes_dict die gueltigen Unterschiede zu neues_dict enthaelt.
   """
   from .datenstruktur import Datenstruktur
   #
   diff = Datenstruktur();
   for schluessel in neues_dict.keys():
      if (schluessel not in altes_dict.keys()):
         print('# Hinweis: Eintrag (' + schluessel + ') nicht erlaubt: wird ignoriert');
         continue;
      else:
         if (isinstance(neues_dict[schluessel], dict)):
            rueckgabe = DifferenzDict(altes_dict=altes_dict[schluessel],
               neues_dict=neues_dict[schluessel]);
            if (len(rueckgabe.keys()) != 0):
               diff.update([(schluessel, rueckgabe)]);
         else:
            if (altes_dict[schluessel] != neues_dict[schluessel]):
               diff.update([(schluessel, neues_dict[schluessel])]);
   #
   return diff;
#
