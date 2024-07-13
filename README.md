# 💬 Talk-to-MySQL: Few-Shot SQL Query Generation with Google PaLM 🧠 and LangChain 🔗🚀

![image](https://github.com/user-attachments/assets/94a21c71-e5c9-4c59-b9b5-8cb085f087f3)


## Asalam alaikum warahmatullah wabarakatu! 🌟

👋 I'm Mustafa Shoukat, a Generative AI Expert. I'm deeply immersed in the world of LLMs and continuously exploring various concepts and techniques to enhance my skills. In this repository, I'll unlock the potential of Google PaLM for code generation with precision and efficiency. 🚀

## 📬 Contact Information

| Name            | Email                           | LinkedIn                                                        | GitHub                                              | Kaggle                                               | LeetCode                                                 |
|-----------------|---------------------------------|-----------------------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|----------------------------------------------------------|
| Mustafa Shoukat | mustafashoukat.ai@gmail.com     | [![LinkedIn Badge](https://img.shields.io/badge/-LinkedIn-blue)](https://www.linkedin.com/in/mustafashoukat/)   | [![GitHub Badge](https://img.shields.io/badge/-GitHub-black)](https://github.com/Mustafa-Shoukat1) | [![Kaggle Badge](https://img.shields.io/badge/-Kaggle-blue)](https://www.kaggle.com/mustafashoukat) | [![LeetCode Badge](https://img.shields.io/badge/-LeetCode-orange)](https://leetcode.com/u/MustafaShoukat/) |

[Google PaLM](https://th.bing.com/th/id/OIP.HMwi10r0TW11pUc-9yZEeQHaE8?rs=1&pid=ImgDetMain)

# 🛒 AtliQ Tees: Talk to a Database

Welcome to the AtliQ Tees project! This end-to-end LLM project leverages Google Palm and LangChain to create a system that can seamlessly interact with a MySQL database through natural language queries.

![AtliQ Tees Banner](https://via.placeholder.com/1200x400.png?text=AtliQ+Tees+Project+Banner)

## 📜 Table of Contents
- [Project Highlights](#project-highlights)
- [Usage](#usage)
- [Sample Questions](#sample-questions)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [License](#license)

## 🎯 Project Highlights

AtliQ Tees is a T-shirt store selling brands like Adidas, Nike, Van Heusen, and Levi's. Their inventory, sales, and discounts data are stored in a MySQL database. This project builds an LLM-based Q&A system using:
- **Google Palm LLM**
- **Hugging Face embeddings**
- **Streamlit for UI**
- **LangChain framework**
- **Chroma as a vector store**
- **Few-shot learning**

![Project Workflow](https://via.placeholder.com/800x400.png?text=Project+Workflow)

The store manager can ask questions like:
- How many white color Adidas T-shirts are left in stock?
- How much sales will be generated if all extra-small T-shirts are sold after applying discounts?

The system intelligently generates accurate SQL queries for the given questions and executes them on the MySQL database.

## 🚀 Usage

1. **Run the Streamlit app** by executing:
    ```bash
    streamlit run main.py
    ```

2. **Ask questions** in the web app that opens in your browser.

![Streamlit App Screenshot](https://via.placeholder.com/800x400.png?text=Streamlit+App+Screenshot)

## ❓ Sample Questions

- How many total T-shirts are left in stock?
- How many T-shirts do we have left for Nike in XS size and white color?
- How much is the total price of the inventory for all S-size T-shirts?
- How much sales amount will be generated if we sell all small size Adidas shirts today after discounts?

## 📁 Project Structure

```plaintext
AtliQ_Tees/
│
├── main.py               # The main Streamlit application script
├── langchain_helper.py   # LangChain helper functions and setup
├── requirements.txt      # List of required Python packages
├── few_shots.py          # Contains few-shot prompts
└── .env                  # Configuration file for storing your Google API key
```

## 📋 Requirements

- Python 3.8+
- Streamlit
- LangChain
- Hugging Face Transformers
- Chroma
- PyMySQL

## ⚙️ Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Mustafa-Shoukat1/atliq-tees.git
    cd atliq-tees
    ```

2. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Create a `.env` file** and add your Google API key:
    ```env
    GOOGLE_API_KEY="AIzaSyCWtLDiKOfa_5_GNV-4cNTjD0Z6To1gt40" 
    ```

4. **Run the Streamlit app:**
    ```bash
    streamlit run main.py
    ```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---


- [AtliQ Tees Banner](https://via.placeholder.com/1200x400.png?text=AtliQ+Tees+Project+Banner)
- [Project Workflow](https://via.placeholder.com/800x400.png?text=Project+Workflow)
- [Streamlit App Screenshot](https://via.placeholder.com/800x400.png?text=Streamlit+App+Screenshot)




