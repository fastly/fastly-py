echo "Publishing ${PROJECT_NAME} to NPM"
echo " Publishing version: ${VERSION}"
echo " Publish tag is ${PUBLISH_TAG}"

# perform publish
if [ "${DRY_RUN}" == "1" ]; then
  echo "(dry run)"
else
  python3 -m pip install --upgrade build && python3 -m build
fi
