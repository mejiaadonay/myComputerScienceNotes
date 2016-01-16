## Linux Command Line Basic
###	 Getting Started with the Shell
***

### Course Summary

We have built this course for beginners who have no experience with the Linux system and the command-line interface.

In this course, you'll learn the basics of the command line interface of a Linux server: the terminal and shell (GNU Bash). This course includes an introduction to files and directories in the Linux filesystem.

### Why Take This Course?

Most servers on the Internet today run on Linux or other Unix-like systems. Installing, configuring, and troubleshooting often relies on the command line interface. This, accordingly, is foundational web knowledge, and in fact many of our intermediate and advanced courses rely on a familiarity with the command-line interface to run servers, work with version control systems and more.

### Prerequisites and Requirements

To take this course, you should have beginner-level experience in a programming languages such as Python or JavaScript. While this course does not involve doing any programming, it does use concepts that are familiar to the beginning programmer such as "function", "expression", and "string".

Note: This course is intended for beginners to the shell environment. If you have done shell scripting or other extensive use of the shell before, this course will probably be too introductory for you. You might want to check out our Configuring Linux Web Servers course.

See the Technology Requirements for using Udacity.

### What Will I Learn?

### Syllabus

# Lesson 1: Get Into the Shell

In this lesson, you'll learn about the terminal user interface and how you can interact with a Linux server using shell commands.
***
## Your own Linux box
To learn the Linux shell, you need a Linux machine to run it on. But we can't really ship a new Linux computer to every one of you. So instead you will set up a Linux **virtual machine** (VM) on your own computer.

You'll be using the [VirtualBox](https://www.virtualbox.org/wiki/Downloads) application to run the virtual machine, and the [vagrant](https://www.vagrantup.com/) software to configure it.

This virtual-machine setup is very similar to the ones you will use in later Udacity courses on the Linux platform. So when you get to those courses, you will not need to re-install this software.

Setting the virtual machine up is not complicated, but it will take some time when your computer downloads the Linux OS. Follow the instructions below to set it up before proceeding on in this course.

## What's a virtual machine?

A virtual machine is a program that runs on your Windows or Mac computer, and that can run a different operating system inside it. In this case, you'll be running an Ubuntu Linux server system.

## 1. Install Git

You can skip this step if you are not running Windows, but many other courses use Git, so you may want to install it now.

