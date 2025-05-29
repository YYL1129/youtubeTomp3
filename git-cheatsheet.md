# 🧠 Git Commands Cheat Sheet

## ✅ Save Current Progress

```bash
git add .
git commit -m "Your message"

## explanation 
git add . — Add all files to staging
git commit -m — Save a snapshot of your code


git checkout -b new-branch-name  
# Create a New Branch (for testing), Safe to test changes without touching main branch

git checkout main 
# Switch Between Branches

git merge branch-name 
# Merge Back Changes (if test works) 

git branch -d branch-name
# Delete a Branch (after merging or if not needed)

git checkout HEAD -- filename.py
# Restore a File to Last Commit

git push origin main
# Push to GitHub (optional)


## Push Current Version to GitHub
# In your Codespace terminal, run:
git push origin main
# This will:
# Upload your committed .py files
# Upload git-cheatsheet.md
# Sync everything to your GitHub repo

# Step 1: Commit the missing file
git add git-cheatsheet.md
git commit -m "Add git command cheat sheet"
# Step 2: Push to GitHub
git push origin main
