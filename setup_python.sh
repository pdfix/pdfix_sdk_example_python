#!/bin/bash

# set the current directory
pushd "$(dirname $0)"

# download and unpack the pdfix sdk build

SDK_VER=6.14.0
SDK_BUILD=864ec876

if [[ "$OSTYPE" == "linux-gnu" ]]; then
  SDK_ZIP="pdfix_sdk_"$SDK_VER"_"$SDK_BUILD"_linux.tar.gz"
  EXTRACT="tar -xzvf"
  BIN_DIR="linux"
  LIB_EXT="so"
elif [[ "$OSTYPE" == "darwin"* ]]; then
  SDK_ZIP="pdfix_sdk_"$SDK_VER"_"$SDK_BUILD"_macos.zip"
  EXTRACT=unzip
  BIN_DIR="darwin"
  LIB_EXT="dylib"
elif [[ "$OSTYPE" == "msys" ]]; then
  SDK_ZIP="pdfix_sdk_"$SDK_VER"_"$SDK_BUILD"_windows.zip"
  EXTRACT=unzip
  BIN_DIR="x64"
  LIB_EXT="dll"
else
  echo "error: unknown platform"
  exit 1
fi

SDK_URL="https://github.com/pdfix/pdfix_sdk_builds/releases/download/$SDK_VER/$SDK_ZIP"
echo $SDK_URL

rm -rf pdfix
mkdir -p pdfix                         && \
pushd pdfix                            && \
curl -L -sS $SDK_URL > $SDK_ZIP        && \
$EXTRACT $SDK_ZIP                      && \
rm $SDK_ZIP                            && \
popd

# copy python sources and binaries
cp pdfix/include/python/* src/
cp pdfix/bin/$BIN_DIR/*.$LIB_EXT src/

popd
