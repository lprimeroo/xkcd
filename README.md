# xkcd

This tiny python script automatically sets the latest xkcd comic as your wallpaper,
provided you set the script as a cron job. [Not maintained anymore]

## Requirements

### Linux

Make sure you install [PyGObject](https://wiki.gnome.org/Projects/PyGObject):

Fedora (YUM)
```
yum install pygobject3
```

Fedora (DNF)
```
dnf install pygobject3
```

Debian & Ubuntu
```
apt-get install python-gi
```

## Installation

Clone and cd into the repository and run `python setup.py install`

## Running

To update your wallpaper run `xkcd-wallpaper` and it should be updated.

Now for it to automatically change your wallpaper, set it as a cron job. Setting up a cron job is easy,
you can read about it [here](http://benr75.com/pages/using_crontab_mac_os_x_unix_linux).

## Screenshots

Will probably look something like this,

![](http://i66.tinypic.com/35a3tbs.jpg)
