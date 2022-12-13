{
  inputs = {
    my-flake.url = "github:Jaculabilis/my-flake";
    nixpkgs.url = "github:NixOS/nixpkgs?ref=refs/tags/22.11";
  };

  outputs = { self, my-flake, nixpkgs }:
  let
    systems = [ "aarch64-linux" "x86_64-linux" ];
    each = system:
    let
      pkgs = nixpkgs.legacyPackages.${system};
    in
    {
      packages.${system}.default = (import nixpkgs {
        inherit system;
        overlays = [ self.overlays.default ];
      }).friendly-hex;

      apps.${system}.default = {
        type = "app";
        program = "${self.packages.${system}.default}/bin/friendly-hex";
      };

      devShells.${system}.default = pkgs.mkShell {
        buildInputs = [ (pkgs.python3.withPackages (py: [ py.poetry ])) ];
        shellHook = ''
          PS1="(nix develop) $PS1"
        '';
      };
    };
  in (my-flake.outputs-for each systems) //
  {
    overlays.default = final: prev: {
      friendly-hex = (final.poetry2nix.mkPoetryApplication {
        projectDir = builtins.path { path = ./.; };
      });
    };
  };
}
