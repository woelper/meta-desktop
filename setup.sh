USER=$(whoami)

OS=redhat

case "$OS" in
    ubuntu)
        sudo cp $(pwd)/meta-desktop.desktop /usr/share/xsessions/
        sudo ln -s $(pwd)/metade-session /usr/local/bin/
        ;;

    redhat)
        su -c "cp $(pwd)/meta-desktop.desktop /usr/share/xsessions/"
        su -c "ln -s $(pwd)/metade-session /usr/local/bin/"
        ;;
esac

python config.py

