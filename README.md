%-------------------------

% Resume in Latex

% Author : Jake Gutierrez

% Based off of: https://github.com/sb2nov/resume

% License : MIT

%------------------------



\\documentclass\[letterpaper,11pt]{article}



\\usepackage{latexsym}

\\usepackage{enumitem}

\\usepackage{academicons}

\\usepackage{fontawesome5}

\\usepackage\[empty]{fullpage}

\\usepackage{titlesec}

\\usepackage{marvosym}

\\usepackage\[usenames,dvipsnames]{color}

\\usepackage{verbatim}

\\usepackage{enumitem}

\\usepackage\[hidelinks]{hyperref}

\\usepackage{fancyhdr}

\\usepackage\[english]{babel}

\\usepackage{tabularx}

\\usepackage{fontawesome5}

\\usepackage{multicol}

\\setlength{\\multicolsep}{-3.0pt}

\\setlength{\\columnsep}{-1pt}

\\input{glyphtounicode}





%----------FONT OPTIONS----------

% sans-serif

% \\usepackage\[sfdefault]{FiraSans}

% \\usepackage\[sfdefault]{roboto}

% \\usepackage\[sfdefault]{noto-sans}

% \\usepackage\[default]{sourcesanspro}



% serif

% \\usepackage{CormorantGaramond}

% \\usepackage{charter}





\\pagestyle{fancy}

\\fancyhf{} % clear all header and footer fields

\\fancyfoot{}

\\renewcommand{\\headrulewidth}{0pt}

\\renewcommand{\\footrulewidth}{0pt}



% Adjust margins

\\addtolength{\\oddsidemargin}{-0.6in}

\\addtolength{\\evensidemargin}{-0.5in}

\\addtolength{\\textwidth}{1.19in}

\\addtolength{\\topmargin}{-.7in}

\\addtolength{\\textheight}{1.4in}



\\urlstyle{same}



\\raggedbottom

\\raggedright

\\setlength{\\tabcolsep}{0in}



% Sections formatting

\\titleformat{\\section}{

&nbsp; \\vspace{-4pt}\\scshape\\raggedright\\large\\bfseries

}{}{0em}{}\[\\color{black}\\titlerule \\vspace{-5pt}]



% Ensure that generate pdf is machine readable/ATS parsable

\\pdfgentounicode=1



%-------------------------

% Custom commands

