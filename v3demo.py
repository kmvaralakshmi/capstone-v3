"""Run the complete Phase 3 pipeline and then serve the dashboard."""

from __future__ import annotations

import argparse
import subprocess
import sys
import webbrowser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
URL = "http://127.0.0.1:8000"


def run_pipeline(skip_download: bool) -> None:
    command = [sys.executable, str(ROOT / "scripts" / "run_pipeline.py")]
    if skip_download:
        command.append("--skip-download")
    result = subprocess.run(command, cwd=ROOT)
    if result.returncode != 0:
        raise SystemExit(result.returncode)


def serve_dashboard(open_browser: bool) -> None:
    print(f"\nPipeline complete. Dashboard: {URL}")
    if open_browser:
        webbrowser.open(URL)
    subprocess.run(
        [
            sys.executable,
            "-m",
            "uvicorn",
            "backend.app:app",
            "--host",
            "127.0.0.1",
            "--port",
            "8000",
        ],
        cwd=ROOT,
        check=False,
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run downloader, Agents 1-7, and the frontend backend in order."
    )
    parser.add_argument(
        "--skip-download",
        action="store_true",
        help="Use existing BRSR files and start with Agents 1-7.",
    )
    parser.add_argument(
        "--no-browser",
        action="store_true",
        help="Do not open the dashboard automatically after the pipeline.",
    )
    args = parser.parse_args()

    print("=== V3 DEMO: downloader -> Agents 1-7 -> dashboard ===")
    run_pipeline(args.skip_download)
    serve_dashboard(not args.no_browser)


if __name__ == "__main__":
    main()
