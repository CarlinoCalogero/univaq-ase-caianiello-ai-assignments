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
    <img src="https://img.shields.io/badge/UNIVAQ-Artificial_Intelligence_Assignments-003366?style=for-the-badge&logo=mortarboard&logoColor=white" alt="UNIVAQ Logo" height="40">
  </a>

<h3 align="center">UNIVAQ ASE &middot; Artificial Intelligence Assignments</h3>

  <p align="center">
    Academic Coursework for the Master's Degree in Computer Science (Advanced Software Engineering)
    <br />
    <strong>University of L'Aquila (UNIVAQ) &middot; Academic Year 2024/2025</strong>
    <br />
    Instructor: Prof. Pasquale Caianiello &middot; Author: Calogero Carlino (Matricola 302154)
    <br />
    <br />
    <a href="#about-the-project"><strong>Explore the Projects »</strong></a>
    <br />
    <br />
    <a href="assignment_1/README.md">Assignment 1 (Maze Runner)</a>
    &middot;
    <a href="assignment_2/README.md">Assignment 2 (Chess Learning Agent)</a>
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
        <li><a href="#repository-structure">Repository Structure</a></li>
        <li><a href="#subproject-overviews">Subproject Overviews</a></li>
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
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This repository contains the complete coursework developed for the **Artificial Intelligence** course (A.Y. 2024/2025) within the **Master's Degree in Computer Science (Advanced Software Engineering)** at the **University of L'Aquila (UNIVAQ)**, under the instruction of **Prof. Pasquale Caianiello**.

The repository is organized into two primary university projects exploring state-space search, informed heuristics, adversarial game engines, and machine learning-guided decision-making:

1. **[Assignment 1: Heuristic Search in Maze Environments](assignment_1/README.md)**: Investigates informed ($A^*$, Greedy Best-First) and uninformed (DFS, Wall Following) search algorithms using Manhattan and Euclidean metrics across procedurally generated mazes, complemented by OpenCV graphical animation and formal empirical statistics.
2. **[Assignment 2: Learning Agent for Board Games (Chess)](assignment_2/README.md)**: Investigates adversarial search algorithms on Chess using `python-chess`. Compares Alpha-Beta MinMax (`abMinMax`), Branch-Limited MinMax (`blMinMax`, `blMinMaxl`), and Predictive MinMax (`predMinMax`, `pred_bl_minmax_l`) driven by neural network regressors (`MLPRegressor` via Scikit-Learn) trained on self-play game states.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Repository Structure

