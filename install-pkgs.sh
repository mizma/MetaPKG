#!/usr/bin/env bash
pkgs=()
install-local-pkgbuild() {
  local location=$1
  local flags=$2
  pushd $location
  source ./PKGBUILD
  yay -S --sudoloop $flags --asdeps "${depends[@]}" || return 1
  makepkg -Afsi --noconfirm
  popd
}
print_usage() {
  echo "Usage: install-pkgs.sh TARGET [TARGETs...]"
}
if [[ $# -eq 0 ]]; then
  print_usage
  exit 1
fi
while [[ $# -gt 0 ]]; do
  case $1 in
    -*|--*)
      echo "Unknown option $1"
      print_usage
      exit 1
      ;;
    *)
      pkgs+=($1)
      shift
      ;;
  esac
done

for i in "${pkgs[@]}"; do
  installflags="--needed"
  install-local-pkgbuild "$i" "$installflags"
done
