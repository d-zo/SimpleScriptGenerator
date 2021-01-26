
SimpleScriptGenerator 0.3.1
===========================

[SimpleScriptGenerator](https://github.com/d-zo/SimpleScriptGenerator)
is a graphical frontend for interactive script creation.
It uses three modifiable configuration files (which constitute a template)
to produce a script file (see [Structure and configuration](#structure-and-configuration)).
The program is written in Python and needs a working Python 3.x environment.

SimpleScriptGenerator can be used with different templates for different purposes.
Projects made with the loaded template can be loaded, saved and exported.
The saved projects are stored in JSON files (in a structure defined in the template)
and the exported projects are saved in a different format.
Since exported projects can't be re-read,
it is recommended to save the projects additionally as JSON files.

The predecessor of SimpleScriptGenerator was created alongside work
at the Institute of Geotechnical Engineering at the Hamburg University of Technology.
Its functionality is provided as a template (set of configuration files) named _abapys_front_
to generate scripts based on functions of the
[abapys](https://github.com/d-zo/abapys) library.
A part of this document describes the usage of SimpleScriptGenerator with the abapys_front
template (see [abapys_front template](#abapys_front-template)).



Installation and running the program
------------------------------------

SimpleScriptGenerator requires a working Python 3.x environment and
can be downloaded and run with Python.
To run SimpleScriptGenerator directly,
browse to the SimpleScriptGenerator folder and run `SimpleScriptGenerator.pyz`
with the Python interpreter.
A Graphical User Interface (GUI) will open,
if a template is found or provided.

In Linux the following commands can be used in a shell
(the first command has to be adjusted to point to the right directory).

```
cd /path/to/SimpleScriptGenerator
python3 SimpleScriptGenerator.pyz
```

In Windows a batch file can be created to provide access to SimpleScriptGenerator from anywhere.
Therefore, the path to the Python interpreter and the path to SimpleScriptGenerator have to be
defined in the following code.

```
@echo off
pushd C:\path\to\SimpleScriptGenerator
C:\path\to\Python\python.exe C:\path\to\SimpleScriptGenerator\SimpleScriptGenerator.pyz
pause
```

If a template is used which files are not located directly in a folder called `Vorlagen`,
the path to the template has to be provided as an argument when running SimpleScriptGenerator.
A template consists of three files `vorlagenlogik.json`, `einstellungen.json` and `codeblock.txt`,
which have to be saved in the same folder
(see [Structure and configuration](#structure-and-configuration)).
The default structure is assumed to look as follows:

```
SimpleScriptGenerator ---+ SimpleScriptGenerator.pyz
                         + Vorlagen/     ---+ vorlagenlogik.json
                                            + einstellungen.json
                                            + codeblock.txt
```

If you have multiple templates,
specify the path to the template to use.
The templates can either be located in the SimpleScriptGenerator folder or somewhere else.
As an example the following structure is used,
where all templates are stored in a folder `SSG_templates`.

```
SimpleScriptGenerator ---+ SimpleScriptGenerator.pyz

SSG_templates         ---+ abapys_front    ---+ vorlagenlogik.json
                         |                    + einstellungen.json
                         |                    + codeblock.txt
                         |
                         + other_template  ---+ vorlagenlogik.json
                                              + einstellungen.json
                                              + codeblock.txt
```

To use the _abapys_front_ template with the structure shown, change the run command for Linux to

```
python3 SimpleScriptGenerator.pyz /path/to/SSG_templates/abapys_front
```

and for Windows to

```
C:\path\to\Python\python.exe C:\path\to\SimpleScriptGenerator\SimpleScriptGenerator.pyz C:\path\to\SSG_templates\abapys_front
```

While everything is controlled from the GUI,
the console output shows hints and warnings (or errors, if something went seriously wrong)
when the program is run.
It can usually be ignored unless you experience strange or unintended behaviour.
In that case be sure to check the console output for clues on what went wrong (and how to correct
it). If an issue is not caused by a template but by the program itself,
make sure to include the console log for the bug report (see [Contributing](#contributing)).



Structure and configuration
---------------------------

SimpleScriptGenerator needs a template (i.e. the three files `vorlagenlogik.json`,
`einstellungen.json` and `codeblock.txt`) to work.
If not specified otherwise, SimpleScriptGenerator expects these files in a folder called `Vorlagen`.
The configuration files of a template are structured in the following way:

 - `vorlagenlogik.json` defines `Name` and export file settings (in `Export`) for the template.
   The internal state variables of this template are defined as `Checks` and
   the logical dependencies and program structure as `Abhaengigkeiten`.
   The logic defined is interactively represented in the
   Graphical User Interface (GUI) of SimpleScriptGenerator.
   The state of the project will be defined by the state of the `Checks` and the actual internal
   variables (with double underscore before and after variable name).
   In the section `Nachbereitung` additional variable names used in the script may be defined.
   When exporting to a script,
   variables use a default format unless a format is specified for their name here.
 - `einstellungen.json` provides the default state and default internal variables for a new project
   as required by `vorlagenlogik.json`.
   The structure will be used to internally represent, load and save projects.
   The default values given here will be used unless overwritten by user input in the GUI or
   loading different values from a project file.
   If this file is changed and the structure does not fit to a previously saved project,
   this project must either be adjusted manually or
   can't be loaded with the changed configuration file.
 - `codeblock.txt` contains all code snippets which will be used on exporting a project.
   The code snippets are saved in blocks with a certain structure and logical checks.
   The checks depend on the state variables and logical dependencies originally
   defined in `checks.json`.
   Whenever a project is exported,
   the current state variables are used to check which blocks are to be inserted in the output.
   Afterwards, all internal variables are replaced by their values.
   The more states and dependencies used,
   the higher the complexity will be,
   to have this file produce useful scripts for all possible states.
   Changes in this file have the most significant influence on exported projects.


After starting SimpleScriptGenerator with any template,
the GUI is loaded with the default settings as defined in `einstellungen.json`.
A new project can be loaded by `Datei->Öffnen`, the current project can be saved by
`Datei->Speichern` and the current project can be exported to a code file
(as defined in `vorlagenlogik.json`) by `Datei->Exportieren`.

SimpleScriptGenerator automatically reads values as soon as the focus leaves the input field
(no need to press the `Enter`-key).
Before updating a value in the structure,
the format is checked based on the default or previously accepted entry.
For example,
if the previous value was an integer,
the current value must also be an integer (not dot allowed).
For floats, the dot is required and for (possibly nested) lists,
the parentheses/brackets have to be in balance.
If the test is not successfull,
the background color of the entry is changed to orange and a warning is issued in the console.
The entry will not be saved unless the error is resolved.



abapys_front template
---------------------

abapys_front is a template to make a more intuitive use of the
[abapys](https://github.com/d-zo/abapys) library.
abapys is a library to support script based working with the
commercial Finite-Element-Analysis software
[Abaqus](https://www.3ds.com/products-services/simulia/products/abaqus/ "SIMULIA Abaqus").
The intention of the abapys_front template is to interactively create complete Python scripts,
which can be run in Abaqus.
The scripts can create whole models or process the output of finished simulations.
Since SimpleScriptGenerator only creates the scripts,
Abaqus is not needed to work with the abapys_front template.

It is recommended to have some basic Abaqus experience to understand,
what the options do.
Still, there are some challenges with the current template, especially for new users:

 - some variables might not be understood without a better description in the GUI (image/sketch)
 - some entry field require nested lists of values, which are not obvious for new users
   and don't fit into the entry area without scrolling

When starting with the abapys_front template,
it is recommended to export a project with the default settings,
run it in Abaqus and try to understand the Python script.
There are some additional comments in the script file (i.e. in the `codeblock.txt` file which
will be assembled into a script file) which might be helpful.
Afterwards, the default settings in the project can be changed (not all at once),
the project can be exported as another Python script and run in Abaqus/compared to the other script.



Contributing
------------

**Bug reports**

If you found a bug, make sure you can reproduce it with the latest version of SimpleScriptGenerator.
Please check that the expected results can actually be achieved and are not caused by an error
in customized configuration files.
Please give detailed and reproducible instructions in your report including

 - the SimpleScriptGenerator version
 - the expected result
 - the result you received
 - the actions/command(s) used

Note: The bug should ideally be reproducible with the default configuration.
If it is caused by a customized configuration,
try to adjust the default configuration until the cause can be identified.


**Feature requests**

If you have an idea for a new feature, consider searching the
[open issues](https://github.com/d-zo/SimpleScriptGenerator/issues) and
[closed issues](https://github.com/d-zo/SimpleScriptGenerator/issues?q=is%3Aissue+is%3Aclosed) first.
Afterwards, please submit a report in the
[Issue tracker](https://github.com/d-zo/SimpleScriptGenerator/issues) explaining the feature and especially

 - why this feature would be useful (use cases)
 - what could possible drawbacks be (e.g. compatibility, dependencies, ...)



License
-------

SimpleScriptGenerator is released under the
[GPL](https://www.gnu.org/licenses/gpl-3.0.html "GNU General Public License"),
version 3 or greater (see also [LICENSE](https://github.com/d-zo/SimpleScriptGenerator/blob/master/LICENSE) file).
It is provided without any warranty.

