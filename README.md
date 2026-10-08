<div align="center">
    <h1 align="center">cs.tts.elhuyar</h1>
</div>
<div align="center">
[![PyPI](https://img.shields.io/pypi/v/cs.tts.elhuyar)](https://pypi.org/project/cs.tts.elhuyar/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/cs.tts.elhuyar)](https://pypi.org/project/cs.tts.elhuyar/)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/cs.tts.elhuyar)](https://pypi.org/project/cs.tts.elhuyar/)
[![PyPI - License](https://img.shields.io/pypi/l/cs.tts.elhuyar)](https://pypi.org/project/cs.tts.elhuyar/)
[![PyPI - Status](https://img.shields.io/pypi/status/cs.tts.elhuyar)](https://pypi.org/project/cs.tts.elhuyar/)


[![PyPI - Plone Versions](https://img.shields.io/pypi/frameworkversions/plone/cs.tts.elhuyar)](https://pypi.org/project/cs.tts.elhuyar/)

[![CI](https://github.com/codesyntax/cs.tts.elhuyar/actions/workflows/main.yml/badge.svg)](https://github.com/codesyntax/cs.tts.elhuyar/actions/workflows/main.yml)
![Code Style](https://img.shields.io/badge/Code%20Style-Black-000000)

[![GitHub contributors](https://img.shields.io/github/contributors/codesyntax/cs.tts.elhuyar)](https://github.com/codesyntax/cs.tts.elhuyar)
[![GitHub Repo stars](https://img.shields.io/github/stars/codesyntax/cs.tts.elhuyar?style=social)](https://github.com/codesyntax/cs.tts.elhuyar)

</div>

An addon offering TTS using Elhuyar services

## Features

TODO: List our awesome features

## Installation

Install cs.tts.elhuyar with `pip`:

```shell
pip install cs.tts.elhuyar
```

And to create the Plone site:

```shell
make create-site
```

## Contribute

- [Issue tracker](https://github.com/codesyntax/cs.tts.elhuyar/issues)
- [Source code](https://github.com/codesyntax/cs.tts.elhuyar/)

### Prerequisites ✅

-   An [operating system](https://6.docs.plone.org/install/create-project-cookieplone.html#prerequisites-for-installation) that runs all the requirements mentioned.
-   [uv](https://6.docs.plone.org/install/create-project-cookieplone.html#uv)
-   [Make](https://6.docs.plone.org/install/create-project-cookieplone.html#make)
-   [Git](https://6.docs.plone.org/install/create-project-cookieplone.html#git)
-   [Docker](https://docs.docker.com/get-started/get-docker/) (optional)

### Installation 🔧

1.  Clone this repository, then change your working directory.

    ```shell
    git clone git@github.com:codesyntax/cs.tts.elhuyar.git
    cd cs.tts.elhuyar
    ```

2.  Install this code base.

    ```shell
    make install
    ```


### Add features using `plonecli` or `bobtemplates.plone`

This package provides markers as strings (`<!-- extra stuff goes here -->`) that are compatible with [`plonecli`](https://github.com/plone/plonecli) and [`bobtemplates.plone`](https://github.com/plone/bobtemplates.plone).
These markers act as hooks to add all kinds of subtemplates, including behaviors, control panels, upgrade steps, or other subtemplates from `plonecli`.

To run `plonecli` with configuration to target this package, run the following command.

```shell
make add <template_name>
```

For example, you can add a content type to your package with the following command.

```shell
make add content_type
```

You can add a behavior with the following command.

```shell
make add behavior
```

```{seealso}
You can check the list of available subtemplates in the [`bobtemplates.plone` `README.md` file](https://github.com/plone/bobtemplates.plone/?tab=readme-ov-file#provided-subtemplates).
See also the documentation of [Mockup and Patternslib](https://6.docs.plone.org/classic-ui/mockup.html) for how to build the UI toolkit for Classic UI.
```

## License

The project is licensed under GPLv2.

## Credits and acknowledgements 🙏

Generated using [Cookieplone (2.0.2)](https://github.com/plone/cookieplone) and [cookieplone-templates (19d0792)](https://github.com/plone/cookieplone-templates/commit/19d07923b43f38bc80271aab3d4ea54388fa9d23) on 2026-10-08 08:19:55.607763. A special thanks to all contributors and supporters!
