# LaTeX-Vorlage

## Form
Gemäß Vorlesung „Wissenschaftliches Arbeiten“.

# Programme
Der PTB wurde mit [LaTeX](https://www.latex-project.org/) erstellt.
Als Editor wurde [TeXstudio](https://www.texstudio.org/) genutzt. Hier müssen die Standarteinstellungen des Compilers
des Literaturverzeichnisses auf biber.exe umgestellt werden.

Als Literaturverzeichniss wurde [BibTEX](http://www.bibtex.org/de/) in verbindung mit dem compiler biber genutzt. 

Zur grafischen Bearbeitung des Literturverzeichnisses wurde [JabRef](https://www.jabref.org/) genutzt.


# LaTeX Vorraussetzungen
## Bibtex
Für das Literaturverzeichniss wurde Bibtex in verbindung mit biber genutzt.
In den Einstellungen vom Texstudio muss also unter dem Menüpunkt **Erzeugung** das Standarf Bibliographieprogramm auf biber umgestellt werden.

## minted
Für die deutlich bessere Einbindung und Syntaxhervorhebung von Quellcode wurde das Paket [minted](https://github.com/gpoore/minted) verwendet.
Um das Paket verwenden zu können, wird Python 2.7.X und das python Paket pygments benötigt.

[Anleitung Stackoverflow](https://tex.stackexchange.com/questions/108661/how-to-use-minted-under-miktex-and-windows-7)
1. Python 2.7.X [herunterladen](https://www.python.org/downloads/) und installieren. Beim installieren ist darauf zu achten dass Python auch in den Umgebungsvariablen angepasst wird.
2. Pythons Paketverwaltung pip installieren
3. Das Paket pygments installieren
    * ```pip install pygments```
4. Den Zugriff auf externe Programme für den Compiler ````-shell-escape```` erlauben.
    * in Den Einstellungen von TexStudio unter dem Menüpunkt **Befehle** den Befehlt für PdfLaTeX mit ````-shell-escape```` ergänzen. Aus dem Standard Befehl ```pdflatex.exe -synctex=1 -interaction=nonstopmode %.tex``` wird dann ```pdflatex.exe -shell-escape -synctex=1 -interaction=nonstopmode %.tex```
