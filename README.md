<p align="center">
  <sub>A thesis submitted to the Department of Aeronautics</sub><br>
  <sub>in partial fulfilment of the requirements for the degree of</sub><br>
  <sub>Master of Engineering (MEng) in Aeronautical Engineering</sub><br>
  <sub>at</sub><br>
  <sub>Imperial College London</sub><br>
</p>

![Cover light](https://raw.githubusercontent.com/GH-X-ST/Nausicaa/main/A_Miscellaneous/A_Readme/Cover.png#gh-light-mode-only)
![Cover dark](https://raw.githubusercontent.com/GH-X-ST/Nausicaa/main/A_Miscellaneous/A_Readme/Cover_dark.png#gh-dark-mode-only)

<br>

<p align="center">
  <a href="https://gh-x-st.github.io/Nausicaa-Thesis/nausicaa_thesis.pdf">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/Thesis-PDF-ffff00?style=for-the-badge&labelColor=0d1117">
      <source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/badge/Thesis-PDF-0000cd?style=for-the-badge&labelColor=ffffff">
      <img src="https://img.shields.io/badge/Thesis-PDF-6e7781?style=for-the-badge&labelColor=ffffff" alt="Thesis PDF">
    </picture>
  </a>
  <a href="https://doi.org/10.5281/zenodo.21083555">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21083555-ff1423?style=for-the-badge&labelColor=0d1117">
      <source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21083555-750014?style=for-the-badge&labelColor=ffffff">
      <img src="https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21083555-2ea043?style=for-the-badge&labelColor=ffffff" alt="Thesis DOI">
    </picture>
  </a>
  <a href="https://gh-x-st.github.io/Nausicaa-Thesis/">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/Pages-Live-FFE873?style=for-the-badge&labelColor=0d1117">
      <source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/badge/Pages-Live-306998?style=for-the-badge&labelColor=ffffff">
      <img src="https://img.shields.io/badge/Pages-Live-3776ab?style=for-the-badge&labelColor=ffffff" alt="GitHub Pages">
    </picture>
  </a>
  <a href="https://github.com/GH-X-ST/Nausicaa">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/Workflow-Nausicaa-fd8000?style=for-the-badge&labelColor=0d1117">
      <source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/badge/Workflow-Nausicaa-006da8?style=for-the-badge&labelColor=ffffff">
      <img src="https://img.shields.io/badge/Workflow-Nausicaa-7b1fa2?style=for-the-badge&labelColor=ffffff" alt="Nausicaa workflow repository">
    </picture>
  </a>
</p>

<br>

# Viability-Guided Sim-to-Real Transfer for a Small Fixed-Wing Glider in Uncertain Indoor Updrafts

This repository hosts the public thesis landing page and canonical PDF copy for Google Scholar, search engines, and citation discovery.

**Author:** Hanchen Li  
**Institution:** Department of Aeronautics, Imperial College London  
**Document type:** Public MEng thesis manuscript  
**Publication date:** 30 June 2026  
**Thesis DOI:** [10.5281/zenodo.21083555](https://doi.org/10.5281/zenodo.21083555)

## Read the Thesis

- **Scholar landing page:** https://gh-x-st.github.io/Nausicaa-Thesis/
- **Direct PDF:** https://gh-x-st.github.io/Nausicaa-Thesis/nausicaa_thesis.pdf
- **Thesis DOI:** https://doi.org/10.5281/zenodo.21083555
- **Project materials DOI:** https://doi.org/10.5281/zenodo.20927007
- **Workflow repository:** https://github.com/GH-X-ST/Nausicaa

## About

This thesis investigates whether a small fixed-wing glider controller developed in simulation can transfer to repeated real flights through uncertain indoor updrafts. The work uses Imperial College London's Brahmal Vasudevan Multi Terrain Aerial Robotics Arena, Vicon motion capture, a manufactured glider, measured command timing, bounded flight-test safety constraints, and fan-generated updrafts represented by measured but imperfect surrogates.

The controller uses **viability-guided manoeuvre primitive selection**: instead of tracking one long planned trajectory through an uncertain flow field, the glider repeatedly chooses short stabilised manoeuvre primitives every `0.10 s`. Each primitive is generated, replayed, and validated offline so the online selector can reason about entry compatibility, continuation probability, failure risk, safety margin, lift exposure, energy change, and timing cost.

<p align="center">
  <img src="https://raw.githubusercontent.com/GH-X-ST/Nausicaa/main/A_Miscellaneous/A_Readme/Example.jpg" alt="Example result: closed-loop flight through an uncertain updraft" width="100%"><br>
  <sup><em>Example result: closed-loop control keeps the glider flying through uncertain updrafts, while a comparable open-loop launch fails.</em></sup>
</p>

The full workflow, data, scripts, logs, and simulation replay artefacts are archived in the companion repository and Zenodo project-materials record. This repository is intentionally small: it provides a clean public manuscript route, stable citation metadata, and a direct PDF URL.

---

## Thesis at a Glance

- **A repeatable indoor lift-transfer problem.**  
  The thesis turns uncertain low-altitude lift exploitation into a controlled laboratory experiment: a hand-launched glider must cross a bounded indoor volume while fan-generated updrafts can either extend flight or remove recovery margin.

- **A traceable sim-to-real workflow.**  
  The work links motion-capture state feedback, offboard computation, command-path latency, aircraft manufacture, measured updraft surrogates, safety constraints, simulation validation, and repeated real flight tests.

<p align="center">
  <img src="https://raw.githubusercontent.com/GH-X-ST/Nausicaa/main/A_Miscellaneous/A_Readme/3.2.2.jpg" alt="System architecture" width="100%"><br>
  <sup><em>Selected flight-test sensing, computation, and command architecture.</em></sup>
</p>

- **Measured but imperfect updraft models.**  
  Fan-generated updrafts are measured with a scanned hot-wire anemometer, fitted with compact surrogate models, and randomised during controller development so the final controller is not tuned to one specific flow map.

<p align="center">
  <img src="https://raw.githubusercontent.com/GH-X-ST/Nausicaa/main/A_Miscellaneous/A_Readme/Time-lapse.jpg" alt="Time-lapse composite of updraft measurement and model fitting" width="100%"><br>
  <sup><em>Time-lapse composite of anemometer measurements and harmonic annular Gaussian model with GP residual correction.</em></sup>
</p>

- **A real glider model connected to hardware.**  
  The simulation model is built around the manufactured aircraft, using measured mass properties, centre of gravity, actuator timing, flight calibration data, and panelwise aerodynamic loading.

<p align="center">
  <img src="https://raw.githubusercontent.com/GH-X-ST/Nausicaa/main/A_Miscellaneous/A_Readme/5.3.2.jpg" alt="Manufactured glider" width="100%"><br>
  <sup><em>Manufactured fifth-iteration glider and key assembly details.</em></sup>
</p>

- **Evidence from simulation and real flights.**  
  The final mission simulations contain `36,000` runs and `384,795` executed `0.10 s` primitive segments. In random fan layouts not used during held-out simulation validation, closed-loop success improves from `30.0%` to `86.7%` in the random three-fan layout and from `20.0%` to `93.3%` in the random four-fan layout.

<p align="center">
  <a href="https://github.com/user-attachments/assets/d4a86b25-39f0-4fcc-bbba-5313a1fb1c9b">
    <img src="https://raw.githubusercontent.com/GH-X-ST/Nausicaa/main/A_Miscellaneous/A_Readme/four-fan-thumbnail.jpg"
         width="100%"
         alt="Four-fan representative flight-test case">
  </a>
  <a href="https://github.com/user-attachments/assets/89417fed-ad15-4e5b-b527-6ba1ec1c0ea1">
    <img src="https://raw.githubusercontent.com/GH-X-ST/Nausicaa/main/A_Miscellaneous/A_Readme/rand-three-fan-thumbnail.jpg"
         width="100%"
         alt="Random three-fan representative flight-test case">
  </a>
  <a href="https://github.com/user-attachments/assets/73b79e11-a070-430c-9abe-ae00ba1c4b7a">
    <img src="https://raw.githubusercontent.com/GH-X-ST/Nausicaa/main/A_Miscellaneous/A_Readme/rand-four-fan-thumbnail.jpg"
         width="100%"
         alt="Random four-fan representative flight-test case">
  </a>
  <sup><em>Representative flight-test cases. Click each image to open the video.</em></sup>
</p>

---

## Repository Roles

| Record | Purpose |
|---|---|
| [Nausicaa-Thesis](https://github.com/GH-X-ST/Nausicaa-Thesis) | Public thesis landing page and canonical PDF route for discovery. |
| [Thesis DOI](https://doi.org/10.5281/zenodo.21083555) | Archival thesis manuscript record. |
| [Project materials DOI](https://doi.org/10.5281/zenodo.20927007) | Archived software, datasets, logs, and reproducibility materials. |
| [Nausicaa](https://github.com/GH-X-ST/Nausicaa) | Workflow repository for scripts, logs, figures, and experiment artefacts. |

## Citation

```bibtex
@mastersthesis{li2026nausicaa_thesis,
  title  = {Viability-Guided Sim-to-Real Transfer for a Small Fixed-Wing Glider in Uncertain Indoor Updrafts},
  author = {Li, Hanchen},
  school = {Imperial College London},
  year   = {2026},
  type   = {MEng thesis},
  note   = {Department of Aeronautics},
  doi    = {10.5281/zenodo.21083555},
  url    = {https://doi.org/10.5281/zenodo.21083555}
}
```

For the archived software, datasets, logs, and reproducibility materials, cite the companion Zenodo record:

```bibtex
@misc{li2026nausicaa_materials,
  title     = {Nausicaa: Project Materials for Viability-Guided Sim-to-Real Transfer for a Small Fixed-Wing Glider in Uncertain Indoor Updrafts},
  author    = {Li, Hanchen},
  year      = {2026},
  publisher = {Zenodo},
  version   = {v2026.06-thesis},
  doi       = {10.5281/zenodo.20927007},
  url       = {https://doi.org/10.5281/zenodo.20927007}
}
```
