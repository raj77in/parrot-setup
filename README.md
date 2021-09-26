# Parrot setup and scripts

My parrot setup based on my kali setup

Also has some interesting files :)

To checkout
```
git clone --recurse-submodules https://github.com/raj77in/parrot-setup

## Few things you will need to install

**Currently I was not able to install multilib so we cannot compile 32 bit binaries**

```
sudo dpkg --print-architecture
sudo dpkg --add-architecture i386
sudo dpkg --print-foreign-architectures
sudo apt-get update
#apt remove gcc gcc-10  gcc-10-cross-base gcc-10-i686-linux-gnu
sudo apt-get install build-essential libc6-dev-i386

sudo apt install tmux obs-studio glances htop open-vm-tools open-vm-tools-desktop
sudo vmware-user-suid-wrapper
```

**Ideally this should work but it does not currently on Parrot 4.11**

```
32 bit compilation

For C language:
sudo apt-get install gcc-multilib
For C++ language:
sudo apt-get install g++-multilib
```

## Setup to compile 32 bit binary

```
apt install docker.io
docker pull i386/ubuntu
docker run -it --rm -v $PWD:/mnt bash
  apt update
  apt install build-essential gcc-multilib
  ## you can now compile your 32 bit binary in docker.
```

## Fonts installation

```
sudo apt install ttf-unifont ttfautohint ttf-xfree86-nonfree-syriac/rolling ttf-xfree86-nonfree ttf-ubuntu-font-family/rolling fonts-ubuntu-title/rolling fonts-noto fonts-hack\*
```

## VIM setup

```
sudo apt install vim-youcompleteme vim-python-jedi m-gui-common vim-gtk3 vim-autopep8 vim-athena python3-venv
ln -s parrot-setup/kali-setup/dotfiles/vim .vim
ln -s .vim/vimrc.d/vimrc .vimrc
```

