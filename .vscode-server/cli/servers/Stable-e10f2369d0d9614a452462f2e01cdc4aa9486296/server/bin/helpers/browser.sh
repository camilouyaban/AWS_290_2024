#!/usr/bin/env sh
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
ROOT="$(dirname "$(dirname "$(dirname "$(readlink -f "$0")")")")"

APP_NAME="code"
VERSION="1.94.1"
COMMIT="e10f2369d0d9614a452462f2e01cdc4aa9486296"
EXEC_NAME="code"
CLI_SCRIPT="$ROOT/out/server-cli.js"
"$ROOT/node" "$CLI_SCRIPT" "$APP_NAME" "$VERSION" "$COMMIT" "$EXEC_NAME" "--openExternal" "$@"
