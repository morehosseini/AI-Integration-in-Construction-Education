---
layout: default
---

<style>
/* Custom styling for AI in Construction Education */
:root {
  --primary: #1e40af;
  --secondary: #f97316;
  --light-bg: #f8fafc;
  --card-bg: #ffffff;
  --dark: #1e293b;
}

.main-content h2 {
  color: var(--primary);
  text-align: center;
  position: relative;
  padding-bottom: 0.75rem;
  margin-bottom: 2rem;
}

.main-content h2::after {
  content: "";
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 80px;
  height: 3px;
  background-color: var(--secondary);
}

.card {
  background-color: var(--card-bg);
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
  padding: 1.5rem;
  margin-bottom: 2rem;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
}

.chapter-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 1.5rem;
  margin-top: 2rem;
}

.chapter-card {
  background-color: var(--card-bg);
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  padding: 1.5rem;
  text-align: center;
  transition: all 0.3s ease;
  border-top: 3px solid transparent;
}

.chapter-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 15px rgba(0, 0, 0, 0.1);
  border-top: 3px solid var(--secondary);
}

.chapter-card h3 {
  color: var(--primary);
  margin-top: 0;
  margin-bottom: 0.5rem;
}

.chapter-card p {
  font-size: 0.95rem;
  margin-bottom: 1rem;
}

.view-btn {
  display: inline-block;
  color: var(--primary);
  font-weight: 500;
  text-decoration: none;
  position: relative;
}

.view-btn::after {
  content: "→";
  margin-left: 5px;
  transition: transform 0.3s ease;
  display: inline-block;
}

.view-btn:hover {
  color: var(--secondary);
}

.view-btn:hover::after {
  transform: translateX(5px);
}

.resources-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
  margin-top: 2rem;
}

.resource-card {
  background-color: var(--card-bg);
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
  padding: 1.5rem;
  text-align: center;
  transition: all 0.3s ease;
}

.resource-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
}

.resource-icon {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  color: var(--primary);
}

.download-btn {
  display: inline-block;
  padding: 0.5rem 1.25rem;
  background-color: var(--primary);
  color: white;
  border-radius: 4px;
  text-decoration: none;
  font-weight: 500;
  transition: all 0.3s ease;
  margin-top: 1rem;
}

.download-btn:hover {
  background-color: var(--secondary);
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  text-decoration: none;
  color: white;
}

.author-card {
  background-color: var(--card-bg);
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
  padding: 2rem;
  margin-top: 2rem;
  text-align: center;
}

.profile-btn {
  display: inline-block;
  padding: 0.6rem 1.2rem;
  margin: 0 0.5rem;
  background-color: var(--primary);
  color: white;
  border-radius: 4px;
  text-decoration: none;
  font-weight: 500;
  transition: all 0.3s ease;
}

.profile-btn:hover {
  background-color: var(--secondary);
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  text-decoration: none;
  color: white;
}

@media (max-width: 768px) {
  .chapter-grid,
  .resources-grid {
    grid-template-columns: 1fr;
  }
}
</style>

## About the Book

<div class="card">
  <p>"AI Integration in Construction Education: Methods and Resources" provides a comprehensive framework for educators to incorporate artificial intelligence concepts into construction education curricula.</p>
  
  <h3 style="color: #1e40af; margin-top: 1.5rem;">Key Features</h3>
  <ul>
    <li><strong>Practical Teaching Resources:</strong> Ready-to-use lesson plans, exercises, and assessments</li>
    <li><strong>Code Examples:</strong> Hands-on AI applications specific to construction challenges</li>
    <li><strong>Implementation Guidelines:</strong> Step-by-step guidance for educators at various levels</li>
    <li><strong>Industry Connections:</strong> Materials that bridge academic learning with industry practice</li>
  </ul>
</div>

## Book Chapters

<p>Explore the supplementary materials for each chapter:</p>

