
#!/usr/bin/env python3

import subprocess
import sys
import os
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).parent.resolve()
DIST = ROOT / "dist"
RELEASE_NOTES = ROOT / "rels.md"


def run(command, check=True):
    print(f"\n> {' '.join(map(str, command))}")
    subprocess.run(command, cwd=ROOT, check=check)


def main():
    print("\n🚀 RELEASE MANAGER\n")

    version = input("New version: ").strip()
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        sys.exit("Invalid version format!")

    commit_name = input("Commit name: ").strip()
    if not commit_name:
        sys.exit("Commit name cannot be empty!")

    if not RELEASE_NOTES.exists():
        sys.exit("rels.md not found!")

    tag = f"v{version}"

    confirm = input(
        f"\nRelease {tag} with commit '{commit_name}'? [y/N]: "
    ).strip().lower()

    if confirm != "y":
        sys.exit("Cancelled.")

    # Update version
    pyproject = ROOT / "pyproject.toml"

    if pyproject.exists():
        print("\nUpdating pyproject.toml...")
        content = pyproject.read_text()
        content = re.sub(
            r'(?m)^version\s*=\s*".*?"',
            f'version = "{version}"',
            content,
            count=1
        )
        pyproject.write_text(content)

    # Build
    print("\n📦 Building packages...")
    shutil.rmtree(DIST, ignore_errors=True)

    run([sys.executable, "-m", "build"])

    # Commit
    print("\n📝 Creating commit...")
    run(["git", "add", "-A"])
    run(["git", "commit", "-m", commit_name])

    # Tag
    run(["git", "tag", "-a", tag, "-m", tag])

    # Push
    print("\n⬆️ Pushing to GitHub...")
    run(["git", "push", "origin", "HEAD"])
    run(["git", "push", "origin", tag])

    # PyPI
    print("\n🐍 Uploading to PyPI...")
    run([
        sys.executable, "-m", "twine", "upload",
        *map(str, DIST.glob("*"))
    ])

    # GitHub Release
    print("\n🐙 Creating GitHub Release...")
    run([
        "gh", "release", "create", tag,
        *map(str, DIST.glob("*")),
        "--title", tag,
        "--notes-file", str(RELEASE_NOTES)
    ])

    print(f"\n✅ Release {tag} published successfully!")


if __name__ == "__main__":
    main()
