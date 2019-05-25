CONTENTS

1. INTRODUCTION
2. PROBLEM STATEMENT
3. METHODOLOGY
4. RESULTS
5. CONCLUSION AND FUTURE WORK
6. REFERENCES 
INTRODUCTION
Sustainability is the development that satisfies the needs of the present without compromising the capacity of future generations, guaranteeing the balance between economic growth, care for the environment and social well-being. 
Since 2000, there has been enormous progress in achieving the target of universal primary education. Achieving inclusive and quality education for all reaffirms the belief that education is one of the most powerful and proven vehicles for sustainable development. This goal ensures that all girls and boys complete free primary and secondary schooling by 2030. It also aims to provide equal access to affordable vocational training, to eliminate gender and wealth disparities, and achieve universal access to a quality higher education.
This project IDE FOR BLIND will endeavor to provide a coding environment (IDE) tailored to the needs of the blind to help them earn a basic earning through the use of a useful skill. This Integrated development is to help those coders who have lost their sight to use their coding skills even now in an environment friendly and adaptive to there need to code and develop in python.This project deals with all the basic codes of Python. It helps the user/coder by interacting with the user in speech format. 
This project consist of a text editor, dedicated input window, descriptive output window, list box with autocomplete suggestions, dedicated hotkeys binded with different keyboard shortcuts for various functions like complie, autocomplete, code in speech format, save, open file etc. 





 
PROBLEM STATEMENT
In World there are disparities in education and still equal access to all levels of education isn’t assured .Education if provided to all it might provide with vocational training for person with disabilities.
Inequality within and among countries that discriminates on the basis of the social, economic and political, age, sex, disability, race, ethnicity, origin, religion or economic or other status.

Approach towards the problem
In order to deal with various problems discussed above this project helps in providing the needs of the blind to help them earn a basic earning through the use of a useful skill. Project helps the person with sight disability in coding with Python language by speaking the code line by line , guiding the user on where the cursor is placed, output of current complied code, errors and autocompleting various syntax in code. 

Sustainable Development Goal
Goal : Quality Education
Target 4.5 : By 2030, eliminate gender disparities in education and ensure equal access to all levels of education and vocational training for the vulnerable, including persons with disabilities, indigenous peoples and children in vulnerable situations 
Goal : Reduce inequality within and among countries 
Target 10.2 : By 2030, empower and promote the social, economic and political inclusion of all, irrespective of age, sex, disability, race, ethnicity, origin, religion or economic or other status




METHODOLOGY
MODULE DIAGRAM:
 
MODULE DESCRIPTION:
1. GUI(Tkinter): To develop GUI(graphical user interface) of project,tkinter a standard Python interface is used.Tkinter is a Python binding to the Tk GUI toolkit. It is the standard Python interface to the Tk GUI toolkit, and is Python's de facto standard GUI. As with most other modern Tk bindings, Tkinter is implemented as a Python wrapper around a complete Tcl interpreter embedded in the Python interpreter. Tkinter calls are translated into Tcl commands which are fed to this embedded interpreter, thus making it possible to mix Python and Tcl in a single application.
It comes with various widgets that have been used in the project:
•	Text Box 
•	List Box
•	Message Label
•	Menu
•	Key binding
2. PYTTSX3: Pyttsx is a good text to speech conversion library in python but it was written only in python2 untill now .Even some fair amount of googling didn’t help much to get a tts library compatible with Python3.
There is however , one library gTTS which works perfectly in python3 but it needs internet connection to work since it relies on google to get the audio data.But Pyttsx is completely offline and works seemlesly and has multiple tts-engine support.The codes in this repos are slightly modified version of the pyttsx module of python 2.x and is a clone from westonpace’s repo. The purpose of creating this repo is to help those who want to have an offline tts lib for Python3 and don’t want to port it from python2 to python3 themselves.
3. JEDI(an awesome autocompletion/static analysis library for Python): Jedi is a static analysis tool for Python that can be used in IDEs/editors. Its historic focus is autocompletion, but does static analysis for now as well. Jedi is fast and is very well tested.Jedi has support for two different goto functions. It’s possible to search for related names and to list all names in a Python file and infer them. 
Jedi is pretty simple and allows you to concentrate on writing a good text editor, while still having very good IDE features for Python.
class jedi.Script(source=None, line=None, column=None, path=None, encoding='utf-8', sys_path=None, environment=None)
A Script is the base for completions, goto or whatever you want to do with Jedi.You can either use the source parameter or path to read a file. Usually you’re going to want to use both of them (in an editor).
The script might be analyzed in a different sys.path than Jedi:
•	if sys_path parameter is not None, it will be used as sys.path for the script.
•	if sys_path parameter is None and VIRTUAL_ENV environment variable is defined, sys.path for the specified environment will be guessed (see jedi.evaluate.sys_path.get_venv_path()) and used for the script.
•	otherwise sys.path will match that of Jedi.
Parameters:	•	source (str) – The source code of the current file, separated by newlines.
•	line (int) – The line to perform actions on (starting with 1).
•	column (int) – The column of the cursor (starting with 0).
•	path (str or None) – The path of the file in the file system, or ''if it hasn’t been saved yet.
•	encoding (str) – The encoding of source, if it is not a Unicode object (default 'utf-8').
•	sys_path (Environment) – sys.path to use during analysis of the script
•	environment – TODO

completions()
Return classes.Completion objects. Those objects contain information about the completions, more than just names.
Returns:	Completion objects, sorted by name and __ comes last.
Return type:	list of classes.Completion

4.PYNPUT: This library allows you to control and monitor input devices. It contains subpackages for each type of input device supported:
pynput.mouse: Contains classes for controlling and monitoring a mouse or trackpad.
pynput.keyboard: Contains classes for controlling and monitoring the keyboard.
All modules mentioned above are automatically imported into the pynput package. To use any of them, import them from the main package.
5. VB AND BAT SCRIPTS: VBScript is an Active Scripting language developed by Microsoft that is modelled on Visual Basic. It allows Microsoft Windows system administrators to generate powerful tools for managing computers with error handling, subroutines, and other advanced programming constructs.
A batch file is a kind of script file in DOS, OS/2 and Microsoft Windows. It consists of a series of commands to be executed by the command-line interpreter, stored in a plain text file.
We have executed the user’s code through bat script and we used VBScript to run it in the background.


RESULTS
HARDWARE REQUIREMENTS:
•	Braille Keyboard:The Braille Keyboard for the Blind and Visually Impaired is a braille keyboard designed for use by individuals who are blind or have low vision. This 104-key keyboard is equipped with clear braille labels that allow the original key legends to show through enabling both blind and sighted users access to the keyboard.
•	A computer with minimum of 1GB of RAM and Dual Core Processor with windows Operating System.
•	A speaker.

SOFTWARE REQUIREMENTS:
•	Python 3.5.2 
•	Python Libraries:
o	Pyttsx3
o	Jedi
o	Tkinter
o	pynput