[Download Git from git-scm.com.](http://git-scm.com/downloads) Install the version for your operating system.

On Windows, Git will provide you with the **Git Bash** terminal program, which you will use to run and connect to your Linux VM.

## 2. Find your terminal program

To take this course you will need to use a **terminal program**, which presents the shell user interface and lets you log in to your Linux VM.

* Windows: Use the **Git Bash** program, which is installed with Git (above).
* Mac OS X: Use the **Terminal** program, located in your **Applications/Utilities** folder.
* Linux: Use any terminal program (e.g. **xterm** or **gnome-terminal**).

## 3. Install VirtualBox


VirtualBox is the software that actually runs the VM. [You can download it from virtualbox.org, here.](https://www.virtualbox.org/wiki/Downloads) Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it.

**Ubuntu 14.04 Note:** If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center, not the virtualbox.org web site. Due to a [reported bug](http://ubuntuforums.org/showthread.php?t=2227131), installing VirtualBox from the site may uninstall other software you need.

## 4. Install Vagrant

Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. [You can download it from vagrantup.com.](https://www.vagrantup.com/downloads) Install the version for your operating system.

**Windows Note:** The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

## 5. Download the VM configuration file

Make a new folder to keep your workspace for this course. You might call it **Shell**, but whatever name you pick is OK. Keep track of what folder you created it in (for instance, **Desktop**).

In the **Downloadables** section of this page, below, you'll find a link to the configuration file, called [Vagrantfile](https://www.udacity.com/api/nodes/4713348570/supplemental_media/vagrantfile/download). Download this file into the new folder you just created.

## 6. Run the virtual machine!

Open your terminal program. Type this shell command and press Enter:

**cd Desktop/Shell**

(If your new folder is called something other than "Shell", or is located somewhere other than "Desktop", change those.)

Then start the VM:

`vagrant up`


This will make your system download the Linux OS and start up the virtual machine. Unfortunately, this will take a long time on most network connections. Fortunately, you only have to do it once, and the same Linux OS image will work for later Udacity courses too.

Once it is done:

`vagrant ssh`

And you will be logged in to the virtual machine and ready to do the course exercises!

## In the VM or out of the VM?

We've set this course's exercises up to work in the virtual machine (VM) that you set up using the **vagrant** program. If you get logged out of the VM, you may end up typing shell commands in to your regular operating system instead of to the Linux system that we've set up for the course. Some commands won't work, and some files probably won't be where the course expects them to be.

## Getting logged out

If you type the command **exit** into the shell, or if you type **Control-D**, you will see a message like this:

```
logout  
Connection to 127.0.0.1 closed.
```

This just means that you got logged out. After logging out, you won't be in the VM any more.

To get back into the VM, use the command **vagrant ssh**.

**If `vagrant ssh` doesn't work**

If you get a message like this:

```
VM must be running to open SSH connection. Run `vagrant up`
to start the virtual machine.
```

This means that the VM program is not running, for instance because you rebooted your computer. This is just fine and it doesn't mean you've lost any work. Just run `vagrant up` to bring the VM back up, then `vagrant ssh` to log in.

This will not take as long as the first time you ran it, because it won't need to download the Linux OS.

**If `vagrant up` doesn't work**

If you get a message like this:

```
A Vagrant environment or target machine is required to run this
command. Run `vagrant init` to create a new Vagrant environment. Or,
get an ID of a target machine from `vagrant global-status` to run
this command on. A final option is to change to a directory with a
Vagrantfile and to try again.
```

That means that **vagrant** can't find the configuration file you downloaded. Go back to [the instructions](https://www.udacity.com/course/viewer#!/c-ud595/l-4597278561/m-4713348570), check to be sure that you did step 5, and then do step 6 again.

### Multiple terminals

If you open up more than one terminal window, only the one(s) that you ran `vagrant ssh` in will be connected to your Linux OS for this course. The others will be connected to your regular OS.

(It's actually really normal for Linux users to have to carefully keep track of which terminal windows are connected to which machines. Don't panic. Just look for whether "vagrant" appears on the command line.)

 
## Instructor Notes
 
The Udacity VM is the official shell for this class, but if your computer already has a Unix* shell you can use it if you prefer.

Caveat: Your computer's own shell may differ from the VM in unanticipated ways, and may not have all the programs installed which the VM provides. The recommended environment is the VM.

* if you're running Linux or Mac OS X for instance

**Commands that works.**

`curl` is the command use for download stuff from the we, if you know the URL
for example `curl + URL`.

### Different shells

Unix and Linux programmers over the years have written many different shell programs. You can read more about them on Wikipedia: the original [Bourne shell](https://en.wikipedia.org/wiki/Bourne_shell) or **sh**; the [C shell](https://en.wikipedia.org/wiki/C_shell) or **csh**; the [Korn shell](https://en.wikipedia.org/wiki/Korn_shell) or **ksh**; the [Z shell](https://en.wikipedia.org/wiki/Z_shell) or **zsh**; as well as the **bash** shell that this course uses.

Different systems may have different shells installed by default. Most Linux systems, and Mac OS X, default to **bash** for interactive shells. However, the most common default shell for scripting (shell programming) is classic **sh**. BSD Unix systems usually default to **sh** or **ksh**.

Almost everything in this course will work the same in any of these shell programs. The exception is one of the file matching (globbing) syntaxes at the end of Lesson 3.

### The Terminal vs The Shell

**Terminal**: is a program that draw text on the window, and allow you to type text on the keyboard, technically is called the Terminal Emulator. The terminal itselt doesn't what to do when you type command/inputs it needs another program to do that, and that is the Shell. When you type in the terminal send the commands/inputs to the Shell and the shell interpret and do the output.

**`date`** display the today's day.

**`expr`** make a calculation because the shell can be uses as a big calculator. For example **`expr 2 + 2`** is equal **4**.

**`echo`** is the command to print some thing to the screen for example **echo** + **an argument** like **`echo United States`** will print `United States` to the screen.

**`uname`** print the name of the operating system.

**`hostname`** print the username of the computer.

**`host udacity.com`** print the IP of udacity.com and some information of the website DNS.

**`bash --version or bash -V`** display the version of the program.

**`history`** display a history of previous commands.

***

**NOTE:** when you type a command in the shell, is similar when you call a function in a program or programming language.

**What is a Shell Command Anyway** is similar to a function call in a programming language like python, java, and C++. They also have a name and take arguments, but the technic of execution is different. The Shell command can be cosidered to run a separte program and start a new process on your computer, and a normal function in programming is uses to organize a program.

### Commands

**NOTE:** the `'`or some character does a special meaning to the terminal and some times will break like this `>` waiting for more input. To get out when the terminal come to this scenario, you fix it typing the same character that leaded to the stage like resumming `'`. if you want to do something like this `echo jose's house` you need an extract character to void the above problem. The correct way to do it is `echo jose\'s house`.
***
`uptime`:




# Lesson 2: Shell Commands

There are different kinds of shell commands that work with the terminal in different ways. This lesson also covers the use of the Linux manual (manpages) to expand your knowledge of shell commands.
***
### Filenames and Contents

**Note:** Read about `.sh` script file extancion and `.pem` for encript key and server file formats.

**`sudo apt-get install unzip`** command to install package in linux server. In order to unzip a zip folder.

**control + r** is reverse-i-search on the terminal which let you search your shell history.

`cat + fileNameOrFilesNames` display the content of the txt file on the terminal.

`wc + file_Name` is a command to anylize files. From left to right **12  393 2483 bivalves.txt** lines, words, bytes and fileName.

### Manual Pages

To get into the manual Pages you **man** + **command_Name**

*	**Name** Name all the commands.
*	**Synopsis** groud all the option that can be uses.
*	**Discription** Tell more about the command in general.

***

`rm` stand for remove and `r` for recursive `f` for force. So `rm -r` will remove all the file withoud asking the user before. `rm -rf`, but `rm -i` will ask the user before deleting every file on you repository. `rmdir` will dilete all empty folders.
***
### Line Based Programs
`bc` is  line based simple calculator.

`less` is line based objective program. You can type `D` and `space bar` to scroll down one page at the time. `U` is use to scroll up one page at the time, and the arrows works the same way as normal. You can type the line number to go to a particular page. You can also sear for a string or work with `/wordToSearchIt`

`>` to go to last line of the page/document and `<` to go to the first line.

### Editing Files in nano

Some editor for the terminal
*	vim
*	emacs
*	joe
*	nano



# Lesson 3: The Linux Filesystem

Working with files and directories is a big part of using the shell. In this lesson you'll learn basic commands for interacting with the filesystem.
***	