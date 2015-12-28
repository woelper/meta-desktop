python compile_xfce.py ; for i in ti*.png; do convert $i ../../Meta/xfwm4/$(basename ${i%.*}.xpm) ;done ; rm tit*.png ; cp *.png ../../Meta/xfwm4
