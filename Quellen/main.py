#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from datetime import datetime

import bibtexparser
import pdfkit

# **********************************************************************************************************************
#  Einstellungen
# **********************************************************************************************************************
current_path = os.path.normpath(os.path.join(os.path.abspath(__file__), "..", "..", "Inhalt"))
bibtex_path = os.path.join(current_path, 'literaturverzeichnis_old.bib')
rel_pdf_path = "./Quellen/"
# **********************************************************************************************************************
#  Einstellungen Ende
# **********************************************************************************************************************


date_format = "%Y-%m-%d"
print("start")


def render_pdf_from_url(bib_database):
    for entry in bib_database.entries:
        # Wenn es sich nicht um eine Internetquelle handelt
        if entry["ENTRYTYPE"] != "misc":
            continue

        # oder der Link zur pdf unter 'note' nicht bereits gesetzt wurde
        if "note" in entry:
            continue

        # oder es keine url gibt
        if "url" not in entry:
            continue

        print(entry)

        pdf_name = entry["ID"].replace(":", "_") + ".pdf"
        try:
            pdf = pdfkit.from_url(entry["url"], output_path=os.path.join(current_path, pdf_name))
            note = "\href{run:" + rel_pdf_path + pdf_name + "}{export.pdf}"
            entry["note"] = note
        except Exception as e:
            print(e)

        entry["urldate"] = datetime.now().strftime(date_format)

        print(entry)
        print("\n")

    # Neue.bib Datei Speichern
    with open(os.path.join(current_path, "test.bib"), 'w') as bibtex_file:
        bibtexparser.dump(bib_database, bibtex_file)


def set_file_link_name(database):
    for entry in database.entries:
        # print(entry)
        if "note" in entry:
            note = entry["note"]
            try:
                filename = note.split(rel_pdf_path)[1].split("}")[0]
                filename = filename.replace("_", " ")
                note = note.replace("export.pdf", filename)
                entry["note"] = note

            except Exception as e:
                print(e)
                print(entry)

        else:
            pass
            print("**********************************")
            print(entry)
            print("**********************************")

    print(database.entries)


    # Neue.bib Datei Speichern
    with open(os.path.join(current_path, "test.bib"), 'w', encoding="utf8") as bibtex_file:
        bibtexparser.dump(database, bibtex_file)






if __name__ == '__main__':
    with open(bibtex_path, encoding="utf8") as bibtex_file:
        bibtex_str = bibtex_file.read()

        bib_database = bibtexparser.loads(bibtex_str)



    set_file_link_name(bib_database)
