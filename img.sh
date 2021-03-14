#!/bin/zsh

echo "{% gp - %}"

n=01
for i in img/*.jpeg
do
  # convert -resize x1080 $i $1-a.jpg
  # convert -resize x1080 -quality 80 -strip $i img/$1-$n.jpg &
  magick $i -resize x1080 -quality 50 -strip img/$1-$n.webp &

  echo "![](https://raw.githubusercontent.com/LeiHao0/BlogAssets/assets/$1-$n.jpg)"
  n=$(printf "%02d" $((n + 1)))
done

echo "{% endgp %}"