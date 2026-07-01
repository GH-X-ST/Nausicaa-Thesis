<p align="center">
  <a href="https://gh-x-st.github.io/Nausicaa-Thesis/">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/Read-Thesis-ffffff?style=for-the-badge&labelColor=0d1117">
      <source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/badge/Read-Thesis-000000?style=for-the-badge&labelColor=ffffff">
      <img src="https://img.shields.io/badge/Read-Thesis-6e7781?style=for-the-badge&labelColor=ffffff" alt="Read thesis">
    </picture>
  </a>

<p align="center">
  <sub>A thesis submitted to the Department of Aeronautics</sub><br>
  <sub>in partial fulfilment of the requirements for the degree of</sub><br>
  <sub>Master of Engineering (MEng) in Aeronautical Engineering</sub><br>
  <sub>at</sub><br>
  <sub>Imperial College London</sub><br>
  <sub>Submitted: 15 June 2026</sub><br>
  <sub>Defended: 19 June 2026</sub><br>
</p>

![Thesis cover light](https://raw.githubusercontent.com/GH-X-ST/Nausicaa/main/A_Miscellaneous/A_Readme/Thesis_Cover.png#gh-light-mode-only)
![Thesis cover dark](https://raw.githubusercontent.com/GH-X-ST/Nausicaa/main/A_Miscellaneous/A_Readme/Thesis_Cover_Dark.png#gh-dark-mode-only)

<br>

<p align="center">
  <a href="https://doi.org/10.5281/zenodo.21083555">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21083555-708090?style=for-the-badge&labelColor=0d1117">
      <source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21083555-232333?style=for-the-badge&labelColor=ffffff">
      <img src="https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21083555-2ea043?style=for-the-badge&labelColor=ffffff" alt="Thesis DOI">
    </picture>
  </a>
  <a href="https://github.com/GH-X-ST/Nausicaa">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/Workflow Repository-Nausicaa-ffff00?style=for-the-badge&labelColor=0d1117">
      <source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/badge/Workflow Repository-Nausicaa-0000cd?style=for-the-badge&labelColor=ffffff">
      <img src="https://img.shields.io/badge/Workflow-Nausicaa-7b1fa2?style=for-the-badge&labelColor=ffffff" alt="Nausicaa workflow repository">
    </picture>
  </a>
</p>

<br>

## About

Motivated by low-altitude flight near flow-shaping boundaries, where local lift can extend endurance but reduce recovery margin, this thesis investigates whether a small fixed-wing glider controller developed in simulation can transfer to repeated real flights through uncertain local updrafts. To study this problem repeatably, the work develops an indoor fixed-wing sim-to-real workflow combining Vicon feedback, measured command latency, a manufactured glider, a safety-bounded flight volume, and fan-generated updrafts represented by imperfect measured surrogates. The controller is formulated as viability-guided manoeuvre primitive selection. Instead of tracking one planned trajectory through an uncertain flow field, the glider repeatedly selects short stabilised manoeuvre primitives every 0.10 s in flight. Each primitive is generated, replayed, and validated offline so online selection can use evidence about entry compatibility, continuation probability, failure risk, safety margin, lift exposure, and energy change. The dense primitive library is compressed into executable tiers, and spatial lift memory is tested. Across 36,000 mission simulations and 384,795 executed primitive segments, for launch speeds above 5.0 m/s the balanced compressed library preserves raw-library performance while reducing the mean evaluated set from 110.1 to 7.0 candidates and completing 85.2 percent of selector decisions within the primitive horizon. Spatial memory changes fewer than 10 percent of selections and gives little aggregate benefit. In random fan layouts not used during controller validation, closed-loop success rises from 30.0 to 86.7 percent in the random three-fan layout and from 20.0 to 93.3 percent in the random four-fan layout. The thesis demonstrates transfer as a traceable evidence chain from modelling and validation to real-flight survival through uncertain indoor lift.

<p align="center">
  <img src="https://raw.githubusercontent.com/GH-X-ST/Nausicaa/main/A_Miscellaneous/A_Readme/1.jpg" alt="Thesis chapter flow from literature review through system architecture, lift field characterisation, aircraft design, controller development, flight test, and conclusions" width="100%"><br>
  <sup><em>Thesis structure.</em></sup>
</p>

---

## Video Evidence

These flight-test videos are supplementary visual evidence that are not embedded in the thesis PDF.

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

## Citation

For academic citation, please cite the MEng thesis:

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
````

 A direct citation is also avaliable when a thesis-format reference is required.
 
```bibtex
@mastersthesis{li2026nausicaa_thesis,
  title  = {Viability-Guided Sim-to-Real Transfer for a Small Fixed-Wing Glider in Uncertain Indoor Updrafts},
  author = {Li, Hanchen},
  school = {Imperial College London},
  year   = {2026},
  type   = {MEng thesis},
  note   = {Department of Aeronautics}
}
```

For the archived software, datasets, logs, and reproducibility materials, please cite the [Zenodo record](https://doi.org/10.5281/zenodo.20927007):

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
