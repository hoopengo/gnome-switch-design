filepath="/tmp/Mkos-Big-Sur.tar.xz"
dirname="Mkos-Big-Sur"

if [ -f "$filepath" ]
then
rm $filepath
fi

wget -O $filepath https://github.com/zayronxio/Mkos-Big-Sur/releases/download/0.3/Mkos-Big-Sur.tar.xz \
&& \
tar -xvf $filepath -C `realpath ~`/.icons/ \
&& \
gsettings set org.gnome.desktop.interface icon-theme $dirname