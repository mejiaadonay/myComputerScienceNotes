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

In the **Downloadables** section of this page, below, you'll find a link to the configuration file, called `Vagrantfile`. Download this file into the new folder you just created.

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

 Previous
 
## Instructor Notes
 
The Udacity VM is the official shell for this class, but if your computer already has a Unix* shell you can use it if you prefer.

Caveat: Your computer's own shell may differ from the VM in unanticipated ways, and may not have all the programs installed which the VM provides. The recommended environment is the VM.

* if you're running Linux or Mac OS X for instance

# Lesson 2: Shell Commands

There are different kinds of shell commands that work with the terminal in different ways. This lesson also covers the use of the Linux manual (manpages) to expand your knowledge of shell commands.

# Lesson 3: The Linux Filesystem

Working with files and directories is a big part of using the shell. In this lesson you'll learn basic commands for interacting with the filesystem.
***	