#python compile_xfce.py ; for i in ti*.png; do convert $i ../../Meta/xfwm4/$(basename ${i%.*}.xpm) ;done ; rm tit*.png ; cp *.png ../../Meta/xfwm4
rm *.png

python compile_xfce.py

for i in top menu left title bottom right
do
    rm $i*toggle*.png
done
#for i in *.png
#do
#    convert $i -trim +repage $i
#done

function cnv {

    for i in *.png
    do
        convert $i ../../Meta${1}/xfwm4/$(basename ${i%.*}.xpm)
    done
}


cnv $1
