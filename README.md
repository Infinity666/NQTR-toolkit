# Navigation Quest Time Routine System for Ren'py

![Last commit](https://img.shields.io/github/last-commit/DonRP/NQTR-toolkit)
![License](https://img.shields.io/github/license/DonRP/NQTR-toolkit)
<span class="discord">
<a href="https://discord.gg/5UFPjP9" title="Discord"><img src="https://img.shields.io/discord/688162156151439536" alt="Discord" /></a>
</span>

This repo is a complete set of tools to create a game where you can explore and relate to characters.

In order to simplify the update work and avoid errors in saving I created functions that check the correct state of variables by inserting them in [after_load](game/tool/core.rpy#L1) (e.g. after a change to a quest that causes a stage to be blocked, the quest should restart) and an abundant use of define.

Feel free to contribute, fork this and send a pull request. 😄


## Code snippets ([VSCode](https://code.visualstudio.com/))
(all begin with `DR_`)

![ezgif com-gif-maker (1)](https://user-images.githubusercontent.com/67595890/179365279-0d0b6d45-0048-4a0d-8c6d-9571b9c328f4.gif)


## Insert Toolkit in your project

I recommend the following ways to include it in your project:

- [**Pull branch**](#pull-branch) (to **insert** it into your game and **update** it easily)
- [**Fork**](https://docs.github.com/en/get-started/quickstart/fork-a-repo) (to improve the repo or create a Toolkit based on mine)
- [Manually](https://github.com/DRincs-Productions/NQTR-toolkit/releases) (not recommended)


### Pull branch

To **insert** or **update** the Toolkit in your repo with Pull branch I recommend the following procedure:

(only if you want to insert the repo) Create a new empty branch, in the example I'll use **NQTR-toolkit**

```shell
git checkout -b NQTR-toolkit
git checkout NQTR-toolkit
git config pull.rebase false
git pull https://github.com/DRincs-Productions/NQTR-toolkit.git tool-only --allow-unrelated-histories

```

At the end make a merge inside the arm of the project.

## Documentation

[Wiki](https://github.com/DRincs-Productions/NQTR-toolkit/wiki)

## Preview

![Navigation](https://user-images.githubusercontent.com/67595890/178109985-6244ffe0-a7d6-426e-a26b-ac93ad8a300a.jpg)

![Map](https://user-images.githubusercontent.com/67595890/178110045-34cd7b96-5010-48bb-89a0-5598d5848fb0.jpg)

![Routine](https://user-images.githubusercontent.com/67595890/178110207-3b0d2932-dd08-4937-8897-47b65c70b33d.jpg)
