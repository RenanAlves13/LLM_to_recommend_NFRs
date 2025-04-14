<h1>🔍 Recommender of Non-Functional Requirements using LLMs</h1>

<p>This project uses various Large Language Models (LLMs) to recommend Non-Functional Requirements (NFRs) based on project data. Multiple models and approaches were tested, including API calls, fine-tuning, and Retrieval-Augmented Generation (RAG).</p>

<h2>🧠 Models and Approaches</h2>

<ul>
  <li><strong>ChatGPT (OpenAI API)</strong>
    <ul>
      <li>✅ Recommendation using standard API calls</li>
      <li>🛠️ Fine-tuned version using a custom dataset for more accurate NFR suggestions</li>
    </ul>
  </li>

  <li><strong>DeepSeek (via API)</strong>
    <ul>
      <li>✅ Recommendation using the DeepSeek API</li>
      <li>📚 Retrieval-Augmented Generation (RAG) with project context and DeepSeek API</li>
    </ul>
  </li>

  <li><strong>DeepSeek (via Ollama)</strong>
    <ul>
      <li>📦 Model downloaded locally using Ollama for offline or controlled environment inference</li>
    </ul>
  </li>
</ul>

<h2>📥 Downloading DeepSeek using Ollama</h2>

<p>To run DeepSeek locally via Ollama, follow these steps:</p>

<pre><code># Step 1: Install Ollama (if not installed)
curl -fsSL https://ollama.com/install.sh | sh

# Step 2: Pull the DeepSeek model
ollama pull deepseek-coder:6.7b-instruct
</code></pre>

<p>Once the model is downloaded, you can run it with:</p>

<pre><code>ollama run deepseek-coder:6.7b-instruct</code></pre>

<p>This allows you to interact with the model locally for recommendation tasks.</p>

<h2>📚 Taxonomy of Non-Functional Requirements</h2>

<p>The recommendations are based on a taxonomy of Non-Functional Requirements (NFRs) inspired by the study “A Data-Driven Recommendation System for Enhancing Non-Functional Requirements Elicitation in Scrum-Based Projects”. Due to licensing restrictions, the original dataset cannot be published in this repository. However, the taxonomy categories used are as follows:</p>

<table>
  <thead>
    <tr>
      <th>Category</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Performance</td>
      <td>Requirements related to system response time, throughput, and resource usage.</td>
    </tr>
    <tr>
      <td>Reliability</td>
      <td>Requirements ensuring the system's ability to operate under specified conditions.</td>
    </tr>
    <tr>
      <td>Security</td>
      <td>Requirements addressing the protection of data and resources.</td>
    </tr>
    <tr>
      <td>Portability</td>
      <td>Ease of transferring the system to different environments.</td>
    </tr>
    <tr>
      <td>Interoperability</td>
      <td>Requirements for interaction with other systems or software.</td>
    </tr>
    <tr>
      <td>Legal and Regulatory</td>
      <td>Requirements ensuring compliance with laws and standards.</td>
    </tr>
  </tbody>
</table>

<h2>📊 Example of Synthetic Project Data</h2>

<p><em>Based on: Coelho, R. B., Farias, L., & Barros, G. (2022). 
A Data-Driven Recommendation System for Enhancing Non-Functional Requirements Elicitation in Scrum-Based Projects. 
In 2022 19th International Conference on Software Architecture Companion (ICSA-C) (pp. 60–63). IEEE. 
<a href="https://doi.org/10.1109/ICSA-C54293.2022.00020" target="_blank">https://doi.org/10.1109/ICSA-C54293.2022.00020</a>
</em></p>

<table>
  <thead>
    <tr>
      <th>ID</th>
      <th>Mod.</th>
      <th>Ope.</th>
      <th>Plat.</th>
      <th>Soft. Arch.</th>
      <th>Dom.</th>
      <th>Obj.</th>
      <th>Prog. Lang.</th>
      <th>Fram.</th>
      <th>APIs</th>
      <th>Data Stor.</th>
      <th>Tasks</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>p₁</td>
      <td>Regist.</td>
      <td>Retrieve data</td>
      <td>Web</td>
      <td>Client-serv</td>
      <td>Educ.</td>
      <td>Prod.</td>
      <td>Python</td>
      <td>FastAPI</td>
      <td>REST</td>
      <td>PostgreSQL</td>
      <td>t₁, t₂</td>
    </tr>
    <tr>
      <td>p₂</td>
      <td>Authen.</td>
      <td>Create Account</td>
      <td>Web</td>
      <td>MVC</td>
      <td>E-Commerce</td>
      <td>Dev.</td>
      <td>JavaScript</td>
      <td>Express.js</td>
      <td>OAuth</td>
      <td>MongoDB</td>
      <td>t₃, t₄</td>
    </tr>
    <tr>
      <td>p₃</td>
      <td>Regist.</td>
      <td>Insert data</td>
      <td>Web</td>
      <td>Layered</td>
      <td>Healthcare</td>
      <td>Test.</td>
      <td>Kotlin</td>
      <td>SpringBoot</td>
      <td>HL7</td>
      <td>MySQL</td>
      <td>t₅, t₆</td>
    </tr>
    <tr>
      <td>p₄</td>
      <td>Search</td>
      <td>Query data</td>
      <td>Web</td>
      <td>Microserv.</td>
      <td>Info. Rec.</td>
      <td>Prod.</td>
      <td>TypeScript</td>
      <td>NestJS</td>
      <td>Elastic</td>
      <td>Elasticsearch</td>
      <td>t₇, t₈</td>
    </tr>
    <tr>
      <td>p₅</td>
      <td>Notific.</td>
      <td>Send alerts</td>
      <td>Mobile</td>
      <td>Layered</td>
      <td>FinTech</td>
      <td>Dev.</td>
      <td>Dart</td>
      <td>Flutter</td>
      <td>Firebase</td>
      <td>Firestore</td>
      <td>t₉</td>
    </tr>
  </tbody>
</table>

<h2>💡 Project Goal</h2>
<p>The goal of this project is to explore how different LLMs can assist in software engineering tasks—specifically, the recommendation of Non-Functional Requirements—by combining natural language understanding and domain-specific prompts.</p>

<hr>

<p>✨ Feel free to explore, clone, and contribute!</p>
