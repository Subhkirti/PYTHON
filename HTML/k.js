var i = 5;
function p1() {
    var a = Math.floor(Math.random() * 10) + 1
    var d = 10;
    d -= a;
    if (d === 0) {
        document.getElementById("s1").innerText = d
        i-=1
        reset()
        rearrange()
        document.getElementById("round").innerHTML = i
        var b = document.getElementById("p1_result").innerText
        var c = Number(b)
        c += 1
        if (c === 3) {
            document.getElementById("p1_result").innerHTML = c
            alert('Player1 is Won the whole the game')
            reset()
        }
        else {
            document.getElementById("p1_result").innerHTML = c

        }
    }
    else {
        document.getElementById("s1").innerText = d
    }
}
function p2() {
    var a = Math.floor(Math.random() * 10) + 1
    var d = 10;
    d -= a;
    if (d === 0) {
        document.getElementById("s2").innerText =d
        i -= 1
        reset()
        document.getElementById("round").innerHTML = i
        var b = document.getElementById("p2_result").innerHTML
        var c = Number(b)
        c += 1
        if (c === 3) {
            document.getElementById("p2_result").innerHTML = c
            alert('Player2 is Won the whole the game')
            reset()
            rearrange()
        }
        else {
            document.getElementById("p2_result").innerHTML = c

        }
    }
    else {
        document.getElementById("s2").innerText = d
    }
}
function reset() {
    document.getElementById("s1").innerHTML = 10
    document.getElementById("s2").innerHTML = 10
}
function rearrange(){
    document.getElementById("p1_result").innerHTML=0
    document.getElementById("p2_result").innerHTML=0
    document.getElementById('round').innerHTML=5

}

