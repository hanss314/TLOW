let actions = [n => { for (var i = n - 1; i > 1; i--) { if (n % i == 0) return i } return -1}, a => a * a, (a, s) => a - s, (a, s) => a + s ];
function state_value(avos, depth, player, act, best = -player, worst = -1) { if (depth == 0) return 0
    if (avos[avos.length - 1] < 0 || (new Set(avos)).size != avos.length) return player;
    for (let i = 0; i < 4; i++) { let v = state_value([...avos, actions[i](avos[avos.length - 1], spoon) % 256], depth - 1, -player)
        if (player * v > player * best) best = v; if (act && v > worst) action = i, worst = v }
    return best }
function r5(previous_avocados, spoon_size, difficulty = 10) { spoon = spoon_size;
    if (previous_avocados.length == 0 || spoon_size < 0) Math.floor(1 + Math.random() * 254)
    state_value(previous_avocados, difficulty, 1, true)
    return action }
