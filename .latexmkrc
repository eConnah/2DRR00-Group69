# Put all temporary files in ./build
$aux_dir = "build";
$bib_dir = "build";
$out_dir = "build";
$log_file = "build";

# PDF stays in the main folder (change if you want)
$pdflatex = 'pdflatex -interaction=nonstopmode -synctex=1 -output-directory=build %O %S';
