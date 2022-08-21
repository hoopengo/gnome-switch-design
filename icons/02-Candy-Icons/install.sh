filepath="/tmp/candy-icons.zip"
dirname="candy-icons-master"

if [ -f "$filepath" ]
then
rm $filepath
fi

wget -O $filepath https://github.com/EliverLara/candy-icons/archive/refs/heads/master.zip \
&& \
unzip -a -o $filepath -d `realpath ~`/.icons/ \
&& \
gsettings set org.gnome.desktop.interface icon-theme $dirname