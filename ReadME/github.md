# Normal Workflow

Create Project
      ↓
Use Git Locally
      ↓
Make Commits
      ↓
Create GitHub Repository
      ↓
Connect Project to GitHub
      ↓
Push Code Online




# Step-by-Step

1. Create Project Folder
   eg: myproject

2. Open Terminal in Project 
   eg; cd myproject 

3. Start Git 
   eg: git init

4. Write Your Code 
   eg:HTML
     Django
     Flutter
     Python   

5. Save Versions
   eg:git add .
      git commit -m "First commit"

      At this point:

     project is only on your laptop
     GitHub is not connected yet  


 # Later Connect to GitHub

  6. Create Repository on Github

  7. Connect Local projecct to Github
     eg: git remote add origin YOUR_REPOSITORY_URL

    eg:  git remote add origin https://github.com/lemon/myproject.


  8. Push Code
    git push -u origin main




# important Understanding 

GIt : Manage Project locally 
Github : Store project online 


you can use git without Github

But GIthub us useful for:
Backend 
portifolio
teamwork
sharing code


terminal 

1. Go to your project folder

cd your-project-folder 

2. initalized git

 git init

3. Connect to github

git remote add origin https://github.com/username/repo-name.git

4. Add all files 

 git add . 

5. commit code

git commit -m "first commit"

6. push to github  

 git branch -M main
git push -u origin main



# when there is multiple commite alreadyn happen 


1. Check changes

 git status

2. add changes

 git add .

3. Commit changes

 git commit -m "updated login page"

4. push to github

 git push 



 # case 3: FIrst tinme tepo already has code


 git pull origin main --allow-unrelated-histories
git add .
git commit -m "merge changes"
git push



# Quick summary 

# First time 

git init
git remote add origin <url>
git add .
git commit -m "first commit"
git branch -M main
git push -u origin main


# After first push 

git add .
git commit -m "message"
git push 

# if GIthub already has files

git pull origin main --allow-unrelated-histories
git add .
git commit -m "merge"
git push


# simple understanding 

add → select changes
commit → save snapshot
push → upload to GitHub
pull → download from GitHub   