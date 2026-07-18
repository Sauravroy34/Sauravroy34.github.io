#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
publish_dir="$repo_root/docs"
build_root="$(mktemp -d)"

cleanup() {
	rm -rf -- "$build_root"
}
trap cleanup EXIT

command -v hugo >/dev/null 2>&1 || {
	echo "hugo is required to build the site" >&2
	exit 1
}

HUGO_ENV=production hugo \
	--source "$repo_root" \
	--destination "$build_root/docs" \
	--gc \
	--minify

case "$publish_dir" in
	"$repo_root/docs") ;;
	*)
		echo "refusing to clean unexpected publish directory: $publish_dir" >&2
		exit 1
		;;
esac

mkdir -p "$publish_dir"
find "$publish_dir" -mindepth 1 -maxdepth 1 -exec rm -rf -- {} +
cp -a "$build_root/docs/." "$publish_dir/"
