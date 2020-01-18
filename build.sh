DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

pushd . &>/dev/null

#
# Hashcat
#

cd $DIR
HASHCAT_DIR="$DIR/hashcat/hashcat"
HASHCAT_VER=`wget -O- -q https://hashcat.net/beta/ | grep hashcat | cut -f 2 -d '"'`
HASHCAT_URL="https://hashcat.net/beta/${HASHCAT_VER}"

rm -rf $HASHCAT_DIR
DOWNDIR=`mktemp -d`
cd $DOWNDIR
echo -n "Downloading $HASHCAT_URL ... "
wget -q -O hashcat.7z $HASHCAT_URL
7z x hashcat.7z &>/dev/null
rm hashcat.7z
mv * $HASHCAT_DIR

rm -rf $DOWNDIR
echo '[ OK ]'

#
# Prince
#

PRINCE_URL=`wget -O- -q https://github.com/hashcat/princeprocessor/releases/latest | grep -i \.7z | grep href | cut -f 2 -d '"'`
PRINCE_URL="https://github.com/${PRINCE_URL}"
PRINCE_DIR="$DIR/hashcat/pp"

rm -rf $PRINCE_DIR

DOWNDIR=`mktemp -d`
cd $DOWNDIR

echo -n "Downloading $PRINCE_URL ... "
wget -O prince.7z -q $PRINCE_URL
7z x prince.7z &>/dev/null
rm prince.7z
mv * $PRINCE_DIR
rm -rf $DOWNDIR
echo '[ OK ]'

#
# Hashcat utils
#

UTILS_URL=`wget -O- -q https://github.com/hashcat/hashcat-utils/releases/latest | grep -i \.7z | grep href | cut -f 2 -d '"'`
UTILS_URL="https://github.com/${UTILS_URL}"
UTILS_DIR="$DIR/hashcat/utils"

rm -rf $UTILS_DIR

DOWNDIR=`mktemp -d`
cd $DOWNDIR

echo -n "Downloading $UTILS_URL ... "
wget -O utils.7z -q $UTILS_URL
7z x utils.7z &>/dev/null
rm utils.7z
mv * $UTILS_DIR
rm -rf $DOWNDIR
echo '[ OK ]'

#
# Sdist
#

echo -n "Creating sdist ... "
cd $DIR
python ./setup.py sdist >/dev/null

echo '[ OK ]'

popd &>/dev/null

