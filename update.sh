#
# update git
#
echo \>\>\> updating git...
git fetch ~/git/HyperMD
git pull ~/git/HyperMD

#
# update python
#
echo \>\>\> updating python3...
pip3 install -e src

#
# update bash command
#
echo \>\>\> updating bash...
cp ~/git/HyperMD/hypermd.sh /usr/local/bin/hypermd
chmod +x /usr/local/bin/hypermd
chmod +x ~/git/HyperMD/install.sh