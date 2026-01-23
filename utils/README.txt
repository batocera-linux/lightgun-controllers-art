# use this program to test your png.info files for guns
genGunImages.py ./Sinden.png ./gun_help.png /usr/share/fonts/truetype/dejavu/DejaVuSans.ttf

# regenerate automatically the image when you save the .infos
eog gun_help.png &
while inotifywait -e modify "../infos/Sinden lightgun.infos"; do ./genGunImages.py "../png/Sinden lightgun.png" gun_help.png /usr/share/fonts/truetype/dejavu/DejaVuSans.ttf ; done
