XAUTH=/tmp/.docker.xauth

echo "Preparing Xauthority data..."
xauth_list=$(xauth nlist :0 | tail -n 1 | sed -e 's/^..../ffff/')
if [ ! -f $XAUTH ]; then
    if [ ! -z "$xauth_list" ]; then
        echo $xauth_list | xauth -f $XAUTH nmerge -
    else
        touch $XAUTH
    fi
    chmod a+r $XAUTH
fi


echo "Done."
echo ""
echo "Verifying file contents:"
file $XAUTH
echo "--> It should say \"X11 Xauthority data\"."
echo ""
echo "Permissions:"
ls -FAlh $XAUTH
echo ""

# echo "Enter your university/institute acronym: "
# read school
# echo "Enter Your (First) Name: "
# read name
echo "Enter container's purpose:  "
read purpose_container

# echo "Welcome ${name} from ${school^^}"
echo "Which version would you like to use?"
read version
echo "Creating new docker container..."

docker run -it \
    --env="DISPLAY=$DISPLAY" \
    --env="QT_X11_NO_MITSHM=1" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    --env="XAUTHORITY=$XAUTH" \
    --volume="$XAUTH:$XAUTH" \
    --volume="/dev/bus/usb:/dev/bus/usb" \
    --volume="/home/$USER:/home/$USER/" \
    --volume="/media/:/media:rw" \
    --net=host \
    --privileged \
    --runtime=nvidia \
    --name ${purpose_container} \
    ${version} \
    bash

echo "Done."
