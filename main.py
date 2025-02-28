# %%
import os
import fitz

# %%
original_pdf = "/Users/longluong/Zotero/storage/BJUI3KDQ/Simon and Blume - 1994 - Mathematics for economists.pdf"
new_pdf = ""

# %% Test

doc = fitz.open(original_pdf)
page = doc[0].get_textpage_ocr()

# %%
# Toc structure:
# List of a list of 3 elements:
# [lvl, title, page]


def create_toc(pdf_path):
    doc = fitz.open(pdf_path)

    return toc
