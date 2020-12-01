# -*- coding: utf-8 -*-
"""
gui.py   v0.5 (2020-11)
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


import tkinter
from tkinter import filedialog, messagebox


# -------------------------------------------------------------------------------------------------
def _Autoscrollfunktion(event):
   event.widget.master.master.configure(scrollregion=event.widget.master.master.bbox('all'),
      width=event.widget.breite, height=event.widget.hoehe);
#


# -------------------------------------------------------------------------------------------------
def _Radscrollfunktion(event, canvas, scrollbar):
   # Windows/Linux Scroll events
   delta = 0;
   if ((event.num == 4) or (event.delta == -120)):
      delta = -1;
   #
   if ((event.num == 5) or (event.delta == 120)):
      delta = 1;
   if (len(scrollbar.state()) == 0):
      # oder Zustand mit != 'disabled' pruefen
      canvas.yview_scroll(delta, 'units');
#


# -------------------------------------------------------------------------------------------------
class GUIbasis(object):
   def __init__(self):
      from .guistil import GUIFarben
      #
      self.tkroot = tkinter.Tk();
      self.tkroot.title('SimpleScriptGenerator');
      self.icondata = b'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';
      self.tkroot.tk.call('wm', 'iconphoto', self.tkroot._w, tkinter.PhotoImage(data=self.icondata));
      #
      self.skript = None;
      self.abhaengigkeiten = None;
      self.struktur = None;
      self.menucanvas = None;
      self.bezugsframe = None;
      #
      self.breite = 600;
      self.hoehe = 800;
      self.scrollbreite = 20;
      self.tkroot.geometry('{}x{}'.format(self.breite, self.hoehe));
      self.tkroot.resizable(False, False);
      #
      self.font_param = ('Helvetica', '-12');
      self.farben = GUIFarben();
      self.pfad = '';
   #
   def _Beenden(self, event=None):
      """GUI-Hauptprogramm beenden.
      """
      self.tkroot.destroy();
   #
   def _FensterProjektLaden(self):
      """Lade eine Projektdatei und gebe die dort gespeicherten Einstellungen in der GUI aus.
      """
      dateiname = filedialog.askopenfilename(title='Datei öffnen', defaultextension='.json',
         filetypes=[('JSON-Projektdatei', '.json')]);
      if ((dateiname == '') or (not dateiname)):
         messagebox.showwarning(parent=self.tkroot, title='Datei öffnen',
            message='Dateiname fehlt - nichts geladen');
         return;
      #
      if (dateiname != ''):
         if (not self.skript.Laden(dateiname=dateiname)):
            messagebox.showwarning(parent=self.tkroot, title='Datei öffnen',
               message='Datei konnte nicht eingelesen werden');
            return;
         #
         self.AktualisiereStruktur();
   #
   def _FensterProjektSpeichern(self):
      """Speichere die aktuellen Einstellungen in einer Projektdatei.
      """
      dateiname = filedialog.asksaveasfilename(parent=self.tkroot, title='Datei speichern',
         defaultextension='.json', filetypes=[('JSON-Projektdatei', '.json')]);
      if ((dateiname == '') or (not dateiname)):
         messagebox.showwarning(parent=self.tkroot, title='Datei speichern',
            message='Dateiname fehlt - nichts gespeichert');
         return;
      #
      self.skript.Speichern(dateiname=dateiname);
   #
   def _FensterProjektExportieren(self):
      """Exportiere aus den aktuellen Einstellungen ein Skript.
      """
      dateiname = filedialog.asksaveasfilename(parent=self.tkroot, title='Exportieren',
         defaultextension='.py', filetypes=[('Python-Abaqus-Skript', '.py')]);
      if ((dateiname == '') or (not dateiname)):
         messagebox.showwarning(parent=self.tkroot, title='Exportieren',
            message='Dateiname fehlt - nichts exportiert');
         return;
      #
      if (not self.skript.Exportieren(dateiname=dateiname)):
         messagebox.showwarning(parent=self.tkroot, title='Exportieren',
            message='Skript konnte nicht exportiert werden');
   #
   def _Standardeinstellungen(self):
      """Lade die Standardeinstellungen aus der Einstellungdatei erneut ein und ueberschreibe alle
      Aenderungen in der GUI.
      """
      fortfahren = messagebox.askyesno(parent=self.tkroot,
         title='Standardeinstellungen laden',
         message='Aktuelle Einstellungen verwerfen und Standardeinstellungen laden?');
      if (not fortfahren):
         return;
      #
      self.skript.Initialisieren(pfad=self.pfad);
      self.AktualisiereStruktur();
   #
   def _CallbackAuswahlAendern(self, gruppe, auswahl):
      """Aendere den Wert des Eintrags, der durch Aenderung den Callback ausgeloest hat und
      aktualisiere die grafische Ausgabe.
      """
      self.skript.AendereEintrag(eintrag=gruppe, wert=auswahl);
      self.AktualisiereStruktur();
   #
   def AktualisiereStruktur(self, element=['aktion']):
      """Speichere Konfiguration der grafischen Elemente und loesche die Struktur von element an.
      Falls element nicht gegeben wird, wird als Standardeinstellung alles geloescht und neu
      eingelesen. Ruft intern die Grafikausgabe auf, die die Aktualisierung der GUI erledigt.
      """
      from .strukturfunktionen import ZugriffEintrag
      #
      # Speichere die aktuelle Position und ausgeklappte Elemente
      menuhoehe_alt = self.bezugsframe.winfo_height();
      scrollposition_alt = self.menucanvas.yview();
      elemliste = [];
      aufgeklappt = [];
      for idx_elem, elem in enumerate(self.bezugsframe.winfo_children()):
         [strukturelem, strukturidx] = self.struktur.Ausgeben(idx_elem);
         elemliste += [strukturelem];
         aufgeklappt += [elem.IstAusgewaehlt()];
      #
      zielidx = self.struktur.AllesBisElementEntfernen(element=element);
      if (zielidx is not None):
         while (zielidx < len(self.bezugsframe.winfo_children())):
            # Element ist in der Struktur. Entferne alle Elemente hinter dem Element
            eintragsliste = self.bezugsframe.winfo_children();
            letztes_element = eintragsliste[-1];
            # Grafikelement und alle Abhaengigkeiten dazu entfernen
            letztes_element.EintraegeEntfernen();
            letztes_element.destroy();
      #
      # Fuege das (neue) Element hinzu
      self.struktur.Hinzufuegen(element=element, index=len(self.bezugsframe.winfo_children()));
      #
      haupt = True;
      guiliste = ZugriffEintrag(daten=self.abhaengigkeiten,
         zieleintrag=element + ['[default]', '[GUI]']);
      if (guiliste is None):
         haupt = False;
         guiliste = ZugriffEintrag(daten=self.abhaengigkeiten, zieleintrag=element + ['[GUI]']);
         if (guiliste is None):
            # Keine weiteren grafischen Elemente
            self.struktur.LetztesElementEntfernen();
            return;
      #
      rueckgabeliste = self.GrafikelementeHinzufuegen(element=element);
      self.skript.RelevanteObjekteSpeichern(liste=rueckgabeliste);
      #
      # Wieder die gespeicherte Ansicht bzw. die beste Naeherung dazu herstellen. Dazu alle vorher
      # ausgeklappten Elemente ausklappen und die Gesamtgroesse ermittlen. Anpassungen sind nur
      # noetig, wenn die Hoehe aller Elemente groesser als die Hoehe des darstellenden Fensters ist
      # (d.h. erst sobald scrollen erforderlich wird)
      for idx_elem, elem in enumerate(self.bezugsframe.winfo_children()):
         [strukturelem, strukturidx] = self.struktur.Ausgeben(idx_elem);
         if (strukturelem in elemliste):
            idx_auswahl = elemliste.index(strukturelem);
            if (aufgeklappt[idx_auswahl]):
               # FIXME: Funktioniert solange mindestens ein Label vorhanden ist,
               #        aber eine robustere Loesung ist sinnvoll
               elem.ToggleAuswaehlen(elem.winfo_children()[0].winfo_children()[1]);
            #
            del elemliste[idx_auswahl];
            del aufgeklappt[idx_auswahl];
      #
      menuhoehe_neu = self.bezugsframe.winfo_height();
      scrollposition_neu = self.menucanvas.yview();
      if (menuhoehe_neu > self.hoehe):
         self.menucanvas.yview_moveto(str(scrollposition_alt[0]*menuhoehe_alt/menuhoehe_neu));
   #
   def GrafikelementeHinzufuegen(self, element):
      """Fuege am Ender der aktuellen grafischen Ausgabe Eintraege hinzu, wenn element in der
      internen Struktur GUI-Eintraege enthaelt.
      """
      from .strukturfunktionen import ZugriffEintrag
      from .guistil import CustomLabelMenu
      #
      haupt = True;
      guiliste = ZugriffEintrag(daten=self.abhaengigkeiten,
         zieleintrag=element + ['[default]', '[GUI]']);
      if (guiliste is None):
         haupt = False;
         guiliste = ZugriffEintrag(daten=self.abhaengigkeiten, zieleintrag=element + ['[GUI]']);
         if (guiliste is None):
            # Keine weiteren grafischen Elemente
            return [];
      #
      bezeichnung = guiliste[0][0];
      if (len(guiliste[0]) != 1):
         print('# Warnung: Der erste Eintrag von [' + ', '.join([x for x in element]) \
            + '] sollte einen Eintrag haben');
      #
      basisframe = CustomLabelMenu(self.farben, self.breite-self.scrollbreite, self.hoehe,
         self.bezugsframe);
      basisframe.grid(row=len(self.bezugsframe.winfo_children()), column=0, sticky='nsew');
      basisframe.bind('<Configure>', _Autoscrollfunktion);
      idx_bezeichnung = 1;
      unterframe = basisframe.NeuerEintrag(text=bezeichnung);
      #
      rueckgabeliste = [];
      for idx_elem, elem in enumerate(guiliste):
         if (idx_elem == 0):
            continue;
         #
         if (elem == []):
            unterframe.NeuerEintrag(text='');
         elif (len(elem) == 1):
            unterframe.NeuerEintrag(text=elem[0]);
         elif (len(elem) == 2):
            if (elem[1].startswith('__') and elem[1].endswith('__')):
               wert = self.skript.LeseEintrag(eintrag=elem[1]);
               if (isinstance(wert, bool)):
                  ref_wert = tkinter.BooleanVar();
                  ref_wert.set(wert);
                  par_elem = unterframe.children['!frame'];
                  self.AddCheckbuttonCallback(parent=par_elem, text=elem[0], name=elem[1],
                     var=ref_wert);
               else:
                  ref_wert = tkinter.StringVar();
                  ref_wert.set(str(wert));
                  [sublabel, subentry] = unterframe.NeuerEintrag(text=elem[0], variable=ref_wert);
                  self._EntryCallbacks(widget=subentry, name=elem[1], var=ref_wert);
            else:
               wert = self.skript.LeseEintrag(eintrag=elem[1]);
               if (isinstance(wert, str)):
                  if (elem[1] in self.abhaengigkeiten.keys()):
                     unterframe.NeuerEintrag(text=elem[0]);
                     for auswahl in self.abhaengigkeiten[elem[1]].keys():
                        if (auswahl == '[default]'):
                           continue;
                        #
                        radiobutton = self._RadioCallback(widget=unterframe, text=auswahl,
                           name=elem[1], auswahl=auswahl);
                        # Die getroffene Wahl hervorheben
                        if (auswahl == wert):
                           unterframe.Auswaehlen(element=radiobutton);
                     #
                     if (self.struktur.HatElement(wert)):
                        print('# Warnung: Eintrag ' + wert \
                           + ' wird verwiesen, obwohl er schon automatisch eingebunden wird');
                        continue;
                     #
                     if (wert in self.abhaengigkeiten[elem[1]].keys()):
                        if (not self.struktur.HatElement(element=[elem[1]])):
                           self.struktur.Hinzufuegen(element=[elem[1]],
                              index=len(self.bezugsframe.winfo_children()));
                           rueckgabeliste += self.GrafikelementeHinzufuegen(element=[elem[1]]);
                           guiliste[0][0];
                        #
                        self.struktur.Hinzufuegen(element=[elem[1], wert],
                           index=len(self.bezugsframe.winfo_children()));
                        rueckgabeliste += self.GrafikelementeHinzufuegen(element=[elem[1], wert]);
                     else:
                        self.struktur.Hinzufuegen(element=[wert],
                           index=len(self.bezugsframe.winfo_children()));
                        rueckgabeliste += self.GrafikelementeHinzufuegen(element=[wert]);
                     #
                     # Wieder einen Kontext mit der urspruenglichen Bezeichnung herstellen, falls
                     # noch weitere GUI-Elemente folgen
                     if (idx_elem < len(guiliste)-1):
                        basisframe = CustomLabelMenu(self.farben, self.breite-self.scrollbreite,
                           self.hoehe, self.bezugsframe);
                        basisframe.grid(row=len(self.bezugsframe.winfo_children()), column=0,
                           sticky='nsew');
                        basisframe.bind('<Configure>', _Autoscrollfunktion);
                        idx_bezeichnung += 1;
                        unterframe = basisframe.NeuerEintrag(text=bezeichnung + ' (' \
                           + str(idx_bezeichnung) + ')');
               #
               elif (isinstance(wert, bool)):
                  ref_wert = tkinter.BooleanVar();
                  ref_wert.set(wert);
                  par_elem = unterframe.children['!frame'];
                  self.AddCheckbuttonCallback(parent=par_elem, text=elem[0], name=elem[1],
                     var=ref_wert);
               else:
                  ref_wert = tkinter.StringVar();
                  ref_wert.set(str(wert));
                  [sublabel, subentry] = unterframe.NeuerEintrag(text=elem[0], variable=ref_wert);
                  self._EntryCallbacks(widget=subentry, name=elem[1], var=ref_wert);
            # Immer bei zwei Elementen das letzte Element in die rueckgabeliste packen
            rueckgabeliste += [elem[1]];
      #
      return rueckgabeliste;
   #
   def _EntryCallbacks(self, widget, name, var):
      """Erzeuge verschiedene Callbacks fuer ein Eingabefeld zum Eintrag name mit der verknuepften
      Eingabevariable var. Zum einen sollen eingetragene Werte in var automatisch geprueft und
      intern gespeichert werden, sofern sie gueltig sind. Zum anderen soll ein Zuruecksetzen von var
      auf den letzten gueltigen Wert des Eintrags name ermoeglicht werden.
      """
      widget.bind('<Return>', lambda event: self._PruefenUndAktualisieren(event, name, var));
      widget.bind('<FocusOut>', lambda event: self._PruefenUndAktualisieren(event, name, var));
      widget.bind('<Leave>', lambda event: self._PruefenUndAktualisieren(event, name, var));
      widget.bind('<Escape>', lambda event: self._Zuruecksetzen(event, name, var));
   #
   def _RadioCallback(self, widget, text, name, auswahl):
      """Erzeuge eine Radio-Auswahl fuer das aktuelle Radiomenu von widget mit dem angezeigten text.
      Bei einer Auswahl wird in der internen Struktur der Wert von name zu auswahl geaendert.
      """
      return widget.NeuerEintrag(text=text,
         command=lambda: self._CallbackAuswahlAendern(gruppe=name, auswahl=auswahl));
   #
   def AddCheckbuttonCallback(self, parent, text, name, var):
      """Erzeuge einen Checkbutton in parent, der text anzeigt und dessen Status in der Variable var
      gespeichert wird. Der Checkbutton ist mit dem Element name der internen struktur verknuepft
      und setzt den Wert entsprechend des Zustandes.
      """
      from .guistil import CustomCheckbutton
      #
      num_elem = len(parent.winfo_children());
      subentry = CustomCheckbutton(parent, text=text, variable=var,
         width=self.breite-self.scrollbreite,
         command=lambda: self.skript.AendereEintrag(eintrag=name, wert=var.get()));
      subentry.grid(row=num_elem, column=0, sticky='nw');
   #
   def _Zuruecksetzen(self, event, element, wert):
      """Lese den letzten gueltigen Wert, der in element zugeordnet worden ist und schreibe ihn
      in die uebergebene StringVar wert.
      """
      alter_wert = self.skript.LeseEintrag(element);
      wert.set(str(alter_wert));
      self._PruefenUndAktualisieren(event=event, element=element, wert=wert),
   #
   def _PruefenUndAktualisieren(self, event, element, wert):
      """Lese den fuer element gespeicherten Eintrag und vergleiche ihn mit wert. Wenn die Eintraege
      identisch sind, gibt es nichts zu tun. Andernfalls wird wert als Eintrag fuer element
      gespeichert. Interpretiert wert und sucht den korrekten Datentyp, so dass i.A. keine Strings
      von Datentypen wie list, float oder int zurueckgegeben werden koennen. Beispielsweise fuehrt
      wert='2.0' zu einer Zuweisung eines floats 2.0 stat eines Strings von '2.0', was im Rahmen
      des Programms beabsichtigtes Verhalten ist.
      """
      from .guihilfen import DatentypAusString
      #
      neuer_wert = DatentypAusString(zeichenkette=str(wert.get()));
      if (neuer_wert is None):
         event.widget.configure(background='#ffaaaa');
         return;
      #
      if ((isinstance(wert, tkinter.StringVar)) and (str(neuer_wert) != wert.get())):
         # Sollte nicht vorkommen, wenn alles korrekt als String an StringVar uebergeben wird
         print('Korrigiere Darstellung von Feldinhalt');
         wert.set(str(neuer_wert));
      #
      event.widget.configure(background='#ffffff');
      alter_wert = self.skript.LeseEintrag(element);
      #
      # Nur Strings zu vergleichen erlaubt i.A. Mehrdeutigkeiten, sollte aber im vorliegenden Fall
      # zu keinen Problemen fuehren, da alle zu verarbeitenden Strings Dateinamen oder vergleichbar
      # sind und nicht als bool/float/int/list interpretiert werden koennen (sollten).
      if (str(neuer_wert) != str(alter_wert)):
         zuordnungsliste = [['eine Wahrheitswert', bool],
                            ['eine Liste', list],
                            #['ein Tupel', tuple],
                            #['ein Dict', dict],
                            ['eine Dezimalzahl', float],
                            ['eine ganze Zahl', int],
                            ['einen Text', str]];
         for datentyp, dateninstanz in zuordnungsliste:
            if (isinstance(alter_wert, dateninstanz) and (not isinstance(neuer_wert, dateninstanz))):
               print('# Warnung: ' + str(neuer_wert) + ' muss ' + datentyp + ' sein');
               event.widget.configure(background='#ffaaaa');
               return;
         #
         self.skript.AendereEintrag(eintrag=element, wert=neuer_wert);
         self.abhaengigkeiten = self.skript.AbhaengigkeitenAusgeben();
   #
   def _Infofenster(self):
      """Zeige ein Fenster mit Informationen zum Programm an.
      """
      from .guihilfen import FensterZentrieren
      from .guistil import CustomLabel, CustomButton
      #
      unterfenster = tkinter.Toplevel(self.tkroot, background=self.farben.farbe_bg_highlight);
      unterfenster.tk.call('wm', 'iconphoto', unterfenster._w, tkinter.PhotoImage(data=self.icondata));
      unterfenster.title('SimpleScriptGenerator Infos');
      #
      infolabel1 = CustomLabel(unterfenster, text='SimpleScriptGenerator v0.3',
         font=('Helvetica', '-18', 'bold'));
      infolabel1.grid(row=0, column=0, padx=30, pady=15);
      #
      infolabel2 = CustomLabel(unterfenster, text='2020  D. Zobel');
      infolabel2.grid(row=1, column=0, padx=30, pady=5);
      #
      button = CustomButton(unterfenster, text="Schließen", command=unterfenster.destroy);
      button.grid(row=2, column=0, padx=10, pady=15);
      #
      FensterZentrieren(self.tkroot, unterfenster);
   #
   def _Vorbereiten(self):
      """Bereite die grafische Umgebung vor. Diese Funktion muss nach dem Erstellen eines GUIbasis-
      Objekts aufgerufen werden, damit alle relevanten Inhalte der GUI vorbereitet werden koennen.
      """
      from .skriptobjekt import Skriptobjekt
      from .guistil import CustomScrollbar
      #
      self.skript = Skriptobjekt();
      #
      menubar = tkinter.Menu(self.tkroot, tearoff=0, borderwidth=0, relief=tkinter.FLAT);
      menu_datei = tkinter.Menu(menubar, tearoff=0);
      #
      menubar.add_cascade(label="Datei", menu=menu_datei);
      menu_datei.add_command(label="Öffnen ...", command=self._FensterProjektLaden);
      menu_datei.add_command(label="Speichern unter ...", command=self._FensterProjektSpeichern);
      menu_datei.add_command(label="Exportieren als ...", command=self._FensterProjektExportieren);
      menu_datei.add_separator();
      menu_datei.add_command(label="Standardeinstellungen laden", command=self._Standardeinstellungen);
      menu_datei.add_separator();
      menu_datei.add_command(label="Beenden", command=self.tkroot.destroy);
      #
      menu_hilfe = tkinter.Menu(menubar, tearoff=0);
      menubar.add_cascade(label='Hilfe', menu=menu_hilfe);
      menu_hilfe.add_command(label='Über SimpleScriptGenerator', command=self._Infofenster);
      #
      self.tkroot.config(menu=menubar);
      #
      self.menucanvas = tkinter.Canvas(self.tkroot, highlightthickness=0, borderwidth=0,
         width=self.breite-self.scrollbreite, height=self.hoehe);
      # Ein Container-Element bereitstellen, das interaktiv angepasst wird
      self.bezugsframe = tkinter.Frame(self.menucanvas);
      self.bezugsframe.grid(row=0, column=0, sticky='nsew');
      #
      menuscrollbar = CustomScrollbar(self.tkroot, orient='vertical', command=self.menucanvas.yview);
      #
      self.menucanvas.configure(yscrollcommand=menuscrollbar.set);
      self.menucanvas.grid(row=0, column=0, sticky='nsew');
      self.menucanvas.create_window((0, 0), window=self.bezugsframe, anchor='nw');
      menuscrollbar.grid(row=0, column=1, sticky='ns');
      #
      #self.bezugsframe.bind('<Configure>', _Autoscrollfunktion);
      self.tkroot.bind('<MouseWheel>', lambda event: _Radscrollfunktion(event, self.menucanvas, menuscrollbar));
      self.tkroot.bind('<Button-4>', lambda event: _Radscrollfunktion(event, self.menucanvas, menuscrollbar));
      self.tkroot.bind('<Button-5>', lambda event: _Radscrollfunktion(event, self.menucanvas, menuscrollbar));
      #
      self.tkroot.bind('<Control-q>', self._Beenden);
   #
   def Ausfuehren(self, pfad):
      """Bereitet die grafische Umgebung vor und uebergibt die Programmsteuerung an die GUI. Liest
      die drei Vorlagedateien aus dem Ordner pfad ein.
      """
      from .zuweisungsliste import Zuweisungsliste
      #
      self._Vorbereiten();
      self.pfad = pfad;
      if (not self.skript.Initialisieren(pfad=self.pfad)):
         print('# Abbruch: Kann notwendige Dateien nicht einlesen');
         return;
      #
      name = self.skript.Vorlagenname();
      if (name is not None):
         self.tkroot.title('SimpleScriptGenerator (' + name + ')');
      #
      self.abhaengigkeiten = self.skript.AbhaengigkeitenAusgeben();
      self.struktur = Zuweisungsliste();
      self.AktualisiereStruktur();
      tkinter.mainloop();
#
