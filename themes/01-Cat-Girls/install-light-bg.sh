set_wallpaper() {
    test mkdir `realpath ~`/.local/share/backgrounds/01-Cat-Girls/
    cp ./wallpapers/light.jpg `realpath ~`/.local/share/backgrounds/01-Cat-Girls/light.jpg
    gsettings set org.gnome.desktop.background picture-uri file://`realpath ~`/.local/share/backgrounds/01-Cat-Girls/light.jpg
}

read -p "Do you wish to change avatar and wallpaper? (y/n): " yn
case $yn in
    [Yy]* ) set_wallpaper; break;;
    [Nn]* ) exit;;
    * ) echo "Please answer [y] or [n]";
esac
