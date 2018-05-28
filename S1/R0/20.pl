constant \ALPHA = 'a'..'z';
sub vignere(Str $plain, Str $key) {
    $plain.comb.pairs.map(sub ($p) {
        my $l = $p.value;
        return $l if $l !~~ /<alpha>/;
        my $pval = $l.lc.ord - 'a'.ord;
        my $kval = $key.comb[$p.key % $key.chars].lc.ord - 'a'.ord;
        chr((($pval + $kval) % 26) + ($l ~~ /<upper>/ ?? 65 !! 97));
    }).join;
}
