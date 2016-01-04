### How to use Git and GitHub
This Notes were taken based on the How to use Git and GitHub course on [Udacity](http://udacity.com).
***
## Lession 1 Notes:
***

#### Git
***
A Version Control System

##### Git command description

**git commit -m "message"**

```
This command is used to save a version of your working file
and save a message indicating the changes made in the file.

When to commit:  commit per logical change. For example, if you fixed a typo, then fixed a bug in a separate part of the file.

Tracking across files?
	Is important if all the files in the repository have a dependency in each other to the program or project to work.
	commad git log --stat
	give you some statisty of what files have change when working and tracking across multiple files.
	
Commits with Miltiple Files.

Entering commit IDs

If it is easier, you may enter the first four or more characters of the commit ID rather than pasting the entire ID.
```
**git log**

```
This command is used to see all file versions and commets made. Each commit does an unique id, the author's name, a date, and the message associated with the commit. You can compare two file by ids to see changes btwn two file versions.
    commad to compare two files
    git diff <id-1> <id-2>
    
    NOTES:
    
    To stop viewing git log output, press q (which stands for quit).
    
    To get colored diff output, run git config --global color.ui auto
    
```

**git clone**
***
```
The 'git clone' is used to clone an existen repository to a local host.
For example cloning an existen repo on a coding sharing and colaboration platform. You the type the commad follow by its HTTPS or URL like
	git clone https://github.com/udacity/asteroids.git
	
	The above command will clone a repo in cloud to a local host machine.
	

```
**git chekout**
***
This command is uses for checking out prior commits<br/>
**Note**: it is not the same as SVN checkout if you are comming from the Version Control System enviroment.

The command Caroline types to checkout the "Revert controls" commit is<br/>
`git checkout b0678b161fcf74467ed3a63110557e3d6229cfa6`


__Using Git commads__

```
/* Set up Git Configuration */

git config --global user.email "you@yourdomain.com"

git config --global user.name "Your Name"

git config --global core.editor "vi"

git config --global color.ui true

/* See Git configuration */

git config --list

/*  To initialise a local repository */

git init 

/*  Add a file to the repo */

git add 

/* commit the change to git */

git commit -m "Message goes here" 

/*  see the commits */

git log 

/*  Git has a 3 Tier Architecture:  Working - Staging - Repo
Changes to files are put in a Checksum SHA-1 hash 40digit value containing parent hash, author and message.
HEAD is the latest commit of the checked out branch */

/*  Basic Commands  */

git status  /*  the command 'git status' tells which files are not added or committed from Working to Staging to Repository */

git commit -m "" /*  Commits and changes to all files that are in Staging into Repo  */

git diff /*  show changes between Working and Local Repo, no file supplied shows all files  */

git diff --staged /*  shows changes between Staged and Local Repo  */

git rm file.txt /*  will remove file from working then git commit -m "" to also remove from Repo */

git rm --cached file.txt /* leaves copy of file in Working but removes from Staging and Repo */

git mv /*  rename or move files - then git commit -m "" to move to Repo */

git commit -am "text goes here" /* adds all files straight to Repo from Staging if they have changes - meaning they skip git add */

git checkout -- file.txt /*  restore Repo file to Working Directory using current branch  */

git reset --soft HEAD^ /* restore repo file to staging */

git reset HEAD file.txt /*  Move a Stage file out of Stage back to Working */

git commit --amend -m "message" file.txt /* Change last commit to Repo (only last one can change) */

/* Reverting --soft --mixed --hard will go back to previous commits*/
git log /* gets the sha1s so you can see the coomits where you want revert  back to  */

git reset --soft sha /* changes Repo but not Staging or Working */

git reset --mixed sha /* changes Repo and Staging but not Working */

git reset --hard sha /* changes all 3 Tiers */

git clean -f /* remove untracked files from Working  */

.gitignore /* ignores files to track in Working / track the .gitignore file */

Global Ignore /* create in home folder  */ 
.gitignore_global
/* Add in  */
.DS_Store
.Trashes
.Spotlight_V100



git config --global core.excludesfile ~/.gitignore_global /* add to gitconfig */

/* Stop tracking changes */

git rm --cached file.txt /* leaves copy in Repo and Working */


/* Track Folders changes
Add an invisble file to a folder like .gitkeeper then add and commit */

/* Commit Log  */
git ls-tree HEAD
git ls-tree master
git log --oneline
git log --author="Neil"
git log --grep="temp"

/* Show Commits */

git show dc094cb /*  show SHA1 */

/* Compare Commits
Branches */

git branch /*  Show local branches * is the one we are on */

git branch -r /* Shows remote branches */

git branch -a /* Shows local and remote */

git branch newbranch /* creates a new branch */

git checkout newbranch /* switch to new branch */

git checkout -b oldbranch /* creates and switches to new branch  */

git push origin newbranch /* Push new branch to remote */


/* Diff in Branches */

git diff master..otherbranch /*  shows diff */

git diff --color-words master..otherbranch /*  shows diff in color */

git branch --merged /*  shows any merged branches */

/* Rename Branch */

git branch -m oldname newname

/* Delete  Branch */

git branch -d nameofbranch

/* Merge Branch  */

git merge branchname /* be on the receiver branch to merge the other branch */

/* Merge Conflicts between the same file on 2 branches are marked in HEAD and other branch */

git merge --abort /*  Abort basically cancels the merge */

/* Manually Fix Files and commit
The Stash */

git stash save "text message here"

git stash list /* shows whats in stash */

git stash show -p stash@{0} /* Show the diff in the stash */

git stash pop stash@{0} /*  restores the stash deletes the tash */

git stash apply stash@{0} /*  restores the stash and keeps the stash */

git stash clear /*  removes all stash */

git stash drop stash@{0}


/* Remotes
You can push and fetch to the remote server, merge any differences - then push any new to the remote - 3 branches work remote server branch, local origin master and local master
Create a repo in GitHub, then add that remote to your local repo */

git remote add origin https://github.com/neilgee/genesischild.git /*  origin can be named whatever followed by the remote */

git remote /* to show all remotes */

git remote show origin /*to see remote URL*/

git remote remove origin /* to remove remote */

git remote rm origin /* to remove remote */

/* Push to Remote from Local */

git push -u origin master /* push to remote(origin) and branch(master)
/* Cloning a GitHub Repo - create and get the URL of a new repository from GitHub, then clone that to your local repo, example below uses local repo named 'nameoffolder' */

git clone https://github.com/neilgee/genesischild.git nameoffolder

/* Push to Remote from Local - more - since when we pushed the local to remote we used -u parameter then the remote branch is tracked to the local branch and we just need to use... */

git push

git push origin newbranch /* Push a branch to a remote */

/* Fetch changes from a cloned Repo */

git fetch origin /*  Pulls down latest committs from remote origin/master not origin, also pull down any branches pushed to Repo
Fetch before you work
Fetch before you pull
Fetch often */

/* Merge with origin/master */

git merge origin/master

git pull /* you can also do git pull which is = git fetch + git merge
Checkout/Copy a remote branch to local */

git branch branchname origin/branchname /*  this will bring the remote branch to local and track with the remote */

/* Delete branch */

git branch -d branchname

/* Checkout and switch branch and track to remote */

git checkout -b nontracking origin/nontracking

/* Remove remote branch */

git push origin --delete branch


/*Undoing*/

git checkout path-to-file /*restores a file before it is staged */

git reset HEAD path-to-file /*if it is staged - restores a file from last commit and then git checkout path-to-file */

git checkout HEAD^ path-to-file /*if is staged and committed - restores from last commit */

git reset --hard HEAD^ /*restore prior commit */

/*Keeping a Fork synced with the original repo*/

git remote add upstream https://github.com/user/originalrepo /* From the forked repo - add the original master repo */

git pull upstream master /* Sync it up */

/*Tags*/

git tag -a v1.0.0 -m "add message here" /*tagging a commit with a version number*/

git push --tags /* pushes tag info to master remote */

/*You can checkout a commit and add a tag to that commit by checking out its SHA */

git checkout f1f4a3d /*checking out a commit - see the commit SHAS by git log */
```

#### Version Control
***

A Version Control System is useful to save preview copies of your file. And it is really handy to compare two different version of two files.

**As a programmer**: is important to save version or changes of sources code at a regular intervals ( e.g every hour or less).

Examples of Version control system:

* Git
* SVN
* CVS
* SBM

#### GitHub
***
Code sharing and collaboration platform
***
Note: It is important to know Unix Command Line Basic

##### What will be cover
***
LESSION 1: Why version control?
			install Git + read-only usage.
			
LESSION 2: read + write Git.

LESSION 3: Share + Collaborate with others in GitHub platform.
***

#### Finding Diffs Between Larger Files
* * *
##### Automatically Compare Files
**Windows** - FC (File Compare) is an utility on the cmd (Command Prompt)

```
Command =  FC 1st-Argument-FileName 2st-Argument-FileName
```

**Mac and Linux** - Diff (Difference).

**Note**: it may differ depending on the command for the terminal using by the user.

```
Command =  diff -u 1st-Argument-FileName 2st-Argument-FileName
```
### Downloading necessary files

* Save [this file](https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.bash) in your home directory with the name `git-completion.bash`.
* Save [this file](https://raw.githubusercontent.com/git/git/master/contrib/completion/git-prompt.sh) in your home directory with the name `git-prompt.sh`.
* Download `bash_profile` from the Downloadables section.
* If you already have a file in your home directory named `.bash_profile`, copy the content from bash_profile_course and paste it at the bottom of `.bash_profile`. Otherwise, move `bash_profile` to your home directory and rename it to `.bash_profile`. If you use Linux, you may need to name this file `.bashrc` instead of `.bash_profile`. (If you're curious to learn more about how bash prompts work, see [this page](http://www.cyberciti.biz/tips/howto-linux-unix-bash-shell-setup-prompt.html).)
* [.bash_profile](https://www.udacity.com/api/nodes/3333158951/supplemental_media/bash-profile-course/download) example download. just rename it the download file with the dot at the biginning.

### Make sure you can start your editor from the terminal

If you use Sublime, you can do this by add the following line to your `.bash_profile` (you may need to change the path if Sublime is installed in a different location for you):

```
alias subl="/Applications/Sublime\ Text\ 2.app/Contents/SharedSupport/bin/subl"
```

### Making Git configurations

Run the following Git configuration commands. The first one will need to be modified if you are using a text editor other than Sublime, or if Sublime is installed in another location for you. See [this page](https://help.github.com/articles/associating-text-editors-with-git/) for the correct command for a couple of other popular text editors. For any other editor, you'll need to enter the command you use to launch that editor from the terminal.

```
git config --global core.editor "'/Applications/Sublime Text 2.app/Contents/SharedSupport/bin/subl' -n -w"

git config --global push.default upstream

git config --global merge.conflictstyle diff3
```
(Instead of the first command, you may be able to use the simpler `git config --global core.editor "subl -n -w"` as shown in the video, but many students have found this does not work for them.)

### Restart the terminal

You'll need to close and re-open the terminal before all your changes take effect.
***

#### General Notes:

##### Relationshipts
    type -> of
    part-> of
    operates -> on

#### Git Errors and Warnings Solution

***
**Should not be doing an octopus**
<br />
Octopus is a strategy Git uses to combine many different versions of code together. This message can appear if you try to use this strategy in an inappropriate situation.
***
**You are in 'detached HEAD' state**
<br />
HEAD is what Git calls the commit you are currently on. You can “detach” the HEAD by switching to a previous commit, which we’ll see in the next video. Despite what it sounds like, it’s actually not a bad thing to detach the HEAD. Git just warns you so that you’ll realize you’re doing it.

***
**Panic! (the 'impossible' happened)** 
This is a real error message, but it’s not output by Git. Instead it’s output by GHC, the compiler for a programming language called Haskell. It’s reserved for particularly surprising errors!

***
**Takeaway** We hope these errors and warnings amused you as much as they amused us! Now that you know what kind of errors Git can throw, you’re ready to start checking out previous versions of files with Caroline.
***

***
## Lession 2 Notes:
***

#### Repository

**Note:** The content of **Git** is in a hidden file .git </config, /object>
<br/>**?** Read about Meta data
<br>

##### How to initialize git an exist repository?
Run the command `git init` to initialize git in an exist repo or create a new folder or directory and run the command once you have navigate to the directory in the command line.<br/>

working directory
Staging Area
Repository

Choosing what changes to commit

If you accidentally add a file to the staging area, you can remove it using `git reset`. For example, if you accidentally add lesson_2_reflections.txt, but don’t want it to be committed yet, run `git reset lesson_2_reflections.txt` and the file will be removed from the staging area, but it will still be in your working directory.

#### ERRORS
***
* fatal: your current branch 'master' does not have any commits yet
<br/> the above error show up when you have 0 commit in a repo. 
But nothing is wrong with the repo, don't panic yet lol.






#### Resources:
***
* [Become a GitHub Pro](http://blog.udacity.com/2015/06/become-github-pro.html)

* [How to write the perfect pull request](https://github.com/blog/1943-how-to-write-the-perfect-pull-request)