\\newcommand{\\resumeItem}\[1]{

&nbsp; \\item\\small{

&nbsp;   {#1 \\vspace{-2pt}}

&nbsp; }

}



\\newcommand{\\classesList}\[4]{

&nbsp;   \\item\\small{

&nbsp;       {#1 #2 #3 #4 \\vspace{-2pt}}

&nbsp; }

}



\\newcommand{\\resumeSubheading}\[4]{

&nbsp; \\vspace{-2pt}\\item

&nbsp;   \\begin{tabular\*}{1.0\\textwidth}\[t]{l@{\\extracolsep{\\fill}}r}

&nbsp;     \\textbf{#1} \& \\textbf{\\small #2} \\\\

&nbsp;     \\textit{\\small#3} \& \\textit{\\small #4} \\\\

&nbsp;   \\end{tabular\*}\\vspace{-7pt}

}



\\newcommand{\\resumeSubSubheading}\[2]{

&nbsp;   \\item

&nbsp;   \\begin{tabular\*}{0.97\\textwidth}{l@{\\extracolsep{\\fill}}r}

&nbsp;     \\textit{\\small#1} \& \\textit{\\small #2} \\\\

&nbsp;   \\end{tabular\*}\\vspace{-7pt}

}



\\newcommand{\\resumeProjectHeading}\[2]{

&nbsp;   \\item

&nbsp;   \\begin{tabular\*}{1.001\\textwidth}{l@{\\extracolsep{\\fill}}r}

&nbsp;     \\small#1 \& \\textbf{\\small #2}\\\\

&nbsp;   \\end{tabular\*}\\vspace{-7pt}

}



\\newcommand{\\resumeSubItem}\[1]{\\resumeItem{#1}\\vspace{-4pt}}



\\renewcommand\\labelitemi{$\\vcenter{\\hbox{\\tiny$\\bullet$}}$}

\\renewcommand\\labelitemii{$\\vcenter{\\hbox{\\tiny$\\bullet$}}$}



\\newcommand{\\resumeSubHeadingListStart}{\\begin{itemize}\[leftmargin=0.0in, label={}]}

\\newcommand{\\resumeSubHeadingListEnd}{\\end{itemize}}

\\newcommand{\\resumeItemListStart}{\\begin{itemize}}

\\newcommand{\\resumeItemListEnd}{\\end{itemize}\\vspace{-5pt}}



%-------------------------------------------

%%%%%%  RESUME STARTS HERE  %%%%%%%%%%%%%%%%%%%%%%%%%%%%





\\begin{document}



%----------HEADING----------

% \\begin{tabular\*}{\\textwidth}{l@{\\extracolsep{\\fill}}r}

%   \\textbf{\\href{http://sourabhbajaj.com/}{\\Large Sourabh Bajaj}} \& Email : \\href{mailto:sourabh@sourabhbajaj.com}{sourabh@sourabhbajaj.com}\\\\

%   \\href{http://sourabhbajaj.com/}{http://www.sourabhbajaj.com} \& Mobile : +1-123-456-7890 \\\\

% \\end{tabular\*}



\\begin{center}

&nbsp;   {\\Huge \\scshape PANDI KABILESH P} \\\\ \\vspace{1pt}

&nbsp;   \\footnotesize

&nbsp;   \\raisebox{-0.1\\height}\\faPhone\\ +91 6374243080 ~

&nbsp;   \\href{mailto:pandikabilesh2270157@gmail.com}{\\raisebox{-0.2\\height}\\faEnvelope\\ \\underline{pandikabilesh2270157@gmail.com}} ~

&nbsp;   \\href{https://www.linkedin.com/in/pandi-kabilesh-p-68aa96324/}{\\raisebox{-0.2\\height}\\faLinkedin\\ \\underline{LinkedIn}} ~

&nbsp;   \\href{https://codeforces.com/profile/pandikabilesh2270157}{\\raisebox{-0.2\\height}\\faKeyboard\\ \\underline{Codeforces}} ~

&nbsp;   \\href{https://leetcode.com/u/dI6w6z00Nj/}{\\raisebox{-0.2\\height}\\faLaptopCode\\ \\underline{LeetCode}} ~

&nbsp;   \\href{https://github.com/PandiKabilesh2006}{\\raisebox{-0.2\\height}\\faGithub\\ \\underline{GitHub}} ~

&nbsp;   \\href{https://www.codechef.com/users/kabilesh2006}{\\raisebox{-0.2\\height}\\faUtensils\\ \\underline{CodeChef}}

&nbsp;   \\vspace{-8pt}

\\end{center}





%-----------EDUCATION-----------

\\section{Education}

&nbsp; \\resumeSubHeadingListStart

&nbsp;   \\resumeSubheading

&nbsp;     {Shiv Nadar University, Chennai}{August 2024 -- May 2028}

&nbsp;     {B.Tech Artificial Intelligence and Data Science}{Chennai, Tamil Nadu}

&nbsp; \\resumeSubHeadingListEnd



%------RELEVANT COURSEWORK-------

% \\section\*{Coding Profiles}

% \\noindent

% \\textbullet\\ 

% Codeforces: \\textbf{Newbie: 1069} 

% \\href{https://codeforces.com/profile/pandikabilesh2270157}{\[Link]}

% \\hspace{1em}

% \\textbullet\\ 

% LeetCode: \\textbf{Rating: 1634} 

% \\href{https://leetcode.com/u/dI6w6z00Nj/}{\[Link]}

% \\hspace{1em}

% \\textbullet\\ 

% CodeChef: \\textbf{2-Star: 1445} 

% \\href{https://www.codechef.com/users/kabilesh2006}{\[Link]}



%-----------PROJECTS-----------



\\section\*{Projects}



\\textbf{Scalable Multi-Tier AI Backend System for Secure Financial Query Processing}

\\hfill \\href{https://github.com/PandiKabilesh2006/bfsi-call-center-ai-assistant}{GitHub}

\\begin{itemize}\[leftmargin=\*, itemsep=0pt, topsep=0pt]

&nbsp;   \\item Architected a modular multi-layer backend system (Guardrails $\\rightarrow$ Retrieval $\\rightarrow$ Inference) with strict separation of concerns to improve maintainability and extensibility.

&nbsp;   \\item Designed deterministic request-routing logic to optimize response latency and prioritize secure data retrieval over probabilistic model inference.

&nbsp;   \\item Implemented embedding-based semantic search with efficient similarity computation to enable scalable query handling.

&nbsp;   \\item Built a fully local, privacy-preserving inference pipeline with production-style project structure supporting future vector database and model integrations.

\\end{itemize}



\\textbf{Scalable Semantic Search \\\& Retrieval System with LLM Grounding}

\\hfill \\href{https://github.com/PandiKabilesh2006/rag-semantic-search-engine}{GitHub}

\\begin{itemize}\[leftmargin=\*, itemsep=0pt, topsep=0pt]

&nbsp;   \\item Architected a modular Retrieval-Augmented Generation (RAG) pipeline integrating FAISS-based vector search with LLM-based grounded response generation.

&nbsp;   \\item Engineered high-performance nearest-neighbor retrieval using dense sentence embeddings to enable efficient semantic search over unstructured text corpora.

&nbsp;   \\item Designed robust backend API integration with retry mechanisms, rate-limit handling, and fault-tolerant error management for external LLM services.

&nbsp;   \\item Deployed a cloud-hosted full-stack application with secure credential management and Git-based continuous deployment workflow.

\\end{itemize}



\\textbf{Production-Ready Real-Time Fraud Detection Backend (FastAPI + ML)}

\\hfill \\href{https://github.com/PandiKabilesh2006/real-time-fraud-detection-system}{GitHub}

\\begin{itemize}\[leftmargin=\*, itemsep=0pt, topsep=0pt]

&nbsp;   \\item Designed and implemented a modular RESTful backend service using FastAPI to perform low-latency real-time fraud prediction with structured JSON APIs.

&nbsp;   \\item Integrated a scikit-learn classification model into a production-style inference pipeline with strict feature schema validation to prevent training--serving skew.

&nbsp;   \\item Engineered tiered decision logic (ALLOW / REVIEW / BLOCK) and structured logging to simulate production observability and rule-based risk evaluation systems.

&nbsp;   \\item Architected a clean, scalable project structure separating API, feature engineering, and inference layers, following backend engineering best practices.

\\end{itemize}

% \\section\*{Projects}



% \\textbf{Scalable Multi-Tier AI Backend System for Secure Financial Query Processing}

% \\hfill \\href{https://github.com/PandiKabilesh2006/bfsi-call-center-ai-assistant}{GitHub} \\\\

% \\vspace{-4pt}

% \\begin{itemize}\[leftmargin=\*, itemsep=1pt, topsep=2pt]

%     \\item Architected a modular multi-layer backend system (Guardrails $\\rightarrow$ Retrieval $\\rightarrow$ Inference) with strict separation of concerns to improve maintainability and extensibility.

%     \\item Designed deterministic request-routing logic to optimize response latency and prioritize secure data retrieval over probabilistic model inference.

%     \\item Implemented embedding-based semantic search with efficient similarity computation to enable scalable query handling.

%     \\item Built a fully local, privacy-preserving inference pipeline with production-style project structure supporting future vector database and model integrations.

% \\end{itemize}



% \\vspace{4pt}



% \\textbf{Scalable Semantic Search \\\& Retrieval System with LLM Grounding}

% \\hfill \\href{https://github.com/PandiKabilesh2006/rag-semantic-search-engine}{GitHub} \\\\

% \\vspace{-4pt}

% \\begin{itemize}\[leftmargin=\*, itemsep=1pt, topsep=2pt]

%     \\item Architected a modular Retrieval-Augmented Generation (RAG) pipeline integrating FAISS-based vector search with LLM-based grounded response generation.

%     \\item Engineered high-performance nearest-neighbor retrieval using dense sentence embeddings to enable efficient semantic search over unstructured text corpora.

%     \\item Designed robust backend API integration with retry mechanisms, rate-limit handling, and fault-tolerant error management for external LLM services.

%     \\item Deployed a cloud-hosted full-stack application with secure credential management and Git-based continuous deployment workflow.

% \\end{itemize}



% \\vspace{4pt}



% \\textbf{Production-Ready Real-Time Fraud Detection Backend (FastAPI + ML)}

% \\hfill \\href{https://github.com/PandiKabilesh2006/real-time-fraud-detection-system}{GitHub} \\\\

% \\vspace{-4pt}

% \\begin{itemize}\[leftmargin=\*, itemsep=1pt, topsep=2pt]

%     \\item Designed and implemented a modular RESTful backend service using FastAPI to perform low-latency real-time fraud prediction with structured JSON APIs.

%     \\item Integrated a scikit-learn classification model into a production-style inference pipeline with strict feature schema validation to prevent training--serving skew.

%     \\item Engineered tiered decision logic (ALLOW / REVIEW / BLOCK) and structured logging to simulate production observability and rule-based risk evaluation systems.

%     \\item Architected a clean, scalable project structure separating API, feature engineering, and inference layers, following backend engineering best practices.

% \\end{itemize}



%-----------ACHIEVEMENTS-----------

\\section\*{Achievements}

\\begin{itemize}\[leftmargin=\*, itemsep=0pt, topsep=0pt]



&nbsp;   \\item Solved \\textbf{700+ DSA problems} across LeetCode, Codeforces, and CodeChef, covering Graphs, DP, Trees, Greedy, and advanced data structures.

&nbsp;   \\hfill \\href{https://codolio.com/profile/pandikabilesh2006}{\[Profile]}



&nbsp;   \\item Competitive Programming: \\textbf{Max Rating 1634 (LeetCode)}, \\textbf{1445 (CodeChef -- 2$\\star$)}, \\textbf{1069 (Codeforces)}.



&nbsp;   \\item Completed advanced Machine Learning and Data Science specializations from \\textbf{DeepLearning.AI, Stanford, and IBM}, strengthening foundations in algorithms, ML systems, and scalable data processing.



\\end{itemize}





%-----------TECHNICAL SKILLS---------------

\\section\*{Technical Skills}



\\textbf{Programming:} Python, C++, C, Java, JavaScript \\\\



\\textbf{Backend \\\& APIs:} FastAPI, RESTful APIs, Modular Architecture, Request Routing, Schema Validation \\\\



\\textbf{Machine Learning \\\& AI:} Scikit-learn, TensorFlow, Keras, NumPy, Pandas, Feature Engineering, Model Evaluation, Neural Networks \\\\



\\textbf{Search \\\& LLM Systems:} Retrieval-Augmented Generation (RAG), FAISS, Vector Search, Sentence Embeddings, Semantic Search, LLM Integration \\\\



\\textbf{Core CS:} Data Structures \\\& Algorithms, OOP, Operating Systems, DBMS, Computer Networks \\\\



\\textbf{Tools \\\& Platforms:} Git, GitHub, Jupyter Notebook, VS Code, Google Colab



\\end{document}

