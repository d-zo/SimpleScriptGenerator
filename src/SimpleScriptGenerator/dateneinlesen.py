# -*- coding: utf-8 -*-
"""
dateneinlesen.py   v0.2 (2023-09)
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
def ExistiertDatei(dateiname):
    """Pruefe die Existenz einer Datei. Gibt True zurueck, falls die Datei vorhanden ist.
    """
    from pathlib import Path

    testdatei = Path(dateiname)
    if (testdatei.is_file()):
        return True
    else:
        return False



# -------------------------------------------------------------------------------------------------
def DatensatzEinlesen(dateiname):
    """Lade eine JSON-formatierte Datei, die mit Datensatz_Speichern erstellt worden ist. Gib die
    eingelesene Struktur zurueck.
    """
    import json

    def Eingabedaten_json(json_objekt):
        """Hilfsfunktion zur Umwandlung von unterstuetzten Strukturen beim Einlesen von
        JSON-formatierten Dateien.
        """
        from .datenstruktur import Datenstruktur

        if (isinstance(json_objekt, dict)):
            return Datenstruktur(json_objekt)
        else:
            return json_objekt

    eingelesen = None
    try:
        with open(dateiname, 'r', encoding='utf-8') as eingabe:
            eingelesen = json.load(eingabe, object_hook=Eingabedaten_json)
    except FileNotFoundError:
        print('# Fehler: Datei ' + dateiname + ' konnte nicht gefunden/geoeffnet werden')
    except:
        print('# Fehler: ' + dateiname + ' konnte nicht eingelesen werden')

    return eingelesen



# -------------------------------------------------------------------------------------------------
def DatensatzSpeichern(datensatz, dateiname):
    """Speichere die Stuktur datensatz als JSON-formatierte Datei namens dateiname.
    """
    import json

    class DatenstrukturEncoder(json.JSONEncoder):
        """Einfacher Encoder fuer Objekte der Datenstruktur-Klasse. Kovertiert Datenstruktur-Elemente
        in dicts und schreibt alle Listeneintraege in eine Zeile.
        """
        def default(self, arg):
            return arg.__dict__

        def iterencode(self, eintrag, _one_shot=False):
            listenstufe = 0
            for dumpstring in super().iterencode(eintrag, _one_shot=_one_shot):
                if (dumpstring[0] =='['):
                    listenstufe += 1
                    dumpstring = ''.join([teil.strip() for teil in dumpstring.split('\n')])

                elif (listenstufe > 0):
                    dumpstring = ' '.join([teil.strip() for teil in dumpstring.split('\n')])
                    if (dumpstring == ' '):
                        continue

                    if (dumpstring[-1] == ','):
                        dumpstring = dumpstring[:-1] + self.item_separator
                    elif (dumpstring[-1] == ':'):
                        dumpstring = dumpstring[:-1] + self.key_separator

                if (dumpstring[-1] == ']'):
                    listenstufe -= 1

                yield dumpstring

    with open(dateiname, 'w') as ausgabe:
        json.dump(datensatz, ausgabe, cls=DatenstrukturEncoder, indent=3)


