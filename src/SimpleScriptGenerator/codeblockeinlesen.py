# -*- coding: utf-8 -*-
"""
codeblockeinlesen.py   v0.2 (2020-11)
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
def CodeblockEinlesen(dateiname):
   """Liest eine spezielle "codeblock"-Datei ein, aus der spaeter die Codeschnipsel fuer die finale
   Ausgabe erzeugt werden. Die Struktur einer "codeblock"-Datei muss um jeden Codeblock das
   Signalwort "# Block ######" bzw. "# End Block ######" enthalten, wobei ###### fuer eine
   sechsstellige Nummer (Block-ID) steht. Die erste Zeile in jedem Block muss "Blockcheck [...]"
   enthalten, wobei [...] True/False oder eine Liste an boolschen Variablen enthalten muss. Anhand
   dieser Variablen kann spaeter die Nutzung des Codeblocks gesteuert werden.
   Gibt ein dict der codebloecke und ein dict der blockchecks zurueck, die jeweils ueber die
   Block-ID identifiziert werden koennen.
   """
   from .dateneinlesen import ExistiertDatei
   #
   if (not ExistiertDatei(dateiname=dateiname)):
      return [None, None];
   #
   bloecke = dict();
   checks = dict();
   #
   startzeile = 0;
   block_id = '';
   temp_block = '';
   in_Block = False;
   hat_checks = False;
   with open(dateiname, 'r') as eingabe:
      for idx_zeile, zeile in enumerate(eingabe):
         aktuelle_zeile = idx_zeile + 1;
         if (in_Block):
            if (zeile.startswith('# End Block')):
               if (block_id in bloecke.keys()):
                  print('# Warnung: Block mit ID ' + str(block_id) + ' in Zeile ' + str(startzeile) + ' bereits definiert');
                  return [None, None];
               #
               if (not hat_checks):
                  print('# Warnung: Block mit ID ' + str(block_id) + ' in Zeile ' + str(startzeile) + ' hat keine Checks');
                  return [None, None];
               #
               temp_zeile = zeile.split();
               if (len(temp_zeile) != 4):
                  print('# Warnung: Block mit ID ' + str(block_id) + ' hat ein ungueltiges Ende in Zeile ' + str(startzeile));
                  return [None, None];
               #
               if (len(temp_zeile[-1]) != 6):
                  print('# Warnung: Block mit ID ' + str(block_id) + ' hat eine ungueltige ID am Blockende in Zeile ' + str(startzeile));
                  return [None, None];
               #
               if (block_id != temp_zeile[-1]):
                  print('# Warnung: Block mit ID ' + str(block_id) + ' hat eine andere ID am Blockende in Zeile ' + str(startzeile));
                  return [None, None];
               #
               bloecke.update([(block_id, temp_block)]);
               temp_block = '';
               in_Block = False;
               continue;
            #
            elif (zeile.startswith('# Blockcheck')):
               temp_check = zeile.split('[');
               if (len(temp_check) != 2):
                  print('# Warnung: Blockcheck in Zeile ' + str(aktuelle_zeile) + ' ungueltig, da [ vor den Checks fehlt');
                  return [None, None];
               #
               temp_check = temp_check[1].split(']');
               if (len(temp_check) != 2):
                  print('# Warnung: Blockcheck in Zeile ' + str(aktuelle_zeile) + ' ungueltig, da ] nach den Checks fehlt');
                  return [None, None];
               #
               if (len(temp_check[0]) < 2):
                  print('# Warnung: Blockcheck in Zeile ' + str(aktuelle_zeile) + ' ungueltig, da Check(s) zu kurz');
                  return [None, None];
               #
               if (block_id in checks.keys()):
                  print('# Warnung: Block mit ID ' + str(block_id) + ' in Zeile ' + str(startzeile) + ' bereits definiert');
                  return [None, None];
               #
               temp_check = temp_check[0].split(',');
               checks.update([(block_id, temp_check)]);
               hat_checks = True;
               continue;
            #
            elif (zeile.startswith('# Block ')):
               print('# Warnung: Ungueltiger Block(anfang) in Zeile ' + str(aktuelle_zeile));
               return [None, None];
            elif (hat_checks):
               temp_block += zeile;
               continue;
            else:
               print('# Warnung: Blockcheck muss in der ersten Zeile eines neuen Blocks sein (fehlt in Zeile ' + str(aktuelle_zeile) + ')');
               return [None, None];
         #
         else:
            if (zeile.startswith('# End Block')):
               print('# Warnung: Ungueltiges Blockende in Zeile ' + str(aktuelle_zeile));
               return [None, None];
            elif (zeile.startswith('# Blockcheck')):
               print('# Warnung: Blockcheck ausserhalb eines Blocks in Zeile ' + str(aktuelle_zeile));
               return [None, None];
            elif (zeile.startswith('# Block ')):
               in_Block = True;
               hat_checks = False;
               zeilenteile = zeile.split(':');
               if (len(zeilenteile) < 2):
                  print('# Warnung: Blockzeile ' + str(aktuelle_zeile) + ' muss Doppelpunkt nach ID enthalten');
                  return [None, None];
               #
               temp_teile = zeilenteile[0].split();
               if (len(temp_teile) != 3):
                  print('# Warnung: Blockzeile ' + str(aktuelle_zeile) + ' ist nicht richtig formatiert');
                  return [None, None];
               #
               if (len(temp_teile[2]) != 6):
                  print('# Warnung: Block in Zeile ' + str(aktuelle_zeile) + ' hat eine ungueltige ID');
                  return [None, None];
               #
               block_id = temp_teile[2];
               startzeile = aktuelle_zeile;
         #
   #
   return [bloecke, checks];
#
