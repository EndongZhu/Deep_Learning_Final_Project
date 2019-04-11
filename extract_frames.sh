# Bash script for extracting frames in videos
# Set environment variables before running script
#   - srcDir: path of video directories
#   - dstDir: path of output frames directories
#   - srcExt: extension type of videos, e.g. mp4, avi, etc.


mkdir -p ${dstDir}
for filename in "${srcDir}"/*.$srcExt; do
    fbname=$(basename "$filename" | cut -d. -f1)
    mkdir -p ${dstDir}/${fbname}
    ffmpeg -i ${filename} -vf fps=10 ${dstDir}/${fbname}/${fbname}_%04d.jpg -hide_banner
done
