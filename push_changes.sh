#!/usr/bin/env bash
set -euo pipefail

# Safe push script for Git Bash. Run this from the repository root or
# run `bash push_changes.sh` inside the repo.

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$REPO_DIR"

if ! command -v git >/dev/null 2>&1; then
  echo "Error: git is not installed or not available in PATH. Install Git and retry." >&2
  exit 1
fi

echo "Repository: $REPO_DIR"

echo "Current git version: $(git --version)"

echo "Showing status (porcelain):"
git status --porcelain

echo "Adding all changes (including untracked files)..."
git add -A

if git diff --cached --quiet; then
  echo "No changes staged for commit. Nothing to commit."
else
  COMMIT_MSG="Add calculator interface, statistics and graphics modules; export functions in package"
  echo "Committing with message: $COMMIT_MSG"
  git commit -m "$COMMIT_MSG"
fi

CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
echo "Current branch: $CURRENT_BRANCH"

# If no upstream, push with -u to set it
UPSTREAM_SET=true
if ! git rev-parse --abbrev-ref --symbolic-full-name @{u} >/dev/null 2>&1; then
  UPSTREAM_SET=false
fi

if [ "$UPSTREAM_SET" = false ]; then
  echo "No upstream set for branch '$CURRENT_BRANCH'. Pushing and setting upstream to origin/$CURRENT_BRANCH..."
  git push -u origin "$CURRENT_BRANCH"
else
  echo "Pushing to origin/$CURRENT_BRANCH..."
  git push origin "$CURRENT_BRANCH"
fi

echo "Done. If push prompted for credentials, follow the prompts or configure an SSH key / credential helper / PAT."
