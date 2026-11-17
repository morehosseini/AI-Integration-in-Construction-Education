# Contributing companion material

This guide is for the authors of *AI Integration in AEC Education: Frameworks, Tools, and Pedagogical Applications* (CRC Press / Taylor & Francis). It explains how to add companion material for your chapter to this repository.

Anything added here is public. The editor, M. Reza Hosseini, approves every addition before it is published.

## 1. What can be submitted

Companion material that supports your chapter:

- appendices, checklists and worksheets
- datasets
- code and notebooks
- slides and teaching activities

Please do not submit chapter text or the book's figures unless the editor has agreed.

## 2. How to submit

- **Default (no GitHub needed).** Send your files to the editor by email or through a shared Drive folder. The editor checks them and adds them to the repository. Contact details are on the [book's website](https://morehosseini.github.io/AI-Integration-in-Construction-Education/).
- **If you use GitHub.** Pull requests are welcome. Fork the repository, add your files to the right folder (section 3), and open a pull request against `main`. Please do not push to `main` directly.
- **Updating a file that is already here.** Send the new version under the same file name, so that any address printed in the book keeps working.

## 3. Where files go

Put each file in your chapter's folder, `chapters/<your chapter folder>/`, in the matching subfolder:

| Subfolder | For |
|---|---|
| `appendices/` | appendices, checklists, worksheets |
| `code/` | scripts, notebooks and software (with a `LICENSE`, see section 6) |
| `datasets/` | data files |
| `slides/` | slides and teaching activities |

Subfolders are created only when files arrive, because Git does not keep empty folders. Do not rename or move the chapter folders (section 8).

## 4. Naming

Use `NN_Short_Name.ext`, where `NN` is a two-digit order number: for example `01_Site_Selection_Worksheet.docx` or `02_Sample_Cost_Data.csv`. Use letters, numbers and underscores, without spaces.

Do not include personal data (student names or numbers, private email addresses) in file names or contents.

## 5. Formats

`.docx`, `.pdf`, `.md`, `.ipynb`, `.py`, `.csv` and `.xlsx`. If you need another format, ask the editor first. If a file is larger than 25 MB, contact the editor before sending it.

## 6. Rights and licences

- Submit only material you have the right to share. Do not include third-party material (text, figures, screenshots, data) without written permission, and name the source inside the file.
- Code is released under the MIT licence: place a `LICENSE` file in the chapter's `code/` folder (see [Chapter 12's](chapters/Chapter_12_Hosseini_AI-Assisted-Programming/code/LICENSE) for an example).
- All other content is released under CC BY-NC 4.0, see the repository [LICENSE](LICENSE).

## 7. Review

The editor reviews every addition before it is merged. This includes pull requests, which are not published until the editor merges them.

## 8. Protected paths

The book prints or describes these addresses, so they must never be renamed, moved or deleted:

- the 15 chapter folder names under `chapters/`
- `LICENSE` (repository root)
- `chapters/Chapter_10_Hosseini_Construction-Data-for-AI/appendices/` and its five files (four appendices and `Lab_data_preprocess.ipynb`)
- `chapters/Chapter_11_Hosseini_Data-Centres/appendices/Appendix_A_Data_Centre_Site_Selection_Checklist.md`
- `chapters/Chapter_12_Hosseini_AI-Assisted-Programming/` and, inside it, `code/LICENSE`, `code/cost-analysis/` and `code/construction-planning-app/` (including `app/core/cpm_engine.py`, `app/core/excel_export.py`, `app/core/validation_engine.py` and `app/libraries/production_rates.csv`)
- `chapters/Chapter_14_Hosseini_Agentic-AI/` and its four appendices

---
Questions? Contact the editor through the [book's website](https://morehosseini.github.io/AI-Integration-in-Construction-Education/).
