#!/usr/bin/env bash

# ICA v2

BASE_URL=https://ica.illumina.com
MID_PATH=/ica/api/swagger
OPENAPI_YAML=openapi_public.yaml
PYTHON_GEN_PROP=generateSourceCodeOnly=true,hideGenerationTimestamp=false

declare docsrc="openapi/docs"

_deps() {
  cmds="wget rsync sed curl npx"
  for i in $cmds; do
    if command -v "$i" >/dev/null; then
      continue
    else
      echo "Command '$i' is required to run syncapi.sh"
      exit 1
    fi
  done
}
_deps

getapi() {
  ep=$BASE_URL/$MID_PATH/$OPENAPI_YAML
  wget -q --show-progress --wait=15 --limit-rate=50K -O swagger/$OPENAPI_YAML "$ep"
}

genapi() {
  npx openapi-generator-cli generate -i swagger/$OPENAPI_YAML -g python -o . \
    --global-property=apiDocs=true,apiTests=true,modelDocs=true,modelTests=true \
    --additional-properties="$PYTHON_GEN_PROP",packageName=libica.openapi.v2
}

mvapidoc() {
  _mvdoc "v2"
}

_mvdoc() {
  libname="$1"

  mkdir -p "$docsrc/$libname/docs"
  gendoc="libica/openapi/$libname/docs"
  if [ -d "$gendoc" ]; then
    rsync -av --remove-source-files "$gendoc" "$docsrc/$libname"
    rmdir "$gendoc"
  fi

  readme="$docsrc/$libname/README.md"
  genreadme=libica/openapi/"$libname"_README.md
  if [ -f "$genreadme" ]; then
    mv -v "$genreadme" "$readme"
  fi
  sed -i -e "s/libica\/openapi\/$libname\///g" "$readme"
  echo
}

chkepver() {
  # check endpoint version
  # Do we have v1 health endpoint equivalent?
  # curl -s "https://aps2.platform.illumina.com/v1/health" | jq
  #curl -s -X GET $BASE_URL/v1/health | jq
  echo "TODO"
}

validateapi() {
  # validate openapi definitions
  npx openapi-generator-cli validate -i swagger/$OPENAPI_YAML
  openapi-spec-validator swagger/$OPENAPI_YAML
}
