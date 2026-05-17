# AI-Assisted Programming: Turning Construction Professionals into Citizen Developers

**Authors:** M. Reza Hosseini, Xiao Xie, Rodrigo F. Herrera, Mohamad Kassem

---
*Part of the AI Integration in AEC Education Repository*

---

## Overview

This chapter addresses a critical gap in construction education: the ability of construction professionals to build their own digital tools using AI as a programming partner. Rather than replacing programmers or producing autonomous agents, the chapter demonstrates a **human-in-the-loop partnership** where the professional frames the problem, directs the AI to write code, reviews the output, and retains full accountability for the result.

The chapter introduces a four-stage **Design Science Research (DSR)** workflow for AI-assisted tool creation and demonstrates it through two complete worked examples — a small data-analysis script and a full construction-planning application.

## Key Concepts

- **Citizen Developer Model** — construction professionals who create functional software tools by directing an AI assistant, without formal programming training.
- **Constrained Prompt Engineering** — writing precise prompts that specify libraries, constraints, error handling, and output formats to control what the AI generates.
- **Hybrid Intelligence Architecture** — pairing an LLM (for interpreting briefs and generating text) with a deterministic engine (for calculations, CPM logic, and data lookups).
- **Human-in-the-Loop Design** — mandatory approval gates where the human expert reviews, adjusts, and signs off before the AI proceeds.
- **Data Grounding** — using static, curated data libraries (production rates, procurement leads) instead of relying on the LLM's internal weights for factual construction data.

## Supplementary Code and Materials

All companion code is provided in the [`code/`](code/) directory.

### 1. Cost Analysis Worked Example

📂 [`code/cost-analysis/`](code/cost-analysis/)

A small, self-contained Python script that analyses construction cost data and charts budget variance. This is the introductory example walked through in the chapter, demonstrating how a single well-constrained prompt produces a working, auditable tool.

**What it does:**
- Reads a CSV of construction cost data (budgeted vs. actual by work package)
- Computes variance and flags over/under-budget packages
- Produces a bar chart saved as `cost_variance.png`

**The prompt that generated it:**
> *Write a Python script that analyses construction cost data from a CSV file.*
> *Constraints: Use only pandas and matplotlib. Do not call external APIs. Handle missing values. Calculate variance between budgeted and actual cost per work package. Produce a bar chart and save it as an image file.*

**To run:**
```bash
cd code/cost-analysis
pip install pandas matplotlib
python construction_cost_analysis.py
```

---

### 2. Construction Planning Application

📂 [`code/construction-planning-app/`](code/construction-planning-app/)

A complete, runnable Streamlit application — the full worked example of the chapter's four-stage DSR framework. It takes a one-line project brief and scaffolds a professional preliminary CPM schedule through a five-stage workflow:

1. **Brief Interpretation** — LLM parses the project brief and asks clarifying questions
2. **Project Information Request** — collects structured project parameters
3. **Basis of Schedule** — maps activities to curated production rate libraries
4. **Schedule Generation** — deterministic Python CPM engine calculates dates, float, and critical path
5. **Excel Export** — produces a downloadable schedule with full audit trail

**Architecture:**
| Layer | Role | Technology |
|---|---|---|
| **LLM Layer** | Interprets briefs, generates narrative, asks questions | Google Gemini API |
| **Engine Layer** | CPM calculations, float, GFA arithmetic | Deterministic Python |
| **Library System** | Production rates, procurement leads, calendars | Static CSV/JSON files |
| **UI Layer** | Interactive multi-page interface | Streamlit |

**To run locally:**
```bash
cd code/construction-planning-app
pip install -r requirements.txt
# Set your Gemini API key
export GEMINI_API_KEY=your_key_here
streamlit run app/main.py
```

**Live demo:** [https://teaching-tools-falzwuuzw6rq8ntn93prcg.streamlit.app](https://teaching-tools-falzwuuzw6rq8ntn93prcg.streamlit.app)

> **Note:** The live demo requires a Gemini API key. Students can explore the source code structure and static libraries without one.

---

### 3. Development History

📂 [`code/development-history/`](code/development-history/)

The complete record of how the planning application was designed and built — including the specification, the design plan, and the rounds of expert critique that reshaped the architecture. This folder is a real, worked instance of the chapter's four-stage DSR framework, showing:

- **`DEVELOPMENT_JOURNEY.md`** — narrative of the full development process, including the critical pivot from full automation to human-in-the-loop scaffolding
- **`planning/`** — architecture analysis, approach documents, and the final implementation plan

This is provided for transparency and as a teaching resource. Students can trace the design decisions that led to the final application architecture.

## How to Use This Chapter

### For Students
- **Start** with the cost analysis example — run it, read the prompt, modify it for your own data
- **Explore** the planning application source code — identify where AI prompts end and deterministic Python logic begins
- **Read** the development history — understand how the architecture evolved through critique
- **Adapt** the constrained prompting approach to your own construction problems

### For Educators
- **Use the cost analysis script** as a ready-made tutorial exercise (30–45 min)
- **Use the planning application** as a case study for discussing hybrid AI architectures
- **Assign** the development history as required reading to demonstrate iterative, evidence-based design
- **Challenge students** to build their own tool using the four-stage DSR framework

## Requirements

- Python 3.10 or later
- Each example lists its own dependencies in `requirements.txt` or inline
- The planning application requires a Google Gemini API key for full functionality

## Related Resources

- [OpenAI — A Practical Guide to Building Agents (PDF)](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf)
- [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)
- [n8n Documentation](https://docs.n8n.io/)
- [MindStudio University](https://university.mindstudio.ai/)

## Citation

> Hosseini, M.R., Xie, X., Herrera, R.F., & Kassem, M. (2026). AI-Assisted Programming: Turning Construction Professionals into Citizen Developers. In M.R. Hosseini (Ed.), *AI Integration in Construction Education: Methods and Resources*. Routledge/Taylor & Francis.

---

## Licence

See the repository [`LICENSE`](../../../LICENSE) file.
