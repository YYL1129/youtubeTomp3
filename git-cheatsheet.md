# 🧠 Git Commands Cheat Sheet

A quick reference to help you manage Git in GitHub Codespaces.

---

## ✅ Save Your Work (Snapshot)

```bash
git add .
git commit -m "Your message"
```

- `git add .` — Stage all changed files  
- `git commit -m` — Save a snapshot with a message

---

## 🌿 Work on a Safe Copy (Branch)

```bash
git checkout -b new-branch-name
```

- Creates a new branch to test code changes safely

---

## 🔁 Switch Between Branches

```bash
git checkout main
```

- Go back to the main branch

---

## 🔀 Merge Branch Changes

```bash
git merge branch-name
```

- Merge your test branch into main (if successful)

---

## 🗑️ Delete Unused Branch

```bash
git branch -d branch-name
```

- Clean up branches you no longer need

---

## ♻️ Revert a File to Last Commit

```bash
git checkout HEAD -- filename.py
```

- Restore the file to its last committed state

---

## 🚀 Push Current Version to GitHub

```bash
git push origin main
```

- Upload your committed files to GitHub

---

## 📥 Push a New File (e.g. cheat sheet)

```bash
git add git-cheatsheet.md
git commit -m "Add git command cheat sheet"
git push origin main
```

- Adds your markdown file and uploads it to your GitHub repo
