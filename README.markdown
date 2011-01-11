# My dotfiles

Let's ride:

    git clone git://github.com/mrts/dotfiles.git
    cd dotfiles
    sudo cp pyerrfilter.py gvimrc.local vimrc.local  /etc/vim/
    sudo cp bash.bashrc.local /etc/
    sudo -c "echo '. /etc/bash.bashrc.local' >> /etc/bash.bashrc"
