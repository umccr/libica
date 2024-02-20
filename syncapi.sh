#!/usr/bin/env bash

BASE_URL=https://aps2.platform.illumina.com
SWAGGER_JSON=swagger/v1/swagger.json
PYTHON_GEN_PROP=generateSourceCodeOnly=true,hideGenerationTimestamp=false

declare -a services=(wes gds tes ens console)
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
  for i in "${services[@]}"; do
    ep=$BASE_URL/$i/$SWAGGER_JSON
    wget -q --show-progress --wait=15 --limit-rate=50K -O swagger/"$i".json "$ep"
  done

  # get ga4gh api FIXME seem still unstable spec
  #ga4gh_ep=https://use1.platform.illumina.com/ga4gh-api/v2/api-docs
  #wget -q --show-progress --wait=15 --limit-rate=50K -O swagger/ga4gh.json "$ga4gh_ep"
}

genapi() {
  for i in "${services[@]}"; do
    npx openapi-generator-cli generate -i swagger/"$i".json -g python -o . \
      --global-property=apiDocs=true,modelDocs=true,apiTests=true,modelTests=true \
      --additional-properties="$PYTHON_GEN_PROP",packageName=libica.openapi.lib"$i"
  done

  # gen ga4gh sdk
  #npx openapi-generator-cli generate -i swagger/ga4gh.json -g python -o . \
  #  --additional-properties="$PYTHON_GEN_PROP",packageName=libica.openapi.libga4gh
}

mvapidoc() {
  for i in "${services[@]}"; do
    _mvdoc "$i"
  done

  #_mvdoc ga4gh
}

_mvdoc() {
  libname="lib$1"

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
  sed -i "" -e "s/libica\/openapi\/$libname\///g" "$readme"
  echo
}

chkepver() {
  # check endpoint version
  curl -s -X GET $BASE_URL/v1/health | jq
}

validateapi() {
  # validate swagger openapi definitions
  for i in "${services[@]}"; do
    REDOCLY_TELEMETRY=off npx @redocly/cli lint swagger/"$i".json
  done
}
