{
  description = "Nix Develop Flake";

  inputs = {
    flake-parts.url = "github:hercules-ci/flake-parts";
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs =
    { flake-parts, ... }@inputs:
    flake-parts.lib.mkFlake { inherit inputs; } {
      perSystem =
        {
          config,
          self',
          inputs',
          pkgs,
          system,
          ...
        }:
        {
          devShells.default = pkgs.mkShell {
            buildInputs = [
              (pkgs.python3.withPackages (
                pythonPkgs: with pythonPkgs; [
                  pandas
                  requests
                  numpy
                  matplotlib
                  scikit-learn
                  ipykernel
                  pip
                  seaborn
                  statsmodels
                ]
              ))

              pkgs.texliveMedium
            ];
            shellHook = ''
              echo "Welcome to the Python devShell on ${system}!"
            '';
          };
        };

      # All supported systems
      systems = [
        "x86_64-linux"
        "aarch64-linux"
        "x86_64-darwin"
        "aarch64-darwin"
      ];
    };
}
