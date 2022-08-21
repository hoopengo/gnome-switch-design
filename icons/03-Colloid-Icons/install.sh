filepath="/tmp/Colloid-Icons.zip"
dirname="/tmp/Colloid-icon-theme-2022-04-22"

if [ -f "$filepath" ]
then
rm $filepath
fi

wget -O $filepath https://github.com/vinceliuice/Colloid-icon-theme/archive/refs/tags/2022-04-22.zip \
&& \
unzip -a -o $filepath -d /tmp/ \
&& \
sh $dirname/install.sh -d ~/.icons -t purple \
&& \
gsettings set org.gnome.desktop.interface icon-theme "Colloid-purple-light" \
&& \
gsettings set org.gnome.desktop.background primary-color '#EE82EE'