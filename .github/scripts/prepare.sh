echo "Publishing ${PROJECT_NAME} to ${PACKAGE_REPO_NAME}"
echo " Publishing version: ${VERSION}"
echo " Publish tag is ${PUBLISH_TAG}"

# prepare publish
if [ "${DRY_RUN}" == "1" ]; then
  echo "(dry run)"
else
  python3 -m pip install --upgrade build && python3 -m build
fi
