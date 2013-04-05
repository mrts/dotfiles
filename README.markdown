# My dotfiles

Let's ride:

    git clone git://github.com/mrts/dotfiles.git
    cd dotfiles
    sudo cp pyerrfilter.py gvimrc.local vimrc.local  /etc/vim/
    sudo cp bash.bashrc.local /etc/
    sudo sh -c "echo '. /etc/bash.bashrc.local' >> /etc/bash.bashrc"

# Black text on white background in a TTY

    setterm -foreground black -background white -store

# In Windows

1. Copy `gvimrc.local` and `vimrc.local` to `\Program Files (x86)\Vim\vim73`.

1. Open `\Program Files (x86)\Vim\_vimrc` and add the following lines
   (`autoread` is required for Visual Studio integration):

        source $VIMRUNTIME/vimrc.local
        source $VIMRUNTIME/gvimrc.local
        
        set directory=.,$TEMP
        set encoding=utf-8
        set autoread
        
        " set nocompatible
        " source $VIMRUNTIME/vimrc_example.vim
        " source $VIMRUNTIME/mswin.vim
        " behave mswin

1. Configure Visual Studio according to the instructions in
   [Vim wiki](http://vim.wikia.com/wiki/Integrate_gvim_with_Visual_Studio).

1. Optionally configure *Git Bash* with `bash.bashrc.local` as described above.
