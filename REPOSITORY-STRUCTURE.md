# AI Integration in AEC Education - Repository Structure

This repository contains the supplementary materials for the book *AI Integration in AEC Education*. The content is organized by chapter in a flat structure.

## Directory Structure

```
AI-Integration-in-Construction-Education/
│
├── index.html                          # Public-facing companion website
├── README.md                           # Repository introduction and chapter status
├── CONTRIBUTING.md                     # Guidelines for authors uploading material
├── REPOSITORY-STRUCTURE.md             # This document
├── LICENSE                             # Copyright and licensing (CC BY-NC 4.0)
│
├── docs/                               # General documentation and shared assets
│   └── graphics/                       # Banners and site graphics
│
└── chapters/                           # Chapter materials
    ├── Chapter_01_Tummalapudi_AI-Simple-Terms/
    ├── Chapter_02_Cheng_AI-Literacy/
    └── ... (15 chapters total)
```

## Inside Each Chapter Folder

Each chapter folder uses a standard template. Subfolders are only present if the chapter has that specific type of material.

```
chapters/Chapter_NN_Author_Short-Title/
├── README.md            # Chapter landing page with title, authors, and abstract
├── figures/             # Final, publication-ready figures (PNG, SVG, TIFF, PDF)
├── appendices/          # Checklists, detailed tables, or supplementary text (.docx/.md)
├── code/                # Scripts, notebooks, or software projects
├── datasets/            # Sample or companion data files
└── assets/              # README-embedded images (distinct from published figures)
```

## File Naming Conventions
When uploading materials, authors should use clear, descriptive names:
- **Figures:** `Figure_1_Descriptive_Name.png`
- **Appendices:** `Appendix_A_Title.docx`
- **Code:** `analysis_script.py`
