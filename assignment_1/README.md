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
    <img src="https://img.shields.io/badge/UNIVAQ-Assignment_1:_Heuristic_Search-003366?style=for-the-badge&logo=mortarboard&logoColor=white" alt="Assignment 1 Logo" height="40">
  </a>

<h3 align="center">Assignment 1: Heuristic Search in Maze Environments</h3>

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
    <a href="code/main.py">Run Main Script</a>
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
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This project was developed as part of the **Artificial Intelligence** coursework for the **Master's Degree in Computer Science (Advanced Software Engineering)** at the **University of L'Aquila (UNIVAQ)** under the supervision of **Prof. Pasquale Caianiello**.

The assignment requires implementing, visualizing, and empirically benchmarking informed (heuristic) and uninformed search strategies inside grid-based maze environments. An autonomous `Agent` explores a customizable $n \times n$ grid (default $10 \times 10$) starting from cell $(0, 0)$ with the objective of reaching the goal cell $(n-1, n-1)$. The agent's percepts are restricted solely to its current coordinates and obstacle distances across 4 cardinal directions (North, South, East, West), precluding full global environment awareness until explored.

### Key Features

* **Search Algorithms**:
  * **A\* Search (`a_star`)**: Optimal and complete informed graph-search balancing path cost $g(n)$ and heuristic estimate $h(n)$.
  * **Greedy Best-First Search (`best_first`)**: Fast heuristic search prioritized purely by estimated distance to goal $h(n)$.
  * **Depth-First Search (`dfs`)**: Uninformed recursive exploration strategy.
  * **Wall Following (`wall_following`)**: Classic rule-based boundary traversal algorithm operating with $O(1)$ auxiliary memory.
* **Heuristic Implementations**:
  * **Manhattan Distance**: $h(x, y) = |x - x_{\text{goal}}| + |y - y_{\text{goal}}|$ (admissible and consistent for 4-directional grid movement).
  * **Euclidean Distance**: $h(x, y) = \sqrt{(x - x_{\text{goal}})^2 + (y - y_{\text{goal}})^2}$.
* **Maze Generation Strategies**:
  * **Recursive Backtracking Generator**: Generates complex, cavernous labyrinths with winding dead ends.
  * **Randomized Generator with Solvability Guarantee**: Places random obstacle densities while ensuring at least one viable pathway connects start to goal.
* **Visualization & Animation**:
  * Real-time OpenCV graphical rendering window showcasing step-by-step traversal.
  * Matplotlib `FuncAnimation` generator exporting animated videos (MP4) using `ffmpeg`.
* **Empirical Benchmarks & Comparative Statistics**:
  * Systematic stress tests across 80 iterations with obstacle densities scaling from 0 to 80 obstacles in a $10 \times 10$ room.
  * Quantitative analysis tracking **Execution Time**, **Path Length**, **Explored Agent States**, and **Total Function Calls**.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [![Python][Python]][Python-url]
* [![NumPy][NumPy]][NumPy-url]
* [![Matplotlib][Matplotlib]][Matplotlib-url]
* [![OpenCV][OpenCV]][OpenCV-url]
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
2. Navigate to the `assignment_1` directory:
   ```sh
   cd univaq-ase-caianiello-ai-assignments/assignment_1
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
   pip install numpy matplotlib opencv-python notebook
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

### Run All Maze Games

Execute the main orchestrator script to run all combinations of search algorithms and maze types with OpenCV visual animations:

```sh
cd code
python main.py
```

### Run an Individual Algorithm / Maze Configuration

You can execute any individual game directly from the `assignment_1/code` directory:

```sh
# A* with Manhattan heuristic on backtracked maze
python -c "from games import manhattan_a_star_backtracked_maze_game; manhattan_a_star_backtracked_maze_game.play(10, 10)"

# Best-First Search with Euclidean heuristic on randomized maze
python -c "from games import euclidean_best_first_random_maze_game; euclidean_best_first_random_maze_game.play(10, 10)"

# Depth-First Search on randomized maze
python -c "from games import dfs_random_maze_game; dfs_random_maze_game.play(10, 10)"

# Wall Following on backtracked maze
python -c "from games import wall_following_backtracked_maze_game; wall_following_backtracked_maze_game.play(10, 10)"
```

### Interactive Notebook & Benchmark Experiments

Open the Jupyter Notebook to inspect comparative statistics, plots, and analysis across the 80 benchmark runs:

```sh
cd code
jupyter notebook notebook.ipynb
```

### Academic Report

The academic paper detailing the theoretical background, complexity proofs ($O(|V|+|E|)$, exponential bounds, heuristic admissibility), and test graphs is available in `report/`:
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
* [OpenCV](https://opencv.org/)
* [NumPy](https://numpy.org/)
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
[NumPy]: https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white
[NumPy-url]: https://numpy.org/
[Matplotlib]: https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black
[Matplotlib-url]: https://matplotlib.org/
[OpenCV]: https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white
[OpenCV-url]: https://opencv.org/
[Jupyter]: https://img.shields.io/badge/Jupyter-%23F37626.svg?style=for-the-badge&logo=Jupyter&logoColor=white
[Jupyter-url]: https://jupyter.org/
[LaTeX]: https://img.shields.io/badge/latex-%23008080.svg?style=for-the-badge&logo=latex&logoColor=white
[LaTeX-url]: https://www.latex-project.org/