<div class="chapter-grid">
  <div class="chapter-card">
    <h3>Chapter 1</h3>
    <p>Introduction to AI in Construction</p>
    <a href="Chapters/Chapter1/" class="view-btn">View Materials</a>
  </div>
  
  <div class="chapter-card">
    <h3>Chapter 2</h3>
    <p>Machine Learning Fundamentals</p>
    <a href="Chapters/Chapter2/" class="view-btn">View Materials</a>
  </div>
  
  <div class="chapter-card">
    <h3>Chapter 3</h3>
    <p>Data Collection and Processing</p>
    <a href="Chapters/Chapter3/" class="view-btn">View Materials</a>
  </div>
  
  <div class="chapter-card">
    <h3>Chapter 4</h3>
    <p>AI Applications in Construction Management</p>
    <a href="Chapters/Chapter4/" class="view-btn">View Materials</a>
  </div>
  
  <div class="chapter-card">
    <h3>Chapter 5</h3>
    <p>Building Information Modeling and AI</p>
    <a href="Chapters/Chapter5/" class="view-btn">View Materials</a>
  </div>
  
  <div class="chapter-card">
    <h3>Chapter 6</h3>
    <p>Computer Vision in Construction</p>
    <a href="Chapters/Chapter6/" class="view-btn">View Materials</a>
  </div>
  
  <div class="chapter-card">
    <h3>Chapter 7</h3>
    <p>Natural Language Processing for Construction</p>
    <a href="Chapters/Chapter7/" class="view-btn">View Materials</a>
  </div>
  
  <div class="chapter-card">
    <h3>Chapter 8</h3>
    <p>Predictive Analytics in Construction</p>
    <a href="Chapters/Chapter8/" class="view-btn">View Materials</a>
  </div>
  
  <div class="chapter-card">
    <h3>Chapter 9</h3>
    <p>AI Ethics and Implementation Challenges</p>
    <a href="Chapters/Chapter9/" class="view-btn">View Materials</a>
  </div>
  
  <div class="chapter-card">
    <h3>Chapter 10</h3>
    <p>Case Studies of AI in Construction Education</p>
    <a href="Chapters/Chapter10/" class="view-btn">View Materials</a>
  </div>
  
  <div class="chapter-card">
    <h3>Chapter 11</h3>
    <p>Assessment Frameworks for AI Learning</p>
    <a href="Chapters/Chapter11/" class="view-btn">View Materials</a>
  </div>
  
  <div class="chapter-card">
    <h3>Chapter 12</h3>
    <p>Future Trends and Opportunities</p>
    <a href="Chapters/Chapter12/" class="view-btn">View Materials</a>
  </div>
</div>

## Featured Resources

<div class="resources-grid">
  <div class="resource-card">
    <div class="resource-icon">📊</div>
    <h3>AI Tools for Construction Education</h3>
    <p>Access curated tools specifically designed for teaching AI in construction contexts.</p>
    <a href="resources/ai-tools/" class="download-btn">Download</a>
  </div>
  
  <div class="resource-card">
    <div class="resource-icon">🗄️</div>
    <h3>Dataset Collections</h3>
    <p>Comprehensive datasets for students to practice with real construction data.</p>
    <a href="resources/datasets/" class="download-btn">Download</a>
  </div>
  
  <div class="resource-card">
    <div class="resource-icon">📝</div>
    <h3>Implementation Case Studies</h3>
    <p>Real-world examples of AI implementation in construction education programs.</p>
    <a href="resources/case-studies/" class="download-btn">Download</a>
  </div>
</div>

## About the Author

<div class="author-card">
  <p>Dr. M. Reza Hosseini is a Senior Lecturer in Construction Technology at the University of Melbourne, specializing in AI applications for construction engineering and education.</p>
  
  <div style="margin-top: 1.5rem;">
    <a href="https://github.com/morehosseini" class="profile-btn">View GitHub</a>
    <a href="https://findanexpert.unimelb.edu.au/profile/830762-reza-hosseini" class="profile-btn">University Profile</a>
  </div>
</div>
