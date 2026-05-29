
# How to Host on GitHub Pages

## Step 1: Create a GitHub Account
If you don't have one, go to https://github.com and sign up for free!

## Step 2: Create a New Repository
1. Click the "+" icon in the top right on GitHub
2. Select "New repository"
3. Name your repository (like "ticketmaster-demo")
4. Choose **Public** (so Appy Pie can access it)
5. Click "Create repository" (don't check any other boxes for now)

## Step 3: Initialize Git Locally
Open Command Prompt or PowerShell and go to your project folder, then run these commands one by one:

```bash
# Initialize git
git init

# Add all files
git add .

# Make your first commit
git commit -m "Initial commit - Ticketmaster demo app"

# Rename main branch (if needed)
git branch -M main

# Add your GitHub repository (replace YOUR_USERNAME and YOUR_REPO_NAME!)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Push to GitHub
git push -u origin main
```

## Step 4: Enable GitHub Pages
1. Go to your repository on GitHub
2. Click on "Settings" (top tab)
3. Scroll down to "Pages" (left sidebar, under "Code and automation")
4. Under "Source", choose:
   - Deploy from a branch
   - Branch: main
   - Folder: / (root) OR /www (we'll use /www)
5. Wait a few minutes - GitHub Pages will build your site!

## Step 5: Get Your Link!
Once GitHub Pages is done, your site will be live at:
`https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/www/`

Use this link in Appy Pie!

## Important Notes
- Use the www folder as your main content (that's where our index.html is!)
- Make sure your repo is **Public** so Appy Pie can access it
- It may take 1-5 minutes for GitHub Pages to update after pushing changes
