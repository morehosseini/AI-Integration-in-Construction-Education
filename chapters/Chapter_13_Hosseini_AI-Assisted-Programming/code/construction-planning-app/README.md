# Construction Planning & Scheduling Application

A human-in-the-loop AI-assisted tool for generating preliminary construction schedules based on minimal project briefs. Built with AI assistance using the chapter's four-stage Design Science Research (DSR) workflow.

## 📂 Project Structure

- **`app/`**: The core Streamlit application code.
  - **`app/core/`**: Deterministic engines — CPM, validation, calendar, procurement, and Excel export.
  - **`app/libraries/`**: Static data grounding — production rates, procurement leads, calendars, WBS templates.
  - **`app/pages/`**: Streamlit multi-page UI (brief → PIR → basis → schedule → export → knowledge).
- **`requirements.txt`**: Python dependencies.

### Related Documentation

- **[Development Journey](../development-history/DEVELOPMENT_JOURNEY.md)**: A full log of how this app was built, including expert reviews and design shifts.
- **[Planning Documents](../development-history/planning/)**: Initial design documents and technical plans.

## 🚀 How to Run Locally

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set your API Key:**
   ```bash
   export GEMINI_API_KEY=your_key_here
   ```

3. **Run the App:**
   ```bash
   streamlit run app/main.py
   ```

4. **Access in Browser:**
   Open [http://localhost:8501](http://localhost:8501)

---
*Companion code for "AI-Assisted Programming: Turning Construction Professionals into Citizen Developers" (Hosseini, Xie, Herrera, Kassem)*
