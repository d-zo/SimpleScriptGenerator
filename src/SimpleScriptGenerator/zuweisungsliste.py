# -*- coding: utf-8 -*-

"""
zuweisungsliste.py   v0.2 (2023-09)
"""

# Copyright 2020-2023 Dominik Zobel.
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
class Zuweisungsliste(object):
    def __init__(self):
        self.elementliste = []
        self.elementindizes = []

    def Hinzufuegen(self, element, index):
        """Fuegt ein neues element zu den intern gespeicherten Elementen hinzu und verknuepft es mit
        dem uebergebenen index.
        """
        self.elementliste += [element]
        self.elementindizes +=[index]

    def Leeren(self):
        self.elementliste = []
        self.elementindizes = []

    def HatElement(self, element):
        if (element in self.elementliste):
            return True
        else:
            return False

    def Laenge(self):
        return len(self.elementliste)

    def Ausgeben(self, index):
        return [self.elementliste[index], self.elementindizes[index]]

    def AllesBisElementEntfernen(self, element):
        """Entfernt alle intern gespeicherten Elemente bis einschliesslich element. Gibt den zu
        element gespeicherten Index zurueck. Falls element nicht intern gespeichert ist, passiert
        nichts und None wird zurueckgegeben.
        """
        index = None
        if (element in self.elementliste):
            elemidx = self.elementliste.index(element)
            index = self.elementindizes[elemidx]

            self.elementliste = self.elementliste[:elemidx]
            self.elementindizes = self.elementindizes[:elemidx]


        return index

    def LetztesElementEntfernen(self):
        del self.elementliste[-1]
        del self.elementindizes[-1]

    def UebersichtAusgeben(self):
        ausgabeliste = []
        for elem, idx in zip(self.elementliste, self.elementindizes):
            ausgabeliste += [str(elem) + ': ' + str(idx)]

        print(', '.join(ausgabeliste))


