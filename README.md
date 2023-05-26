# mantui

mantui is a friendly terminal user interface for Linux man pages.

## About

Linux man pages can be a little intimidating.
mantui provides a friendly interface for command manuals,
with a nicely formatted version of the man page
and a table of contents for quick navigation.

### Built With

- [Textual](https://github.com/Textualize/textual)
- [Pandoc](https://pandoc.org/)

## Getting Started

### Prerequisites

mantui uses [pandoc](https://pandoc.org/) to convert the man page files.
If you don't already have pandoc on your system, you will need to install
pandoc using your platform's package manager.

See https://pandoc.org/installing for more information.

### Installation

Install mantui using [pipx](https://pypa.github.io/pipx/):

```
pipx install git+https://github.com/TomJGooding/mantui.git
```

## Usage

Run `mantui` from the command line followed by the command name for the
man page you want to view:

```
$ mantui grep
```

You can navigate the app with your mouse or keyboard.

## Licence

Licensed under the [GNU General Public License v3.0](LICENSE).
