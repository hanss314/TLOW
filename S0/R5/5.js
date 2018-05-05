let actions = [n => { for (var i = n - 1; i > 1; i--) { if (n % i == 0) return i } return -1}, a => a * a, (a, s) => a - s, (a, s) => a + s ];
function r5(avos, spoon, depth = 10, player = 1, act = true, best = -player, worst = -1) { 
    if (avos.length == 0 || spoon < 0) return Math.floor(1 + Math.random() * 254); if (depth == 0) return 0
    if (avos[avos.length - 1] < 0 || (new Set(avos)).size != avos.length) return player
    for (let i = 0; i < 4; i++) {
        let v = r5([...avos, actions[i](avos[avos.length - 1], spoon) % 256], spoon, depth - 1, -player, false)
        if (player * v > player * best) best = v; 
        if (act && v > worst) action = i, worst = v }
    return act ? action : best
}
