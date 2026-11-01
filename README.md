# 📊 Employee Data Analysis with Python

A hands-on data analysis project built in **Jupyter Notebook** using **Pandas, NumPy, Matplotlib and Scikit-learn**. It works on an employee dataset and covers the complete beginner-to-intermediate workflow: data exploration, cleaning, visualization, and basic machine learning.

---

## 📌 Overview

The notebook is organized as a series of practicals, each focusing on one stage of the data analysis pipeline. The dataset (`employee_dataset.csv`) contains **50 employee records with 9 columns**.

### Dataset Columns

| Column | Description |
|--------|-------------|
| `EmployeeID` | Unique employee ID |
| `name` | Employee name |
| `salary` | Salary of the employee |
| `Dept` | Department (IT, HR, Finance, Marketing, Operations, Sales, Admin) |
| `age` | Age |
| `experience` | Years of experience |
| `status` | Active / Not Active |
| `performance` | Performance rating (Below Average, Average, Good, Excellent, Outstanding) |
| `city` | City of the employee |

## 🧭 What's Inside

| Practical | Topic | Key Work |
|-----------|-------|----------|
| **05** | Data Exploration | Filtering by city, sorting by salary, grouping employees by department |
| **06** | Missing Values | Detecting nulls with `isnull()`, dropping columns, filling missing salary with the mean |
| **07** | Data Quality & Aggregation | Converting salary with `pd.to_numeric()`, status vs city analysis, average salary by department |
| **08** | Data Visualization | Bar chart (city), pie chart (status), histogram (salary), scatter plot (experience vs salary) |
| **09** | Feature Encoding | One-hot encoding of the `Dept` column with `pd.get_dummies()` |
| **10** | Linear Regression | Label encoding of target, train/test split, model training and evaluation |
| **11** | Model Comparison | Linear Regression vs Decision Tree Regressor |
| **12** | Clustering | K-Means clustering with K=2 and K=3, plotted with cluster centers |
| **13** | Results Summary | Model results collected in a comparison table |

## 📈 Key Findings

- Dataset has **50 rows, 9 columns** and no missing values in the original file
- **HR** has the most employees (10), followed by **Sales** (9) and **Admin** (8)
- **IT** has the highest average salary (~155,900), while **Finance** has the lowest (~115,000)
- Most employees in every city are *Active*; Faisalabad is the exception, with more *Not Active* employees

### Model Results

| Model | MSE | R² |
|-------|-----|-----|
| Linear Regression | 3.40 | -1.01 |
| Decision Tree | 5.20 | -2.08 |

> Both models have a negative R², which means they perform worse than simply predicting the average. This is expected: only department and salary were used as features, and the dataset is very small (50 rows). Better features and more data would improve results.

## 🛠️ Tech Stack

- **Python 3**
- **Pandas**: data manipulation
- **NumPy**: numerical operations
- **Matplotlib**: visualization
- **Scikit-learn**: encoding, regression, clustering
- **Jupyter Notebook**

## 📂 Project Structure

```
├── Data_Analysis.ipynb      # Main notebook (all practicals)
├── employee_dataset.csv     # Dataset
├── requirements.txt         # Dependencies
└── README.md
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/ayesha-khokhar/employee-data-analysis.git
cd employee-data-analysis
```

### 2. Install dependencies

```bash
pip install pandas numpy matplotlib scikit-learn jupyter
```

### 3. Update the dataset path

In the notebook, change the file path to where the CSV is on your system:

```python
df = pd.read_csv('employee_dataset.csv')
```

### 4. Run the notebook

```bash
jupyter notebook Data_Analysis.ipynb
```

## 🔮 Future Improvements

- Add more features (age, experience, city) to improve model performance
- Try classification models (Logistic Regression, Random Forest) for the performance column
- Run K-Means on the actual employee data instead of sample data
- Build an interactive dashboard using Streamlit

## 👩‍💻 Author

**Ayesha Khokhar**
- GitHub: [@ayesha-khokhar](https://github.com/ayesha-khokhar)

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
