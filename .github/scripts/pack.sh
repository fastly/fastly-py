# install deps
pip install --upgrade build

# mark version
sed -i "s/^VERSION = .*$/VERSION = \"${VERSION}\"/" setup.py
sed -i "s/^version = .*$/version = \"${VERSION}\"/" pyproject.toml

# make a package
mkdir -p "${GITHUB_WORKSPACE}/temp"
python -m build --outdir "${GITHUB_WORKSPACE}/temp"

# save the output filename to env
PACKAGE_FILENAME=$(cd "${GITHUB_WORKSPACE}/temp" && ls -1 -- *.tar.gz)
echo "PACKAGE_FILENAME=${PACKAGE_FILENAME}" >> "${GITHUB_ENV}"

# move package to dist
mkdir -p "${GITHUB_WORKSPACE}/dist"
mv "${GITHUB_WORKSPACE}/temp/${PACKAGE_FILENAME}" "${GITHUB_WORKSPACE}/dist/${PACKAGE_FILENAME}"