```text
univaq-ase-caianiello-ai-assignments/
├── assignment_1/                       # Assignment 1: Heuristic Search in Maze Environments
│   ├── code/                           # Source code (Agent, games, heuristics, generators, UI)
│   │   ├── domain/                     # Agent state representation, directions, maze models
│   │   ├── games/                      # Game runner modules for each algorithm & maze combination
│   │   ├── heuristics/                 # Manhattan and Euclidean distance heuristic implementations
│   │   ├── maze_generators/            # Recursive backtracking & randomized maze generators
│   │   ├── screen/                     # OpenCV display and Matplotlib animation renderers
│   │   ├── main.py                     # Entry point running all maze game scenarios
│   │   └── notebook.ipynb              # Interactive Jupyter notebook with 80-run benchmark analysis
│   ├── notes/                          # Coursework notes and instructions
│   ├── problem/                        # Homework problem specifications (PDF / DOCX)
│   ├── report/                         # Final academic paper (report.pdf, report.tex, benchmark plots)
│   └── README.md                       # Assignment 1 documentation
├── assignment_2/                       # Assignment 2: Learning Agent for Board Games (Chess)
│   ├── code/                           # Source code (MinMax variants, ML regressors, game engine)
│   │   ├── games/                      # Recorded game logs (.json telemetry & .txt PGN moves)
│   │   ├── stats/                      # CSV results of benchmark experiments
│   │   ├── ab_minmax.py                # MinMax with Alpha-Beta Pruning
│   │   ├── bl_minmax.py                # Branch-Limited MinMax (H0 static heuristic)
│   │   ├── bl_minmax_l.py              # Generalized Branch-Limited MinMax (Hl lookahead heuristic)
│   │   ├── pred_minmax.py              # Predictive MinMax using trained neural network regressor
│   │   ├── pred_bl_minmax_l.py         # Predictive Branch-Limited MinMax
│   │   ├── chess_game.py               # Board state representation and chess game mechanics
│   │   ├── data_analyst.py             # Self-play simulation and dataset generation
│   │   ├── trainer.py                  # Scikit-learn MLPRegressor training routines
│   │   ├── oracle.py                   # Regressor inference wrapper for move predictions
│   │   ├── scorekeeper.py              # Game state recorder & Chess.com exporter
│   │   ├── statistician.py             # Tournament orchestrator & statistical evaluation harness
│   │   ├── main.py                     # Entry point for simulated chess matches
│   │   └── notebook.ipynb              # Interactive Jupyter notebook with depth sweeps & evaluations
│   ├── notes/                          # Problem notes and references
│   ├── problem/                        # Homework problem specifications (PDF)
│   ├── report/                         # Final academic paper (report.pdf, report.tex, figures)
│   └── README.md                       # Assignment 2 documentation
├── site.json                           # Portfolio metadata and author profile
└── README.md                           # Main repository documentation
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Subproject Overviews

#### Assignment 1: Heuristic Search in Maze Environments
* **Algorithms Implemented**: Depth-First Search (DFS), Wall Following, Greedy Best-First Search, and $A^*$ Search.
* **Heuristics Evaluated**: Manhattan Distance ($L_1$ norm) and Euclidean Distance ($L_2$ norm).
* **Maze Generators**: Recursive Backtracking generator and Solvability-Guaranteed Randomized generator.
* **Evaluation Metrics**: 80 empirical test runs in a $10 \times 10$ environment tracking execution time, solution path length, expanded agent states, and function call overhead.
* **Documentation**: See [`assignment_1/README.md`](assignment_1/README.md) for full details.

#### Assignment 2: Learning Agent for Board Games (Chess)
* **Algorithms Implemented**: Alpha-Beta MinMax (`abMinMax`), Branch-Limited MinMax (`blMinMax`), Lookahead Branch-Limited MinMax (`blMinMaxl`), Predictive MinMax (`predMinMax`), and Hybrid Predictive Branch-Limited MinMax (`pred_bl_minmax_l`).
* **Machine Learning & Regressors**: Multi-Layer Perceptron Regressors (`MLPRegressor`) trained on standard ($H_0$) and extended board feature vectors ($h_1, \dots, h_n$) including material, piece-square evaluations, mobility, king safety, and pawn structure.
* **Integrations**: Telemetry recorded via `Scorekeeper` in JSON format and PGN format ready for [Chess.com Analysis](https://www.chess.com/analysis?tab=analysis).
* **Documentation**: See [`assignment_2/README.md`](assignment_2/README.md) for full details.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [![Python][Python]][Python-url]
* [![python-chess][python-chess]][python-chess-url]
* [![scikit-learn][scikit-learn]][scikit-learn-url]
* [![OpenCV][OpenCV]][OpenCV-url]
* [![NumPy][NumPy]][NumPy-url]
* [![Pandas][Pandas]][Pandas-url]
* [![Matplotlib][Matplotlib]][Matplotlib-url]
* [![Jupyter][Jupyter]][Jupyter-url]
* [![LaTeX][LaTeX]][LaTeX-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To obtain a local copy of this repository and run the assignments, follow the instructions below.

### Prerequisites

* Python 3.10 or higher
* `pip` package manager
* Virtual environment tool (such as `venv` or `conda`)

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/CarlinoCalogero/univaq-ase-caianiello-ai-assignments.git
   ```
2. Navigate to the project root directory:
   ```sh
   cd univaq-ase-caianiello-ai-assignments
   ```
3. Create and activate a Python virtual environment:
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
4. Install all required dependencies for both assignments:
   ```sh
   pip install chess scikit-learn pandas numpy matplotlib opencv-python tqdm randomcolor notebook
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

### Running Assignment 1 (Maze Runner)

Launch all maze simulation games with real-time OpenCV rendering:

```sh
cd assignment_1/code
python main.py
```

Or open the Jupyter notebook for benchmark plots:

```sh
cd assignment_1/code
jupyter notebook notebook.ipynb
```

For more options and game configurations, refer to the [Assignment 1 README](assignment_1/README.md).

### Running Assignment 2 (Chess Learning Agent)

Launch automated chess matches between adversarial and predictive engines:

```sh
cd assignment_2/code
python main.py
```

Or run the Jupyter notebook for machine learning regressions and parameter sweeps:

```sh
cd assignment_2/code
jupyter notebook notebook.ipynb
```

For detailed engine configuration, dataset generation, and Chess.com export instructions, refer to the [Assignment 2 README](assignment_2/README.md).

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
* Prof. Pasquale Caianiello — Artificial Intelligence Course Instructor (A.Y. 2024/2025)
* [Best-README-Template](https://github.com/othneildrew/Best-README-Template) by Othneil Drew
* [python-chess](https://python-chess.readthedocs.io/)
* [scikit-learn](https://scikit-learn.org/)
* [OpenCV](https://opencv.org/)
* [NumPy](https://numpy.org/), [Pandas](https://pandas.pydata.org/), & [Matplotlib](https://matplotlib.org/)

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
[OpenCV]: https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white
[OpenCV-url]: https://opencv.org/
[NumPy]: https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white
[NumPy-url]: https://numpy.org/
[Pandas]: https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white
[Pandas-url]: https://pandas.pydata.org/
[Matplotlib]: https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black
[Matplotlib-url]: https://matplotlib.org/
[Jupyter]: https://img.shields.io/badge/Jupyter-%23F37626.svg?style=for-the-badge&logo=Jupyter&logoColor=white
[Jupyter-url]: https://jupyter.org/
[LaTeX]: https://img.shields.io/badge/latex-%23008080.svg?style=for-the-badge&logo=latex&logoColor=white
[LaTeX-url]: https://www.latex-project.org/
