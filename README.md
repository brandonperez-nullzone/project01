# Dynamic System Evaluator

**Dynamic System Evaluator** is a lightweight Python project for controlled evaluations, configuration testing, and environment-aware execution. It automatically prepares its configuration, runs locally, and adapts to any compatible system without manual setup.

---

## Overview

The tool performs a basic inspection of the running context, generates required configuration files, and executes predefined tasks accordingly.  
All actions occur **locally** — no external network connections, no background services, and no system-level modifications.

Use cases include:
- Internal security or configuration assessments
- Educational demonstrations and safe automation exercises
- Reproducible, portable setups for training or testing

---

## Quick Start

**Requirements**
- Python 3.8+

**Install**
```bash
pip install -r requirements.txt
```
**Run**
python3 main.py
The system will initialize, generate any missing configuration files, and display a summary of the current execution context. No manual configuration is required.
