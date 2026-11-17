# Repository structure

This repository holds the companion material for the book *AI Integration in AEC Education: Frameworks, Tools, and Pedagogical Applications*. Everything is organised by chapter.

## Top level

```
AI-Integration-in-Construction-Education/
├── index.html                  # Companion website (GitHub Pages)
├── README.md                   # Introduction and chapter list
├── CONTRIBUTING.md             # How authors send companion material
├── REPOSITORY-STRUCTURE.md     # This document
├── LICENSE                     # CC BY-NC 4.0 (content)
├── assets/editors/             # Editor photographs used by index.html
├── docs/
│   ├── book-info/              # Title, editors, parts and chapters
│   ├── contributor-guidelines/ # Pointer to CONTRIBUTING.md
│   └── graphics/               # Banner and site graphics
├── templates/                  # Layout of each chapter README
└── chapters/                   # One folder per chapter (15)
    ├── Chapter_01_Tummalapudi_AI-Simple-Terms/
    ├── Chapter_02_Cheng_AI-Literacy/
    ├── Chapter_03_Martek_AI-Engineering-Education/
    ├── Chapter_04_Kassem_AI-Capability-Framework/
    ├── Chapter_05_Hosseini_AI-Ethics-Foundations/
    ├── Chapter_06_Gaspar_Teaching-Methodologies/
    ├── Chapter_07_Bartels_AI-Education-Germany/
    ├── Chapter_08_Debs_GPT-LLM-Benefits/
    ├── Chapter_09_Katooziani_LLM-Adaptive-Learning/
    ├── Chapter_10_Hosseini_Construction-Data-for-AI/
    ├── Chapter_11_Hosseini_Data-Centres/
    ├── Chapter_12_Hosseini_AI-Assisted-Programming/
    ├── Chapter_13_McArthur_Digital-Twins/
    ├── Chapter_14_Hosseini_Agentic-AI/
    └── Chapter_15_Hosseini_AI-Ethics-Operationalisation/
```

## Inside a chapter folder

Subfolders exist only where the chapter has that kind of material.

```
chapters/Chapter_NN_Author_Short-Title/
├── README.md       # Title, authors, part, status, abstract, materials, citation, licence
├── appendices/     # Appendices, checklists and worksheets (.docx, .pdf, .md, .ipynb)
├── code/           # Scripts and software, with their own LICENSE (MIT)
├── datasets/       # Companion data files (added when files arrive)
├── slides/         # Teaching slides (added when files arrive)
├── figures/        # Figure files as supplied during manuscript preparation
└── assets/         # Images used by the chapter README (Chapter 12 only)
```

## Naming

- New companion files: `NN_Short_Name.ext`, for example `01_Site_Selection_Worksheet.docx`.
- Chapter folders keep the names shown above. Some addresses inside these folders are printed in the book; see "Protected paths" in [CONTRIBUTING.md](CONTRIBUTING.md#8-protected-paths).
