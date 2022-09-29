# Distro Guide

## Debian & Ubuntu

If you run Debian or some derivative of it (e.g. Ubuntu), use this:

```bash
cd ~ && sudo wget https://raw.githubusercontent.com/amfoss/attendance-tracker/master/dependencies/debian.sh -O debian.sh && sudo bash -e debian.sh
```

## Fedora

For fedora users:

```bash
cd ~ && sudo wget https://raw.githubusercontent.com/amfoss/attendance-tracker/master/dependencies/fedora.sh -O fedora.sh && sudo bash -e fedora.sh
```

## Arch Linux

For arch-based distros:

```bash
cd ~ && sudo wget https://raw.githubusercontent.com/amfoss/attendance-tracker/master/dependencies/arch.sh -O arch.sh && sudo bash -e arch.sh
```

## MacOS

For Mac users:

```bash
cd ~ && sudo wget https://raw.githubusercontent.com/amfoss/attendance-tracker/master/dependencies/mac.sh -O mac.sh && sudo bash -e mac.sh
```

## Dependencies List

Below is the list of packages & modules required by the script (useful if installing manually):

```
git
python3
python3-pip
(pip) requests
```