const alph = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

const s1r0 = (input, key, arr = [...input]) => arr
    .map((e, i) =>
        alph.includes(e) ?
        alph[(alph.indexOf(e) + alph.indexOf(key[i % key.length])) % 26] :
        e)
    .map((e, i) => /[A-Z]/.test(arr[i]) ? e.toUpperCase() : e)
    .join('')