---
# https://vitepress.dev/reference/default-theme-home-page
layout: home

hero:
  name: "SC25 Trame Tutorial"
  text: "HPC-Enabled Web, Jupyter, and Desktop"
  tagline: "Creation of Bespoke Scientific Visualization Applications for Simulation, Experiment, and AI Data"

  actions:
    - theme: brand
      text: Python
      link: /python/
    - theme: alt
      text: Jupyter
      link: /jupyter/
    - theme: alt
      text: Binder
      link: https://mybinder.org/v2/gh/Kitware/sc25-trame-tutorial/main?labpath=jupyter

features:
  - title: Python virtual environments
    icon:
      src: https://cdn.worldvectorlogo.com/logos/python-5.svg
      alt: Python
      width: 54
    details: This tutorial can be done using local Python virtual environments for demonstrations and exercises. This track is prefered as it allow you to use your common dev tools and IDE when exploring trame.
    link: /python/
  - title: Jupyter Lab
    icon:
      src: https://upload.wikimedia.org/wikipedia/commons/3/38/Jupyter_logo.svg
      alt: Jupyter Lab
      width: 45
    details: This tutorial can be done using a local setup of Jupyter Lab. A special track with dedicated notebook has beed created and available to ease demonstrations and exercises.
    link: /jupyter/
  - title: Binder
    icon:
      src: https://mybinder.readthedocs.io/en/latest/_static/favicon.png
      alt: Binder
      width: 48
    details: This tutorial can be followed online by using Binder for most of the demonstrations and exercises. That track is designed to overcome system incompatibility that prevent the two previous track to be used.
    link: https://mybinder.org/v2/gh/Kitware/sc25-trame-tutorial/main?labpath=jupyter
  - title: Peacock 2.0 (INL)
    icon:
      src: /usecases.svg
      alt: Peacock
      width: 54
    details: Trame Peacock provides a refresh takes on input deck editor for MOOSE simulations.
    link: /usecases/peacock
  - title: Building Interactive Dashboards for the Beam, Plasma & Accelerator Simulation Toolkit (BLAST) with trame
    icon:
      src: /usecases.svg
      alt: BLAST codes on HPC
      width: 54
    details: The Beam, Plasma & Accelerator Simulation Toolkit (BLAST) is a comprehensive suite of simulation codes for modeling particle accelerators, beams, and plasmas. This talk presents our experience leveraging trame to develop interactive dashboards for the BLAST codes WarpX and ImpactX. We will present how trame is enabling more intuitive and efficient simulation workflows, as well as the integration and control of digital twin infrastructures that combine simulations, AI/ML models, and experimental data.
    link: /usecases/blast
  - title: ArrowFlow (M-Star)
    icon:
      src: /usecases.svg
      alt: ArrowFlow
      width: 54
    details: Near realtime CFD simulation with template based solution exploration.
    link: /usecases/arrowflow
  - title: EPIC (LANL)
    icon:
      src: /usecases.svg
      alt: EPIC
      width: 54
    details: Enabling genomic discovery via visualization at scale with ParaView and trame.
    link: /usecases/epic
  - title: DAIMSAL (ANL)
    icon:
      src: /usecases.svg
      alt: DAIMSAL
      width: 54
    details: something cool...
    link: /usecases/daimsal
  - title: (XAI+NR).TK
    icon:
      src: /usecases.svg
      alt: XAITK + NRTK
      width: 54
    details: Explainable AI and Natural robustness analysis for AI models.
    link: /usecases/xaitk-nrtk
---

## Content description

In this hands-on tutorial, participants will learn to create bespoke scientific visualization applications using Trame, a powerful Python framework for building interactive, web-based visualization frontends. Trame simplifies web-based application development by managing UI layout, state, events, and widgets entirely in Python—abstracting away the need to write HTML, CSS, or JavaScript. Trame wraps popular visualization engines like VTK and ParaView, allowing users to rapidly develop rich applications that run seamlessly across web browsers, Jupyter notebooks, and desktop environments—ideal for HPC-enabled simulations, experimental workflows, and AI-driven data analysis. The tutorial will introduce how to design responsive and modern GUIs using Vuetify through Trame’s declarative Python syntax, enabling sophisticated layouts, widgets, and event handling. We will present how to integrate 3D visualization using VTK and ParaView, showcasing different rendering modalities for the interactive exploration of complex datasets. Together, we will explore integrating Markdown content and common Python plotting libraries—including Matplotlib, Altair, PyVista, and Plotly—into Trame applications to support a broad spectrum of scientific visualization needs. We will cover both intermediate and advanced topics, leveraging modern examples drawn from simulation, experimental science, and AI-driven analysis to ground the material in real-world workflows. By the end, participants will be equipped to build tailored visualization applications that bridge HPC backends with intuitive, interactive frontends, all from within the Python ecosystem.

## Requirements

For this tutorial we are expecting to have the following software available on your computer.
- __git__ for downloading the hands-on material. ([Home page](https://git-scm.com/))
- __uv__ for handling Python versions and virtual environments to ensure isolation. ([Home page](https://docs.astral.sh/uv/getting-started/installation/))
- __ParaView__ for running some visualization examples. ([Download page](https://www.paraview.org/download/))
- __IDE__ or __Text editor__ for editing Python files. (i.e. [VSCode](https://code.visualstudio.com/))

## Duration

The total content will be deliver over 6 hours in 30 minutes chunk with blocks of 1 hour and 30 minutes.

## Getting hands-on material

```bash
git clone https://github.com/Kitware/sc25-trame-tutorial.git
cd sc25-trame-tutorial
```

## Tutorial goals


- Introduce Trame as a modern, Pythonic solution for building interactive scientific visualization applications across web, desktop, and Jupyter environments.
- Demonstrate integration of rich visualization backends (VTK, ParaView) with GUI elements and plotting libraries.
- Provide hands-on experience designing custom apps that can handle data from simulations, experiments, and AI workflows—especially in HPC contexts.

__For Beginning Attendees__
- Understand the basic architecture of a Trame application.
- Learn how to launch a simple app in the browser or Jupyter using Python only.
- Use basic widgets (buttons, sliders, layouts) to control visualization parameters.
- Integrate interactive 3D visualizations using VTK or ParaView.
- Understand Trame’s state management system and how to link UI controls with visualization logic.
- Embed plotting libraries like Matplotlib, Altair, PyVista, and Plotly in multi-panel apps.

__For Intermediate Attendees__ 
- Explore multiple rendering modalities and advanced 3D interaction patterns (e.g., linked views, LOD control, client/server rendering).
- Customize Vuetify components and extend the UI with advanced interactions.
- Learn to structure more complex applications with custom layouts and multiple views.

__For Advanced Attendees__
- Integrate HPC or AI data pipelines and enable dynamic data loading or streaming.
- Optimize performance for large datasets and explore strategies for scalability.
- Deploy Trame applications to the desktop, Jupyter, and cloud.
