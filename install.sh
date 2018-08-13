#
# install python
#
echo \>\>\> installing python3 module
pip3 install -e src

#
# install bash command
#
echo \>\>\> install bash commands
cp ~/git/HyperMD/hypermd.sh /usr/local/bin/hypermd
chmod +x /usr/local/bin/hypermd
chmod +x ~/git/HyperMD/install.sh