from pick import pick
import os
import shutil
import atexit

art = r""" _____               _   _____ _
|   __|_ _ _ ___ ___| |_|     | |_ ___ ___ ___ 
|__   | | | | -_| -_|  _|   --|   | -_| -_|  _|
|_____|_____|___|___|_| |_____|_|_|___|___|_|
"""

print(art)

indicator = "[›]"


@atexit.register
def agretation():
    print("\nThanks for using SweetCheer!\n")


def install_icons(icons_dirname: str) -> bool:
    try:
        os.system(f"sh ./icons/{icons_dirname}/install.sh")
    except Exception:
        return False
    else:
        return True
    finally:
        print("Installing icons theme done.")


def set_avatar(theme_dirname: str):
    choose, _ = pick(
        title="Choose night/light",
        options=["night", "light"],
        indicator=indicator,
    )

    filename = choose + ".png"

    try:
        shutil.copyfile(
            f"./themes/{theme_dirname}/avatar/{filename}",
            f"/var/lib/AccountsService/icons/{os.getlogin()}",  # os.environ.get('USER') - can return root
        )
    except PermissionError:
        print(
            """Cannot set avatar. Permissions Denied. (https://github.com/hoopengo/sweetcheer/issues/1)"""
        )
    else:
        print(f"Successfully set {choose} avatar.")


def set_wallpapers(theme_dirname: str):
    wallpaper_path = f"{os.path.expanduser('~')}/.local/share/backgrounds/"

    if not os.path.isdir(wallpaper_path):
        os.mkdir(wallpaper_path)

    for name, theme_color in zip(
        ("light.png", "night.png"),
        ("picture-uri", "picture-uri-dark"),
    ):
        shutil.copy(
            f"./themes/{theme_dirname}/wallpaper/{name}",
            f"{wallpaper_path}/{theme_dirname}=={name}",
        )
        os.system(
            f"gsettings set org.gnome.desktop.background {theme_color} file://{wallpaper_path}/{theme_dirname}=={name}"
        )


def install_theme(theme_dirname: str) -> bool:
    try:
        if input("Set avatar? [Y/n]: ").strip().lower() in ["", "y"]:
            set_avatar(theme_dirname)

        if input("Set wallpapers? [Y/n]: ").strip().lower() in ["", "y"]:
            set_wallpapers(theme_dirname)
    except Exception as err:
        print(err)
        return False
    else:
        return True
    finally:
        print("Installing theme done.")


def generate_options_by_folder(dirname: str):
    return [
        file_or_dir
        for file_or_dir in os.listdir(dirname)
        if os.path.isdir(dirname + "/" + file_or_dir)
    ]


def ask(title: str, dirname: str):
    select = generate_options_by_folder(dirname)
    select.append("Skip")

    cursor_pick, index = pick(
        title=title,
        options=select,
        indicator=indicator,
        default_index=len(select) - 1,
    )

    if index == len(select) - 1:
        return None

    return cursor_pick


# Icons picker.
icons_dirname = ask(title="Please pick a icons:", dirname="./icons")

if icons_dirname is not None:
    if install_icons(icons_dirname):
        print(f"\nSuccessfully installed - {icons_dirname}\n")


# Theme picker.
theme_dirname = ask(title="Please pick a theme:", dirname="./themes")

if theme_dirname is not None:
    if install_theme(theme_dirname):
        print(f"\nSuccessfully installed - {theme_dirname}\n")
    else:
        print(f"Don't installed - {theme_dirname}\n")
