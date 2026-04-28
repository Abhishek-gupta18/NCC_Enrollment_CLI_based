{ pkgs }: {
  deps = [
    pkgs.imagemagick6_light
    pkgs.replitPackages.prybar-python310
    pkgs.replitPackages.stderred
  ];
}