# 🛠️ click-cli-tool

A minimal Python command-line application built with [Click](https://click.palletsprojects.com/) and managed using [uv](https://github.com/astral-sh/uv). Includes optional plotting support with Plotly.

---

## 🚀 Features

- Simple CLI commands using `Click`
- Lightweight dependency management via `uv`
- Ready to run in Docker
- Example plotting support (if enabled)

---

## 📦 Installation

### 🔧 Option 1: Using Docker (Recommended)

```bash
docker build -t click-cli-tool .
docker run --rm click-cli-tool --help
