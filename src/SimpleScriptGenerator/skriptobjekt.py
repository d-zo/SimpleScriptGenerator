# -*- coding: utf-8 -*-
"""
skriptobjekt.py   v0.2 (2020-12)
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
class Skriptobjekt(object):
   """Klasse zur interaktiven Erstellung eines Skripts
   """
   def __init__(self):
      self.name = None;
      self.einstellungen = None;
      self.codebloecke = None;
      self.blockchecks = None;
      self.zuweisung = None;
      self.Initialisiert = False;
      self.checks = None;
      self.relevanteObjekte = None;
   #
   def Initialisieren(self, pfad):
      """Laedt alle erforderlichen Dateien fuer das Skriptobjekt aus dem angegebenen pfad ein und
      initialisiert die internen Werte.
      """
      from .datenstruktur import Datenstruktur
      from .dateneinlesen import DatensatzEinlesen
      from .codeblockeinlesen import CodeblockEinlesen
      from .strukturfunktionen import Zugriffstruktur
      #
      self.pfad = pfad;
      self.codebloecke, self.blockchecks = CodeblockEinlesen(dateiname=self.pfad + 'codeblock.txt');
      self.einstellungen = DatensatzEinlesen(dateiname=self.pfad + 'einstellungen.json');
      self.checks = DatensatzEinlesen(dateiname=self.pfad + 'vorlagenlogik.json');
      if ((self.codebloecke is None) or (self.einstellungen is None) or (self.checks is None)):
         return False;
      #
      if ('Name' in self.checks):
         self.name = self.checks['Name'];
      #
      self.zuweisung = Datenstruktur();
      Zugriffstruktur(struktur=self.einstellungen, zugriff=self.zuweisung);
      self._SynchronisiereChecks();
      self.Initialisiert = True;
      return True;
   #
   def Vorlagenname(self):
      """Gib den eingelesenen Namen der Vorlage zurueck oder None, falls dieser nicht existiert.
      """
      return self.name;
   #
   def LeseEintrag(self, eintrag):
      """Gibt den Wert der internen Struktur mit dem Schluessel eintrag als Kopie zurueck.
      """
      import copy
      from .strukturfunktionen import ZugriffEintrag
      #
      return copy.deepcopy(ZugriffEintrag(daten=self.einstellungen, zieleintrag=self.zuweisung[eintrag]));
   #
   def _AbhaengigkeitenAktualisieren(self, gruppe, auswahl):
      #print('Untersuche Abh. zu ' + gruppe + ' und ' + str(auswahl));
      if (gruppe in self.checks['Checks']):
         self.checks['Checks'].update([(gruppe, auswahl)]);
      #
      if (gruppe not in self.checks['Abhaengigkeiten']):
         #print('# Warung: ' + gruppe + ' nicht in Abhaengigkeiten gefunden');
         return;
      #
      for eintrag in self.checks['Abhaengigkeiten'][gruppe]['[default]'].keys():
         if (eintrag == '[GUI]'):
            continue;
         #
         wert = self.checks['Abhaengigkeiten'][gruppe]['[default]'][eintrag];
         self.checks['Checks'].update([(eintrag, wert)]);
      #
      if (auswahl == ''):
         auswahl = 'ohne';
      #
      for eintrag in self.checks['Abhaengigkeiten'][gruppe][auswahl].keys():
         if (eintrag == '[GUI]'):
            continue;
         #
         wert = self.checks['Abhaengigkeiten'][gruppe][auswahl][eintrag];
         self.checks['Checks'].update([(eintrag, wert)]);
   #
   def _SynchronisiereChecks(self):
      """Prueft alle Checks/Abhaengigkeiten und aktualisiere die interne Struktur.
      """
      from .strukturfunktionen import ZugriffEintrag
      #
      for eintrag in self.zuweisung.keys():
         if (eintrag.startswith('__') and eintrag.endswith('__')):
            continue;
         #
         wert = ZugriffEintrag(daten=self.einstellungen, zieleintrag=self.zuweisung[eintrag]);
         #
         if (wert is not None):
            self._AbhaengigkeitenAktualisieren(gruppe=eintrag, auswahl=wert);
   #
   def AendereEintrag(self, eintrag, wert):
      """Aendere den Zielwert der internen Struktur mit dem Schluessel eintrag zu wert.
      """
      from .strukturfunktionen import ZugriffEintrag
      #
      # Um den Eintrag erfolgreich zu aendern, muss das dict mit dem Eintrag zurueckgegeben werden.
      # Deshalb wird eine Tiefenebene weniger gesucht.
      zieleintrag = self.zuweisung[eintrag];
      if (len(zieleintrag) == 1):
         zieldict = self.einstellungen;
      else:
         zieldict = ZugriffEintrag(daten=self.einstellungen, zieleintrag=zieleintrag[:-1]);
      #
      if ((zieldict[eintrag] is not None) and (wert is not None)):
         zieldict.update([(eintrag, wert)]);
         if (not (eintrag.startswith('__') and eintrag.endswith('__'))):
            #print('Aendere Eintrag u. Abh. zu ' + eintrag + ' und ' + wert);
            self._AbhaengigkeitenAktualisieren(gruppe=eintrag, auswahl=wert);
         #
         return True;
      else:
         return False;
   #
   def RelevanteObjekteSpeichern(self, liste):
      self.relevanteObjekte = liste;
   #
   def Laden(self, dateiname):
      """Laedt Projekteinstellungen aus einer Datei namens dateiname. Anschliessend wird geprueft,
      ob die Einstellungen gueltig sind. Wenn die Pruefung erfolgreich ist, werden die geladenen
      Einstellungen uebernommen, sonst verworfen.
      """
      import copy
      from .dateneinlesen import DatensatzEinlesen
      from .strukturfunktionen import AktualisiereGleichartigesDict
      #
      neue_einstellungen = DatensatzEinlesen(dateiname=dateiname);
      if (neue_einstellungen is not None):
         einstellungen = copy.deepcopy(self.einstellungen);
         if (AktualisiereGleichartigesDict(altes_dict=einstellungen, neues_dict=neue_einstellungen)):
            self.einstellungen = einstellungen;
            self._SynchronisiereChecks();
            return True;
         else:
            print('# Warnung: Einstellungen wegen ungueltiger Eintraege nicht uebernommen');
      #
      else:
         print('# Warnung: Konnte keine Einstellungen einlesen');
      #
      return False;
   #
   def Speichern(self, dateiname, minimal=False):
      """Speichere die aktuellen Einstellungen als Differenz zu den Standardeinstellungen.
      """
      import os
      import copy
      import datetime
      from .datenstruktur import Datenstruktur
      from .dateneinlesen import DatensatzEinlesen, DatensatzSpeichern
      from .strukturfunktionen import DifferenzDict, ErgaenzeDict
      #
      zeitpunkt = datetime.datetime.now();
      self.einstellungen['allgemein'].update([('datum', zeitpunkt.strftime('%Y-%m-%d'))]);
      #
      projektversion = 1;
      projektname = self.einstellungen['allgemein']['name'];
      if (projektname == 'Einstellungsvorlage'):
         projektname = dateiname.split(os.sep)[-1];
         if (projektname.endswith('.json')):
            projektname = projektname[:-5];
         #
         self.einstellungen['allgemein'].update([('name', projektname)]);
      else:
         projektversion = int(self.einstellungen['allgemein']['version']) + 1;
      #
      self.einstellungen['allgemein'].update([('version', projektversion)]);
      # Ermittle die aktuelle Version der Einstellungsvorlage
      einstellungsvorlage = DatensatzEinlesen(dateiname=self.pfad + 'einstellungen.json');
      #
      if (minimal):
         diff = DifferenzDict(altes_dict=einstellungsvorlage, neues_dict=self.einstellungen);
         # Speichere die aktuelle Version der Einstellungsvorlage mit dazu. Die Gruppe allgemein
         # existiert auf jeden Fall, da wir sichergestellt haben, dass sich dort ein Namen ungleich
         # dem Vorlagennamen befindet
         diff['allgemein'].update([('vorlagenversion', einstellungsvorlage['allgemein']['vorlagenversion'])]);
         diff['allgemein'].update([('version', projektversion)]);
         diff['allgemein'].update([('datum', zeitpunkt.strftime('%Y-%m-%d'))]);
         DatensatzSpeichern(datensatz=diff, dateiname=dateiname);
      elif (self.relevanteObjekte is not None):
         einstellungen = Datenstruktur();
         for schluessel in self.relevanteObjekte:
            ErgaenzeDict(bezugs_dict=einstellungen, schluesselliste=self.zuweisung[schluessel],
               wert=self.LeseEintrag(eintrag=schluessel));
         #
         if ('allgemein' not in einstellungen.keys()):
            einstellungen.update([('allgemein', Datenstruktur())]);
         #
         einstellungen['allgemein'].update([('name', projektname)]);
         einstellungen['allgemein'].update([('vorlagenversion', einstellungsvorlage['allgemein']['vorlagenversion'])]);
         einstellungen['allgemein'].update([('version', projektversion)]);
         einstellungen['allgemein'].update([('datum', zeitpunkt.strftime('%Y-%m-%d'))]);
         #
         DatensatzSpeichern(datensatz=einstellungen, dateiname=dateiname);
      else:
         einstellungen = copy.deepcopy(self.einstellungen);
         if (einstellungen['aktion'] == 'modellerstellung'):
            del einstellungen['ausgabeverarbeitung'];
         elif (einstellungen['aktion'] == 'ausgabeverarbeitung'):
            del einstellungen['modellerstellung'];
         #
         DatensatzSpeichern(datensatz=einstellungen, dateiname=dateiname);
   #
   def _PruefeUndSortiereChecks(self):
      import copy
      from itertools import chain as iter_chain
      #
      erlaubte_checks = copy.deepcopy(self.checks['Checks']);
      # Zusaetzliche Boolsche Operatoren erlauben (and wird standardmaessig genutzt)
      erlaubte_checks.update({'or': 'or',
                             'not': 'not'});
      liste_block_ids = list(self.blockchecks.keys());
      liste_block_ids.sort();
      gueltige_checks = [];
      for block_id in liste_block_ids:
         einzelblock = self.blockchecks[block_id];
         # Liste abflachen
         temp_blockcheck = list(iter_chain.from_iterable([eintrag.split() for eintrag in einzelblock]));
         if (any([eintrag not in erlaubte_checks for eintrag in temp_blockcheck])):
            print('# Fehler: Ungueltiger Check in Block ' + str(block_id));
            return None;
         #
         temp_check = [];
         for einzel_check in einzelblock:
            begriffe = einzel_check.split();
            temp_check += [' '.join([str(erlaubte_checks[einzelbegriff]) for einzelbegriff in begriffe])];
         #
         gesamtcheck = ') and ('.join(temp_check);
         gesamtcheck = '(' + gesamtcheck + ')';
         if (eval(gesamtcheck)):
            gueltige_checks += [block_id];
      #
      return gueltige_checks;
   #
   def AbhaengigkeitenAusgeben(self):
      import copy
      #
      return copy.deepcopy(self.checks['Abhaengigkeiten']);
   #
   def Exportieren(self, dateiname):
      from .strukturfunktionen import Zuweisungsliste
      #
      # Pruefe alle Checks und speichere die schluessel (IDs), fuer die die checks erfuellt sind
      check_ids = self._PruefeUndSortiereChecks();
      if (check_ids is None):
         print('# Fehler: Kann wegen ungueltiger Checks nicht exportieren');
         return False;
      #
      if (check_ids == []):
         print('# Warnung: Kein Check war erfolgreich - Keine Daten zum Exportieren');
         return False;
      #
      ausgabetext = '\n'.join([self.codebloecke[block_id] for block_id in check_ids]);
      #
      # Ersetze alle Variablen in den jeweiligen eintraegen
      zuweisung = Zuweisungsliste(struktur=self.einstellungen, anfang='__', ende='__');
      for schluessel in zuweisung.keys():
         ersatz = zuweisung[schluessel];
         #
         if (isinstance(ersatz, str)):
            if (ersatz not in self.checks['Nachbereitung']['Variablennamen']):
               ersatz = '\'' + ersatz + '\'';
         #
         if (schluessel in self.checks['Nachbereitung']['Formatstring']):
            # Sonderfaelle beruecksichtigen
            if (schluessel.endswith('[0]__')):
               formatstring = self.checks['Nachbereitung']['Formatstring'][schluessel][0];
               # Gebe Eintraege zeilenweise aus aber mit Anfuehrungszeichen um vorhandene Strings
               segmente = formatstring.split('{');
               segmente = [x.split('}')[0] for x in segmente if len(x) > 0];
               einzelzeilen = [];
               for zeile in ersatz:
                  mod_zeile = [];
                  for idx_seg, teilsegment in enumerate(segmente):
                     # leer, zahl oder s -> string
                     if (teilsegment == ''):
                        mod_zeile += ['\'' + zeile[idx_seg] + '\''];
                     elif ((teilsegment[-1] == 's') or (teilsegment[-1].isdigit())):
                        mod_zeile += ['\'' + zeile[idx_seg] + '\''];
                     else:
                        mod_zeile += [zeile[idx_seg]];
                  #
                  einzelzeilen += ['[' + formatstring.format(*mod_zeile) + ']'];
               #
               ersatz = ',\n '.join(einzelzeilen);
            #
            elif (isinstance(self.checks['Nachbereitung']['Formatstring'][schluessel], list)):
               formatliste = self.checks['Nachbereitung']['Formatstring'][schluessel];
               # Erwartet entweder genau eine Formatangabe, oder soviele (einzelne) Listeneintraege
               # wie elemente in der Variablen gespeichert sind
               if (len(formatliste) == 1):
                  teilsegment = formatliste[0].split('}')[0];
                  # s -> string, f -> float, alles andere nicht aendern
                  if (teilsegment[-1] == 's'):
                     mod_zeile = ['\'' + elem + '\'' for elem in ersatz];
                  elif (teilsegment[-1] == 'f'):
                     mod_zeile = ersatz;
                  else:
                     mod_zeile = [str(x) for x in ersatz];
                  #
                  formatstring = ', '.join([formatliste[0] for x in range(len(ersatz))]);
                  ersatz = '[' + formatstring.format(*mod_zeile) + ']';
               else:
                  segmente = [x.split('}')[0] for x in formatliste];
                  mod_zeile = [];
                  for idx_seg, teilsegment in enumerate(segmente):
                     # s -> string, f -> float, alles andere nicht aendern
                     if (teilsegment[-1] == 's'):
                        mod_zeile += ['\'' + ersatz[idx_seg] + '\''];
                     elif (teilsegment[-1] == 'f'):
                        mod_zeile += [ersatz[idx_seg]];
                     else:
                        mod_zeile += [str(ersatz[idx_seg])];
                  #
                  formatstring = ', '.join(formatliste);
                  ersatz = '[' + formatstring.format(*mod_zeile) + ']';
            #
            else:
               ersatz = self.checks['Nachbereitung']['Formatstring'][schluessel].format(ersatz);
         #
         else:
            # Sonderfaelle beruecksichtigen
            if (schluessel.endswith('[0]__')):
               ersatz = ',\n'.join([str(zuweisung[schluessel][idx]) for idx in range(len(zuweisung[schluessel]))]);
            else:
               ersatz = str(ersatz);
         #
         ausgabetext = ausgabetext.replace(schluessel, ersatz);
      #
      # Speichere den finalen String in einer Datei namens dateiname
      with open(dateiname, 'w') as ausgabe:
         ausgabe.write(ausgabetext);
      #
      return True;
#
