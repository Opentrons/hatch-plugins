from __future__ import annotations

from pathlib import Path
from os import linesep
import subprocess


def _indent(msg: str, count: int = 0) -> str:
    lines = msg.split(linesep)
    indent = "\t" * count
    return indent + f"{indent}{linesep}".join(lines)


class SubprocFailed(Exception):
    def __init__(self, command: str, returncode: int, stdout: str, stderr: str) -> None:
        self.message = f"Command {command} failed: {returncode}!{linesep}stdout:{linesep}{_indent(stdout, 1)}{linesep}stderr:{linesep}{_indent(stderr, 1)}"
        self.command = command
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr

    def __repr__(self) -> str:
        return f"<SubprocFailed command={self.command} returncode={self.returncode}>"

    def __str__(self) -> str:
        return self.message


def build_wheel(proj_path: Path, output_path: Path | None = None) -> Path:
    output = output_path or proj_path / "dist"
    output.mkdir()
    cmd = [
        "python",
        "-m",
        "build",
        "--no-isolation",
        "--wheel",
        "-o",
        str(output),
        str(proj_path),
    ]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    stdout_content = stdout.decode("utf-8")
    stderr_content = stderr.decode("utf-8")
    if proc.returncode:
        raise SubprocFailed(
            " ".join(cmd), proc.returncode, stdout_content, stderr_content
        )
    for line in stdout_content.split(linesep):
        if ".whl" in line:
            for part in line.split(" "):
                if ".whl" in part:
                    return output / part
    raise RuntimeError(
        f'Failed to find wheel in stdout from {" ".join(cmd)}!{linesep}stdout:{linesep}{_indent(stdout_content)}'
    )
