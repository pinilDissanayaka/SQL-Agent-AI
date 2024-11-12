# SQL Agent AI 🧠💻

SQL Agent AI is your intelligent assistant for SQL tasks! Powered by cutting-edge Large Language Models (LLMs), this tool lets you generate, optimize, and troubleshoot SQL queries with ease. Say goodbye to complex SQL writing—just ask, and SQL Agent AI will handle the rest!

![sqlAgent](https://github.com/user-attachments/assets/80edb8b2-cd4e-4b69-9a2f-8fbc6933d71a)

## ✨ Features
1. 🔄 Natural Language to SQL Query Conversion
- Effortlessly turn plain English into SQL queries.
2. 🚀 Advanced Query Optimization
- Get performance tips and best practices for complex queries.
3. 🔧 Choose Your LLM
- Select between OpenAI GPT or Meta LLaMA 3.2 70B for customized results.
4. 🖥️ Interactive Streamlit Interface
- Simple, user-friendly web interface for quick interaction.
5. 🛡️ Error Handling & Debugging
- Instant feedback on query issues and step-by-step explanations.
6. 📊 Query Execution & Visualization
- Run SQL queries directly and visualize results with charts and tables.

## 🛠️ Tech Stack
- 🔗 LangChain: Manages LLM interactions and prompt engineering.
- 🧠 OpenAI GPT: Generates SQL queries from natural language.
- 🤖 Meta LLaMA 3.2 70B: Offers alternative performance options.
- 🌐 Streamlit: Provides a responsive web UI.
- 🛢️ SQLAlchemy: Manages database connections.
- 🐬 MySQL (default): Supports expansion to PostgreSQL, SQLite, Microsoft SQL Server, etc.
- 📈 Matplotlib/Plotly: Visualize SQL query results.

## ⚙️ Installation

1. Clone the repository:
```
git clone https://github.com/yourusername/sql-agent-ai.git
cd sql-agent-ai
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Run the app:
```
streamlit run app.py
```

## 🚀 Usage
1. Open the app in your browser (default: http://localhost:8501).
2. Type your question or task in the natural language input.
3. Select OpenAI GPT or Meta LLaMA 3.2 70B.
4. Click Generate SQL to get the query.
5. (Optional) Click Run Query to execute it and see results.
6. Review optimization tips and feedback.

## 🔧 Configuration
- Database Setup: Default is MySQL. Adjust the execute_sql_query function for other databases.
- Model Configuration: Ensure access to LLMs with appropriate credentials.
- Visualizations: Customize visual settings in the visualize_data function.

## 🤝 Contributing
We'd love your help! To contribute:

1. Fork the repository.
2. Create a new branch:
```
git checkout -b feature/your-feature-name
```

3. Commit your changes:
```
git commit -m 'Add new feature'
```

4. Push to your branch:
```
git push origin feature/your-feature-name
```
5. Open a Pull Request.

## 📜 License
Licensed under the MIT License.

## 📬 Contact
Questions or feedback? Open an issue.
