py="--0; tlow9 = lambda s: s if s else f'py={py!r}\\nhs={hs!r}\\n{py}{hs}'\n"
hs="0#_=0; tlow9 s = if null s then ['p','y','='] ++ show py ++ ['\\n','h','s'] ++ show hs ++ ['\\n'] ++ py ++ hs else s"
--0; tlow9 = lambda s: s if s else f'py={py!r}\nhs={hs!r}\n{py}{hs}'
0#_=0; tlow9 s = if null s then ['p','y','='] ++ show py ++ ['\n','h','s'] ++ show hs ++ ['\n'] ++ py ++ hs else s

