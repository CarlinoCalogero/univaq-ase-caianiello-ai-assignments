<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/CarlinoCalogero/univaq-ase-caianiello-ai-assignments">
    <img src="https://img.shields.io/badge/UNIVAQ-Assignment_2:_Learning_Agent-003366?style=for-the-badge&logo=mortarboard&logoColor=white" alt="Assignment 2 Logo" height="40">
  </a>

<h3 align="center">Assignment 2: Learning Agent for Board Games (Chess)</h3>

  <p align="center">
    University Coursework for the Master's Degree in Computer Science (Advanced Software Engineering)
    <br />
    <strong>University of L'Aquila (UNIVAQ) &middot; Artificial Intelligence (A.Y. 2024/2025)</strong>
    <br />
    Instructor: Prof. Pasquale Caianiello &middot; Author: Calogero Carlino (Matricola 302154)
    <br />
    <br />
    <a href="report/report.pdf"><strong>Read the Report (PDF) »</strong></a>
    <br />
    <br />
    <a href="code/notebook.ipynb">Explore Notebook</a>
    &middot;
    <a href="code/main.py">Run Matches Script</a>
    &middot;
    <a href="https://github.com/CarlinoCalogero/univaq-ase-caianiello-ai-assignments/issues">Report Issue</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#key-features">Key Features</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li>
      <a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This project was developed as part of the **Artificial Intelligence** coursework for the **Master's Degree in Computer Science (Advanced Software Engineering)** at the **University of L'Aquila (UNIVAQ)** under the supervision of **Prof. Pasquale Caianiello**.

The assignment requires building an autonomous game-playing decision engine for Chess capable of improving and accelerating its decision-making performance through play and statistical learning. The system transitions from classical exhaustive search to breadth-limited search, and ultimately to predictive decision-making using trained machine learning regressors.

### Key Features

* **Decision-Making & Adversarial Search Engines**:
  * **`ab_minmax` (Alpha-Beta MinMax)**: Classical MinMax search fortified with dynamic alpha-beta pruning, systematically eliminating subtrees that cannot influence the final decision.
  * **`bl_minmax` (Branch-Limited MinMax)**: Constrains exploration of the legal moves set (`possiblemoves(s)`) exclusively to the most promising transitions according to their static heuristic evaluation $H_0$, enforcing a hard limit on the branching factor.
  * **`bl_minmax_l` (Generalized Branch-Limited MinMax)**: Generalizes breadth pruning by filtering moves according to intermediate lookahead evaluations $H_l$ ($0 < l < L$) to find the optimal balance between computational overhead and move accuracy.
  * **`pred_minmax` (Predictive MinMax)**: Replaces exhaustive recursive lookahead to depth $L$ with fast inferences from a trained non-linear regressor $R(s) \approx H_L(s)$, drastically slashing computation time.
  * **`pred_bl_minmax` & `pred_bl_minmax_l`**: Hybrid predictive branch-limited algorithms combining learned evaluations and branch trimming.
* **Feature Engineering & Machine Learning Pipeline**:
  * **Datasets**:
    * `dataset.csv`: Base features computed using the standard static evaluation function $H_0$.
    * `extended_dataset.csv`: Advanced board state representations incorporating piece values, positional weighting matrices, material imbalances, mobility, king safety, and pawn structure ($h_1, \dots, h_n$).
  * **Multi-Layer Perceptron Regressors**: Built with `scikit-learn` (`MLPRegressor`) and normalized using `StandardScaler` to accurately approximate target lookahead values $H_L$.
  * **Automated Data Collection & Training**: Dedicated modules (`data_analyst.py`, `trainer.py`, `oracle.py`) manage self-play game simulation, dataset persistence, model fitting, and real-time inference.
