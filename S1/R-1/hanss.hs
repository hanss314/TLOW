f=0:1:zipWith(+)f(tail f)
main=mapM_ print f