* **Telemetry, Scorekeeping & Platform Integration**:
  * **`Scorekeeper` (`scorekeeper.py`)**: Logs game states, move notations, FEN board positions, and game outcomes into structured `.json` and `.txt` files.
  * **Chess.com Analysis Compatibility**: Exported text logs can be uploaded directly to [Chess.com Analysis](https://www.chess.com/analysis?tab=analysis) for in-depth engine verification and review.
  * **Automated Experimentation (`statistician.py`)**: Runs high-throughput tournaments and parametric sweeps over search depth $L$, intermediate depth $l$, and branching factors $bf$, plotting performance and heuristic accuracy.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [![Python][Python]][Python-url]
* [![python-chess][python-chess]][python-chess-url]
* [![scikit-learn][scikit-learn]][scikit-learn-url]
* [![Pandas][Pandas]][Pandas-url]
* [![NumPy][NumPy]][NumPy-url]
* [![Matplotlib][Matplotlib]][Matplotlib-url]
* [![Jupyter][Jupyter]][Jupyter-url]
* [![LaTeX][LaTeX]][LaTeX-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

Follow these steps to set up the project locally.

### Prerequisites

* Python 3.10 or higher
* `pip` package manager
* Virtual environment (recommended)

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/CarlinoCalogero/univaq-ase-caianiello-ai-assignments.git
   ```
2. Navigate to the `assignment_2` directory:
   ```sh
   cd univaq-ase-caianiello-ai-assignments/assignment_2
   ```
3. Create and activate a virtual environment:
   * **Windows (PowerShell)**:
     ```sh
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
   * **Linux / macOS**:
     ```sh
     python3 -m venv venv
     source venv/bin/activate
     ```
4. Install required dependencies:
   ```sh
   pip install chess scikit-learn pandas numpy matplotlib tqdm randomcolor notebook
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

### Run Chess Matches & Tournaments

Run automated tournaments between different engines (e.g. `abMinMax` vs `blMinMax`, `abMinMax` vs `predMinMax`):

```sh
cd code
python main.py
```

Matches will be simulated, tracked with progress bars via `tqdm`, and recorded to `code/games/` with `.json` telemetry and `.txt` move logs.

### Train Regressors & Generate Datasets

Generate training data from self-play and train neural network regressors:

```python
from data_analyst import generate_dataset, generate_extended_dataset
from trainer import train_mlp_regressor, train_mlp_regressor_with_extended_dataset

# Generate datasets from simulated games
generate_dataset("./dataset.csv", match_count=100)
generate_extended_dataset("./extended_dataset.csv", match_count=100)

# Train MLP Regressors
mlp_regressor, scaler = train_mlp_regressor("./dataset.csv")
extended_mlp_regressor, extended_scaler = train_mlp_regressor_with_extended_dataset("./extended_dataset.csv")
```

### Interactive Notebook & Experiments

Launch the Jupyter Notebook to explore experiments, regression curves, depth benchmarks ($L=10$), and comparative performance graphs:

```sh
cd code
jupyter notebook notebook.ipynb
```

### Analyze Games on Chess.com

Every game played by the system records FEN positions and move notation. Inspect the generated `.txt` files in `code/games/` and paste them directly into the [Chess.com Analysis Board](https://www.chess.com/analysis?tab=analysis) for move quality and accuracy evaluation.

### Academic Report

Read the comprehensive technical paper covering mathematical formulation, experimental methodology, and conclusion in `report/`:
* [report/report.pdf](report/report.pdf)
* [report/report.tex](report/report.tex)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

This repository contains completed coursework for an academic university project and is now archived. As such, **outside contributions, pull requests, and feature requests are not accepted**.

However, project contributors are showcased below:

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Top contributors:

<a href="https://github.com/CarlinoCalogero/univaq-ase-caianiello-ai-assignments/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=CarlinoCalogero/univaq-ase-caianiello-ai-assignments" alt="contrib.rocks image" />
</a>

* **[Calogero Carlino](https://github.com/CarlinoCalogero)** — Author & Developer

<!-- CONTACT -->
## Contact

**Calogero Carlino** - Game Programmer & Master's Graduate in Computer Science
* **Email**: [carlinocalogero.dev@gmail.com](mailto:carlinocalogero.dev@gmail.com)
* **LinkedIn**: [https://www.linkedin.com/in/calogero-carlino-2a94a33b5/](https://www.linkedin.com/in/calogero-carlino-2a94a33b5/)
* **Portfolio**: [https://carlinocalogero.github.io](https://carlinocalogero.github.io)
* **GitHub**: [@CarlinoCalogero](https://github.com/CarlinoCalogero)

Project Link: [https://github.com/CarlinoCalogero/univaq-ase-caianiello-ai-assignments](https://github.com/CarlinoCalogero/univaq-ase-caianiello-ai-assignments)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [University of L'Aquila (UNIVAQ)](https://www.univaq.it/) — Master's Degree in Computer Science (Advanced Software Engineering)
* Prof. Pasquale Caianiello — Artificial Intelligence Course Instructor
* [Best-README-Template](https://github.com/othneildrew/Best-README-Template) by Othneil Drew
* [python-chess](https://python-chess.readthedocs.io/)
* [scikit-learn](https://scikit-learn.org/)
* [Pandas](https://pandas.pydata.org/) & [NumPy](https://numpy.org/)
* [Matplotlib](https://matplotlib.org/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/CarlinoCalogero/univaq-ase-caianiello-ai-assignments.svg?style=for-the-badge
[contributors-url]: https://github.com/CarlinoCalogero/univaq-ase-caianiello-ai-assignments/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/CarlinoCalogero/univaq-ase-caianiello-ai-assignments.svg?style=for-the-badge
[forks-url]: https://github.com/CarlinoCalogero/univaq-ase-caianiello-ai-assignments/network/members
[stars-shield]: https://img.shields.io/github/stars/CarlinoCalogero/univaq-ase-caianiello-ai-assignments.svg?style=for-the-badge
[stars-url]: https://github.com/CarlinoCalogero/univaq-ase-caianiello-ai-assignments/stargazers
[issues-shield]: https://img.shields.io/github/issues/CarlinoCalogero/univaq-ase-caianiello-ai-assignments.svg?style=for-the-badge
[issues-url]: https://github.com/CarlinoCalogero/univaq-ase-caianiello-ai-assignments/issues
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/calogero-carlino-2a94a33b5/

<!-- Technology Badges -->
[Python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[python-chess]: https://img.shields.io/badge/python--chess-%23333333.svg?style=for-the-badge&logo=lichess&logoColor=white
[python-chess-url]: https://python-chess.readthedocs.io/
[scikit-learn]: https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white
[scikit-learn-url]: https://scikit-learn.org/
[Pandas]: https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white
[Pandas-url]: https://pandas.pydata.org/
[NumPy]: https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white
[NumPy-url]: https://numpy.org/
[Matplotlib]: https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black
[Matplotlib-url]: https://matplotlib.org/
[Jupyter]: https://img.shields.io/badge/Jupyter-%23F37626.svg?style=for-the-badge&logo=Jupyter&logoColor=white
[Jupyter-url]: https://jupyter.org/
[LaTeX]: https://img.shields.io/badge/latex-%23008080.svg?style=for-the-badge&logo=latex&logoColor=white
[LaTeX-url]: https://www.latex-project.org/
